import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
spec = importlib.util.spec_from_file_location("sanitize_synced", ROOT / "scripts" / "sanitize_synced.py")
san = importlib.util.module_from_spec(spec)
spec.loader.exec_module(san)

DIRTY = """---
id: x
tags:
  - gtm/intelligence
  - wiki/competitive
bounded_autonomy_note: human-invoked prompt, see vault
---
# Title

Real file: `gtm-os/contracts/foo-contract.yaml` and gtm-os/mcp/speed-to-lead/mock_data.json.
Writes need approval where CLAUDE.md requires.
"""


def test_sanitize_removes_known_leakage():
    out = san.sanitize_text(DIRTY)
    assert "bounded_autonomy_note" not in out
    assert "wiki/competitive" not in out
    assert "gtm-os/" not in out
    assert "CLAUDE.md" not in out
    assert "gtm-prompt-library/contracts/foo-contract.yaml" in out
    assert "02-execution-and-workflows/08-ai-workflows/mock_data.json" in out
    assert "gtm/intelligence" in out and "Real file" in out


def test_sanitize_is_idempotent():
    once = san.sanitize_text(DIRTY)
    assert san.sanitize_text(once) == once


def test_clean_text_is_unchanged():
    clean = "---\nid: x\ntags:\n  - gtm/intelligence\n---\n# T\n\nNothing to strip.\n"
    assert san.sanitize_text(clean) == clean


def write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text)
    return p


def test_check_mode_exits_nonzero_and_changes_nothing(tmp_path, capsys):
    p = write(tmp_path, "a.md", DIRTY)
    assert san.run([str(p)], check=True, root=tmp_path) == 1
    assert p.read_text() == DIRTY
    assert "would change: a.md" in capsys.readouterr().out


def test_fix_mode_rewrites_then_check_passes(tmp_path):
    p = write(tmp_path, "a.md", DIRTY)
    assert san.run([str(p)], check=False, root=tmp_path) == 0
    assert "bounded_autonomy_note" not in p.read_text()
    assert san.run([str(p)], check=True, root=tmp_path) == 0


def test_unmapped_leftover_is_reported(tmp_path, capsys):
    p = write(tmp_path, "a.md", "# T\n\nSee gtm-os/unknown/thing.md for details.\n")
    assert san.run([str(p)], check=False, root=tmp_path) == 1
    assert "a.md:3: gtm-os path" in capsys.readouterr().out


def test_folder_target_only_touches_text_files(tmp_path):
    write(tmp_path, "a.md", DIRTY)
    (tmp_path / "img.png").write_bytes(b"\x89PNG gtm-os/ not text")
    files = [p.name for p in san.collect_files([str(tmp_path)], tmp_path)]
    assert files == ["a.md"]


def test_repo_synced_folders_are_already_clean():
    assert san.run(san.DEFAULT_TARGETS, check=True) == 0


def test_cli_accepts_directory_outside_repo(tmp_path, capsys):
    """A staging folder given on the command line is cleaned in place, nested files included."""
    sub = tmp_path / "staging" / "nested"
    sub.mkdir(parents=True)
    f = sub / "a.md"
    f.write_text(DIRTY, encoding="utf-8")
    assert san.main(["--check", str(tmp_path / "staging")]) == 1
    assert f.read_text(encoding="utf-8") == DIRTY
    assert san.main([str(tmp_path / "staging")]) == 0
    assert "gtm-os/" not in f.read_text(encoding="utf-8")
    assert san.main(["--check", str(tmp_path / "staging")]) == 0
