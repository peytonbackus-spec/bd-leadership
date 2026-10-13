import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
spec = importlib.util.spec_from_file_location("check_repo", ROOT / "scripts" / "check_repo.py")
check_repo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_repo)


def make_repo(tmp_path, files: dict):
    for rel, text in files.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    return sorted(files)


# --- the real repo passes checks a-c (what CI enforces) ------------------------

@pytest.mark.parametrize("check", [check_repo.check_content, check_repo.check_leakage, check_repo.check_links])
def test_repo_passes_ci_checks(check):
    assert check() == []


def test_repo_denylist_check_passes_or_skips():
    findings, skipped = check_repo.check_denylist()
    assert findings == [] or skipped


# --- a) content -----------------------------------------------------------------

def test_flags_heading_only_and_empty_markdown(tmp_path):
    files = make_repo(tmp_path, {"a/README.md": "# Title\n\n## Sub\n", "b/empty.md": "\n",
                                 "c/ok.md": "---\nid: x\n---\n# Title\n\nReal text.\n"})
    findings = check_repo.check_content(tmp_path, files)
    assert "a/README.md: heading-only markdown file" in findings
    assert "b/empty.md: empty markdown file" in findings
    assert not any(f.startswith("c/") for f in findings)


def test_flags_frontmatter_plus_heading_as_heading_only(tmp_path):
    files = make_repo(tmp_path, {"x.md": "---\nid: x\n---\n# Only a heading\n"})
    assert check_repo.check_content(tmp_path, files) == ["x.md: heading-only markdown file"]


def test_flags_empty_folder(tmp_path):
    files = make_repo(tmp_path, {"a/README.md": "# T\n\nText.\n"})
    (tmp_path / "empty-dir").mkdir()
    assert "empty-dir/: empty folder (no repo files)" in check_repo.check_content(tmp_path, files)


# --- b) leakage -----------------------------------------------------------------

@pytest.mark.parametrize("line", ["see gtm-os/contracts/x.yaml", "tags: [wiki/competitive]",
                                  "bounded_autonomy_note: x", "per CLAUDE.md rule",
                                  "open /Users/someone/vault", "python3 ~/vault/x.py"])
def test_flags_vault_leakage(tmp_path, line):
    files = make_repo(tmp_path, {"doc.md": f"# T\n\n{line}\n"})
    assert len(check_repo.check_leakage(tmp_path, files)) == 1


def test_leakage_ignores_clean_text_and_exempt_files(tmp_path):
    files = make_repo(tmp_path, {"doc.md": "# T\n\nA wiki is fine; so is 5~/day.\n",
                                 "CHANGELOG.md": "- removed gtm-os/ paths\n"})
    assert check_repo.check_leakage(tmp_path, files) == []


# --- c) links -------------------------------------------------------------------

def test_flags_broken_link_and_missing_anchor(tmp_path):
    files = make_repo(tmp_path, {
        "README.md": "# Home\n\n[ok](docs/a.md#real-section) [bad](docs/missing.md) [anchor](docs/a.md#nope)\n",
        "docs/a.md": "# A\n\n## Real Section\n\nText.\n",
    })
    findings = check_repo.check_links(tmp_path, files)
    assert any("broken link docs/missing.md" in f for f in findings)
    assert any("missing anchor docs/a.md#nope" in f for f in findings)
    assert not any("real-section" in f for f in findings)


def test_links_inside_code_fences_are_ignored(tmp_path):
    files = make_repo(tmp_path, {"README.md": "# H\n\n```\n[x](nowhere.md)\n```\n"})
    assert check_repo.check_links(tmp_path, files) == []


def test_flags_missing_readme_code_path(tmp_path):
    files = make_repo(tmp_path, {"README.md": "# H\n\nRun `tools/real.py` then `tools/gone.py`.\n",
                                 "tools/real.py": "print(1)\n"})
    findings = check_repo.check_links(tmp_path, files)
    assert findings == ["README.md:3: missing path tools/gone.py"]


def test_github_slug():
    assert check_repo.github_slug("5. Compliance Rules") == "5-compliance-rules"
    assert check_repo.github_slug("Cold Call Scorecard (1-5 Scale)") == "cold-call-scorecard-1-5-scale"


# --- d) deny-list (fictional terms only) ---------------------------------------

def test_denylist_whole_word_contents_and_filenames(tmp_path):
    deny = tmp_path / "deny.txt"
    deny.write_text("# comment\nZorbex\nAcme Widgets\n")
    files = make_repo(tmp_path, {
        "notes.md": "# N\n\nWorked at zorbex.\nZorbexian is a different word.\nAcme  Widgets has two spaces.\nACME WIDGETS shouts.\n",
        "case/zorbex-story.md": "# S\n\nText.\n",
    })
    findings, skipped = check_repo.check_denylist(tmp_path, files, deny)
    assert skipped is None
    assert findings == ["case/zorbex-story.md: deny-list match in filename",
                        "notes.md:3: deny-list match", "notes.md:6: deny-list match"]


def test_denylist_output_never_includes_term(tmp_path):
    deny = tmp_path / "deny.txt"
    deny.write_text("Zorbex\n")
    files = make_repo(tmp_path, {"a.md": "# A\n\nZorbex\n"})
    findings, _ = check_repo.check_denylist(tmp_path, files, deny)
    assert findings and not any("zorbex" in f.lower() for f in findings)


def test_missing_denylist_skips_without_failing(tmp_path):
    files = make_repo(tmp_path, {"a.md": "# A\n\nText.\n"})
    findings, skipped = check_repo.check_denylist(tmp_path, files, tmp_path / "absent.txt")
    assert findings == [] and "skipped" in skipped


def test_main_exit_code_for_ci_checks():
    assert check_repo.main(["--checks", "a,b,c"]) == 0
