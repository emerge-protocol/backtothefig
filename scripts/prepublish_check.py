#!/usr/bin/env python3
"""Checks to run before anything in this repository is made public. Exits 1 on any finding.

  python3 scripts/prepublish_check.py
  python3 scripts/prepublish_check.py --source path/to/master-prompt.v15.md   # also check quotes

What it looks for:
  - open questions: "TO CONFIRM" anywhere, and update posts still named draft-*
  - em and en dashes (our prompts and our writing do not use them)
  - email addresses
  - relative links that point at files that do not exist
  - with --source: lines quoted from the master prompt that are not word for word
  - anything matching private/denylist.txt: names and details of how Figs are built,
    which must never ship. The list stays out of git (see .gitignore), because a
    published list of what to hide would itself say what is hidden.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT = {".md", ".json", ".py", ".txt"}
SELF = Path(__file__).resolve()

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
ALLOWED_EMAILS = set()  # add a public contact address here once it is decided
DENYLIST = ROOT / "private" / "denylist.txt"  # one regex per line, "#" for comments


def denylist():
    if not DENYLIST.exists():
        return None
    lines = DENYLIST.read_text(encoding="utf-8").splitlines()
    return [re.compile(line.strip()) for line in lines if line.strip() and not line.strip().startswith("#")]


def files():
    for p in sorted(ROOT.rglob("*")):
        skip = ".git" in p.parts or "private" in p.relative_to(ROOT).parts
        if p.is_file() and p.suffix in TEXT and not skip and p.resolve() != SELF:
            yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="the master prompt file, to check quotes against")
    args = ap.parse_args()
    findings = []
    hidden = denylist()

    def add(path, line_no, why, text):
        findings.append(f"{path.relative_to(ROOT)}:{line_no}: {why}: {text.strip()[:100]}")

    for p in files():
        if p.name.startswith("draft-"):
            findings.append(f"{p.relative_to(ROOT)}: still named draft-")
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if "TO CONFIRM" in line:
                add(p, n, "open question", line)
            if re.search("[\u2013\u2014]", line):
                add(p, n, "em or en dash", line)
            for m in EMAIL.finditer(line):
                if m.group(0) not in ALLOWED_EMAILS:
                    add(p, n, "email address", m.group(0))
            for pattern in hidden or []:
                for m in pattern.finditer(line):
                    add(p, n, "on the private denylist", m.group(0))
            if p.suffix == ".md":
                for target in re.findall(r"\]\(([^)\s]+)\)", line):
                    if re.match(r"[a-z]+:", target) or target.startswith("#"):
                        continue
                    file_part = target.split("#", 1)[0]
                    if file_part and not (p.parent / file_part).exists():
                        add(p, n, "broken link", target)

    if args.source:
        norm = lambda s: re.sub(r"\s+", " ", s).strip()
        source = norm(Path(args.source).read_text(encoding="utf-8"))
        for name in ("intentions.md", "master-prompt/how-we-write-it.md"):
            p = ROOT / name
            in_callout = False
            for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                if not line.startswith(">"):
                    in_callout = False
                    continue
                if line.startswith("> [!"):
                    in_callout = True
                if in_callout:
                    continue
                quoted = norm(line[1:])
                if quoted and quoted not in source:
                    add(p, n, "quote not word for word in the master prompt", quoted)

    if hidden is None:
        print("note: private/denylist.txt not found, so the check for internal names was skipped")
    for f in findings:
        print(f)
    print(f"{len(findings)} finding(s)" if findings else "clean")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
