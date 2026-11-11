# dragon-agents

[![License: MIT](https://img.shields.io/github/license/VirInvictus/dragon-agents)](LICENSE)
[![Release](https://img.shields.io/github/v/tag/VirInvictus/dragon-agents)](https://github.com/VirInvictus/dragon-agents/tags)
[![ci](https://github.com/VirInvictus/dragon-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/VirInvictus/dragon-agents/actions/workflows/ci.yml)

A local ZCode plugin of research subagents for repo, markets, and collection-pipeline work. Twenty-six agents, each restricted to Read + Bash. Twenty-five are read-only: they gather and report, and the main thread decides and edits. The twenty-sixth, `claw`, is the one gated execution seat (v0.8.0): its writes ride the Calibre acquisition pipeline's own structural gates (backups outside the tree, the HMAC-sealed manifest it may never seal itself, refuse-beyond-the-approved-list, one rolled-back transaction), and it never opens the library database directly. No agent commits or spawns subagents of its own.

| Agent | Job |
|---|---|
| `repo-cartographer` | Structured repo map (layout, stack, conventions, tests, risk areas) before planning sessions. |
| `doc-drift-auditor` | Standard-layout docs vs code reality: VERSION sync, roadmap boxes, spec claims, patchnotes hygiene. |
| `cascade-checker` | Downstream call-site inventory for a changed shared-library API, with per-repo breakage risk. |
| `spec-compliance-reviewer` | Diff vs `spec.md` contract; violations and unaddressed claims with `path:line` evidence. |
| `ci-triage` | Failed CI run via `gh` to root cause, decisive log lines, and fix direction. |
| `slop-reader` | Fresh-eyes AI-prose pass on commissioned docs; flags quotes, never rewrites. |
| `release-auditor` | Pre-tag readiness and post-tag sweep: VERSION carriers, patchnotes entry style, tag message health. |
| `workspace-sentinel` | One sweep, every owned repo: dirty trees, unpushed commits and tags, untagged releases, stale catalog rows. |
| `ci-posture-auditor` | Workflows vs the house-hardened CI shape (SHA pins, permissions, concurrency, timeouts); names the stragglers. |
| `debt-census` | TODO/FIXME/HACK and dead-reference census, dated by blame, as a cleanup worklist. |
| `code-reviewer` | Bug-hunting review of a diff: correctness, edge cases, scope creep, userspace-break risk. |
| `git-archaeologist` | When did this break and why: regression windows and provenance from log, blame, pickaxe; bisect plans, never executed. |
| `claim-verifier` | Independent re-verification of a findings list: confirmed / refuted / unverifiable per claim. |
| `dependency-auditor` | Declared vs imported, floors vs used APIs, stdlib purity, Flatpak vendor staleness, toolchain drift. |
| `test-gap-analyst` | Static coverage map: untested behaviors, suite-discovery failures, duplicated test files; never executes tests. |
| `duplication-scout` | Cross-repo similar-module detection feeding the library-graduation rule; evidence, never the recommendation. |
| `stock-broker` | Markets research briefs: companies, ETFs, peers, and the surrounding markets (rates, FX, commodities) from keyless public sources; portfolio-relative guidance, never execution. |
| `ledger-analyst` | Personal-finance briefs from hledger journals: cashflow, budget vs actual, net worth, cost basis; encrypted org files fenced off by charter. |
| `librarian` | Books-collection research over the Calibre library: catalog health, wings and tag tree, series gaps, ownership duplicates, EPUB audits, taxonomy drift; book IDs and dated counts, never writes. |
| `data-analyst` | Read-only duckdb profiling of named local datasets: schema, nulls, top-N, joins; compact findings without flooding the main thread. |
| `security-auditor` | Defensive review of owned repos: gitleaks (redacted), risky patterns, advisory cross-checks via gh; ranked findings only. |
| `charter-architect` | Designs new agents: scorecard verdict (declining is valid), live-probed charter draft, and the full release kit as text; composes, never applies. |
| `syshealth-auditor` | Backup and system-health census: borg freshness from state reads, sys_maintain staleness and failures, failed units, disk space; root-gated checks reported as directions. |
| `music-archivist` | Music-collection research over lattice's read-only audits: health digest, genre hygiene against taxonomy.md, duplicates, codec coverage, discography gaps, listening candidates; album paths, never a tag edit. |
| `claw` | Executes Calibre import phases 1 and 2: vets a downloads batch (battery, dup screen, gated repairs, stamps, staging, manifest) and imports the signed manifest; decision points return as prompts, the seal stays with the main thread. |
| `shadow` | Read-only compliance pass over one import phase: manifest versus disk, verdicts versus decisions, imported ID sets, stamp read-backs, bak diffs; blocking findings before sign or commit. |

## Install

In ZCode: Settings → Plugin Management → Discover tab → `+` → add this directory as a local marketplace → install **dragon-agents**. Plugins from local (cache) marketplaces like this one install **disabled** until first enabled; only bundled official marketplace plugins are enabled by default. After enabling, trust the `enabledPlugins` key in `~/.zcode/cli/config.json` and a canary dispatch over the UI toggle, and remember the agent roster only lands in conversations opened after an app restart.

## Model guidance

Any text model works; the agents were written for text-only subagents (no vision). Flash-tier models are the sensible default; on analysis-heavy dispatches (cascade-checker, spec-compliance-reviewer, stock-broker, ledger-analyst, security-auditor, charter-architect, claw, shadow) a stronger model is worth it. Per-agent model picks live in Settings → Subagents.

## Development

`python3 scripts/validate.py` checks both manifests and every agent charter (frontmatter fields, `tools: [Read, Bash]` only, the read-only and no-subagent charter lines, and the twenty-six-agent roster). CI runs the same script on every push. `AGENTS.md` documents the plugin's rules and the marketplace/runtime gotchas; read it before changing how the plugin is packaged.

## License

MIT. See [LICENSE](LICENSE).
