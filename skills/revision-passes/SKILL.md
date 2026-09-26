---
name: revision-passes
description: Revision workflow built on John McPhee's "Draft No. 4" (supported by King, Klinkenborg, Cron, Strunk & White and McKee) — separate passes for structure drawn from the material, the lead as a promise, reading aloud, boxing weak words for Draft No. 4, frame of reference, fact and continuity checkpoints, and omission ("greening" about 10% so nobody notices what is gone). Use it whenever someone has a draft (story, chapter, essay, article, lore entry, script) and wants to revise, tighten, cut, restructure, fix the opening or ending, or hit a word count, or asks "how do I make this better," "this is too long," "the structure isn't working," "where should this start." Also use it when there is plenty of material but it will not organize into a piece.
---

<!-- spine: McPhee -->

# Revision Passes

Revision done as a series of passes, each hunting for one kind of problem. It produces a **revised draft plus a revision log** that records every pass: what was looked for, what changed (with before and after), and the word count. It is not a single "make it better" rewrite.

**Important:** never quote or reproduce text from the source books. Paraphrase the concepts and work on the person's own draft.

## What revision is

- Revision is the heart of the writing process, not a cleanup after it. Once a draft exists, the real writing has begun. [McPhee, Draft No. 4]
- Do a piece of writing three or four times over, never once. Get something down, however rough, then work it over, then work it again. [McPhee, Draft No. 4]
- The first draft costs far more time and dread than all the later drafts together. After it, the problems start to become interesting. [McPhee, Draft No. 4]
- Writing is selection. From the first word, you're deciding what stays out. [McPhee, Omission]
- A piece should run only as long as its chosen material can carry. Loving your research is no reason to keep all of it. [McPhee, Omission]
- It's done when you can't make it any better. Someone else might, but you've given what you have. [McPhee, Structure]

## The pass sequence

Run the passes in this order. Details, checklists and outputs are in `references/pass-sequence.md`.

1. **Structure pass.** Does the order come out of the material or get forced onto it? Is the lead sound? Does the high moment land about three-fifths of the way through? Is the ending the one the material offers?
2. **Read-aloud pass.** Read the whole draft aloud. The ear catches clunks, rhythm breaks and repetition that the eye slides over.
3. **Static pass.** Strip out the noise: showy phrasing, fad words, filler, anything that sounds like writing rather than saying.
4. **Draft No. 4 boxes.** Box every word or phrase that is wrong, or that works but could be exactly right. Then settle each box with a dictionary.
5. **Frame-of-reference pass.** Check every comparison and allusion. Will it still mean something to the reader? Is it doing its own work, or borrowing vividness from something famous?
6. **Checkpoint pass.** Tick every word that carries a fact: names, numbers, timelines, world rules. Anything you can't verify gets fixed or removed.
7. **Omission pass.** Green about ten percent. Remove lines so that nobody would notice anything is gone. See `references/greening.md`.

Then hand the draft to `sentence-craft`, and finally `style-audit`.

## How to use this in practice

1. **Measure first.** Record the word count and read the draft through once without changing anything.
2. **Pick the passes the draft needs.** A new first draft gets all seven. A near-final piece usually needs passes 4, 6 and 7.
3. **Log as you go.** For each pass, record what you looked for, three to five representative before/after changes, and the word count afterwards.
4. **Report.** Give the revised draft, the log, and the percentage cut. If you didn't reach ten percent, say what resisted cutting and why.

## Supporting lenses

- The second draft should come in about ten percent shorter than the first. Every story has slack, and failing to find a tenth usually means not looking hard. [King, On Writing]
- Before revising, rest the draft until you can read it as a stranger would. [King, On Writing]
- Revise sentence by sentence, in small changes. Judging whole chunks as "terrible" or "great" leads nowhere; the missing section may appear when you split one long sentence in two. [Klinkenborg]
- A draft's existence pushes back against real change. Treat every sentence as still open, as if you'd stopped everywhere at once. [Klinkenborg]
- Keep a who-knows-what-when chart through revision. Moving a scene moves what the reader knows. [Cron ch12]
- Revising is part of writing. Heavy surgery is not a sign of failure. [S&W V.5]
- Rich, ornate prose is hard to digest. Reread with fresh eyes and cut the excess without mercy. [S&W V.6]
- For story problems (a turn missing, a flat ending), go back to the climax and rewrite backward. Every scene must earn its place from there. [McKee ch13]

## Reference files

- The passes in full, with a checklist and output for each → `references/pass-sequence.md`
- Leads, structural shapes, endings, and choosing details → `references/leads-and-structure.md`
- Cutting ten percent without losing anything → `references/greening.md`

## Where the books disagree

- **How to draft, and so what revision has to do.** McPhee and King both blurt a first draft and fix it in later passes. Klinkenborg rejects provisional sentences and revises at the moment of composing. Resolution used here: whatever the drafting habit, run the structural and omission passes on every draft. Klinkenborg's sentence-by-sentence rereading is pass 4's method.
- **Outline or no outline?** McPhee builds structure before writing, from coded notes and index cards, and knows the ending in advance. Klinkenborg says outlines ration material and block discovery. Resolution: in revision, build the structure from the draft's existing material, McPhee's cards made from paragraphs already written. That's discovery first, structure second, which both books accept.
- **Where to start the story.** McPhee often starts at a later, stronger moment and flashes back. King prefers straight chronology. Resolution: pass 1 tests both openings. Keep whichever lead is sounder and promises only what the piece delivers.
- **Is chronology the natural order?** McPhee says chronology usually wins, because readers follow it easily. Klinkenborg warns that chronology only looks natural; it's a choice, and often a dull one. Resolution: let events keep time order when the story's cause and effect runs that way. In pass 1, ask of every section whether it's placed there for a reason, or only because that's the order the material arrived in.

## Source ledger (70/30)

| Book | Role | Tagged principles |
|---|---|---|
| John McPhee, *Draft No. 4* | Spine | 58 of 85 (68.2%) |
| Verlyn Klinkenborg, *Several Short Sentences About Writing* | Support | 7 |
| William Strunk Jr. & E. B. White, *The Elements of Style* | Support | 7 |
| Lisa Cron, *Wired for Story* | Support | 5 |
| Stephen King, *On Writing* | Support | 5 |
| Robert McKee, *Story* | Support | 3 |

Counts cover this file and `references/`. Source of truth: the `claude-code-dotfiles` repo. Recount there with `python3 tools/check_70_30.py`.
