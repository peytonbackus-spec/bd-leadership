"""Strip known private-vault leakage from files synced into this repo.

Run after any vault sync. Standalone, idempotent, and safe to re-run.

What it fixes automatically:
  - `bounded_autonomy_note:` frontmatter lines are removed.
  - `wiki/competitive` tag lines are removed.
  - Known `gtm-os/...` paths are rewritten to their repo-relative locations.
  - "per/see/under/where CLAUDE.md ..." clauses are removed.

What it can only report (needs a human): any remaining `gtm-os/`, `wiki/competitive`
or `CLAUDE.md` text it has no rule for. Those are listed as path:line and make
--check (and a normal run) exit non-zero.

Usage:
    python3 scripts/sanitize_synced.py            # fix files in place
    python3 scripts/sanitize_synced.py --check    # change nothing; exit 1 if anything would change
    python3 scripts/sanitize_synced.py PATH...    # limit to files or folders (default: synced folders)
"""
import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Folders that receive synced content.
DEFAULT_TARGETS = ["gtm-prompt-library", "02-execution-and-workflows/09-gtm-tool-evaluation", "raw-sources"]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".csv", ".txt"}

# Known vault locations and where the same thing lives in this repo.
PATH_MAP = [
    ("gtm-os/contracts/", "gtm-prompt-library/contracts/"),
    ("gtm-os/schemas/", "gtm-prompt-library/schemas/"),
    ("gtm-os/mcp/speed-to-lead/", "02-execution-and-workflows/08-ai-workflows/"),
]

LINE_REMOVALS = [
    re.compile(r"(?m)^bounded_autonomy_note:.*\n"),
    re.compile(r"(?m)^[ \t]*-[ \t]*wiki/competitive[ \t]*\n"),
]
CLAUDE_MD_CLAUSE = re.compile(r"[ \t]*(?:per|see|under|where)[ \t]+CLAUDE\.md(?:'s)?(?:[ \t]+section[ \t]+\d+(?:'s)?)?[^.\n;)]*")

LEFTOVER_PATTERNS = [
    ("gtm-os path", re.compile(r"gtm-os/")),
    ("wiki/competitive", re.compile(r"wiki/competitive")),
    ("CLAUDE.md reference", re.compile(r"CLAUDE\.md")),
]


def sanitize_text(text: str) -> str:
    for pattern in LINE_REMOVALS:
        text = pattern.sub("", text)
    for old, new in PATH_MAP:
        text = text.replace(old, new)
    return CLAUDE_MD_CLAUSE.sub("", text)


def leftovers(text: str) -> list:
    """(line number, label) for every leakage pattern still present."""
    found = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for label, pattern in LEFTOVER_PATTERNS:
            if pattern.search(line):
                found.append((lineno, label))
    return found


def collect_files(targets, root: Path = REPO_ROOT) -> list:
    files = []
    for target in targets:
        path = (root / target) if not Path(target).is_absolute() else Path(target)
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files += [p for p in sorted(path.rglob("*")) if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES]
    return files


def run(targets, check: bool, root: Path = REPO_ROOT) -> int:
    changed, unresolved = [], []
    for path in collect_files(targets, root):
        rel = path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)
        original = path.read_text(encoding="utf-8")
        cleaned = sanitize_text(original)
        if cleaned != original:
            changed.append(rel)
            if not check:
                path.write_text(cleaned, encoding="utf-8")
        unresolved += [f"{rel}:{lineno}: {label}" for lineno, label in leftovers(cleaned)]

    verb = "would change" if check else "changed"
    for rel in changed:
        print(f"{verb}: {rel}")
    for item in unresolved:
        print(f"needs manual fix: {item}")
    print(f"{len(changed)} file(s) {verb}; {len(unresolved)} item(s) need manual fixes.")
    return 1 if (changed and check) or unresolved else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="*", help="Files or folders to process (default: synced folders)")
    parser.add_argument("--check", action="store_true", help="Change nothing; exit non-zero if anything would change")
    args = parser.parse_args(argv)
    return run(args.paths or DEFAULT_TARGETS, args.check)


if __name__ == "__main__":
    sys.exit(main())
