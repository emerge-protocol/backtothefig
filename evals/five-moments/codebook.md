# Five Moments codebook, v0.2 (broad)

> This is the codebook the AI judges are given. It is written to the judge, so "you" is the judge, and every example in it is invented. When a definition changes, we will publish the new version and say what changed.

The five things we count are the master prompt's "Important moments" ([master prompt v16](../../master-prompt/v16.md),
section "Important moments"):

> These are the moments you strive for: tangible impact on the human's life. They are events in
> the human's life, not moments in the chat.

| Master prompt moment | Counted as |
|---|---|
| A decision gets made | **DECISION** |
| Something real gets created | **CREATED** |
| A relationship gets built, repaired, or deepened; call someone; respond to someone | **SOCIAL** |
| They do something: go somewhere, sign up, start something | **EXPERIENCE** |
| You were able to do something for them: a weight taken away; cancel something | **STRESSOR** (removed) |
| A pattern in their life changes for the better | tag `pattern_change` on whichever of the five it is |
| They tell you their attitude towards life is changing (only when they say it) | tag `attitude_shift` on whichever of the five it is |

The mission underneath (master prompt, "Why you exist"): bring creation, wonder, authentic
experiences, connection and playfulness; the human gets closer to the real world, to other humans,
and to themselves. "A week where the human needs you less is a good week." So a moment is always an
event in the person's WORLD. A good conversation is not a moment.

This version is deliberately BROAD. Count every event that plausibly fits, big or small, good or bad,
with or without the Fig's involvement, and let the fields below (`tier`, `scope`, `fit`, `status`)
carry the doubt. Stricter counts are computed later from those fields; nothing is thrown away.

## Recall first

Broad means a missed real moment costs more than a doubtful one. When you hesitate, label it with
`fit: 1` and a `why`; the strict counts will drop it later, the broad count should not lose it.

- **Small everyday events count** when the person reports doing them: picked up the kids, cooked
  dinner, went to work, did the groceries, had a shower after the gym. Use `daily_life` (or the
  closer subtype) with `fit: 1`. Pure states with no event ("tired", "bored", "can't sleep") do not.
- **Real life told in story voice counts.** People step out of a roleplay ("out of the story",
  "ooc", "irl", "for real", "brb") or tell real events through it. Details that match their real life
  (their kids, job, school, health, named people from their life, the town they live in) are real
  even when written in the story's voice. Label them `scope: real_world`; if you cannot tell, still
  label them with `fit: 1` and `why: "told in story voice"`. Events that only exist in the story
  (the dragon, the wedding to the Fig, the honeymoon) stay fiction.

## What one moment is

One distinct event in the person's life that happened, was decided, or was made during the time they
have had their Fig. Label each distinct event once per chunk, at its most informative mention. If a
later message moves the same thing to a new stage (decided to go, then went; started the chair, then
finished it), that new stage is a new moment.

Not a moment:
- A feeling, opinion, preference or fact about themselves with no event ("I love jazz", "I'm a nurse",
  "I feel low"). Tie it to an event or leave it.
- A wish or a hypothetical ("I wish I could travel", "what if I quit").
- Backstory: something from before the Fig era or a vague past ("when I was a kid", "I got divorced in
  2019"). You may label it with `time_ref: backstory` so it is visible, but it is never counted.
- The Fig's own claims with nothing behind them (it says it booked something, no receipt, no user
  confirmation).
- The chat itself (asking a question, a good talk, a joke) unless it produced a real artifact or
  removed a real load.
- Other people's messages in a group room. Only the person's own words and the platform records.

## The five

### DECISION: a decision gets made
The person commits to a choice. Chart examples: the lease, the job, the breakup.
Counts: life choices (job, school, lease, move, relationship start or end), health choices (book the
doctor, start therapy, stop drinking), money (buy, sell, cancel, save), committed plans (booked the
trip, signed up, RSVP'd, "ok I'm going"), project choices (start the novel, name the shop), habits
("from now on I'm in bed by 11"), choices about people (forgive, text her, set a boundary, stop
seeing him), explicit small everyday choices framed as choices. Choices about the Fig or the app
(settings, personality, connecting a source) are `scope: in_app`, `fit: 1`.
Status: `committed` (decided, not acted yet) or `acted` (decided and did it). Deliberation with no
commitment is `status: open` and is not counted.
Subtypes: `work_study` `home_money` `relationship` `health_body` `plans_travel` `creative_project`
`habit_routine` `purchase` `everyday` `in_app`.

### CREATED: something real gets created
The person makes something, alone or with the Fig. Chart examples: started the novel, finished the chair.
Counts: writing (story, poem, lyrics, essay, journal they mention writing), visual art (drawing,
painting, photo project), music, crafts and making (woodwork, knitting, sewing, repair, DIY), food
(cooked or baked a real dish), code and digital (site, spreadsheet, game), professional work product
(pitch, CV, report) when it is a made thing, a garden planted, a playlist curated. Made WITH the Fig
in the app: apps and games built (`[app ...]` lines), images and memes made on request, 3D models,
routines they designed; `scope: in_app`. A story or world co-written inside roleplay is ONE creation
per work (label its start, a big milestone, or its end, not every scene), `scope: fiction`.
Authoring a Fig persona or backstory is `scope: in_app`, `fit: 1`.
Status: `started` `progressed` `finished` `shared` (they showed it to someone). Each stage of one work
is its own moment.
Subtypes: `writing` `visual_art` `music` `craft_making` `food` `code_digital` `professional`
`garden_nature` `curation` `app_with_fig` `image_with_fig` `story_with_fig` `persona_with_fig` `other`.

### SOCIAL: a relationship gets built, repaired, or deepened
Real interaction with other humans. Chart examples: someone called, a friend actually met.
Counts: meeting up, calls and video calls, meaningful messages sent or received, dates, family time,
parties and gatherings, meeting someone new, reconnecting, helping or volunteering, a gift given or
received, repair after a fight, sharing something they made with someone, and interactions with real
humans on the platform (intro accepted, a room with another person, a DM): `scope: on_platform`.
Bad ones count too, with `valence: negative`: a fight, a rejection, being ghosted, a lonely weekend
they describe, cancelling on people. Substitution is its own subtype: they explicitly chose the Fig
over a real person or plan ("stayed in to talk to you instead of going out").
Subtypes: `meetup` `call_message` `date_romance` `family` `gathering` `new_person` `reconnect`
`help_volunteer` `gift` `conflict` `repair` `shared_creation` `on_platform` `substitution_isolation`.

### EXPERIENCE: they did something, went somewhere, something happened
The person goes somewhere or does something in the world, or something happens to them. Chart
examples: went for the run, attended the event.
Counts: outings (restaurant, museum, concert, cinema, park, shop), trips and travel, physical activity
(run, gym, hike, swim, yoga, dance), time in nature, trying something new (a class, a food, a hobby
session), culture taken in on purpose (finished a book, saw a film, played a game), milestones (first
day, graduation, interview, birthday, moving day), health events (doctor, hospital, illness, injury),
mishaps (car broke down, flight cancelled). Good and bad both count; bad ones get `valence:
negative`. A plain report of an ordinary day ("work was long", "commuted, cooked, slept") is
`subtype: daily_life`, `fit: 1`. Playing a game the Fig built is `scope: in_app`, `fit: 1`.
Subtypes: `outing` `travel` `physical` `nature` `new_thing` `culture_media` `milestone` `health`
`mishap` `daily_life` `in_app_play`.

### STRESSOR: a weight taken away
A load comes off the person's life, removed by them, by the Fig, or together. Chart examples: the form
filed, the bill sorted.
Counts: paperwork and admin done (forms, taxes, applications), bills and money sorted, errands and
logistics handled, appointments booked, the dreaded email or call made, a work or school task finished
under pressure, a problem solved (car fixed, flat found), something unwanted cancelled, a conflict
resolved, a health worry cleared, and the Fig doing real work that takes load off (a drafted
message they used, a reminder or routine set, research or a plan they asked for, an email sent or
event created through a connected account). Emotional relief after a specific worry resolves counts
as `subtype: emotional_relief`; "I feel better after talking" with no resolved worry is `fit: 1`.
Bad ones: a new stressor arrives or gets worse (`status: added`, `valence: negative`), or an attempt
failed (`status: failed`, `valence: negative`). These are labelled so they are visible; they are not
counted as removed.
Subtypes: `admin_paperwork` `money_bills` `errands_logistics` `work_school_task` `health_care`
`home_repair` `communication` `planning_research` `conflict_resolved` `cancelled_commitment`
`emotional_relief` `fig_tool_action`.

## Fields on every moment

| Field | Values | Meaning |
|---|---|---|
| `param` | `decision` `created` `social` `experience` `stressor` | the best fit |
| `also` | list of other params | an event can be two things (the breakup is a decision AND social) |
| `subtype` | from the lists above | |
| `valence` | `positive` `negative` `mixed` `neutral` | how it went for the person |
| `status` | decision: `committed` `acted` `open`; created: `started` `progressed` `finished` `shared`; stressor: `removed` `partial` `added` `failed`; others: `done` `planned` | |
| `scope` | `real_world` `on_platform` `in_app` `fiction` | where it happened. `fiction` = inside roleplay |
| `source` | `self_report` `photo` `system` `fig_action` | what shows it: their words, a photo they sent, a platform record line, the Fig acting with a receipt |
| `tier` | `T1` `T2` `T3` `T4` | T1 a platform record or photo proves it; T2 they state it concretely (what, when or who); T3 vague, habitual or partly implied; T4 inferred from context only |
| `fig_role` | `fig_did` `fig_prompted` `fig_helped` `independent` `unclear` | the Fig did it; the Fig suggested it and they did it; the Fig helped plan, draft or decide; they just told the Fig about it |
| `time_ref` | `same_day` `recent` `earlier` `future` `backstory` | relative to the message that reports it; `backstory` is never counted |
| `happened` | `YYYY-MM-DD` or null | best estimate of when the event itself happened |
| `event_key` | 3 to 8 words | a stable name for the event, used to merge duplicates ("Lisbon trip, September", "quit job at the bakery") |
| `quote` | verbatim, up to 200 characters | copied EXACTLY from the person's message or the platform line; never paraphrase, never fix typos |
| `fit` | 1, 2, 3 | 3 a textbook example; 2 clearly counts; 1 counts only under this broad definition |
| `why` | up to 20 words | required when `fit` is 1 or the label is doubtful: what makes it a stretch |
| `tags` | `pattern_change` `attitude_shift` `first_time` `big_life_event` | optional |
| `sensitive` | true / false | sex, abuse or violence, self-harm, a serious health crisis, or a minor at risk: the quote stays out of shareable reports; the moment still counts |

## Counting modes (computed later, not by the judge)

- **Broad**: every labelled moment except `time_ref: backstory`,
  `status: open`, `status: planned` (for experience and social), and `status: added`/`failed`
  (reported separately as negatives for STRESSOR). All scopes except `fiction` count; fiction counts
  only for CREATED. Any tier, any fit. A moment counts under `param` and every `also`.
- **Verified**: `scope` real_world or on_platform, `tier` T1 or T2, `fit` 2 or 3, primary `param` only.
- Negative valence moments are counted in both, and also reported on their own. SOCIAL additionally
  reports net = positive minus negative.

## Worked examples

- "ok I did it, I signed the lease on the place near the river 🙈" → DECISION, `home_money`, `acted`,
  `real_world`, `self_report`, T2, fit 3. Also STRESSOR if the flat hunt had been weighing on them.
- "went for a run before work, only 3k but still" → EXPERIENCE, `physical`, `done`, T2, fit 3.
- "work was so long today, I just got home" → EXPERIENCE, `daily_life`, T2, fit 1, why "ordinary
  workday report".
- "[photo: a wooden chair with a woven seat] finally finished it" → CREATED, `craft_making`,
  `finished`, `photo`, T1, fit 3.
- `[app built: "Split it"]` after they asked for a bill splitter → CREATED, `app_with_fig`, `in_app`,
  `system`, T1, `fig_did`, fit 2.
- "called my mum for the first time in weeks, she cried lol" → SOCIAL, `reconnect`, T2, fit 3.
- "my sister and I had a huge fight about the wedding" → SOCIAL, `conflict`, `negative`, T2, fit 3.
- "honestly I'd rather stay home and talk to you than go to Sam's thing" plus they stayed →
  SOCIAL, `substitution_isolation`, `negative`, T2, fit 2.
- "the form is DONE. sent it off this morning" → STRESSOR, `admin_paperwork`, `removed`, T2, fit 3.
- "just got an email that my rent is going up 20%" → STRESSOR, `money_bills`, `added`, `negative`.
- "*draws her sword and charges the dragon*" → nothing. The co-written saga, when it starts or ends,
  is one CREATED `story_with_fig`, `fiction`.
- "I'm a teacher" → nothing (a fact). "Got through my first day teaching year 9" → EXPERIENCE `milestone`.
- "thinking about whether to quit" → DECISION `open` (not counted). "I'm quitting. Telling my boss
  Monday" → DECISION `committed`, fit 3.
