---
name: skill-forge
description: The workshop that turns a book into a Claude skill the way this repo does it — one spine book supplying ~70% of the principles, named supporting books the other ~30%, every principle paraphrased and source-tagged, broken into a SKILL.md plus reference files, verified by tools/check_70_30.py, and wired into its router. Use it whenever someone wants to build a new skill from a book (or several), add a book to an existing skill, turn notes or a method into a skill, says "make a skill out of this book", "distill this into a skill", "add Primal Branding as a skill", or needs the 70/30 ratio, the source tags, the ledger or the checker explained or fixed. This is the meta-skill: it builds the other skills.
---

<!-- router: meta-skill describing this repo's own skill-building workflow; it states process steps, not book-sourced craft principles, so the 70/30 source check does not apply -->

# Skill Forge

This is the workshop that made every book-skill in this repo. Give it a book (an epub, a PDF, a set of notes) and a place for the skill to live, and it produces a skill in the exact shape the rest of the repo uses: one **spine** book carrying about 70% of the ideas, named **supporting** books carrying the rest, every idea paraphrased in your own words and tagged with its source, split across a `SKILL.md` and `references/*.md`, checked by `tools/check_70_30.py`, and wired into the router that fires it.

It produces, every time:
- a new `skills/<name>/` folder with `SKILL.md` and `references/`;
- a spine marker and a source ledger that the checker verifies;
- the skill wired into its room (`writers-room`, `series-forge`, or `marketing-head`);
- a green run of `python3 tools/check_70_30.py`.

**The one rule that governs everything:** never quote or reproduce text from the source books. Read them, understand them, then write every principle in your own words with your own examples. A source tag like `[Spine ch3]` says where an idea came from; it is not permission to copy a sentence.

## The workflow, end to end

Follow these in order. Each is detailed in a reference file.

1. **Extract the book to plain text.** epub or PDF in its own folder, converted to text you can read and search. → `references/workflow.md`
2. **Study it and distill notes.** One idea per line, each with its chapter, in your own words. This is where the real work is. → `references/workflow.md`
3. **Choose the spine and the supports.** One book is the spine (~70%). Pick a few books already in the repo that round it out (~30%); don't invent support you can't tag. → `references/ratio-and-tags.md`
4. **Write `SKILL.md`** in the repo's anatomy: frontmatter, spine marker, intro, core ideas, how-to-use, reference pointers, "Where the books disagree", source ledger. → `references/anatomy.md`
5. **Write the `references/*.md` files.** Move the detail out of `SKILL.md` into topic files, every principle tagged. → `references/anatomy.md`
6. **Tag every principle** `[Book chX]` and hold the 70/30 ratio (spine 65–75% of all tags). → `references/ratio-and-tags.md`
7. **Teach the checker any new book.** Add the book to the `BOOKS`, `TAG`, `LEDGER_NAMES` and `TITLES` lists in `tools/check_70_30.py`. → `references/ratio-and-tags.md`
8. **Wire it into its router** and any mirror list, so the room actually fires it. → `references/workflow.md`
9. **Run the checker until green.** `python3 tools/check_70_30.py`, and `--write` to sync the ledger to the counted tags. → `references/ratio-and-tags.md`
10. **Update the READMEs**, then commit and push on the working branch. → `references/workflow.md`

## The shape of a finished skill

```
skills/<name>/
  SKILL.md              frontmatter + spine marker + principles + ledger
  references/
    <topic-1>.md        detail, every principle source-tagged
    <topic-2>.md
    ...
```

`SKILL.md` carries the short, always-loaded guidance. The `references/` files carry the depth, opened only when the skill's own steps send you there. Keep `SKILL.md` lean; push detail down into references.

## The 70/30 rule in one look

- Every principle ends with a source tag: `[Spine chN]` or `[Support chN]`.
- The spine book must supply **65–75%** of all tagged principles across `SKILL.md` + `references/`.
- A `<!-- spine: Name -->` comment near the top names the spine.
- A **Source ledger** table at the foot of `SKILL.md` lists each book, its role and its tag count. The checker rewrites this table from the real counts with `--write`, so it can never drift from the text.
- A **router** (a skill that only fires other skills) carries no principles and no tags; it is marked `<!-- router ... -->` and is exempt. This meta-skill is marked that way too, because it states process, not book principles.

## When to use which room

Wire a new craft skill into the room that matches its job:

| The skill is about | Wire it into |
|---|---|
| writing, story, prose, genre craft | `writers-room` (and `story-forge` if it is a drafting station) |
| sequels, prequels, series, continuations | `series-forge` |
| marketing, sales, social, growth | `marketing-head` |

Add the skill's name to the router's firing table and to any "mirror" list the router keeps, or the room won't know it exists.

## Reference files

- The step-by-step, from raw book to pushed commit → `references/workflow.md`
- The anatomy of a `SKILL.md` and its reference files → `references/anatomy.md`
- The 70/30 ratio, the tag format and the checker → `references/ratio-and-tags.md`

## Common mistakes this skill prevents

- **Quoting the book.** The fastest way to make a skill you can't ship. Paraphrase, always.
- **Support you can't tag.** If you can't point an idea to a real book in the repo, it doesn't get a tag, and untagged filler doesn't belong in a skill.
- **A ledger that lies.** Hand-written counts drift. Always regenerate with `--write` and let the checker be the source of truth.
- **A skill nobody fires.** A skill not wired into a room is dead weight. Wire it, then test that the room lists it.
- **A new book the checker doesn't know.** The checker silently ignores tags for books not in its lists, so the ratio looks wrong. Teach it the book first.
