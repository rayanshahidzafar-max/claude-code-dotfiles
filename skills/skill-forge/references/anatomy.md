# The anatomy of a skill

Every book-skill in this repo has the same parts in the same order. Copy an
existing skill (for example `contagious-content`) as a template and refill it.

## SKILL.md, top to bottom

### 1. Frontmatter

```
---
name: <kebab-case-name>
description: <what it is, built on whose book, supported by whom — then a long,
trigger-rich sentence listing the jobs and phrasings that should invoke it>
---
```

- `name` matches the folder name, kebab-case.
- `description` does two jobs: it says what the skill is and which books it rests on,
  and it packs the phrases a user might say so the skill gets picked. Study the
  descriptions of shipped skills — they are deliberately long and keyword-dense.

### 2. Spine marker

```
<!-- spine: Berger -->
```

- One HTML comment naming the spine book by its short tag-name. The checker reads this
  to know which book must hit ~70%.
- A router (fires other skills, states no principles) uses `<!-- router: ... -->`
  instead and carries zero tags.

### 3. Title and intro

- An `#` title in Title Case.
- A short paragraph on what the skill does and what it produces (name the output, e.g.
  a sheet or a plan). Then a line or two pointing to sibling skills for neighbouring jobs.
- The standing rule, stated plainly: never quote the source books; paraphrase and use
  your own examples.

### 4. Core ideas

- A bulleted list of the load-bearing principles, each **paraphrased** and each ending
  in a source tag: `[Spine ch1]`, `[Support ch5]`.
- These are the always-loaded heart of the skill. Keep them to the ideas a reader needs
  every time; send the rest to references.

### 5. How to use this in practice

- A numbered procedure that turns the principles into steps. Each step can carry its own
  tag and an arrow to the reference file that details it: `→ references/triggers.md`.

### 6. Tables and at-a-glance aids

- Where a model has named parts (STEPPS, a checklist), a table earns its place. Each row
  can be reinforced by tagged bullets beneath it.

### 7. Reference files pointer

- A short list mapping each `references/*.md` to what it covers, so a reader knows where
  to go for depth.

### 8. Where the books disagree

- A section naming real tensions between the spine and the supports, and the resolution
  this skill uses. **Name the books here without tagging them** — the checker skips this
  section when counting, because it discusses books rather than drawing principles from
  them.

### 9. Source ledger (70/30)

```
## Source ledger (70/30)

| Book | Role | Tagged principles |
|---|---|---|
| Jonah Berger, *Contagious* | Spine | 113 of 162 (69.8%) |
| Brendan Kane, *One Million Followers* | Support | 15 |
| ...                                   | Support | ...|

Counts cover this file and `references/`. Source of truth: the `claude-code-dotfiles`
repo. Recount there with `python3 tools/check_70_30.py`.
```

- Do not hand-count this. Write the table header and one placeholder row, then run
  `python3 tools/check_70_30.py --write`, which fills it from the real tag counts.

## references/*.md

- One file per topic the skill goes deep on. Named for the topic (`emotion.md`,
  `triggers.md`).
- Same rule: every principle paraphrased, every principle tagged.
- These are where most of the tags live, which is why the checker counts `SKILL.md`
  **and** `references/` together.
- Open them from `SKILL.md` only when a step needs them; they are not always-loaded.

## A good principle line

- One idea, concrete, actionable, in your own words, with a tag.
- Good: `People copy what they can see; a product nobody can see used can't spread by imitation. [Spine ch4]`
- Bad (quotes): copying the author's sentence and tagging it.
- Bad (vague): `Visibility matters. [Spine ch4]`
- Bad (untaggable): a claim with no book behind it.
