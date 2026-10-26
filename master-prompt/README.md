# The master prompt

The master prompt is the set of standing instructions every Fig reads before anything else: before its own personality, before what it knows about you, before your message. It says what a Fig is for, how it speaks, what it never does, and how it acts in the world.

**Current version: [v16](v16.md)**, last changed 20 October 2026. Every version and what changed: [CHANGELOG](../CHANGELOG.md).

## What a Fig reads, in layers

1. **The master prompt.** The same for every Fig.
2. **Its persona.** The name, personality, humour, voice and backstory you chose for it, or a prompt you wrote for it yourself. The master prompt calls this "configuration, not memory": it describes the Fig, never you.
3. **What it knows about you.** See [How a Fig learns about you](../memory.md).
4. **The room.** A group or shared room adds its own rules for that room.
5. **Task instructions.** Longer instructions for one kind of task, such as writing reflections for your board or building an app.

When these disagree, the order is written into the master prompt itself, with the privacy and safety floors on top. See [the floors](../intentions.md#the-floors).

## What is in this edition

55% of v16 is published word for word: 6,931 of its 12,670 words. The rest is summarized where it sits, in blocks marked *Summarized in this edition*:

| Section | What is summarized |
|---|---|
| Available capabilities and current authority | the whole section |
| Who you are | how the Fig's settings reach it, and how its personal notes about showing up are written |
| How you speak | the whole voice: its register, length and rhythm, its thoughts and stage directions, how it handles time, sharing and asking, how it takes on your words, and its formatting and punctuation |
| What you never do | how a Fig answers questions about what it is and about privacy; the habits of speech it avoids |
| How you tailor yourself to the human | one paragraph, on when memory is written |
| Your knowledge | what the Fig has in front of it, old memory against new, and search (one summary); meeting someone who has connected nothing |
| How you work | long tasks; interrupted and redirected tasks; the evidence behind each reply |
| Acting in the world | honesty about outcomes; two of the five places it looks; connecting accounts, email and location |
| Later: wake-ups and the look-ahead | everything except the paragraph on location |
| Forget, correct, off the record | how forgetting is carried out |
| The canvas: more than words | which buttons and cards can appear where |
| Skills and tools | the whole section |
| Editing yourself | changes a Fig makes to itself without being asked |
| Building things | the whole section |
| The Reflections board | when reflections arrive |

There are three reasons. Most of these parts describe how the system works behind the scenes, and we publish what Figs are asked to do, never how Figs are built. From v16, the voice is summarized too: what a Fig does when it speaks is described, but the words that make its voice are not published. And one paragraph holds the privacy facts a Fig repeats when asked; it stays summarized until each fact has been checked against our privacy policy. Each summary says what that part makes a Fig do, including what it limits, and nothing was summarized to sound better than it is. The purpose, the principles, the critical rules, the order of precedence, the safety floors, and the rules on correcting and going off the record are published in full.

[`edition.json`](edition.json) records the decision for every block of the master prompt. It keeps a preview only of blocks published word for word, so it never repeats what the edition leaves out.

## How an edition is made

We keep the master prompt itself with the rest of the product. The public edition is built from that exact file:

```bash
# bring the decisions up to date with a new version (new or changed blocks become "todo")
python3 scripts/build_edition.py sync  --source path/to/master-prompt.v17.md --spec master-prompt/edition.json
# decide each "todo" block in edition.json, then build
python3 scripts/build_edition.py build --source path/to/master-prompt.v17.md --spec master-prompt/edition.json --out master-prompt/v17.md
```

- **Word for word means byte for byte.** A block is a heading, a paragraph or a single list item, and verbatim blocks are copied exactly. The one change is display only: a `<` outside code is written as `&lt;` so GitHub shows it instead of hiding it.
- **Nothing changes silently.** Each block is identified by a fingerprint of its exact text. A block that is new, or that changed by a single character, stops the build until someone decides whether it is published word for word or summarized.
- **You can tell which file it came from.** The edition prints the sha256 of the exact file it was built from.
- **The title is the edition's.** The file a Fig runs can keep a working title on its first line. The edition's title gives the version it is published as, and the edition says so.

## Where it is used

Version 16 is the master prompt of our newest Figs, which a first group of testers uses today. Other Figs still follow an earlier set of instructions with the same intentions but not this text. We will update this page when that changes.

## Not published yet

The master prompt is the core, but a Fig also follows other written instructions. These are next, in this order:

1. **Reflections.** The instructions a Fig follows when it writes cards for your board, the main way it reaches out first.
2. **Observations and mental models.** How a Fig turns what happens into notes about you. Summarized today in [How a Fig learns about you](../memory.md).
3. **Persona nuances.** How a Fig refines its own personality over time, and the limits on that.
4. **Group and room conduct.** How Figs behave in rooms with more than one person.
