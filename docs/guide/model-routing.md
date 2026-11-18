# Model routing: which model for which seat and task

The most consequential decision in a subagent fleet is which model
each dispatch runs on. Uber's fleet-cost work calls the subagent model
default "the most impactful lever" in its cost equation; our own roster
learned the same lesson from the other direction, by pinning every seat
deliberately instead of letting it inherit. This document is the
routing principle, the evidence behind it, and the refusal cases.

## The principle

One sentence: **breadth runs on the fast tier, judgment runs on the
strong tier, and anything that writes or gates other work runs on the
strong tier at max effort.**

Expanded into the four rules this roster dispatches by:

1. **Fast-tier (GLM-5.3-Flash) for rubric-driven breadth.** Sweeps,
   censuses, status digests, structured extraction, anything whose
   shape is defined by a rubric rather than by judgment. Flash carries
   three times the plan quota of GLM-5.3, and independent measurement
   puts it at 99% pass on everyday task suites at roughly a
   twenty-fifth of the per-task cost of the strong tier.
2. **Strong tier (GLM-5.3) for judgment whose verdicts gate other
   work.** Diff-versus-contract reviews, release readiness, claim
   verification, upstream port/skip calls. A wrong verdict here chains:
   a false "ready" ships a broken tag, a false "clean" merges a defect.
   The recorded failure case: a fast-tier model at low effort
   affirmatively certified a defect it had missed, then composed a
   final answer contradicting its own correct deliberation; identical
   briefs were clean at max effort. A certified error is worse than a
   miss because downstream steps build on it.
3. **Anything that writes, on the strong tier.** Write seats hold
   fences, and fences are judgment under pressure. The quota arithmetic
   does not matter: write dispatches are rare next to sweeps, and the
   cost of a misfenced write dwarfs any token savings.
4. **Multimodal seats on the fast tier, as a functional requirement.**
   The strong tier is text-only, so the pin is the capability: a vision
   seat pinned to a text-only model returns "inconclusive" on every
   dispatch. Verify this pin after every reinstall rather than letting
   it inherit.

## The evidence, briefly

- Fast tier: Intelligence Index 28 vs 32 for the strong tier, at $0.58
  vs $5.01 per benchmark task (Artificial Analysis); 99% vs 100% on an
  independent everyday-task suite at $0.0004 vs $0.0101 per task.
  Vendor-reported: DeepSWE 63.4 vs the previous generation's 46.2.
  Verdict: for bounded, rubric-shaped work the gap is noise and the
  price gap is not.
- Strong tier: the public leaderboard delta shows the gain is
  resolution rate, not token efficiency (near-identical cost per
  rollout, far higher solve rate on hard coding), and the gain is
  coding-targeted rather than universal. That is exactly the profile of
  judgment work and exactly not the profile of sweeps.
- Effort interacts with all of this: thinking is always on, and both
  models silently fall back to `max` when given an unrecognized effort
  value. Set effort explicitly; `low` is the only real throttle on
  thinking-token spend, and it is the wrong setting for any
  certification or gate (see rule 2's failure case).

## The cheapest verifier that can fail

Routing is not only about which model does the work; it is about which
checker accepts it. The documented ordering, from four independent
sources converging on the same answer:

1. **Deterministic checks first** (tests, typecheck, structural
   validators): enforced by the harness, not requested in prose. A
   validator in CI cannot be argued with, forgotten, or degraded by
   context growth. This roster's charter validator is the pattern: a
   stdlib script that pins fence literals into charters so a future
   edit cannot silently drop them.
2. **A cheap model against a rubric second**: the documented
   goal-checking mechanism, and the right shape for "did the dispatch
   actually return the required table".
3. **A clean-context reviewer third**: the same model class, but a
   fresh context that never saw how the work was produced. Clean-context
   review catches materially more defects than shared-context review
   (on record: roughly two real bugs per pull request, the majority
   rated severe). This is why our diff reviewer and pre-release auditor
   are separate dispatches, never the author re-grading its own work.
4. **The strong tier last**, for the calls none of the above can make.

Code beats tokens for anything computable: sorting a list by token
generation is more expensive than running a sort.

## Refusal cases: when not to route down

- Verification and certification of any kind (issue-triage verdicts,
  release readiness, claim verification): strong tier, max effort.
- Writes of any kind: strong tier.
- Anything whose wrong output chains downstream: strong tier. The
  routing question is not "could the fast tier probably do this" but
  "what does a silent wrong answer cost."
- Anything needing vision: fast tier, because it is the only tier that
  can see, and the pin is checked, not assumed.

## The dispatch-table shape

Keep one table, one row per seat, one model per row, one reason per
row. The reason column is the discipline: a row that cannot state why
it needs its tier gets re-examined. Ours lives in the operator's global
dispatch rules; the shape matters more than the contents. Re-verify the
whole table after every harness reinstall, because reinstalls have
twice wiped it to "inherit default" on this setup.

---

Practical sources for every claim above: [references.md](references.md),
section "Model routing". The deep version, with all numbers and their
as-of dates, is [research/glm53-optimization-report.md](../research/glm53-optimization-report.md)
(Q3) and [research/harness-optimization-report.md](../research/harness-optimization-report.md)
(Q5, "cheap verification").
