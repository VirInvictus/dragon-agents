# AGENTS.md

Guidance for any agent (or human) working in this repo. It is the source of truth for the **dragon-agents** ZCode plugin: six read-only research subagents installed through a local directory marketplace.

## What lives here

- `agents/*.md`: the six agents (repo-cartographer, doc-drift-auditor, cascade-checker, spec-compliance-reviewer, ci-triage, slop-reader). Each file is frontmatter (`name`, `description`, `color`, `tools`) plus the agent's system prompt.
- `marketplace.json`: the marketplace manifest (at the repo root; see Manifest mechanics).
- `.zcode-plugin/plugin.json`: the plugin manifest (name, version, description, author, license) and nothing else.
- `scripts/validate.py`: structural checks; CI runs it on every push.

## Non-negotiables

- **Agents stay read-only.** Every agent keeps `tools: [Read, Bash]`, and its charter keeps the read-only and "Do not spawn subagents" lines. They gather and report; the main thread decides and edits. Never add a write path, a build step, or nested-subagent capability to any agent.
- **Stdlib only.** This repo is markdown, JSON, and one stdlib-Python validator. No dependencies, no lockfile, no runtime of any kind.
- **Dispatch names are `dragon-agents:<name>`**, and the `name` in frontmatter must match the filename exactly.

## Manifest mechanics (verified against zcode.cjs, 2026-09-03)

- `marketplace.json` MUST sit at the repo root: the directory-source loader probes `<dir>/marketplace.json` then `<dir>/.claude-plugin/marketplace.json`, and never reads `.zcode-plugin/marketplace.json`.
- The `agents/` directory is scanned by convention. The manifest does not need an `agents` key; the component enumerator scans the conventional directory when it exists.
- `plugin.json` stays minimal; its `version` is the single source of truth for releases, tagged as annotated `v`-prefixed tags at the release commit.

## Runtime gotchas (why your edits may look "broken")

- The installed plugin runs from a cache copy (`~/.zcode/cli/plugins/cache/dragon-agents/dragon-agents/<version>/`), not from this repo. After editing, refresh the plugin via Plugin Marketplace so the cache copy follows.
- Plugins from cache marketplaces install DISABLED until first enabled; the bundled official plugins are the ones enabled by default.
- The agent roster is baked at each conversation's app-server boot: a mid-session enable or roster change never hot-applies to an open conversation. Test in a fresh conversation, canary `dragon-agents:repo-cartographer` on this repo first.
- The marketplace Enable button may keep saying "Enable" after a successful click. Trust `enabledPlugins` in `~/.zcode/cli/config.json` and a canary dispatch over the button.

## Validation

Run `python3 scripts/validate.py` before committing. It checks that both JSON manifests parse and match the expected shape, that every agent file's frontmatter is well-formed (name matches filename, tools exactly `Read, Bash`, non-empty description), that each charter carries the read-only and no-subagent lines, and that the roster is exactly the expected six. CI runs the same script.
