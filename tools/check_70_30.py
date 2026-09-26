#!/usr/bin/env python3
"""Check the 70/30 rule for every writing skill in skills/.

Every principle in a skill carries a source tag naming the book it comes from,
e.g. [McKee ch7], [S&W R17], [Diamond ch14]. Each SKILL.md declares its spine
book in an HTML comment (<!-- spine: McKee -->). This script counts the tags in
SKILL.md plus references/*.md, skips the "Where the books disagree" section
(which names books without tagging them), and checks that the spine book
supplies 70% (+/- 5) of the tagged principles. It also checks the counts in
each skill's "Source ledger" table, so the ledger can't drift from the text.

Usage: python3 tools/check_70_30.py [--write] [skills_dir]
  --write  rewrite each skill's "Source ledger" table from the counted tags
Exit code 1 if any skill fails.
"""
import re
import sys
from pathlib import Path

BOOKS = ["McKee", "Cron", "King", "McPhee", "Klinkenborg", "S&W", "Diamond"]
TAG = re.compile(r"\[(McKee|Cron|King|McPhee|Klinkenborg|S&W|Diamond)\b[^\]]*\]")
SPINE = re.compile(r"<!--\s*spine:\s*(\S+)\s*-->")
LEDGER_ROW = re.compile(r"^\|\s*(?P<book>[^|]+?)\s*\|\s*(?P<role>Spine|Support)\s*\|\s*(?P<n>\d+)")
LEDGER_NAMES = {"McKee": "McKee", "Cron": "Cron", "King": "King", "McPhee": "McPhee",
                "Klinkenborg": "Klinkenborg", "Strunk": "S&W", "Diamond": "Diamond"}
TITLES = {
    "McKee": "Robert McKee, *Story*",
    "Cron": "Lisa Cron, *Wired for Story*",
    "King": "Stephen King, *On Writing*",
    "McPhee": "John McPhee, *Draft No. 4*",
    "Klinkenborg": "Verlyn Klinkenborg, *Several Short Sentences About Writing*",
    "S&W": "William Strunk Jr. & E. B. White, *The Elements of Style*",
    "Diamond": "Jared Diamond, *Guns, Germs, and Steel*",
}
LOW, HIGH = 65.0, 75.0


def skill_files(skill_dir):
    yield skill_dir / "SKILL.md"
    yield from sorted((skill_dir / "references").glob("*.md"))


def count_tags(skill_dir):
    counts = dict.fromkeys(BOOKS, 0)
    for path in skill_files(skill_dir):
        skipping = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                skipping = line.lower().startswith("## where the books disagree")
            if not skipping:
                for match in TAG.finditer(line):
                    counts[match.group(1)] += 1
    return counts


def read_ledger(skill_md):
    ledger, inside = {}, False
    for line in skill_md.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            inside = line.lower().startswith("## source ledger")
        if inside:
            row = LEDGER_ROW.match(line)
            if row:
                book = next((tag for name, tag in LEDGER_NAMES.items() if name in row["book"]), None)
                if book:
                    ledger[book] = int(row["n"])
    return ledger


def write_ledger(skill_md, spine, counts):
    total = sum(counts.values())
    rows = ["| Book | Role | Tagged principles |", "|---|---|---|",
            f"| {TITLES[spine]} | Spine | {counts[spine]} of {total} ({100.0 * counts[spine] / total:.1f}%) |"]
    for book, n in sorted(counts.items(), key=lambda item: -item[1]):
        if n and book != spine:
            rows.append(f"| {TITLES[book]} | Support | {n} |")
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    start = next(i for i, line in enumerate(lines) if line.lower().startswith("## source ledger"))
    first = next(i for i in range(start, len(lines)) if lines[i].startswith("|"))
    last = first
    while last < len(lines) and lines[last].startswith("|"):
        last += 1
    lines[first:last] = rows
    skill_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    args = [a for a in sys.argv[1:] if a != "--write"]
    write = "--write" in sys.argv[1:]
    skills_dir = Path(args[0] if args else Path(__file__).resolve().parent.parent / "skills")
    failures = 0
    print(f"{'skill':<16} {'spine':<12} {'spine':>5} {'total':>5} {'share':>6}  support")
    for skill_dir in sorted(p for p in skills_dir.iterdir() if (p / "SKILL.md").exists()):
        skill_md = skill_dir / "SKILL.md"
        spine_match = SPINE.search(skill_md.read_text(encoding="utf-8"))
        if not spine_match:
            print(f"{skill_dir.name:<16} no <!-- spine: ... --> marker")
            failures += 1
            continue
        spine = spine_match.group(1)
        counts = count_tags(skill_dir)
        total = sum(counts.values())
        share = 100.0 * counts[spine] / total if total else 0.0
        support = ", ".join(f"{b} {n}" for b, n in counts.items() if n and b != spine)
        problems = []
        if not LOW <= share <= HIGH:
            problems.append(f"spine share {share:.1f}% outside {LOW:.0f}-{HIGH:.0f}%")
        if write and total:
            write_ledger(skill_md, spine, counts)
        ledger = read_ledger(skill_md)
        actual = {b: n for b, n in counts.items() if n}
        if ledger != actual:
            problems.append(f"ledger {ledger} != counted {actual}")
        status = "OK" if not problems else "FAIL: " + "; ".join(problems)
        failures += bool(problems)
        print(f"{skill_dir.name:<16} {spine:<12} {counts[spine]:>5} {total:>5} {share:>5.1f}%  {support}  {status}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
