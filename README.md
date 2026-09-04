# dragon-agents

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

## License

MIT. See [LICENSE](LICENSE).
