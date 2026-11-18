# Platform settings: GLM-5.3 and GLM-5.3-Flash mechanics worth setting once

The set-once checklist for driving these models hard through a
CLI agent harness. Every item is sourced in
[references.md](references.md); the quirks carry their issue numbers
where the vendor's own tracker is the record.

## Endpoint wiring

- Claude-Code-class harnesses point at Z.ai's Anthropic-compatible
  endpoint with the base URL and auth token env vars, plus a long
  API timeout (the documented default is fifty minutes, and that is
  not padding: max-effort GLM-5.3 runs measure a median
  time-to-first-token over a minute, and long-horizon turns run far
  longer).
- A `[1m]` suffix on the model name requests the 1M-context variant;
  an in-session effort command sets `reasoning_effort` per turn.
- Wrong-endpoint selection is the documented cause of surprise
  "insufficient balance" errors: plan keys, team keys, and standard
  API keys are separate and non-interchangeable, and a depleted plan
  quota waits for the next window rather than falling back to balance.

## Reasoning effort

Thinking is forced on in both models; there is no off switch. Three
real levels exist (`low`, `high`, `max`), the default is `max`, and any
unrecognized effort value **silently falls back to `max`**: you can
believe you set `low` and be paying for `max`. Set the value explicitly
on every request, and after any harness update, verify what the harness
actually sends (harness-level vocabularies get remapped onto the three
levels, and the remap table has changed between versions).

`low` is the only real throttle on thinking spend, and thinking bills
as output tokens, which on the credit formula is the dominant axis.
The safe rule: `low` for genuinely trivial turns only; `max` for
judgment, writes, and gates (see [model-routing.md](model-routing.md)).

## The cache is the dominant lever

Caching is implicit and automatic; the operator's job is to protect
the prefix. Cached input bills at roughly a quarter of uncached input
on the plan's credit multipliers (1.7 vs 6.9 for GLM-5.3, 0.56 vs 2.3
for Flash) and at roughly a fifth on the API pricing page ($0.26 vs
$1.40 per million tokens on GLM-5.3); either basis, the discount is
the largest single lever on the bill. Hit-rate discipline is entirely
behavioral:

- Keep system prompts and standing rule files **byte-stable**. A
  one-token change invalidates the cache from that point forward. Do
  not edit charters, rule files, or prompt scaffolding mid-session;
  the cached prefix on every live conversation is the reason (editor
  formatting hooks that rewrite files on save are an invisible cache
  killer).
- Append-only conversation ordering; no timestamps or random values in
  prefixes; deterministic serialization of anything that enters the
  prompt.
- Long reference documents belong in the system message, where they
  cache, not re-sent per turn.
- When an agent turn carries preserved reasoning blocks forward, they
  must be returned byte-identical and in original order: editing or
  reordering them hurts both reasoning continuity and the hit rate.
- No public cache TTL exists; treat long gaps between turns as cache
  misses and batch accordingly.

One production incident worth knowing when picking a host (this
does not affect first-party use): a provider's GLM-5.3 deployment
cross-tenant-leaked prompt text through a KV-cache pool smaller than
the advertised context. The operator lessons transfer: a host's KV
pool must exceed the context it sells, and the test is output
coherence, because status codes lie.

## Peak and off-peak

Peak is weekdays 14:00-18:00 Singapore time (UTC+8); everything else,
including all weekend, is off-peak, and the two framings on the plan
pages agree on the ratio (roughly 3x peak vs off-peak for the strong
tier). Max-effort strong-tier batch work moves off-peak as a matter of
policy: it is the same run for roughly a third of the cost. Interactive
work ignores this; bulk waves and long unattended loops schedule
around it. One caution: reconcile the two published framings against
the account dashboard before scripting anything against exact
multipliers.

## The credit formula

Plan credits = (input x multiplier + cached input x multiplier + output
x multiplier) / 10,000. For GLM-5.3 the multipliers are roughly 6.9
input, 1.7 cached, **24 output**; for Flash roughly 2.3 / 0.56 / 8.
Output dominates, thinking bills as output, so effort level is the
spend lever, and a multi-hour max-effort loop is where budgets die
(one practitioner's mis-routed prototype burned 450M tokens overnight).
Cap `max_tokens` deliberately; the default is 65536 with a 131072
ceiling.

## Tool calling: three real traps

1. **Flatten tool schemas.** With empty top-level `properties` and all
   fields inside `oneOf` branches, the model returns stable empty `{}`
   arguments (open vendor issue); the flat equivalent of the same tool
   works. Any agent-frontend that generates nested schemas should
   flatten before dispatch.
2. **`tool_choice` supports only `auto`** on the OpenAI-style surface,
   and on the Anthropic-compatible Messages surface `none` is ignored:
   the model keeps issuing calls, so the fix is stripping `tools` from
   the request entirely, not asking it to stop.
3. **Keep function counts sane.** The upstream cap sits near 128
   functions, and heavy tool catalogs have a measured context tax:
   one fleet measured 50-70k tokens of pre-loaded schemas re-sent
   every turn, fixed by loading definitions on demand.

## Sampling and output language

Defaults are temperature 1.0, top_p 0.95, and vendor benchmark configs
corroborate them; tune at most one knob, never both, and stay in the
documented ranges (out-of-range values are silently accepted on some
surfaces and rejected on others).

GLM-5.x has a documented tendency to emit Chinese tokens or full
sentences mid-English session, reproduced across three model
generations, surviving full context resets (open issues; the vendor's
bilingual training is the stated cause). Mitigations that work: an
explicit always-respond-in-language rule in the system prompt, and a
fresh session when drift appears.

## Harness-side hardening

Three settings outside the API that decide whether storms are
survivable, in the operator's configuration rather than the vendor's:

1. **Raise the model-request retry window** well past the default
   (this setup runs thirty retries with a two-minute delay cap, about
   fifty minutes of survival) so a provider overload window rides out
   instead of killing mid-mission turns with all their gathered
   context.
2. **Lower the dead-stream cutoff** below the retry window; a hung
   stream wastes retry-window minutes.
3. **Know the second, hidden counter.** Mid-stream reconnection after
   an established stream dies is typically a separate hardcoded limit
   that no env var reaches; request failures and stream deaths render
   through the same UI string but are different failure classes with
   different budgets. Watch which kind actually failed before
   adjusting anything.

Also know the harness lifecycle facts that bite: the subagent roster
bakes at app boot (a mid-session roster change never hot-applies to an
open conversation), and reinstalls can wipe per-agent model pins, so
the pin table is re-verified after every reinstall rather than assumed.

---

Every number above is sourced with its as-of date in
[references.md](references.md) (sections "Platform mechanics" and
"Known bugs"). The deep version is
[research/glm53-optimization-report.md](../research/glm53-optimization-report.md).
