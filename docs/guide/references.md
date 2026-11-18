# References

Every source behind this guide, merged from the two research passes of
2026-11-18. "As-of" is the date the page was fetched and read; pages
that state their own publication date carry both. Vendor-reported
numbers are labeled where they were used. The full reports,
including dead-end logs and per-source verdicts, live in
[research/](research/).

## Platform mechanics (GLM-5.3, GLM-5.3-Flash, the coding plan)

| Source | What it supported | As-of |
|---|---|---|
| docs.z.ai/guides/llm/glm-5.3 | Specs, forced thinking, effort levels, endpoints | 2026-11-18 |
| docs.z.ai/guides/llm/glm-5.3-flash | Flash specs, architecture, 3x quota, FlashX | 2026-11-18 |
| docs.z.ai/devpack/overview | Credit formula, multipliers, off-peak, tier routing | 2026-11-18 |
| docs.z.ai/devpack/notice/usage-revision (2026-07-30) | Peak/off-peak multipliers, team seats | 2026-11-18 |
| docs.z.ai/devpack/faq | Quota mechanics, no balance fallback, error 1113 | 2026-11-18 |
| docs.z.ai/devpack/usage-policy | Per-tier concurrency guidance | 2026-11-18 |
| docs.z.ai/devpack/quick-start | Protocol endpoints, key separation | 2026-11-18 |
| docs.z.ai/devpack/latest-model | Model switching, [1m] suffix, effort conversion | 2026-11-18 |
| docs.z.ai/devpack/resources/best-practice | Task shape, plan-first, session hygiene | 2026-11-18 |
| docs.z.ai/devpack/resources/memory-mechanism | Memory file sizing, rule-file splitting | 2026-11-18 |
| docs.z.ai/guides/capabilities/thinking + thinking-mode | reasoning_effort, preserved-thinking cache interaction | 2026-11-18 |
| docs.z.ai/guides/capabilities/function-calling | tool_choice auto-only, schema guidance | 2026-11-18 |
| docs.z.ai/guides/capabilities/cache | Implicit caching, hit-rate discipline, cached_tokens | 2026-11-18 |
| docs.z.ai/guides/capabilities/struct-output | JSON mode, schema-in-prompt pattern | 2026-11-18 |
| docs.z.ai/guides/overview/pricing | Cached-input prices (~19-20% of input) | 2026-11-18 |
| docs.z.ai/guides/overview/migrate-to-glm-new | Defaults, migration trap, tool_stream | 2026-11-18 |
| docs.z.ai/guides/overview/concept-param | Parameter defaults, max_tokens ceiling | 2026-11-18 |
| docs.z.ai/scenario-example/develop-tools/claude | Harness env vars, long API timeout | 2026-11-18 |
| z.ai/blog/glm-5.3 (2026-08-14) | Release facts, benchmark harness configs | 2026-11-18 |
| z.ai/blog/glm-5.3-flash (2026-08-26) | Cited via search summary + HN quotes; body JS-walled | 2026-11-18 |
| github.com/zai-org/GLM-5 (README, pushed 2026-10-15) | Effort fallback, clear_thinking guidance, serving links | 2026-11-18 |
| github.com/zai-org/GLM-5 issues #54/#142/#158/#163/#169/#170/#175 | Language bleed, oneOf tool args, low-effort QC failure, batching | 2026-11-18 |
| huggingface.co/zai-org/GLM-5.3 | Model card, bilingual training statement | 2026-11-18 |
| github.com/zai-org/ZCode (pushed 2026-11-16) | Harness config, provider schema, batch isolation | 2026-11-18 |
| github.com/musistudio/claude-code-router (pushed 2026-11-16) | Maintained multi-model routing plane with Z.ai support | 2026-11-18 |
| aihubmix.com GLM-5.3 hands-on (2026-08-14) | Verified quirks: silent fallbacks, tool_choice none, ranges | 2026-11-18 |
| artificialanalysis.ai/models/glm-5-3 and /glm-5-3-flash | Intelligence Index, cost per task, TTFT, cache discount | 2026-11-18 |
| reinvently.co.uk Featherbench page | Per-task pass rates and costs, small-sample caveats | 2026-11-18 |
| verdent.ai GLM-5.3 review | Public DeepSWE check, resolution-rate-not-efficiency verdict | 2026-11-18 |
| wagtail.org/blog/one-month-on-glm-53-flash (2026-10-02) | One-month practitioner run, 450M-token incident | 2026-11-18 |
| blog.cloudflare.com/kv-cache-exposure-remediation (2026-10-26) | Cross-tenant KV leak, host-picking lessons | 2026-11-18 |
| developer.nvidia.com GLM-5.3 serving post (2026-11-14) | Self-host throughput and tuning method | 2026-11-18 |
| HN threads via Algolia (items 49294997, 49449507) | Practitioner sentiment, congestion and looping reports | 2026-11-18 |
| reddit.com r/SillyTavernAI 1vsokwq (2026-08-19) | Minimal server-side prompt extraction | 2026-11-18 |
| reddit.com r/cursor 1uhnvid (search-summary only) | GLM-5.2 language-drift reports | 2026-11-18 |
| github.com/zai-org/GLM-4.5 + resources | Lineage: parsers, thinking-mode history | 2026-11-18 |
| github.com/zai-org/GLM-skills, zai-coding-plugins, MetaGLM repos | Ecosystem freshness verdicts | 2026-11-18 |

## Harness and fleet literature

| Source | What it supported | As-of / published |
|---|---|---|
| anthropic.com/research/multi-agent-research-system | 90.2% gain, 15x/4x tokens, 80% variance, delegation rules, evals, resume-from-checkpoint | 2025-06-13 |
| anthropic.com/engineering/building-effective-agents | Workflows vs agents, simplest-solution rule | 2024-12-19 |
| anthropic.com/engineering/effective-context-engineering-for-ai-agents | Context rot, attention budget, JIT context, compaction, subagent 1-2k summaries | 2025 (undated) |
| anthropic.com/engineering/claude-code-best-practices | Deterministic vs non-deterministic layers, CLAUDE.md <200 lines, budgets, /usage | living doc, read 2026-11-18 |
| anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | Code-vs-tokens economics, progressive disclosure | read 2026-11-18 |
| claude.com/blog/steering-claude-code (2026-06-18) | Seven-method table, subagents zero-context-cost, hooks bypass compaction | 2026-06-18 |
| code.claude.com/docs/en/sub-agents | Frontmatter, silent field-ignore, 15k description warning, concurrency 20 + do-not-retry, depth 3 | living doc, read 2026-11-18 |
| code.claude.com/docs/en/checkpointing | Checkpoint limits (subagent and shell changes not restored) | living doc, read 2026-11-18 |
| cognition.com/blog/dont-build-multi-agents (2025-06-12) | Share-context principles, single-threaded agent | 2025-06-12 |
| cognition.com/blog/multi-agents-working (2026-04-22) | Writes single-threaded, clean-context reviewer (2 bugs/PR, 58% severe) | 2026-04-22 |
| ampcode.com/how-i-use-amp (2025-05-15) | Small threads, 100k blur, new-thread advice | 2025-05-15 |
| opencode.ai/docs/agents | Deny-rule permissions, launch allowlist, config schema | living doc, read 2026-11-18 |
| cursor.com/docs/subagents and /docs/rules | Context-limit design rationale, faster-model parallel search, rules discipline | living doc, read 2026-11-18 |
| geminicli.com/docs/core/subagents | @-forcing, per-agent overrides | living doc, read 2026-11-18 |
| learn.chatgpt.com/docs/agent-approvals-security | Sandbox vs approval layers | living doc, read 2026-11-18 |
| manus.im Context Engineering post (2025-07-18) | KV-cache hit rate, 100:1 ratio, prefix rules, keep-errors-in, todo recitation | 2025-07-18 |
| github.com/humanlayer/12-factor-agents | Contact-humans-with-tools, launch/pause/resume, compact errors | read 2026-11-18 |
| humanlayer.dev writing-a-good-claude-md (2025-11-25) | Instruction budget 150-200, ignore-reminder injection | 2025-11-25 |
| uber.com efficient-software-factory (2026-08-27) | Cost equation, -34%/-52%, subagent-model top lever, 400k cap, MCP 50-70k, cache TTL split | 2026-08-27 |
| arxiv.org/abs/2510.04618 (ACE, 2025-10-06) | Evolving playbooks, brevity bias, context collapse | 2025-10-06 |
| platform.claude.com/docs/en/api/rate-limits | 429/retry-after vs 529 overloaded | living doc, read 2026-11-18 |
| saastr.com Replit incident coverage | DB deletion under prompt-only prohibition, fabricated fix | incident 2025-07 |
| gitclear.com AI code quality 2025 + 2026 | Duplication and copy/paste trend data | 2025-02-04, 2026 |
| github.com/hesreallyhim/awesome-claude-code | Ecosystem index | read 2026-11-18 |
| ghuntley.com/ralph (2025-07-14) | Loop-technique boundary case | 2025-07-14 |
| vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals (2026-01-27) | Always-loaded index 100% vs skills 79% | 2026-01-27 |
| dev.to analysis of the 80% system-prompt cut (2026-07-28) | Secondary/single-source for that claim | 2026-07-28 |
| agents.md | Open instruction-format adoption | read 2026-11-18 |
| github.com/jezweb/roo-commander (archived 2026-05-04) | Boomerang delegation and its long-context failure | archived |

## Unknowns worth re-checking

- Whether the GLM-5 open bugs cited here (language bleed #142/#163,
  oneOf tool arguments #169) are fixed; both were open at fetch time.
- A public per-tier rate-limit table: login-walled; only
  project-concurrency guidance is public.
- Cache TTL: unpublished ("reasonable time limits").
- Peak/off-peak framing: the overview (50% off-peak) and the revision
  notice (1x/3x) agree on the ratio but not the absolute base;
  reconcile against the dashboard before scripting schedules.
- The primary text of Anthropic's "80% system-prompt cut" post:
  single-source via secondary coverage.
- Quantified fleet-pruning studies: none published; the criterion in
  the literature is measured degradation.

## Refresh guidance

Re-run the research quarterly, or immediately on any plan-tier
revision notice, model release, or harness version jump. The two
highest-churn sections of this guide are the peak/off-peak mechanics
and the open-bug register; everything else (fences, gates, context
craft, routing principles) has been stable across every source's
publication date.
