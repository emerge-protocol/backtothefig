#!/usr/bin/env python3
"""Build the public edition of a Fig master prompt.

The master prompt is a Markdown file. This script splits it into blocks (a
heading line, a paragraph, or a single list item) and looks each block up in
an edition spec by a fingerprint of its exact text. Then it writes the public
edition:

  verbatim  the block is copied exactly as it is in the master prompt
  summary   the block is replaced, where it sits, by a short summary that
            says it is one
  folded    the block is covered by the summary just before it

A block whose fingerprint is not in the spec stops the build, and so does a
block still marked "todo". That is the point of the script: no sentence enters
or leaves the public edition without a person deciding, and a sentence that
changes in a new version of the master prompt comes back for a new decision.

The spec keeps a short preview only of blocks that are published word for
word, so it never repeats text the edition leaves out.

Standard library only.

  # 1. bring the spec up to date with a new master prompt (new blocks become "todo")
  python3 scripts/build_edition.py sync  --source PATH/master-prompt.v16.md --spec master-prompt/edition.json
  # 2. decide every "todo" block in the spec, then build
  python3 scripts/build_edition.py build --source PATH/master-prompt.v16.md --spec master-prompt/edition.json --out master-prompt/v16.md
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

MODES = {"verbatim", "summary", "folded", "todo"}
LIST_ITEM = re.compile(r"^\s{0,3}(?:[-*+]|\d+\.)\s")


def blocks_of(text):
    """Split Markdown into (block, run) pairs. A heading line is a block of its own;
    a run of non-blank lines is a block, except that each list item in it is its own
    block. `run` numbers the run a block came from, so tight lists can be put back
    together exactly."""
    blocks, run, run_id = [], [], 0

    def flush():
        nonlocal run, run_id
        if not run:
            return
        current = []
        for line in run:
            if LIST_ITEM.match(line) and current:
                blocks.append(("\n".join(current), run_id))
                current = []
            current.append(line)
        blocks.append(("\n".join(current), run_id))
        run = []
        run_id += 1

    for line in text.splitlines():
        if line.strip() == "":
            flush()
        elif line.startswith("#"):
            flush()
            blocks.append((line, run_id))
            run_id += 1
        else:
            run.append(line)
    flush()
    return blocks


def fingerprint(block):
    return hashlib.sha256(block.encode("utf-8")).hexdigest()[:12]


def preview(block, n=90):
    one_line = " ".join(block.split())
    return one_line if len(one_line) <= n else one_line[: n - 3] + "..."


def words(s):
    return len(s.split())


def display_safe(block):
    """Escape < outside inline code so GitHub shows it instead of eating it as HTML.
    The words a reader sees stay exactly the master prompt's."""
    parts = re.split(r"(`[^`]*`)", block)
    return "".join(p if p.startswith("`") else p.replace("<", "&lt;") for p in parts)


def load_spec(path):
    spec = json.loads(Path(path).read_text(encoding="utf-8"))
    by_id = {b["id"]: b for b in spec.get("blocks", [])}
    return spec, by_id


def tidy(entry, block):
    """Keep a preview only where the edition shows the text anyway."""
    entry = dict(entry)
    if entry.get("publish") in ("verbatim", "todo"):
        entry["preview"] = preview(block)
    else:
        entry.pop("preview", None)
    return entry


def cmd_sync(args):
    source = Path(args.source).read_text(encoding="utf-8")
    spec_path = Path(args.spec)
    if spec_path.exists():
        spec, by_id = load_spec(spec_path)
    else:
        spec, by_id = {"source_name": Path(args.source).name, "preface": "", "blocks": []}, {}
    new_blocks, seen, added = [], set(), 0
    for block, _ in blocks_of(source):
        fid = fingerprint(block)
        if fid in seen:
            continue
        seen.add(fid)
        if fid in by_id:
            entry = by_id[fid]
        else:
            entry = {"id": fid, "publish": "todo"}
            added += 1
        new_blocks.append(tidy(entry, block))
    dropped = [b for fid, b in by_id.items() if fid not in seen]
    spec["source_name"] = Path(args.source).name
    spec["blocks"] = new_blocks
    spec_path.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"spec: {len(new_blocks)} blocks, {added} new (marked todo), {len(dropped)} no longer in the source")
    for b in dropped:
        print(f"  gone: [{b.get('publish')}] {b.get('preview', b['id'])}")
    for block, _ in blocks_of(source):
        if spec_path.exists() and fingerprint(block) not in by_id:
            print(f"  todo: {preview(block)}")
    return 0


def cmd_build(args):
    source_bytes = Path(args.source).read_bytes()
    source = source_bytes.decode("utf-8")
    spec, by_id = load_spec(args.spec)
    blocks = blocks_of(source)

    problems = []
    previous = None
    for block, _ in blocks:
        entry = by_id.get(fingerprint(block))
        if entry is None:
            problems.append(f"not in the spec (run sync): {preview(block)}")
        elif entry.get("publish") not in MODES:
            problems.append(f"unknown mode {entry.get('publish')!r}: {preview(block)}")
        elif entry["publish"] == "todo":
            problems.append(f"still todo: {preview(block)}")
        elif entry["publish"] == "summary" and not entry.get("summary", "").strip():
            problems.append(f"summary is empty: {preview(block)}")
        elif entry["publish"] == "folded" and previous not in ("summary", "folded"):
            problems.append(f"folded, but no summary right before it would cover it: {preview(block)}")
        previous = entry.get("publish") if entry else None
    if problems:
        print("The edition was not built. Decide these blocks first:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1

    mode = lambda b: by_id[fingerprint(b)]["publish"]
    total_words = sum(words(b) for b, _ in blocks)
    verbatim_words = sum(words(b) for b, _ in blocks if mode(b) == "verbatim")
    summaries = sum(1 for b, _ in blocks if mode(b) == "summary")
    stats = {
        "source_name": spec.get("source_name", Path(args.source).name),
        "sha256": hashlib.sha256(source_bytes).hexdigest(),
        "words_total": total_words,
        "words_verbatim": verbatim_words,
        "verbatim_pct": round(100 * verbatim_words / total_words) if total_words else 0,
        "summaries": summaries,
    }

    pieces = []  # (text, run of the verbatim block or None)
    preface_done = False
    for block, run in blocks:
        entry = by_id[fingerprint(block)]
        if entry["publish"] == "verbatim":
            pieces.append((display_safe(block), run))
        elif entry["publish"] == "summary":
            label = entry.get("label", "Summarized in this edition")
            pieces.append((f"> **{label}.** " + " ".join(entry["summary"].split()), None))
        if not preface_done and block.startswith("# "):
            preface = spec.get("preface", "").format(**stats).strip()
            if preface:
                pieces.append((preface, None))
            preface_done = True

    out = "<!-- Generated by scripts/build_edition.py from the master prompt. Edit master-prompt/edition.json, not this file. -->"
    last_run = None
    for text, run in pieces:
        # items of one tight list in the source stay one tight list
        out += ("\n" if run is not None and run == last_run else "\n\n") + text
        last_run = run
    footer = spec.get("footer", "").format(**stats).strip()
    if footer:
        out += "\n\n" + footer
    Path(args.out).write_text(out + "\n", encoding="utf-8")
    print(
        f"wrote {args.out}: {stats['verbatim_pct']}% of the words verbatim "
        f"({verbatim_words} of {total_words}), {summaries} summaries, source sha256 {stats['sha256'][:16]}..."
    )
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sync", help="add new blocks of the source to the spec as todo")
    s.add_argument("--source", required=True)
    s.add_argument("--spec", required=True)
    b = sub.add_parser("build", help="write the public edition")
    b.add_argument("--source", required=True)
    b.add_argument("--spec", required=True)
    b.add_argument("--out", required=True)
    args = p.parse_args()
    return cmd_sync(args) if args.cmd == "sync" else cmd_build(args)


if __name__ == "__main__":
    sys.exit(main())
