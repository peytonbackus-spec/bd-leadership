"""Repo guardrail checks for a public portfolio repo.

Checks (run all by default, or pick with --checks):
  a  content   Heading-only or empty markdown files, and empty folders.
  b  leakage   Private-vault leftovers and absolute/home paths.
  c  links     Broken relative links and #anchors in markdown, plus repo paths
               quoted in README.md code.
  d  denylist  Terms from a local, gitignored deny-list file (env DENYLIST_FILE,
               default .denylist.local), matched as whole words, case-insensitive,
               in file contents and filenames. If the file is absent, the check
               is skipped and never fails. Output is path:line only; the matched
               term is never printed.

Files scanned: those git tracks or would track (`git ls-files --cached --others
--exclude-standard`) that exist on disk, so new uncommitted files are checked
and deleted-but-unstaged files are not.

Usage:
    python3 scripts/check_repo.py                 # a, b, c, d
    python3 scripts/check_repo.py --checks a,b,c  # what CI runs
Exit code is 1 if any check reports a finding.
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".json", ".csv", ".html", ".sh", ".txt", ".ini", ".toml", ".example"}
SKIP_DIR_NAMES = {".git", ".pytest_cache", "__pycache__", ".venv", "venv", "node_modules"}

# Files that legitimately name the patterns: the checker and sanitizer, their tests,
# the changelog (it records their removal), and the project's own CLAUDE.md.
LEAKAGE_EXEMPT = {"scripts/check_repo.py", "tests/test_repo_guardrails.py", "scripts/sanitize_synced.py",
                  "tests/test_sanitize_synced.py", "CHANGELOG.md", "CLAUDE.md"}
LEAKAGE_PATTERNS = [
    ("vault path", re.compile(r"gtm-os/")),
    ("vault tag", re.compile(r"wiki/competitive")),
    ("vault frontmatter", re.compile(r"bounded_autonomy_note")),
    ("CLAUDE.md reference", re.compile(r"CLAUDE\.md")),
    ("absolute user path", re.compile(r"/Users/|/home/[a-z]")),
    ("home-relative path", re.compile(r"(?<![\w.])~/")),
]

DEFAULT_DENYLIST = ".denylist.local"


def repo_files(root: Path = REPO_ROOT) -> list:
    """Repo-relative POSIX paths that git tracks or would track and that exist on disk."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=root, capture_output=True, text=True, check=True,
        ).stdout
        paths = out.splitlines()
    except (OSError, subprocess.CalledProcessError):
        paths = [p.relative_to(root).as_posix() for p in root.rglob("*")
                 if p.is_file() and not SKIP_DIR_NAMES.intersection(p.relative_to(root).parts)]
    return sorted(p for p in paths if (root / p).is_file())


def _is_text(path: str) -> bool:
    return Path(path).suffix.lower() in TEXT_SUFFIXES or Path(path).name.startswith(".env")


def _read(root: Path, path: str) -> str:
    return (root / path).read_text(encoding="utf-8", errors="ignore")


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:]
    return text


# --- a) content ---------------------------------------------------------------

def check_content(root: Path = REPO_ROOT, files: list = None) -> list:
    files = files if files is not None else repo_files(root)
    findings = []
    for path in files:
        if not path.endswith(".md"):
            continue
        body = [ln for ln in _strip_frontmatter(_read(root, path)).splitlines() if ln.strip()]
        if not body:
            findings.append(f"{path}: empty markdown file")
        elif all(ln.lstrip().startswith("#") for ln in body):
            findings.append(f"{path}: heading-only markdown file")

    # Folders on disk with no repo file anywhere beneath them.
    populated = {Path(p).parent for p in files}
    populated |= {anc for p in list(populated) for anc in p.parents}
    candidates = []
    for dirpath, dirnames, _ in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES and not d.startswith(".")]
        rel = Path(dirpath).relative_to(root)
        if rel != Path(".") and rel not in populated:
            candidates.append(rel.as_posix())
    ignored = set()
    if candidates:
        try:
            ignored = set(subprocess.run(["git", "check-ignore", "--stdin"], cwd=root, input="\n".join(candidates),
                                         capture_output=True, text=True).stdout.split("\n"))
        except OSError:
            pass
    findings += [f"{d}/: empty folder (no repo files)" for d in candidates
                 if d not in ignored and not any(d.startswith(i.rstrip("/") + "/") for i in ignored if i)]
    return findings


# --- b) leakage ---------------------------------------------------------------

def check_leakage(root: Path = REPO_ROOT, files: list = None) -> list:
    files = files if files is not None else repo_files(root)
    findings = []
    for path in files:
        if path in LEAKAGE_EXEMPT or not _is_text(path):
            continue
        for lineno, line in enumerate(_read(root, path).splitlines(), 1):
            for label, pattern in LEAKAGE_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path}:{lineno}: {label}")
    return findings


# --- c) links -----------------------------------------------------------------

LINK_RE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"```.*?```", re.S)


def github_slug(heading: str) -> str:
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


def heading_anchors(text: str) -> set:
    anchors, seen = set(), {}
    for line in FENCE_RE.sub("", text).splitlines():
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if not m:
            continue
        slug = github_slug(m.group(1))
        n = seen.get(slug, 0)
        anchors.add(slug if n == 0 else f"{slug}-{n}")
        seen[slug] = n + 1
    return anchors


def check_links(root: Path = REPO_ROOT, files: list = None) -> list:
    files = files if files is not None else repo_files(root)
    findings = []
    for path in files:
        if not path.endswith(".md"):
            continue
        text = _read(root, path)
        for lineno, line in enumerate(FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text).splitlines(), 1):
            for m in LINK_RE.finditer(line):
                href = m.group(1)
                if href.startswith(("http://", "https://", "mailto:")):
                    continue
                target, _, anchor = href.partition("#")
                target_path = (root / path).parent / urllib.parse.unquote(target) if target else root / path
                if not target_path.exists():
                    findings.append(f"{path}:{lineno}: broken link {href}")
                elif anchor and target_path.suffix == ".md" and anchor not in heading_anchors(target_path.read_text(errors="ignore")):
                    findings.append(f"{path}:{lineno}: missing anchor {href}")

    # README: repo paths quoted in code (inline or fenced) must exist.
    readme = root / "README.md"
    if readme.exists():
        top_dirs = {Path(p).parts[0] for p in files if len(Path(p).parts) > 1}
        token_re = re.compile(r"(?<![\w./-])((?:%s)/[\w./-]*\w)" % "|".join(re.escape(d) for d in sorted(top_dirs)))
        for lineno, line in enumerate(readme.read_text().splitlines(), 1):
            if "`" not in line and not line.startswith(("python", "pytest", "bash")):
                continue
            for token in token_re.findall(line):
                if not (root / token).exists():
                    findings.append(f"README.md:{lineno}: missing path {token}")
    return findings


# --- d) deny-list -------------------------------------------------------------

def load_denylist(path: Path):
    """Return compiled whole-word patterns, or None if the file is absent."""
    if not path.exists():
        return None
    terms = [t.strip() for t in path.read_text(encoding="utf-8").splitlines()
             if t.strip() and not t.strip().startswith("#")]
    return [re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I) for t in terms]


def check_denylist(root: Path = REPO_ROOT, files: list = None, denylist_path: Path = None):
    """Return (findings, skipped_message). Findings are path[:line] only, never the term."""
    denylist_path = denylist_path or root / os.environ.get("DENYLIST_FILE", DEFAULT_DENYLIST)
    patterns = load_denylist(Path(denylist_path))
    if patterns is None:
        return [], f"deny-list file not found ({Path(denylist_path).name}); check d skipped"
    files = files if files is not None else repo_files(root)
    findings = []
    for path in files:
        if any(p.search(path) for p in patterns):
            findings.append(f"{path}: deny-list match in filename")
        if not _is_text(path):
            continue
        for lineno, line in enumerate(_read(root, path).splitlines(), 1):
            if any(p.search(line) for p in patterns):
                findings.append(f"{path}:{lineno}: deny-list match")
    return findings, None


# --- CLI ----------------------------------------------------------------------

CHECKS = {"a": ("content", check_content), "b": ("leakage", check_leakage), "c": ("links", check_links)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Repo guardrail checks")
    parser.add_argument("--checks", default="a,b,c,d", help="Comma-separated subset of a,b,c,d")
    args = parser.parse_args(argv)
    selected = [c.strip() for c in args.checks.split(",") if c.strip()]

    files = repo_files()
    failed = False
    for key in selected:
        if key == "d":
            findings, skipped = check_denylist(files=files)
            name = "denylist"
            if skipped:
                print(f"[d] {name}: SKIPPED - {skipped}")
                continue
        else:
            name, fn = CHECKS[key]
            findings = fn(files=files)
        status = "FAIL" if findings else "ok"
        print(f"[{key}] {name}: {status} ({len(findings)} finding(s))")
        for f in findings:
            print(f"    {f}")
        failed = failed or bool(findings)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
