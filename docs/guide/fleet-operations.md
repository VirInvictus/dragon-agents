# Fleet operations: budgets, storms, dispatch craft, recovery

How the roster is run on a normal day and a bad day.

## Budgets: lower than the ceiling, on purpose

The platform default for concurrent subagents is twenty, with a
three-layer nesting cap and a spawn error that explicitly tells the
orchestrator not to retry. This fleet holds a standing budget of four,
a deliberate third of the ceiling, for three reasons recorded in its
own history:

1. **Storm headroom.** Hosted-model providers degrade under
   multi-tenant load; a wave sized to the ceiling hammers the same
   overloaded endpoint with all its retries at once, while a small
   wave survives and a dead agent's work is re-runnable. This fleet
   sits at a fifth of the ceiling for exactly that headroom. The rule:
   when the day's logs show fresh retry or network-failure events,
   shrink to two concurrent and run the rest sequentially.
2. **Capacity for the built-ins.** Model-backed tools (web fetchers,
   plugin seats) share the same pool; the budget leaves room for them.
3. **The failure that set the rule.** An early run fanned out to eight
   agents that spawned their own, hit the rate limit, and lost the
   entire session's research. A slower sequential search that survives
   beats a parallel one that dies.

Know the cap's sharp edges: the do-not-retry error is correct behavior
to copy into dispatch prompts (a retry hammering a capped pool makes it
worse), and resumes can take fresh slots without checking the limit, so
resume storms can exceed the cap.

## Dispatch prompts: the four parts

The orchestrator-teaching rules from the multi-agent literature, in the
shape this fleet requires for every dispatch:

- **Objective**: what the mission is, stated so completion is checkable.
- **Output format**: the exact shape of the final report (tables,
  verdict vocabulary, refusal lines).
- **Tools and scope**: which repos, which files, which surface ladder
  rungs; self-contained, because a subagent starts with zero context.
- **Boundaries**: what it must not do (write, spawn, authenticate),
  restated even when the charter already says it.

Scale effort to the query: simple fact-finding gets one agent and a
handful of tool calls; comparisons get a few agents with divided
responsibilities; only genuinely complex missions get a wide wave.
Parallelize at both levels (several seats at once, several tool calls
per seat): parallel research cut complex-query time by up to 90% in
the source measurements.

Two standing disciplines ride on top: **wave review** (before
dispatching wave N+1, read what wave N actually returned and re-aim;
reusing a failed prompt verbatim re-pays full price for known
failures), and **shared scratch ledgers** (waves of two or more agents
append findings to one file as they go, so the wave communicates
mid-flight and a killed agent's work survives it).

## Context craft

- **Subagents exist to compress** (the definition and its economics are
  in [subagent-design.md](subagent-design.md)): a seat may burn tens of
  thousands of tokens exploring and returns a thousand or two. Keep the
  main thread for iterative work and shared-context phases; route
  verbose operations (log processing, full-file reads, documentation
  fetches, test output) through seats so the noise never reaches the
  parent.
- **Carry identifiers, not payloads.** Keep paths, queries, and links
  in context; load data at runtime through ranged reads instead of
  ingesting whole objects. Reference files by path in rule files
  instead of pasting their contents.
- **Compact on a schedule, before the cliff forces it.** One fleet forces
  compaction at 400k tokens even on 1M-context models because per-turn
  re-sends make long contexts expensive regardless of window size;
  a practitioner boundary worth respecting is that around 100k tokens
  threads start to feel imprecise. Prefer new sessions over ever-longer
  ones; the recorded practitioner verdict is that most newcomers'
  problems trace to not starting new threads often enough.
- **Keep errors in context; checkpoint outside it.** Failed actions and
  their traces stay in the conversation (erasing failure removes the
  evidence the model needs to change its approach); the durable state
  (mission scope, findings so far, roster, decisions) goes to a scratch
  file on a cadence, because harness checkpoints do not restore
  subagent edits or shell-side changes and are not a version-control
  replacement.
- **Recite objectives.** For long missions, rewrite a short objectives
  file continuously so the goal stays in recent attention; drift in
  fifty-tool-call tasks is the documented failure this counters.
- **Do not mutate the toolset mid-mission.** Adding or removing tools
  invalidates the prompt cache from the front and orphans history that
  references removed tools; mask availability at decision time instead.

## Recovery ladder for dead dispatches

Subagents stall between a completed tool call and the next model
request, and watchdogs kill them silently. The top-down ladder, never
jumping straight to a bare re-dispatch:

1. **Keep the launch id** of every dispatch until its mission lands;
   it is the resume handle. A harness restart of a stopped agent
   resumes with its full gathered context intact.
2. **Resume first**: send the interrupted agent a continuation message.
   This works even after a kill, and no re-spend on gathered material.
3. **Resume failed: salvage the transcript.** Session transcripts are
   written live to disk; read the tail, harvest the findings, and hand
   them to the replacement as context alongside the original prompt.
4. **Transcript unusable: same-prompt re-dispatch**, unchanged mission,
   recovered context added.

During storms, add the checkpoint cadence (append findings to the
shared ledger every few steps) so even an unresumable agent with an
unusable transcript leaves its work behind.

## Review gates and cost levers

The gate chain for any change that will be committed: implement in the
main thread, structural checks and tests locally, a clean-context
diff reviewer before commit (never the author re-grading), provider CI
green, a readiness audit before any tag, and execution of the release
only after the verdict. Clean-context review earns its dispatch: the
documented production numbers are roughly two real bugs per review,
most rated severe, precisely because the reviewer never saw how the
work was produced.

Cost levers, in order of measured impact (one large fleet cut unit
costs by a third to a half with the model held constant):

1. The subagent model default (see [model-routing.md](model-routing.md)).
2. Reasoning effort as an explicit fleet default, not inherited.
3. A compaction cap that balances context size against cache bursts.
4. Cache-TTL selection matched to usage rhythm (longer entries for
   human-paced main threads, shorter for short-lived seats).
5. A tool-catalog diet (definitions on demand, not pre-loaded).

Track spend outcome-denominated where possible (cost per release, per
review, per accepted dispatch) rather than in raw tokens, and check
per-seat usage share periodically: a seat that never earns its context
cost is a pruning candidate, and the pruning criterion is measured
degradation, never a hunch.

## The applicability reminder

Multi-agent pays only where the task value covers the token multiplier
(the 15x/4x arithmetic and its source are stated in
[subagent-design.md](subagent-design.md)), and the strongest
counterweight literature still holds: writes single-threaded,
additional agents contributing intelligence rather than actions,
unstructured swarms a distraction. Everything in this file operates
inside that boundary.
