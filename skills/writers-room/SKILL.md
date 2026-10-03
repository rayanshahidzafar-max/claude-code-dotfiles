---
name: writers-room
description: One door to every writing skill. For any story, any writing, or any social media hooks and material, it fires the whole team in the right order and settles their conflicts — social (viral-hooks, storytelling, dumbify, anti-ai-writing), story and writing (story-forge, worldbuilding, story-design, reader-brain, revision-passes, sentence-craft, style-audit), series (series-forge, which runs series-doctor, series-engine and sequel-craft), persuasion (storybrand, expert-secrets-playbook, sell-like-crazy, 100m-offers, 100m-money-models) and video (seedance-shotlist-director). Use this FIRST whenever the user asks for a story, chapter, scene, sequel, prequel or series, lore or world; an essay, article, email, bio, newsletter or script; reels, video scripts, hooks, captions, carousels, threads, posts, subject lines or ad copy; or wants any of that improved, even if they name only one skill or just say "write", "hook me" or "make content".
---

<!-- router: fires other skills and holds no craft principles of its own, so the 70/30 source check does not apply -->

# Writers' Room

Every writing job comes through this door. The room works out which lanes the job touches, fires every skill in those lanes plus the always-on core, runs them in order, and settles their disagreements before anything reaches the page. It ends with the finished piece and a **Skills fired** ledger that shows what each skill did.

## How to fire a skill

- Load each skill with the Skill tool before using it, once per conversation. The names below are base names. Your skills list may show a prefix (for example `anthropic-skills:viral-hooks`); use each name exactly as the list shows it.
- If a skill isn't installed here, skip it, say so in the ledger, and keep going. Never claim a skill ran when it didn't.
- Open a skill's reference files only when its own instructions send you there for this job.
- If the user names one skill and says "only," run just that skill. Their choice beats the room.

## Before anything: who is it for?

- If the skills list has an operating skill for the person or client the piece is for (one whose description says to consult it for them), load it first. Its standards override everything below.
- For social pieces, find a voice sample: the user's past posts, or a voice skill if one is installed. With none, write on the mechanics and mark the ledger "voice unverified," as `viral-hooks` requires.
- Anything presented as true (the user's life, clients, numbers, results) uses real material only. Fiction is invention; a post that claims to be a true story is not fiction.

## Step 1 — Read the job

Tag every lane the request touches. Most jobs touch one or two.

| Lane | The job looks like |
|---|---|
| STORY | a story, chapter, scene, fan fiction, micro-fiction post, "write me a story about…" |
| SERIES | a sequel, prequel, continuation, the next book or part, a spin-off, side story or crossover, an origin story, a series plan or series bible |
| WORLD | a setting, faction, planet, history, lore bible, game world |
| SOCIAL | hooks, reels, TikToks, video scripts, captions, carousels, threads, posts, newsletters, subject lines |
| PROSE | essays, articles, blog posts, emails, bios, speeches, cover letters, "improve this writing" |
| PERSUADE | anything that sells: ads, sales pages, pitches, offers, launches, funnels, brand one-liners |
| VIDEO | turning a script, scene or story into shots for Seedance |

A story that continues, precedes or branches off an existing one is SERIES, not STORY.

"Everything," "full stack," "the works" or "the story plus the content" means **FULL STACK** (below).

## Step 2 — Fire the stack

**The always-on core fires on every job, in every lane:**

- `viral-hooks`. Every piece has an opening. In SOCIAL and PERSUADE it writes the hook; in the other lanes it supplies candidate openings and the lane's own skills choose.
- `style-audit`. The correctness pass. Light mode (usage errors only) for social and spoken pieces.
- `anti-ai-writing`. Always the very last pass: the full pass on written text, the spoken subset on scripts.

**Then each lane's stack, in order.** Each skill's exact job is in `references/lanes.md`.

| Lane | Order |
|---|---|
| STORY | `story-forge` runs the pipeline → `worldbuilding` → `story-design` (+ `storytelling`'s but/therefore test on the outline) → `reader-brain` → draft (+ `viral-hooks` first-line candidates) → `revision-passes` (+ `dumbify` clarity check) → `sentence-craft` → `style-audit` → `anti-ai-writing` (+ `storytelling`'s last-line test) |
| SERIES | `series-forge` runs the job: `series-doctor`, `series-engine` and `sequel-craft` in its mode's order (sequel, prequel, continuation, spin-off, series plan) → the STORY stack above for the installment → its launch pack |
| WORLD | `worldbuilding` → `story-design` (pressure points) → `reader-brain` → `sentence-craft` → `dumbify` (reader-facing entries) → `viral-hooks` (entry openers) → `style-audit` → `anti-ai-writing` |
| SOCIAL | `story-design` + `reader-brain` (the turn and the stakes) → `storytelling` → `viral-hooks` → `dumbify` → `revision-passes` (cut ~10% if over ~150 words) → `sentence-craft` (written long-form only) → `style-audit` (light) → `anti-ai-writing` |
| PROSE | `revision-passes` (structure, lead) → `storytelling` (if it tells a story) → `reader-brain` (narrative nonfiction) → `sentence-craft` → `dumbify` (if it explains or teaches) → `viral-hooks` (title, subject line, first line) → `style-audit` → `anti-ai-writing` |
| PERSUADE | `storybrand` → `expert-secrets-playbook` → `100m-offers` (if there's an offer) → `100m-money-models` (if offers are sequenced) → `sell-like-crazy` (funnel stage, CTA) → `storytelling` → `viral-hooks` → `dumbify` → `style-audit` → `anti-ai-writing` |
| VIDEO | `storytelling` (script) → `viral-hooks` (visual hook) → `dumbify` → `anti-ai-writing` (spoken subset) → `seedance-shotlist-director` |

When a job touches two lanes, run the primary lane first: the deliverable the user will read or post. Then add the other lane's skills that aren't already running.

**Also in the room when the job calls for it:**
- `nonviolent-communication` for hard or conflict-laden messages.
- `habit-design` and `deep-work` for building a writing routine, alongside `story-forge`'s standing orders.
- The file-format skills (`docx`, `pdf`, `pptx`, `docs`) when the user asks for a file.

**Scale to the job.** A one-line fix still gets the core. A skill with nothing to add reports "no change needed" rather than inventing work.

## FULL STACK

1. Run the primary lane to a finished piece (STORY, for a story).
2. Build a SOCIAL pack from the finished piece:
   - hooks for the platforms the user names (three per platform; Reels and TikTok if none are named);
   - a 30–60 second reel script;
   - carousel slide text;
   - a caption.
3. VIDEO: a Seedance shotlist for the reel.
4. PERSUADE, only if there's something to sell (a book, a game, a service).

## Step 3 — Settle conflicts

The skills were written separately, and they sometimes disagree. The rulings in brief (the full table is in `references/conflicts.md`):

- **Em dashes.** `anti-ai-writing` bans them in written copy. In fiction a dash survives only for an abrupt break or interruption where no simpler mark works, per `style-audit`'s dash rule.
- **Metaphor.** `anti-ai-writing`'s analogy tests govern social, business and prose copy. In fiction, `sentence-craft`'s test governs: rare, exact, sudden.
- **Hooks.** In SOCIAL and PERSUADE, `viral-hooks` decides. In STORY and PROSE, `viral-hooks` proposes, and `reader-brain` and `sentence-craft` decide. No bait openings anywhere.
- **"You" framing.** Social hooks only. Fiction never forces "you."
- **Reading level.** `dumbify`'s targets apply to social, teaching and selling. In fiction it only flags sentences a reader must read twice.
- **Invention.** Fiction invents; anything presented as real never does. `storytelling`, `anti-ai-writing` and every persuasion skill agree.
- **Series jobs.** `series-forge`'s rulings (cliffhangers, recaps, vague canon vs. concrete prose, spoilers, prequel suspense) apply on top of these.
- **Any other tie.** The skill closest to the deliverable wins: `viral-hooks` for a hook, `storytelling` for a spoken script, `story-design` for plot, `sentence-craft` for fiction sentences, `style-audit` for grammar in formal prose, `anti-ai-writing` for voice.

## Step 4 — Deliver

Give the finished piece first, then the ledger:

```
SKILLS FIRED — lanes: SOCIAL (+ STORY)
 1. story-design      the turn: expects X, gets Y
 2. storytelling      lens "…"; 2 "and then" beats → but/therefore; last dab "…"
 3. viral-hooks       3 hooks (levers …); chose #2
 …
 9. anti-ai-writing   final pass: 2 fixes (em dash, hollow reframe)
Skipped: seedance-shotlist-director (no video asked) · voice unverified (no sample)
```

Give one line per skill: what it changed, or "no change needed." A skill that never loaded doesn't appear in the fired list.
