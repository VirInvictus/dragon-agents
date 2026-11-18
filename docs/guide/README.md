# The optimization guide arsenal

Distilled from two research passes run on 2026-11-18 (73 cited sources
across them, all fetched live that day) plus a year of operating the
roster this repository ships. The research reports live verbatim under
[research/](research/); the five documents here are the operational
distillation. Nothing here is doctrine from a single vendor post: where
a claim rests on one source, the references file says so.

## The system this guide describes

One operator, one harness, no fleet of humans. The setup, in
privacy-respecting terms:

- A Claude-Code-class CLI agent harness running Z.ai's GLM-5.3 and
  GLM-5.3-Flash, the main thread on the Flash tier.
- A personal subagent roster of thirty-eight seats: twenty-seven
  read-only researchers, one multimodal judge, and ten chartered write
  lanes behind structural fences (propose-by-default, allowlisted
  mutations, read-back verification, never a commit). Every seat is a
  markdown charter validated by a structural checker in CI. Roster
  counts in this guide are stated as of 2026-11-18; the authoritative
  live count is the repo README's fleet-at-a-glance table and the
  validator's roster check, and they move on every roster release.
- A long-standing personal workspace of dozens of repositories,
  local-first: no Docker, no cloud services in the product path, and
  nothing load-bearing that stops working offline.
- Dispatch discipline over raw parallelism: a hard four-concurrent
  budget held well under the platform's ceiling, shared scratch ledgers
  for waves, wave review between rounds, and a storm-shrinking rule
  when the provider degrades.

No machine-specific infrastructure, no personal data surfaces, and no
identifying details appear anywhere in this guide: it publishes the
patterns, and the specific systems stay out of it.

## The files

| File | What it answers |
|---|---|
| [model-routing.md](model-routing.md) | Which model for which seat and task, and why the routing principle beats per-task vibes. |
| [platform-settings.md](platform-settings.md) | GLM-5.3 / GLM-5.3-Flash mechanics worth setting once: endpoints, effort, caching, peak hours, tool-call quirks, sampling, known bugs. |
| [subagent-design.md](subagent-design.md) | Charter and fence design: read-only defaults, structural write paths, description precision, validation-as-CI. |
| [fleet-operations.md](fleet-operations.md) | Operating discipline: budgets, storm behavior, dispatch prompts, context craft, recovery ladders, review gates, cost levers. |
| [references.md](references.md) | Every source behind the guide, with as-of dates, plus the unknowns worth re-checking. |
| [research/](research/) | The two full research reports, verbatim. |

## Reading order

Start with [model-routing.md](model-routing.md); it changes dispatch
behavior the same day. [platform-settings.md](platform-settings.md) is
the set-once checklist. [subagent-design.md](subagent-design.md) and
[fleet-operations.md](fleet-operations.md) are the long game: how the
roster is built and how it is run. The top-ten list at the head of each
research report is the fastest skim.

## Provenance and refresh

The research passes were dispatched on 2026-11-18 to a chartered
web-research seat (keyless public sources only; primary docs over
summaries; every claim dated; marketing labeled). The territory moves
fast: GLM-5.3 was three months old at research time, several platform
bugs were open, and plan-tier mechanics carry revision notices. Treat
[references.md](references.md) as the re-check list, and re-run the
research quarterly or on any plan-tier revision notice.
