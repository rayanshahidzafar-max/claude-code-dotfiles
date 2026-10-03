---
name: series-forge
description: The continuation, sequel and prequel builder. For any job that continues, extends or branches a story, it fires the three series skills (series-doctor, series-engine, sequel-craft) together with the whole writing team (story-forge, worldbuilding, story-design, reader-brain, revision-passes, sentence-craft, style-audit) and the social, persuasion and video skills (viral-hooks, storytelling, dumbify, anti-ai-writing, storybrand, sell-like-crazy, 100m-offers, seedance-shotlist-director), keeps the series canon in one folder, and settles their conflicts. Use it whenever someone asks for a sequel, prequel, part two, the next book, episode or chapter in a series, a continuation of an existing story, "what happens next", an origin story or backstory novella, a spin-off, side story or crossover, a trilogy, saga or season plan, a series bible or canon check, or wants to turn a standalone story into a series.
---

<!-- router: fires other skills and holds no craft principles of its own, so the 70/30 source check does not apply -->

# Series Forge

Every job that continues a story comes through here: a sequel, a prequel, a continuation past the ending, a spin-off, or a whole series plan. The forge finds the canon and names the mode. It fires the three series skills in the right order, runs the full writing team on the installment, and builds a launch pack. It ends with the canon updated and a **Skills fired** ledger.

## How to fire a skill

- Load each skill with the Skill tool before using it, once per conversation. The names below are base names. Your skills list may show a prefix (for example `anthropic-skills:viral-hooks`); use each name exactly as the list shows it.
- If a skill isn't installed here, skip it, say so in the ledger, and keep going. Never claim a skill ran when it didn't.
- Open a skill's reference files only when its own instructions send you there for this job.
- If the user names one skill and says "only", run just that skill.
- A skill with nothing to add reports "no change needed" rather than inventing work.

## Step 0 — Find the canon

- **Read the source in full** before writing a word of the continuation: every earlier installment the new one touches, start to finish. Continuity breaks when a continuation is built from memory or a summary.
- **Open the series folder,** `stories/series/<series-slug>/` (layout in `references/modes.md`). If it doesn't exist yet, create it: `series-engine` writes the outline and the bible, `sequel-craft` the loop ledger, and `series-doctor` the reader path.
- **Published books but no bible?** Build the bible from the books before anything else.
- **Who is it for?** If the skills list has an operating skill for the person or client the series belongs to, load it first, as `writers-room` does. Its standards override everything below.

## Step 1 — Name the mode

| Mode | The job looks like |
|---|---|
| SEQUEL | the next book, part two, "what happens next", the next episode or chapter of a series |
| PREQUEL | an origin story, "before the story", a backstory novella, a book zero, how they met |
| CONTINUATION | going past a planned ending: a new season or arc, years later, extending a finished series, turning a standalone into a series |
| SPIN-OFF | another character's own story, a side story running alongside, a crossover, a companion, a second series in the same world |
| SERIES PLAN | designing a trilogy, saga or season before the books exist; a series bible; a canon check |

If a job fits two modes, run the mode that produces the deliverable and borrow the other's checks. Name the mode at the top of the ledger.

## Step 2 — Fire the series stack

The three series skills run first, in the mode's order. Each skill's exact job in each mode is in `references/modes.md`.

| Mode | Order |
|---|---|
| SEQUEL | `series-doctor` (checkup: type, pattern, what readers loved, what's stuck) → `series-engine` (engine and arcs, bible) → `sequel-craft` (installment plan, loop ledger) |
| PREQUEL | `series-engine` (the canon timeline: what's fixed) → `sequel-craft` (prequel method, installment plan) → `series-doctor` (its place on the reader path) |
| CONTINUATION | `series-doctor` (extend, relaunch or end?) → `series-engine` (the new arc or season; does the engine still run?) → `sequel-craft` (installment plan) |
| SPIN-OFF | `series-doctor` (what carries over, and when) → `series-engine` (the spin-off's own pilot, inside the shared bible) → `sequel-craft` (links, spoiler-free references, installment plan) |
| SERIES PLAN | `series-engine` (outline, engines, units, arcs, bible) → `series-doctor` (type and pattern check, exits, reader path) → `sequel-craft` (each book's question asked and answered; the first plants) |

## Step 3 — Fire the writing team on the installment

When there's an installment to write, run the STORY lane, with `story-forge` running the stations. The installment plan goes into `00-brief.md` as its SERIES block, and every station gets a series duty:

| Station | Skill | Series duty |
|---|---|---|
| 1 World | `worldbuilding` | only what's new or changed since the last book; every new fact checked against the bible |
| 2 Design | `story-design` (+ `storytelling`'s but/therefore test) | the book's own spine, plus this book's segment of each long arc |
| 3 Reader check | `reader-brain` | two reads: one as a newcomer starting here, one as a returning reader |
| 4 Draft | `story-forge` (+ `viral-hooks` first-line candidates) | the ledger's due plants go in; nothing contradicts the canon |
| 7 Revision | `revision-passes` (+ `dumbify` clarity check) | a continuity pass against the bible; recaps cut to the minimum |
| 8 Sentences | `sentence-craft` | fresh wording for every recap and reintroduction |
| 9 Audit | `style-audit` | the series style sheet joins the audit |
| Last | `anti-ai-writing` (+ `storytelling`'s last-line test) | the last page checked as the hook for the next book |

Then update the canon: mark the ledger rows this book paid or opened, add new facts to the bible tagged with this book's number, and update the reader path.

## Step 4 — The launch pack

By default the forge also builds the material that sells the installment and moves readers along the path. "No launch pack" skips it.

- **Series line and blurb.** `storybrand` writes the one-line promise, `storytelling` the blurb's story, and `viral-hooks` its first line; then `dumbify`, `style-audit`, `anti-ai-writing`. No spoilers for earlier books.
- **Back-matter page.** The read-through hook or teaser for the next book and the reading order, from `sequel-craft` and `series-doctor`.
- **Social pack.** Three hooks per platform, a 30–60 second reel script, carousel text and a caption (`viral-hooks`, `storytelling`, `dumbify`, `anti-ai-writing`).
- **Video.** A Seedance shotlist for the reel (`seedance-shotlist-director`).
- **Reader gift or offer,** only when there's a list to build or something to sell: a prequel giveaway, a bundle, a preorder. Use `expert-secrets-playbook`, `100m-offers`, `100m-money-models` and `sell-like-crazy`, with their honesty rules in force.

**Also in the room when the job calls for it:** `habit-design` and `deep-work` for a multi-book writing schedule or a batch-writing plan; the file-format skills (`docx`, `pdf`, `pptx`, `docs`) when the user asks for a file, such as a series bible as a document.

## Step 5 — Settle conflicts

The rulings in brief (the full table is in `references/conflicts.md`):

- **Cliffhangers.** Every book answers its own main question. The pull to the next book comes from a new question opened after that answer.
- **Recaps.** Woven into the story, cut to the minimum, in fresh words. A front-matter recap only after a long gap or with a big cast.
- **Vague canon, concrete prose.** Specific in the scene; flexible on facts a later book may need to move.
- **Plan or discover.** Plan the plants that later reveals depend on; discover the rest.
- **Spoilers.** Hooks, blurbs and recaps tease the question, never an earlier book's answer.
- **Honesty.** Never announce a series length that isn't written, never fake "last chance" urgency, never invent reader quotes.
- Everything else falls back on `writers-room`'s rulings.

## Step 6 — Deliver

Give the installment (or the plan) first, then the updated canon files, then the launch pack, then the ledger:

```
SKILLS FIRED — mode: SEQUEL (book 2 of "…")
 1. series-doctor     robust-arc lead, linked-trilogy pattern; stuck: …; fix: …
 2. series-engine     engine still runs (…); arc B moves to book 3; bible opened
 3. sequel-craft      answers "…", asks "…"; 4 payoffs due, 3 new plants; soft cliffhanger
 4. story-forge       stations 0–9; draft 1 #### → draft 2 #### (−##%)
 …
14. anti-ai-writing   final pass; last page checked as the hook
Canon: bible +12 facts (book 2) · ledger 4 paid, 3 opened · reader path updated
Skipped: …
```

Give one line per skill: what it changed, or "no change needed". A skill that never loaded doesn't appear in the fired list.

## Scale

- **A short story continuation** (a few thousand words): the whole pipeline runs in one session, to a finished story.
- **A novel-length installment:** this session delivers the plan, the canon files and a chapter-by-chapter outline. Drafting then continues chapter by chapter in later sessions, carrying the ledger and the bible forward.
- **A plan only:** say "plan only". The series stack runs and the canon files are written, but no installment is drafted and no launch pack is built.
