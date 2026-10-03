# Writing skills — ten books, 70/30

Ten Claude Code skills built entirely from ten books, plus two front doors:

- `writers-room` fires the whole team for any writing job.
- `series-forge` builds sequels, prequels and continuations.

Each book skill has one **spine** book that supplies about 70% of its principles. The other nine books supply the remaining 30% as **support**, wherever they sharpen or challenge the spine.

## The story skills (seven craft books)

| Skill | Spine (≈70%) | What it does |
|---|---|---|
| `story-forge` | Stephen King, *On Writing* | The whole pipeline, from blank page to finished story. Covers the door-closed draft, the drawer, the door-open rewrite, and the 10% cut. Runs the other six as stations. |
| `worldbuilding` | Jared Diamond, *Guns, Germs, and Steel* | Derives a story world's societies, technology, plagues and conflicts from causes |
| `story-design` | Robert McKee, *Story* | Structure: values, scenes that turn, inciting incident, crisis, climax, antagonism |
| `reader-brain` | Lisa Cron, *Wired for Story* | Reads the story as a reader's brain does: goal, inner issue, cause and effect, setups |
| `revision-passes` | John McPhee, *Draft No. 4* | Revision in passes: structure, lead, boxes and dictionary, checkpoints, omission |
| `sentence-craft` | Verlyn Klinkenborg, *Several Short Sentences About Writing* | Sentence by sentence: what it says, what it implies, rhythm, names of things |
| `style-audit` | William Strunk Jr. & E. B. White, *The Elements of Style* | The final filter: usage, composition, White's reminders, misused words |

## The series skills (three books on writing series)

| Skill | Spine (≈70%) | What it does |
|---|---|---|
| `series-engine` | Paul Tomlinson, *Writing a Series* | Designs the series as a story engine: premise line, the seven engines, episodic/serial/hybrid, units and seasons, arcs across books, renewable suspense, the pilot, and the living series bible |
| `sequel-craft` | Helen B. Scheuerer, *How to Write a Successful Series* | Plans each installment so it stands complete and pulls readers on: the question each book answers and asks, recaps, foreshadowing, breadcrumbs, open loops, cliffhangers, prequels, finales, and the loop ledger |
| `series-doctor` | Sara Rosett, *How to Write a Series* | Diagnoses and grows a series: its type and pattern, fixes for stuck problems, extending, ending, spin-offs, universes, companions, crossovers, and the reader path between books |

## The front doors

### `writers-room`: any writing job

`writers-room` is the one skill to reach for. It triggers on any story, any writing, or any social media hooks and material. It then:

- sorts the job into lanes: STORY, SERIES, WORLD, SOCIAL, PROSE, PERSUADE, VIDEO;
- fires every skill in those lanes, plus an always-on core (`viral-hooks`, `style-audit`, and `anti-ai-writing` as the last pass);
- settles the places where the skills disagree (em dashes, metaphor, hook vs. lead, "you" framing, reading level, real vs. invented);
- ends with a **Skills fired** ledger showing what each skill did.

### `series-forge`: sequels, prequels and continuations

`series-forge` takes every job that continues a story. It:

- reads the earlier installments in full and opens the series canon folder (`stories/series/<slug>/`: outline, bible, loop ledger, reader path);
- names the mode: SEQUEL, PREQUEL, CONTINUATION, SPIN-OFF or SERIES PLAN;
- fires `series-doctor`, `series-engine` and `sequel-craft` in that mode's order;
- runs the whole writing team on the installment through `story-forge`, giving each station a series duty;
- builds a launch pack by default: series line and blurb, back-matter teaser, social pack, Seedance shotlist, and a reader gift or offer when there's something to give or sell;
- settles the series conflicts (cliffhangers, recaps, vague canon vs. concrete prose, spoilers, prequel suspense);
- ends with the canon updated and a **Skills fired** ledger.

Both front doors are routers: they hold no craft principles of their own, so the 70/30 check verifies that they carry no source tags. Besides the ten skills here, they call skills from your claude.ai account (`viral-hooks`, `storytelling`, `dumbify`, `anti-ai-writing`, `storybrand`, `expert-secrets-playbook`, `sell-like-crazy`, `100m-offers`, `100m-money-models`, `seedance-shotlist-director`, `nonviolent-communication`, `habit-design`, `deep-work`). If one isn't installed where you run it, they skip it and say so.

The pipeline order used by `story-forge` is:

brief → worldbuilding → story-design → reader-brain → **door-closed draft** → rest → **door-open reread** → second draft (−10%) + revision-passes → sentence-craft → style-audit → readers

## The rules these skills are built on

1. **The books are 100% of the base.** Every principle in every skill traces to one of the ten books. Untagged lines are procedure only (steps, templates, file layouts), never outside craft advice.
2. **Every principle carries a source tag** naming its book and chapter or section, e.g. `[McKee ch14]`, `[S&W R17]`, `[McPhee, Omission]`, `[Diamond ch14]`, `[Tomlinson ch4]`, `[Scheuerer ch13]`, `[Rosett, Troubleshooting]`.
3. **70/30 is counted, not guessed.** The spine book must supply between 65% and 75% of a skill's tagged principles. The count covers `SKILL.md` and `references/`.
4. **Each skill has a "Where the books disagree" section.** When books conflict (plan vs. discover, fast draft vs. finished sentences, cliffhanger vs. closure, vague canon vs. concrete prose), the section names the conflict and states the resolution used. That section is left out of the count.
5. **Paraphrase only.** No text from the books is reproduced. Concepts are restated in plain words, with original examples.

Rosett's book has no numbered chapters, so its tags name her sections: Introduction, Why, Types, Arcs, Patterns, Hooks, Ending, Connecting, Extending, Batch Writing, Troubleshooting, Marketing, Overwhelm.

## Checking the ratio

```bash
python3 tools/check_70_30.py          # verify every skill; exits 1 on failure
python3 tools/check_70_30.py --write  # after editing a skill: refresh each "Source ledger" table
```

Current counts:

| Skill | Spine | Spine / total | Share |
|---|---|---|---|
| reader-brain | Cron | 50 / 72 | 69.4% |
| revision-passes | McPhee | 58 / 85 | 68.2% |
| sentence-craft | Klinkenborg | 41 / 59 | 69.5% |
| sequel-craft | Scheuerer | 99 / 140 | 70.7% |
| series-doctor | Rosett | 87 / 125 | 69.6% |
| series-engine | Tomlinson | 116 / 165 | 70.3% |
| story-design | McKee | 85 / 121 | 70.2% |
| story-forge | King | 68 / 95 | 71.6% |
| style-audit | Strunk & White | 59 / 82 | 72.0% |
| worldbuilding | Diamond | 67 / 97 | 69.1% |
| series-forge | router | 0 tags | routes only |
| writers-room | router | 0 tags | routes only |

## Installing

See the main [README](../README.md#writing-skills). Copy each skill directory into `~/.claude/skills/`. Don't copy this README or `tools/`.

## Relationship to other skills

The seven story skills are for fiction and long-form prose. Each one's description points social-media work to `storytelling`, `viral-hooks` and `anti-ai-writing`, which keeps each skill's triggering clean. The three series skills sit one level up: they plan across books, and `story-forge` still writes each book. `writers-room` and `series-forge` are where all of them meet, each skill with a defined role.
