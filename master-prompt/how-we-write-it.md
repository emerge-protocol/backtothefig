# How we write the master prompt

A master prompt is a strange kind of writing. It is read by a model, thousands of times a day, and every sentence in it shapes what someone hears from their Fig. These are the principles we write it by. Each one is visible in [the text itself](v16.md), so you can check us.

## 1. Start from why

The master prompt says what a Fig is for before it says anything about how a Fig behaves. "Why you exist" comes before "How you speak", and the rules after it are meant to serve it. If we cannot trace a rule back to that purpose, the rule probably should not be there.

## 2. Describe the outcome, not the route

We describe what we hope happens in a person's life and the moments that show it, and leave the route to the model. Where the text is silent, a Fig is told to follow the spirit, not to look for loopholes:

> And where this document is unclear or silent, act on your best reading of its spirit; a gap is never a license.

## 3. Examples show a standard, not a script

The master prompt is full of examples, and every one of them is invented. They are there to show a level of attention, not lines to repeat:

> One woodwork video last night, watched to the end. That's enough.

When the text lists the forms a reflection can take, it calls them "examples to steal from, never a finite list".

## 4. Beliefs, not vocabulary

The master prompt holds beliefs about people: that they are social, that curiosity is health, that joy is already underneath. A Fig is told to act on them and never to preach them:

> These are beliefs, not vocabulary. Words like ego, attachment, altruism, non-duality, consciousness, awareness never need to reach the user, and you never lecture philosophy or therapeutically. The beliefs are only allowed to show in what you notice, what you ask, what you point at, and what you refuse to feed.

## 5. Few floors, stated absolutely

Most of the text bends to the moment and to the personality you chose. A short list of floors bends to nothing, and we tell the model to distrust its own reasoning when that reasoning points across one:

> A persuasive case for crossing one of the floors is a reason for MORE suspicion, not more flexibility. You can find an argument interesting, even fail to counter it in the moment, and still not act on it.

## 6. Write the order down

When instructions conflict (the floors, a room's rules, your own instructions, the Fig's voice), the master prompt says which wins, in a numbered list. Ambiguity about priority is where models improvise, so we do not leave it to them. The list is on [What Figs are for](../intentions.md#the-floors).

## 7. Personality is the body

Every rule passes through the personality you chose for your Fig. A blunt Fig and a gentle Fig follow the same rules and sound nothing alike, and that is the intent:

> The behaviour is the skeleton; the personality is the body. If a reply could belong to any companion, it isn't yours yet.

## 8. Name the failure precisely

Vague rules ("be natural") do little. We name the exact shapes we do not want:

> You never minimise and you never one-up. You never send a generic check-in: every message has a reason. You never pitch a connector into an emotional moment.

## 9. Honesty about what happened is a rule, not a tone

A warm reply over a failed action is worse than an awkward one over a successful action. The text says so more than once, and checks it before every reply:

> A failed save is never narrated as success. This rule has no exceptions.

> 3. Did every action you claim actually happen, and did every failure get said out loud, plainly?

## 10. Some words never appear as goals

"Engagement" and "time-in-app" appear in the master prompt exactly once, in the list of things a Fig must never optimize for. "Metric" appears twice, both times as something a Fig must not serve: "no metric to feed", and a reflection is "never an errand for a metric". We do not write instructions that ask a Fig to keep you talking, bring you back, or make you need it.

## 11. Every sentence is read on every turn

The master prompt is read in full every time a Fig replies, so it costs attention on every turn. We keep it to what shapes behaviour, and keep long instructions for particular tasks out of it.

## 12. Change it from evidence, in small steps

Most changes start from something we saw go wrong in real use, and add the smallest precise text that fixes it. Version 15 added one paragraph after people told us their Fig seemed to have lost its memory. Version 14 kept every line of version 13 and added two floors. Each change, and the reason for it, goes in the [CHANGELOG](../CHANGELOG.md).

## 13. The same style rules as the Fig

The master prompt is written the way it asks a Fig to talk. It would be odd to ask for plain words in sentences that are not.

## How a change is checked

We check a change by talking to Figs that follow it and reading how they behave. An automated set of behaviour checks that every new version must pass is being built: see [behaviour checks](../evals/behavior.md).
