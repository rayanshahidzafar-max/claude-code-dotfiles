---
name: style-audit
description: Final-pass prose audit built on Strunk & White's "The Elements of Style", checked against Strunk's 1918 original (supported by King, Klinkenborg, McPhee, McKee, Cron, Highsmith, Ligotti and Writing the Uncanny) — the rules of usage and composition (active voice, positive form, concrete language, omit needless words, parallel form, emphatic endings), the topic-sentence paragraph, White's reminders on style, commonly misused words, matters of form, and drills for faults that keep coming back. Use it whenever someone asks to proofread, copy-edit, line-edit, polish, check grammar, punctuation or usage, "clean this up," "is this correct," or wants a last check before publishing, submitting or sending any prose (fiction, essays, articles, lore, cover letters, emails). Also the last station of the story-forge pipeline.
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
- Style isn't a surface manner. It is how the writer sees, showing where the subject meets the way it is told. An audit that flattens a voice into neutral prose has removed the style, not corrected it. [Ligotti, Style]

## How to run the audit

Work through the text in this order. Each pass has its own reference file.

1. **Usage** (rules 1–11): possessives, commas, splices, fragments, colons, dashes, agreement, pronoun case, dangling modifiers. → `references/rules.md`
   - The finer comma and semicolon points from Strunk's 1918 original → `references/strunk-1918.md`
2. **Composition** (rules 12–22): design, paragraphs, active voice, positive form, concrete language, needless words, loose sentences, parallelism, related words together, tense in summaries, emphatic endings. → `references/rules.md`
   - In essays and other exposition, also check paragraph shape against the 1918 topic-sentence rule. → `references/strunk-1918.md`
3. **Reminders** (White's 21): overwriting, overstatement, qualifiers, breeziness, explaining too much, awkward adverbs, who is speaking, fancy words, dialect, clarity, opinion, figures of speech, shortcuts, foreign phrases, the standard over the offbeat. → `references/reminders.md`
4. **Misused words:** check the text against both lists, the later edition's and Strunk's 1918 entries. When one turns up, recast the sentence instead of swapping a synonym. → `references/misused-words.md`
5. **Matters of form**:
   - Don't put colloquialisms in quotation marks as if apologizing for them. [S&W III]
   - Don't use exclamation marks to emphasize plain statements. Save them for true exclamations. [S&W III]
   - For manuscripts and reports, run the full checklist (numerals, parentheses, quotations, references, titles, spelling). → `references/strunk-1918.md`
6. **Mechanical flags from the other books** (below): run them as a search pass.
7. **Report** with the template in `references/audit-report.md`.
8. **Drill (optional):** if the same fault shows up three or more times, offer a short drill built from the writer's own sentences. → `references/strunk-1918.md`

## When to overrule a rule

- The rules are a guide, not a cage. Writers often steer by stars that are themselves moving. When an ear-tested sentence breaks a rule and reads better, keep it, and note why in the report. [S&W V]
- Rewriting belongs to the job, not after it. Heavy surgery is no sign of defeat, and it's worth keeping both versions to compare. [S&W V.5]
- In fiction, dialogue follows the character's speech, not the rules. Audit the narration strictly and the dialogue only for clarity and attribution. [S&W V.15]
- A repeated word can be doing work. Repeating an adjective can thicken a mood: a blurred moon that casts a blurred light. Before "fixing" a repetition, ask whether it earns its place. [Uncanny, McKnight Hardy]
- In first-person or close narration, a stiff connective or a pompous word may be the narrator's character, a clue the writer planted on purpose. Audit it as voice, and ask before cutting. [Uncanny, Shearman]
- In horror and weird fiction, intense figurative language may be the only bridge to an experience the reader has never had. Audit those figures for concreteness and control, not for plainness. [Ligotti, Sickness]

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
- Unclear sentences. Clarity comes first and is the best single guide to style. On the first read, write "unclear" in the margin and come back to it. [Highsmith ch8]
- A passage an editor or test reader found unclear. Readers will stumble there too, even if it has already been rewritten twice, so clarify it again. [Highsmith ch9]
- Redundant sentences. Strike them on the first pass, because prose isn't sacred. [Highsmith ch8]
- Rounding-off sentences at the end of a chapter or section that tell readers what they already know. Cut them. [Highsmith ch8]
- Verbs that set the mood. Check that each key verb carries the intended feeling: a door that shuts someone out is not a door that closes behind them. [Highsmith ch6]
- Announced emotion: narration that declares the feeling ("the sea was so frightening!") instead of creating it. The reader feels nothing. [Uncanny, Royle]
- Overwrought prose and overexplained thoughts. [Uncanny, Royle]
- A key word that has gone flat. A word's history can restore its bite ("worry" once meant to seize by the throat). Check the etymology before reaching for a fancier word. [Uncanny, Jarvis]

## Reference files

- Rules 1–22 with examples and fixes → `references/rules.md`
- White's 21 reminders → `references/reminders.md`
- Commonly misused words, including Strunk's 1918 entries → `references/misused-words.md`
- Strunk's 1918 original: the edition map, finer punctuation, the topic-sentence paragraph, matters of form, spelling and drills → `references/strunk-1918.md`
- The report template → `references/audit-report.md`

## Where the books disagree

- **Rules or experiments?** Strunk & White issue rules. Klinkenborg says there are only experiments, to test by ear. Resolution used here: apply the rules as the default, and flag any deliberate exception that survives reading aloud. Don't silently "correct" it.
- **Fragments.** Rule 6 warns against breaking sentences in two by accident, though Strunk's 1918 text itself lets an emphatic word stand alone when the emphasis is earned. King defends the well-turned fragment. Resolution: flag accidental fragments; leave deliberate ones that are working for rhythm or emphasis.
- **Adverbs.** White says avoid explaining manner after "he said." King calls adverbs dandelions but keeps one when it does real work. Resolution: flag every adverb on a tag, and keep only those whose meaning can't be carried by the line itself.
- **The paragraph.** Rule 13 makes the paragraph a unit built around one topic, and the 1918 original adds a topic-sentence rule. King treats fiction paragraphs as beats of rhythm. Klinkenborg rejects the topic-sentence model. Strunk's 1918 text already exempts short paragraphs of fast narrative, where the break itself does the work. Resolution: in exposition and essays, audit for one topic per paragraph and the topic-sentence shape. In fiction, audit only for dialogue (each speaker a new paragraph) and for unreadable walls.
- **Plain or febrile?** S&W ask for plainness and concrete words. Ligotti defends feverish, metaphor-rich prose for nightmare. The essayists in *Writing the Uncanny* want startling figures and the occasional deliberate repetition. Resolution: in horror and weird fiction, audit figures for concreteness and control, not plainness. Cut vague intensifiers such as "indescribable" or "eldritch," and keep any metaphor that makes the impossible visible.
- **Split infinitives.** The 1918 original treats them as a fault. The later edition lets a split stand when it reads better. Resolution: flag only the clumsy ones.
- **Write for a reader, or for yourself?** Cron and King write toward a reader, the Ideal Reader. White warns against trying to guess what readers want. Resolution: write for one real person you trust, never for an imagined market.

## Source ledger (70/30)

| Book | Role | Tagged principles |
|---|---|---|
| William Strunk Jr. & E. B. White, *The Elements of Style* | Spine | 86 of 121 (71.1%) |
| Verlyn Klinkenborg, *Several Short Sentences About Writing* | Support | 8 |
| Stephen King, *On Writing* | Support | 6 |
| John McPhee, *Draft No. 4* | Support | 5 |
| Patricia Highsmith, *Plotting and Writing Suspense Fiction* | Support | 5 |
| Dan Coxon & Richard V. Hirst (eds.), *Writing the Uncanny* | Support | 5 |
| Robert McKee, *Story* | Support | 2 |
| Lisa Cron, *Wired for Story* | Support | 2 |
| Thomas Ligotti, *The Conspiracy Against the Human Race* | Support | 2 |

Counts cover this file and `references/`. Source of truth: the `claude-code-dotfiles` repo. Recount there with `python3 tools/check_70_30.py`.
