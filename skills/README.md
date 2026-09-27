# Writing skills — seven books, 70/30

Seven Claude Code skills for writing fiction, built entirely from seven books, plus one front door, `writers-room`, that fires them together with the social, persuasion and video skills. Each skill has one **spine** book that supplies about 70% of its principles. The other books supply the remaining 30% as **support**, wherever they sharpen or challenge the spine.

| Skill | Spine (≈70%) | What it does |
|---|---|---|
| `story-forge` | Stephen King, *On Writing* | The whole pipeline, from blank page to finished story. Covers the door-closed draft, the drawer, the door-open rewrite, and the 10% cut. Runs the other six as stations. |
| `worldbuilding` | Jared Diamond, *Guns, Germs, and Steel* | Derives a story world's societies, technology, plagues and conflicts from causes |
| `story-design` | Robert McKee, *Story* | Structure: values, scenes that turn, inciting incident, crisis, climax, antagonism |
| `reader-brain` | Lisa Cron, *Wired for Story* | Reads the story as a reader's brain does: goal, inner issue, cause and effect, setups |
| `revision-passes` | John McPhee, *Draft No. 4* | Revision in passes: structure, lead, boxes and dictionary, checkpoints, omission |
| `sentence-craft` | Verlyn Klinkenborg, *Several Short Sentences About Writing* | Sentence by sentence: what it says, what it implies, rhythm, names of things |
| `style-audit` | William Strunk Jr. & E. B. White, *The Elements of Style* | The final filter: usage, composition, White's reminders, misused words |

## The front door: `writers-room`

`writers-room` is the one skill to reach for. It triggers on any story, any writing, or any social media hooks and material. It then:

- sorts the job into lanes: STORY, WORLD, SOCIAL, PROSE, PERSUADE, VIDEO;
- fires every skill in those lanes, plus an always-on core (`viral-hooks`, `style-audit`, and `anti-ai-writing` as the last pass);
- settles the places where the skills disagree (em dashes, metaphor, hook vs. lead, "you" framing, reading level, real vs. invented);
- ends with a **Skills fired** ledger showing what each skill did.

It's a router: it holds no craft principles of its own, so the 70/30 check verifies that it carries no source tags. Besides the seven skills here, it calls skills from your claude.ai account (`viral-hooks`, `storytelling`, `dumbify`, `anti-ai-writing`, `storybrand`, `expert-secrets-playbook`, `sell-like-crazy`, `100m-offers`, `100m-money-models`, `seedance-shotlist-director`, `nonviolent-communication`, `habit-design`, `deep-work`). If one isn't installed where you run it, it skips that skill and says so.

The pipeline order used by `story-forge` is:

brief → worldbuilding → story-design → reader-brain → **door-closed draft** → rest → **door-open reread** → second draft (−10%) + revision-passes → sentence-craft → style-audit → readers

## The rules these skills are built on

1. **The books are 100% of the base.** Every principle in every skill traces to one of the seven books. Untagged lines are procedure only (steps, templates, file layouts), never outside craft advice.
2. **Every principle carries a source tag** naming its book and chapter, e.g. `[McKee ch14]`, `[S&W R17]`, `[McPhee, Omission]`, `[Diamond ch14]`.
3. **70/30 is counted, not guessed.** The spine book must supply between 65% and 75% of a skill's tagged principles. The count covers `SKILL.md` and `references/`.
4. **Each skill has a "Where the books disagree" section.** When books conflict (plan vs. discover, fast draft vs. finished sentences, rules vs. experiments), the section names the conflict and states the resolution used. That section is left out of the count.
5. **Paraphrase only.** No text from the books is reproduced. Concepts are restated in plain words, with original examples.

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
| story-design | McKee | 85 / 121 | 70.2% |
| story-forge | King | 68 / 95 | 71.6% |
| style-audit | Strunk & White | 59 / 82 | 72.0% |
| worldbuilding | Diamond | 67 / 97 | 69.1% |
| writers-room | router | 0 tags | routes only |

## Installing

See the main [README](../README.md#writing-skills). Copy each skill directory into `~/.claude/skills/`. Don't copy this README or `tools/`.

## Relationship to other skills

The seven book skills are for fiction and long-form prose, and each one's description points social-media work to `storytelling`, `viral-hooks` and `anti-ai-writing`. That keeps each skill's own triggering clean. `writers-room` is where they meet: it brings the book skills and the social skills into the same job, each with a defined role.
