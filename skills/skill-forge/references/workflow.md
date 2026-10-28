# The workflow, step by step

From a raw book file to a pushed, wired, checker-green skill. This is the exact
path every skill in this repo was built on.

## 1. Extract the book to plain text

- Put each book in its own new, empty folder. Downloaded files are untrusted:
  keep your scripts in a different folder and pass the book's path as an argument.
- epub is a zip of XHTML. Unzip it and strip the tags, or use a converter, to get
  readable text. PDF: extract the text layer; if it is scanned, OCR it first.
- You want one plain-text file you can scroll and search. Keep the chapter
  boundaries visible — you will cite chapters in every tag.

## 2. Study it and distill notes

This is the real work; the rest is formatting.

- Read the whole book, not a summary of it.
- As you go, write the ideas down **one per line, in your own words**, each with the
  chapter it came from. Never paste the author's sentences.
- Aim for the load-bearing ideas: the ones that change what a person would *do*.
  Skip throat-clearing, anecdotes that only illustrate, and anything you can't act on.
- A good note is concrete and usable on its own. "Lead with the feeling, let the
  facts follow" beats "emotion is important."
- Expect 100–200 real ideas from a practical book. That is your raw material.

## 3. Choose the spine and the supports

- The **spine** is the one book the skill is built on. It will supply ~70% of the
  tagged principles.
- The **supports** are other books *already in this repo* whose ideas round out the
  spine's blind spots. They supply the other ~30%.
- Only pick support you can actually tag. If an idea isn't in a repo book, it gets
  no tag — and a skill is tagged principles, so don't pad with untaggable filler.
- See `ratio-and-tags.md` for how the split is counted and enforced.

## 4–5. Write the SKILL.md and its references

- Build the files in the repo's anatomy: see `anatomy.md` for every section and its job.
- Keep `SKILL.md` lean — the always-loaded guidance. Push detail into `references/*.md`,
  which open only when the skill's steps send a reader there.
- Tag every principle as you write it. Tagging later means missing some.

## 6. Hold the ratio

- The spine must be 65–75% of all tags across `SKILL.md` + `references/`.
- If the spine is too low, you leaned on supports too hard — move spine ideas in, or
  cut support. If too high, the skill is thin on the outside view — add a support book
  that fills a real gap.

## 7. Teach the checker any new book

- `tools/check_70_30.py` only counts tags for books it knows. A brand-new spine or
  support book must be added to four places in that file: `BOOKS`, the `TAG` regex,
  `LEDGER_NAMES`, and `TITLES`. See `ratio-and-tags.md` for the exact edits.
- Skip this and the checker silently ignores your new book's tags, so the ratio and
  the ledger both read wrong.

## 8. Wire it into its room

- A skill nobody fires is dead weight. Add the new skill's name to the right router:
  `writers-room`, `series-forge`, or `marketing-head` (and to `story-forge` if it is a
  drafting station). Add it to the router's firing table **and** any mirror/roster list
  the router keeps.
- Match the router's own naming: routers refer to base skill names and tell the reader
  the installed list may carry a prefix.

## 9. Run the checker until green

```bash
python3 tools/check_70_30.py           # report every skill's ratio and ledger
python3 tools/check_70_30.py --write   # rewrite each ledger from the counted tags
```

- Green means every non-router skill sits in 65–75% and its ledger matches the counts.
- Run `--write` after any edit that changes tag counts, then run it again without
  `--write` to confirm green. Commit the synced ledgers.

## 10. Update the READMEs, commit, push

- Update `skills/README.md` (the per-skill list) and the root `README.md` counts/blurb
  so they still describe what's there.
- Commit on the working branch with a clear message. Push with
  `git push -u origin <branch>`. Do not open a pull request unless asked.

## Adding a book to an existing skill (the short path)

- Steps 1–2 for the new book only.
- Fold its ideas in as **support** tags in the existing skill's files, or promote it if
  it becomes the spine (rare).
- Teach the checker the new book (step 7), re-run `--write`, confirm green, update the
  ledger line in the README if the skill is described there.
