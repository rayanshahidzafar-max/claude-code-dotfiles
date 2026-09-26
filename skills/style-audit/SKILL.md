---
name: style-audit
description: Final-pass prose audit built on Strunk & White's "The Elements of Style" (supported by King, Klinkenborg, McPhee, McKee and Cron) — the rules of usage and composition (active voice, positive form, concrete language, omit needless words, parallel form, emphatic endings), White's reminders on style, and commonly misused words. Use it whenever someone asks to proofread, copy-edit, line-edit, polish, check grammar, punctuation or usage, "clean this up," "is this correct," or wants a last check before publishing, submitting or sending any prose (fiction, essays, articles, lore, cover letters, emails). Also the last station of the story-forge pipeline.
---

<!-- spine: S&W -->

# Style Audit

The last filter before a piece goes out. It produces an **audit report**: a table of every finding with its location, the rule, the original, the fix, and a one-line reason, followed by the corrected text. It isn't a rewrite in a new voice. The job is to make the writer's own prose plain, correct and clear, not to replace it.

**Important:** never quote or reproduce text from the source books. Paraphrase the rules, use your own examples, and apply them to the person's text.

## The attitude behind the rules

- Style is approached through plainness, simplicity, orderliness and sincerity. It isn't a garnish added on top. [S&W V]
- To have a style, begin by affecting none. Put yourself in the background and draw attention to the sense of the writing, not to the writer. [S&W V.1]
- Readers are often struggling, so sympathize with them. But never talk down; nobody writes well while distrusting the reader's intelligence. [S&W V]
- Write for the one reader you trust, not for a crowd. Don't chase what you imagine the market wants. [S&W V]
- Good writing rests on faith in the work and the reader, not on grammatical tricks. The rules serve clarity. They aren't the point. [S&W V]
- Forceful writing is compact, and every word must do work. That doesn't mean every sentence is short or every detail cut. [S&W R17]

## How to run the audit

Work through the text in this order. Each pass has its own reference file.

1. **Usage** (rules 1–11): possessives, commas, splices, fragments, colons, dashes, agreement, pronoun case, dangling modifiers. → `references/rules.md`
2. **Composition** (rules 12–22): design, paragraphs, active voice, positive form, concrete language, needless words, loose sentences, parallelism, related words together, tense in summaries, emphatic endings. → `references/rules.md`
3. **Reminders** (White's 21): overwriting, overstatement, qualifiers, breeziness, explaining too much, awkward adverbs, who is speaking, fancy words, dialect, clarity, opinion, figures of speech, shortcuts, foreign phrases, the standard over the offbeat. → `references/reminders.md`
4. **Misused words:** check the text against the list. → `references/misused-words.md`
5. **Matters of form**:
   - Don't put colloquialisms in quotation marks as if apologizing for them. [S&W III]
   - Don't use exclamation marks to emphasize plain statements. Save them for true exclamations. [S&W III]
6. **Mechanical flags from the other books** (below): run them as a search pass.
7. **Report** with the template in `references/audit-report.md`.

## When to overrule a rule

- The rules are a guide, not a cage. Writers often steer by stars that are themselves moving. When an ear-tested sentence breaks a rule and reads better, keep it, and note why in the report. [S&W V]
- Revising is part of writing. Heavy surgery is no sign of defeat, and it's worth keeping both versions to compare. [S&W V.5]
- In fiction, dialogue follows the character's speech, not the rules. Audit the narration strictly and the dialogue only for clarity and attribution. [S&W V.15]

## Mechanical flags from the other books

Search for these and judge each hit. Not every hit is an error.

- Adverbs, especially on dialogue tags: "he said angrily." Context should already carry the manner. [King, Toolbox]
- Verbs doing the work of "said" ("she hissed," "he chortled"). Plain "said" disappears; fancy tags call attention to themselves. [King, Toolbox]
- Passive voice, which usually hides the actor and reads as timid. [King, Toolbox]
- Dressed-up vocabulary, chosen to impress rather than to mean. [King, Toolbox]
- Fragments. Keep a fragment only if it's deliberate and does work for pace or emphasis. [King, Toolbox]
- Paragraph length as a map of intent. Walls of text look forbidding; strings of one-liners look breathless. Check the shape of the page. [King, Toolbox]
- Sentences opening with "There is/are" or "It is/was." [Klinkenborg]
- Counts of "to be" verbs. A cluster signals a static passage. [Klinkenborg]
- "With" and "as" used as all-purpose joiners. [Klinkenborg]
- Nouns built from verbs ("made an examination of" → "examined"). [Klinkenborg]
- Forced-logic words: "moreover," "thus," "indeed," "in fact." [Klinkenborg]
- Volunteer phrases and clichés. [Klinkenborg]
- Ambiguity read by the literal reader: any sentence that can be taken two ways. [Klinkenborg]
- The ear test: read the passage aloud and mark every place the ear catches. [Klinkenborg]
- Indirection: a new thing slipped in with "the," as if the reader already knew it. [McPhee, Draft No. 4]
- A word-frequency count to catch fad words, repeated "but"s, and distinctive words used more than once. [McPhee, Structure]
- Dictionary checks on any word used for its sound rather than its exact meaning. [McPhee, Draft No. 4]
- Borrowed vividness: "she looked like [a famous person]" with no description of our own. [McPhee, Frame of Reference]
- In description, "is," "are" and "there is." Every metaphor must pass the test: what do I actually see or hear? [McKee ch18]
- In dialogue, a line that announces its own cleverness. [McKee ch18]
- Any metaphor the reader can't grasp at reading speed. [Cron ch6]
- The author editorializing inside the narration, telling the reader what to think of a character or event. [Cron ch3]
- The author on stage: passages about the writer's own feelings, process or cleverness rather than the subject. [McPhee, Omission]

## Reference files

- Rules 1–22 with examples and fixes → `references/rules.md`
- White's 21 reminders → `references/reminders.md`
- Commonly misused words → `references/misused-words.md`
- The report template → `references/audit-report.md`

## Where the books disagree

- **Rules or experiments?** Strunk & White issue rules. Klinkenborg says there are only experiments, to test by ear. Resolution used here: apply the rules as the default, and flag any deliberate exception that survives reading aloud. Don't silently "correct" it.
- **Fragments.** Rule 6 warns against breaking sentences in two by accident. King defends the well-turned fragment. Resolution: flag accidental fragments; leave deliberate ones in fiction that are working for rhythm.
- **Adverbs.** White says avoid explaining manner after "he said." King calls adverbs dandelions but keeps one when it does real work. Resolution: flag every adverb on a tag, and keep only those whose meaning can't be carried by the line itself.
- **The paragraph.** Rule 13 makes the paragraph a unit built around one topic. King treats fiction paragraphs as beats of rhythm. Klinkenborg rejects the topic-sentence model. Resolution: in exposition and essays, audit for one topic per paragraph. In fiction, audit only for dialogue (each speaker a new paragraph) and for unreadable walls.
- **Write for a reader, or for yourself?** Cron and King write toward a reader, the Ideal Reader. White warns never to seek to know the reader's wants. Resolution: write for one real person you trust, never for an imagined market.

## Source ledger (70/30)

| Book | Role | Tagged principles |
|---|---|---|
| William Strunk Jr. & E. B. White, *The Elements of Style* | Spine | 59 of 82 (72.0%) |
| Verlyn Klinkenborg, *Several Short Sentences About Writing* | Support | 8 |
| Stephen King, *On Writing* | Support | 6 |
| John McPhee, *Draft No. 4* | Support | 5 |
| Robert McKee, *Story* | Support | 2 |
| Lisa Cron, *Wired for Story* | Support | 2 |

Counts cover this file and `references/`. Source of truth: the `claude-code-dotfiles` repo. Recount there with `python3 tools/check_70_30.py`.
