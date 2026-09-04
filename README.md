# dragon-agents

[![License: MIT](https://img.shields.io/github/license/VirInvictus/dragon-agents)](LICENSE)
[![Release](https://img.shields.io/github/v/tag/VirInvictus/dragon-agents)](https://github.com/VirInvictus/dragon-agents/tags)
[![ci](https://github.com/VirInvictus/dragon-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/VirInvictus/dragon-agents/actions/workflows/ci.yml)

A local ZCode plugin of read-only research subagents for repo work. Six agents, each restricted to Read + Bash, each forbidden from writing, committing, or spawning subagents of its own. They gather and report; the main thread decides and edits.

| Agent | Job |
|---|---|
| `repo-cartographer` | Structured repo map (layout, stack, conventions, tests, risk areas) before planning sessions. |
| `doc-drift-auditor` | Standard-layout docs vs code reality: VERSION sync, roadmap boxes, spec claims, patchnotes hygiene. |
| `cascade-checker` | Downstream call-site inventory for a changed shared-library API, with per-repo breakage risk. |
| `spec-compliance-reviewer` | Diff vs `spec.md` contract; violations and unaddressed claims with `path:line` evidence. |
| `ci-triage` | Failed CI run via `gh` to root cause, decisive log lines, and fix direction. |
| `slop-reader` | Fresh-eyes AI-prose pass on commissioned docs; flags quotes, never rewrites. |

## Install

In ZCode: Settings → Plugin Management → Discover tab → `+` → add this directory as a local marketplace → install **dragon-agents**. New plugins are enabled by default.

## Model guidance

Any text model works; the agents were written for text-only subagents (no vision). Flash-tier models are the sensible default; on analysis-heavy dispatches (cascade-checker, spec-compliance-reviewer) a stronger model is worth it. Per-agent model picks live in Settings → Subagents.

## Development

`python3 scripts/validate.py` checks both manifests and every agent charter (frontmatter fields, `tools: [Read, Bash]` only, the read-only and no-subagent charter lines, and the six-agent roster). CI runs the same script on every push. `AGENTS.md` documents the plugin's rules and the marketplace/runtime gotchas; read it before changing how the plugin is packaged.

## License

MIT. See [LICENSE](LICENSE).
