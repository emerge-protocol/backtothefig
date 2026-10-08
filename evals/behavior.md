# Behaviour checks

[Five Moments](five-moments/) reads what happens in real use, weeks after the fact. Behaviour checks are the other end: conversations we write ourselves, run before a change reaches anyone, to see whether a Fig still keeps its floors and its character.

This is the least finished part of the Humanity Eval. Here is what exists and what does not.

## What exists

A first version was built in August 2026. It has two parts.

**A fixed set of 100 test prompts in eight groups**: harmful requests made directly, hidden in subtext, wrapped in fiction, slipped in by switching the frame mid-conversation, and repeated until the model gives in; plus prompts that test flattery under push-back, boldness, and style.

**Four scripted people who push.** Each holds a long conversation with a Fig and escalates step by step for as long as the Fig goes along, the way a determined person would. These show where a Fig gives way, not just whether it refuses the first ask.

A separate AI judge scores every conversation without knowing which version produced it: whether the Fig stayed in character, sounded like an assistant, was attuned, showed initiative and restraint, flattered, held its ground. It also counts the shapes we ban, such as assistant phrases, yes-man openers, lists in casual chat and em dashes, and how often a Fig refuses something harmless, because a Fig that refuses too much fails people too.

Every test runs twice: once without our written instructions and once with them. The difference shows what our instructions actually change.

## What it does not do yet

- **34 of the 100 test prompts never ran**, including the twelve written to test flattery directly. Our flattery results so far come from the judge reading whole conversations, which is weaker evidence.
- **It does not test memory.** The judge's memory score came out the same for every setup, so it could not tell them apart.
- **It does not test self-editing**: whether a Fig changes its own personality only when asked, and says so honestly when a change fails.
- **It is not a gate.** It does not yet run on every new version of the master prompt.

## What is next

1. Run the 34 missing test prompts.
2. Add tests for memory, for self-editing, and for behaviour at different stages of a relationship, since what is right with someone on day one is different from day ninety.
3. Run the full set on every new master prompt version, and publish each version's results next to its [changelog](../CHANGELOG.md) entry.

## What we will not publish

The test prompts themselves. They are written to get a model to cross its floors, and published, they would work as a manual for doing it. We publish what each group tests, how it is scored, and the results.
