# The 70/30 ratio, the tags, and the checker

What the ratio is, how a tag is written, and how `tools/check_70_30.py` enforces
both so a skill can't drift from its sources.

## The ratio

- One **spine** book supplies about **70%** of a skill's tagged principles. The checker
  passes anything from **65% to 75%**.
- Named **support** books supply the rest. There can be several; none should rival the
  spine.
- The ratio is counted over **tagged principles**, across `SKILL.md` and every file in
  `references/`, not over words or lines.
- Why 70/30: enough of one book to give the skill a coherent spine and voice, enough
  outside view to cover that book's blind spots and name where books disagree.

## The tag format

- Every principle ends with a bracketed tag naming the book and the place:
  `[Spine ch3]`, `[Spine ch7]`, `[Spine R17]`, `[Support, Hooks]`.
- The name inside the tag is the book's short tag-name (the same token used in the
  spine marker and the checker's lists), not the full title.
- The chapter/section part is free text after the name; the checker matches the name and
  ignores the rest.
- The **"Where the books disagree"** section names books in prose **without** bracket
  tags; the checker skips that whole section when counting.

## What the checker verifies

`python3 tools/check_70_30.py` walks every `skills/<name>/` and, for each:

- **Router** (`<!-- router ... -->`): must carry **zero** tags. A router that stated
  principles would dodge the ratio. Fails if any tag is found.
- **Craft skill**: must have a `<!-- spine: Name -->` marker; the spine's share of all
  tags must land in 65–75%; and the **Source ledger** table must match the counted tags
  exactly.

It prints a line per skill with the spine, the spine count, the total, the share and the
support breakdown, and exits non-zero if anything fails.

```bash
python3 tools/check_70_30.py           # check only
python3 tools/check_70_30.py --write   # rewrite every ledger from real counts, then check
python3 tools/check_70_30.py skills/   # point it at a skills dir explicitly
```

Run `--write` after any edit that changes counts, commit the synced ledgers, then run it
once more plain to confirm green.

## Teaching the checker a new book

The checker only counts books it knows. Adding a new spine or support book means editing
four lists in `tools/check_70_30.py` so they agree:

1. **`BOOKS`** — add the short tag-name string (e.g. `"Hanlon"`).
2. **`TAG`** — add the name to the alternation in the compiled regex, so `[Hanlon ch2]`
   is recognised.
3. **`LEDGER_NAMES`** — map the name as it appears in a ledger row to the tag-name
   (e.g. `"Hanlon": "Hanlon"`; use a distinct key if the ledger prints a different word).
4. **`TITLES`** — add the full citation shown in the ledger
   (e.g. `"Hanlon": "Patrick Hanlon, *Primal Branding*"`).

Miss any one and the counts, the regex and the ledger fall out of step: tags go
uncounted, the share reads low, and `--write` writes a ledger the plain run then rejects.

## Reading a checker line

```
contagious-content  Berger        113   162   69.8%  Kane 15, Vaynerchuk 10, ...  OK
<skill>             <spine>     <spine> <all> <share> <supports>                 <status>
```

- `share` outside 65–75% → move spine principles in or trim support.
- `ledger ... != counted ...` → you edited tags but didn't re-run `--write`.
- `router carries N source tags` → a router picked up a principle; remove it.
- `no <!-- spine: ... --> marker` → add the spine marker, or the router marker if it
  fires other skills and states nothing itself.
