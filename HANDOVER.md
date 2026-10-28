# Handover — the 70/30 book-skills

This file is the single place to pick up this repo and keep building. It says
what the repo is, how the skills were made, how to verify them, and what is
left to do. If you read nothing else, read **How to add the next skill** below.

Last updated: 2026-10-28. Working branch: `claude/stories-skills-70-30-rdb1cs`.

---

## What this repo is

Personal Claude Code configuration, plus a set of **skills built from books**.
Each book-skill distils one book into instructions Claude can follow, with a
fixed discipline:

- one **spine** book supplies about **70%** of the skill's principles;
- named **support** books supply the other **30%**;
- every principle is **paraphrased** (never quoted) and **source-tagged**
  (`[Berger ch3]`);
- the skill is split across a `SKILL.md` and `references/*.md`;
- a checker, `tools/check_70_30.py`, verifies the ratio and the ledger;
- craft skills are fired by **routers** (`writers-room`, `series-forge`,
  `marketing-head`).

The workflow that produces all of this is itself a skill: **`skill-forge`**.
It is the meta-skill — the one that builds the others. Start there.

## Layout

```
README.md                 repo overview + device setup
HANDOVER.md               this file
settings.json             global Claude Code settings (plugins, marketplaces)
tools/check_70_30.py      verifies every skill's 70/30 ratio and ledger
skills/
  README.md               per-skill catalogue + current counts
  skill-forge/            THE META-SKILL: how to build a book-skill
  <22 book-skills>/       SKILL.md + references/, each with a spine book
  writers-room/           router: any writing job
  series-forge/           router: sequels, prequels, continuations
  marketing-head/         router: any marketing/sales/social job
```

## The 22 books, by family

- **Story craft (7):** King *On Writing* (`story-forge`), Diamond *Guns, Germs,
  and Steel* (`worldbuilding`), McKee *Story* (`story-design`), Cron *Wired for
  Story* (`reader-brain`), McPhee *Draft No. 4* (`revision-passes`), Klinkenborg
  *Several Short Sentences* (`sentence-craft`), Strunk & White *The Elements of
  Style* (`style-audit`).
- **Series (3):** Tomlinson *Writing a Series* (`series-engine`), Scheuerer *How
  to Write a Successful Series* (`sequel-craft`), Rosett *How to Write a Series*
  (`series-doctor`).
- **Genre (3):** Highsmith *Plotting and Writing Suspense Fiction*
  (`suspense-craft`), Ligotti *The Conspiracy Against the Human Race*
  (`cosmic-horror`), Coxon & Hirst (eds.) *Writing the Uncanny* (`uncanny-craft`).
- **Naming (2):** Watkins *Hello, My Name Is Awesome* (`name-craft`), Edwards
  *Copywriting Secrets* (`title-craft`).
- **Marketing (7):** Berger *Contagious* (`contagious-content`), Eyal *Hooked*
  (`habit-hooks`), Kane *One Million Followers* (`audience-growth`), Sugarman
  *The Adweek Copywriting Handbook* (`slippery-copy`), Vaynerchuk *Jab, Jab,
  Jab, Right Hook* (`platform-native`), Schaefer *Belonging to the Brand*
  (`brand-community`), Ellis & Brown *Hacking Growth* (`growth-experiments`).

Full per-skill counts and shares are in [`skills/README.md`](skills/README.md).

## How to add the next skill

This is the whole job, short form. The long form is the `skill-forge` skill
(`skills/skill-forge/SKILL.md` and its `references/`).

1. **Extract** the book to plain text, in its own folder.
2. **Distil** it into notes — one idea per line, in your own words, with chapters.
3. **Pick** the spine (this book) and a few repo books as support.
4. **Write** `skills/<name>/SKILL.md` + `references/*.md` in the repo's anatomy
   (copy an existing skill as a template). Tag every principle. Never quote.
5. **Teach the checker** the new book: add it to `BOOKS`, the `TAG` regex,
   `LEDGER_NAMES` and `TITLES` in `tools/check_70_30.py`.
6. **Wire** the skill into its router (and `story-forge` if it is a station).
7. **Verify:** `python3 tools/check_70_30.py --write` then run it again plain;
   it must exit 0, spine share 65–75%, ledger matching counts.
8. **Document:** add the skill to `skills/README.md` (and the root `README.md`
   count if it changed).
9. **Commit and push** on the working branch. No pull request unless asked.

## How to verify the repo is sound

```bash
cd claude-code-dotfiles
python3 tools/check_70_30.py        # exit 0 = every skill's ratio and ledger are good
```

A green run means: every craft skill's spine is 65–75% of its tags, every
ledger matches the real counts, and every router (and the `skill-forge`
meta-skill) carries zero principle tags.

## Conventions that are easy to get wrong

- **Paraphrase, never quote** the source books. A tag marks where an idea came
  from; it is not licence to copy a sentence.
- **Routers carry no tags.** `writers-room`, `series-forge`, `marketing-head`,
  and `skill-forge` are marked `<!-- router ... -->` and must stay tag-free, or
  the checker fails them.
- **The "Where the books disagree" section names books without tagging them.**
  The checker skips that section when counting — keep tags out of it.
- **Don't hand-edit a ledger.** Regenerate it with `--write`.
- **A new book must be taught to the checker** before its tags count. Miss that
  and the ratio silently reads low.
- **Example tags in docs** (like in `skill-forge`) must use placeholder names
  (`[Spine ch3]`, `[Support ch5]`), never real repo book names, or the checker
  counts them.

## What's left to do (pending work)

- **Patrick Hanlon, *Primal Branding*** — discussed, never uploaded. A natural
  next marketing skill (brand belief, the seven pieces of a brand's "primal
  code"). Would support/pair with `brand-community` and `contagious-content`.
- **Russell Brunson, *Traffic Secrets*** — discussed, never uploaded. A natural
  growth/audience skill (your dream customer, traffic you own vs. earn vs. buy,
  funnels). Would pair with `audience-growth` and `growth-experiments`.
- When either book is provided, run the `skill-forge` workflow above. Remember
  to teach the checker the new book (`Hanlon`, `Brunson`).

## Installing the skills on a device

See [`README.md`](README.md). In short: copy each `skills/<name>/` directory
into `~/.claude/skills/`. Don't copy `skills/README.md`, this file, or `tools/`.
