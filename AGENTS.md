# AGENTS.md

Guidance for any agent (or human) working in this repo. It is the source of truth for the **dragon-agents** ZCode plugin: thirty subagents installed through a local directory marketplace (twenty-one read-only by charter, plus nine chartered write seats: claw's gated pipeline lanes, the five fence-gated audit-and-fix seats added at v0.9.0, the two purpose-built write agents added at v1.0.0, latro the research-report writer and assay the grader, and imprint, the GitHub-metadata seat added at v1.1.0).

## What lives here

- `agents/*.md`: the thirty agents (repo-cartographer, doc-drift-auditor, cascade-checker, spec-compliance-reviewer, ci-triage, slop-reader, release-auditor, workspace-sentinel, ci-posture-auditor, debt-census, code-reviewer, git-archaeologist, claim-verifier, dependency-auditor, test-gap-analyst, duplication-scout, stock-broker, ledger-analyst, librarian, data-analyst, security-auditor, charter-architect, syshealth-auditor, music-archivist, claw, shadow, latro, assay, imprint, schedule-analyst). Each file is frontmatter (`name`, `description`, `color`, `tools`) plus the agent's system prompt.
- `patchnotes.md`: release notes, newest at top (introduced at v0.2.0); release tags carry the entry verbatim per the workspace tag procedure.
- `roadmap.md`: the forward plan; completed waves ticked, v0.5 candidates with entry conditions, the watch list, and the declined-with-reasons ledger so skips stay decided. Docs-only commits to it follow the refresh-procedure precedent (no version bump, no tag).
- `marketplace.json`: the marketplace manifest (at the repo root; see Manifest mechanics).
- `.zcode-plugin/plugin.json`: the plugin manifest (name, version, description, author, license) and nothing else.
- `scripts/validate.py`: structural checks; CI runs it on every push.

## Non-negotiables

- **Read-only by default; write seats are chartered, never casual.** Agents gather and report; the main thread decides, reviews diffs, and commits. Write capability exists only under a chartered fence. `claw` (v0.8.0, Brandon's recorded amendment of 2026-11-10) writes through tool-side structural gates only (loose files under the dispatched batch directory with backups outside the tree, plus `cquarry run phase1/phase2`), with the manifest seal and every library write beyond the phase-2 verb fenced off. The five charter-fence seats (v0.9.0, Brandon's amendment of 2026-11-11: charter-architect, ci-posture-auditor, doc-drift-auditor, debt-census, test-gap-analyst) carry `tools: [Read, Edit, Write, Bash]` with a charter that names the mode discipline (report-only default), the Clean tree precondition, the never-commit rule, the exact write scope, the re-verification step, and the itemized report. The two v1.0.0 purpose-built write seats extend the same principle: latro carries `tools: [Read, Write, Bash, WebSearch, WebFetch]` with the one-new-file fence (no Edit tool, occupied path is a REFUSED, keyless web only, never a commit), and assay carries `tools: [Read, Bash, WebSearch, WebFetch]` whose single write is a quoted-heredoc append to a repo's roadmap.md, gated by the clean-tree precondition and re-verified with `git diff --numstat` (additions only, zero deletions, original lines byte-identical). imprint (v1.1.0, Brandon's request) carries `tools: [Read, Bash]` with no Write or Edit at all: its writes ride exactly two gh verbs (`gh repo edit --description` and `--add-topic`/`--remove-topic`, plus `--homepage` only when a dispatch names it), propose mode is the default, apply dispatches must enumerate their repos, every mutation is read back, and the itemized before/after report is the audit trail because these writes publish to github.com instantly with no local diff; visibility, archive, rename, default branch, collaborators, branch protection, repo creation or deletion, gists, issues and PRs, and every tag and release surface are forbidden absolutely. Every other agent keeps `tools: [Read, Bash]` and the read-only line, and every agent keeps the "Do not spawn subagents" line; validate.py enforces the per-class shape. Never add a write seat without its fences, and never add a build step or nested-subagent capability to any agent.
- **Stdlib only.** This repo is markdown, JSON, and one stdlib-Python validator. No dependencies, no lockfile, no runtime of any kind.
- **Dispatch names are `dragon-agents:<name>`**, and the `name` in frontmatter must match the filename exactly.
- **Every agent carries the debug-reporting duty (v1.3.0, always-on).** Each charter's `## Debug reporting` section requires a `## Debug Report` block at the end of the agent's final message, on every dispatch including clean ones: one bullet per friction point actually hit (`tool`, `environment`, `model`, `charter`, `dispatch`, `idea`), or exactly `- none`. Agents only report; they never create, comment on, or label a GitHub issue. Filing is the dispatcher's job, below.

## Debug reporting and issue filing (the dispatcher's half)

The charters produce the `## Debug Report` blocks; the dispatcher files them. Filing is part of the dispatch, not a follow-up: a turn that dispatched a dragon agent and left its Debug Report untriaged is an incomplete turn. After every dragon-agents dispatch:

1. Read the agent's `## Debug Report` block. `- none` means nothing to do; stop there.
2. For each bullet, decide whether it is actionable for this repo (a charter fix, a validator gap, a documented dead surface, a real environment problem, a tooling idea). Non-actionable lines are dropped, not filed.
3. Dedupe against open issues first: `gh issue list --repo VirInvictus/dragon-agents --label debug --state open`.
4. File one issue per finding: `gh issue create --repo VirInvictus/dragon-agents --label debug --title "[<agent-name>] <one-line summary>"`, with the body carrying the dispatch date, the category, the evidence as quoted, and the model pin the agent ran under (Settings → Subagents), so the two-week triage can group improvements per agent and per model. Tiny related items from one dispatch may batch into one issue when that is cleaner.
5. The `debug` label must exist before the first filing: `gh label create debug --repo VirInvictus/dragon-agents --description "Findings from the agents' standing debug-report duty" --color B60205` (one-time setup; skipped if present).

The experiment window is 2026-11-11 → 2026-11-25; the review checklist lives in roadmap.md. After the window, the standing duty is kept, stripped, or refined on the evidence, and this section updates with the verdict.

## Manifest mechanics (verified against zcode.cjs, 2026-09-03)

- `marketplace.json` MUST sit at the repo root: the directory-source loader probes `<dir>/marketplace.json` then `<dir>/.claude-plugin/marketplace.json`, and never reads `.zcode-plugin/marketplace.json`.
- The `agents/` directory is scanned by convention. The manifest does not need an `agents` key; the component enumerator scans the conventional directory when it exists.
- `plugin.json` stays minimal; its `version` is the single source of truth for releases, tagged as annotated `v`-prefixed tags at the release commit.

## Runtime gotchas (why your edits may look "broken")

- The installed plugin runs from a version-pinned cache copy (`~/.zcode/cli/plugins/cache/dragon-agents/dragon-agents/<version>/`), not from this repo. Proven refresh procedure (2026-09-03, v0.1.1 test bump): bump `version` in `.zcode-plugin/plugin.json` and push, then in Plugin Marketplace update the **dragon-agents source**, then **Uninstall → Install** the plugin. A plugin-level Update against a stale source silently no-ops, and there is no Update/Reinstall affordance for directory-marketplace plugins at all (the detail page's "…" menu is Enable + Uninstall only). Verify the new cache slot appeared; roster changes only land in conversations opened after the swap.
- The marketplace keeps its own snapshot at `~/.zcode/cli/plugins/marketplaces/dragon-agents/`, a git clone of the GitHub remote that only moves when the marketplace is refreshed; a reinstall against a stale snapshot silently reinstalls the old version (2026-10-30: reinstall pulled v0.5.0 from a snapshot last pulled 2026-10-06, hours before v0.6.0 was pushed). If the in-app source update is missed or no-ops, the snapshot can be fast-forwarded manually while the plugin is uninstalled: `git -C ~/.zcode/cli/plugins/marketplaces/dragon-agents pull --ff-only` (verified live 2026-10-30), then Install and verify `installed_plugins.json` shows the new version.
- Plugins from cache marketplaces install DISABLED until first enabled; the bundled official plugins are the ones enabled by default.
- The agent roster is baked at each conversation's app-server boot: a mid-session enable or roster change never hot-applies to an open conversation. Test in a fresh conversation, canary `dragon-agents:repo-cartographer` on this repo first.
- The marketplace Enable button may keep saying "Enable" after a successful click. Trust `enabledPlugins` in `~/.zcode/cli/config.json` and a canary dispatch over the button.

## Validation

Run `python3 scripts/validate.py` before committing. It checks that both JSON manifests parse and match the expected shape, that every agent file's frontmatter is well-formed (name matches filename, non-empty description, tools matching the agent's class), that read-only charters carry the read-only line, write-seat charters carry the Clean tree and never-commit fences, latro carries the new-file and never-authenticate fences, assay carries the read-only-lane, append-only, clean-tree, never-commit, and never-authenticate fences, imprint carries the metadata-lane, two-mutations-allowlist, never-commit, and forbidden-mutations fences, that every charter carries the no-subagent line and the `## Debug reporting` section, and that the roster is exactly the expected thirty. CI runs the same script.

## Release flow

A release is a version bump plus the plugin refresh: bump `version` in
`.zcode-plugin/plugin.json`, land the agent/docs changes, commit and push
verified work (the standing push grant in the global file), wait for CI
(validate.py) to go green, then tag: annotated `vX.Y.Z` at the release
commit, message = the `patchnotes.md` entry verbatim (`--cleanup=verbatim`;
the full tag procedure lives in `~/.zcode/AGENTS.md`); the tag itself
still waits for Brandon's go. Then run the refresh procedure in Runtime
gotchas. Docs-only commits follow the no-bump precedent in "What lives
here".
