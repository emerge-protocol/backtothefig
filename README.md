# Back to the Fig, in the open

On [backtothefig.com](https://backtothefig.com) we make four promises to the people who use Figs. One of them reads: *“The intentions are transparent. A public Masterprompt, and each message is explained.”*

This repository keeps that promise. It is where we publish what Figs are for, the instructions they run on, how we check whether they do what we say, and what changes along the way.

## Start here

| | |
|---|---|
| [What Figs are for](intentions.md) | What a Fig is trying to do in your life, what it must never optimize for, and the rules no instruction can override. |
| [The master prompt](master-prompt/) | The instructions every Fig reads before it talks to you, published word for word except where marked, with the reason for every summary. Plus [how we write it](master-prompt/how-we-write-it.md). |
| [How a Fig learns about you](memory.md) | What it keeps, how it decides what matters, how you correct it, and how you make it forget. |
| [How we check](evals/) | The Humanity Eval: what we measure instead of attention, how we measure it, and what we are still building. |
| [What changed](CHANGELOG.md) | Every version of the master prompt: what changed and why. |
| [Updates](updates/) | Notes from the team as we build. |
| [Tell us](FEEDBACK.md) | When a Fig does something that goes against what is written here. |

## Why we publish this

An AI that knows your calendar, your messages and the people you love should have its intentions on the table. The default business model for consumer apps is attention, and an app this close to your life, built that way, would be a manipulation engine. We will not build that. Promises are cheap, so here is the part you can check: the instructions themselves, how we measure ourselves, and the history of both.

## Status

Figs are in alpha, and so is this repository. Some of it describes things that work today, and some describes things we are still building. We say which is which. If something here does not match what your Fig does, one of the two is wrong, and we want to know.

### Where this master prompt runs

Version 16 is the master prompt of our newest Figs, which a first group of testers uses today. Other Figs still follow an earlier set of instructions with the same intentions but not this text. We will update this page when that changes.

## What we publish, and what we keep back

One rule decides it: **we publish what Figs are asked to do and why, never how Figs are built.**

**We publish** the purpose, the principles, the rules that protect you, how a Fig speaks and acts, how it learns about you, and how we evaluate it. Including the parts that do not flatter us.

**We summarize** the parts of the master prompt that are about how the system works behind the scenes. Every summary is marked where it sits and says, in plain words, what that part makes a Fig do.

**We never publish** how the system is built, anything about a person who uses Figs, the exact test prompts we use to try to break Figs (published, they would work as a manual for doing it), or access and security details. Which companies process your data is in our [privacy policy](https://backtothefig.com/privacy).

## How this repository stays honest

- **The published master prompt is built from the real file by a script.** Verbatim parts are byte for byte. A changed sentence cannot slip in or out of the public edition without a person deciding, and the edition prints the fingerprint (sha256) of the exact file it came from.
- **Every new master prompt version gets a changelog entry.**
- **Evaluation results come with their sample sizes, their intervals and their limits**, and the methods are published with them, so anyone can see what a number does and does not show.

## Layout

```
intentions.md            what Figs are for, and the floors
master-prompt/
  README.md              how the master prompt works and how this edition is made
  v16.md                 the public edition of the current master prompt
  edition.json           block-by-block publication decisions
  how-we-write-it.md     the principles we write it by
memory.md                how a Fig learns about you, and how you correct it
evals/
  README.md              the Humanity Eval
  five-moments/          real-life moments: method and codebook
  behavior.md            behaviour checks: what we test before a change ships
CHANGELOG.md             master prompt versions
updates/                 notes from the team
FEEDBACK.md              how to tell us when a Fig breaks these intentions
scripts/                 the edition builder and the pre-publish check
```

## License

© 2026 Emerge Protocol Ltd. All rights reserved.

Back to the Fig is made by Emerge Protocol Ltd, registered in England and Wales, company no. 16142850.
