# Roadmap

Forward plan for the dragon-agents roster: what shipped, what could ship
next and under what conditions, and what was declined with reasons so no
future session re-litigates it. Updated as of v0.6.0.

## Standing rules (how this roster grows)

- **Research-first waves.** Every candidate faces the five-criterion
  scorecard before chartering: context win (keeps big output out of the
  main thread), trigger precision (sharp, non-overlapping description),
  frequency (roughly weekly real use), charter fit (read-only, Read+Bash,
  research-only, no builds), and source stability (the surface will not
  rot next quarter). Evidence base recorded under "Records kept here".
- **The non-negotiables hold at every version:** agents stay read-only
  with `tools: [Read, Bash]`, no nesting, and this repo stays stdlib-only
  markdown and JSON. Builders, executors, and orchestrators are excluded
  by charter, not by oversight.
- **Modes before agents.** A candidate expressible as a mode of an
  existing agent prefers the mode unless trigger precision genuinely
  suffers.
- **Probe surfaces live before chartering.** Both waves so far were
  corrected by live probing (Stooq's JavaScript wall, the www.sec.gov
  block, a nonexistent hledger flag, duckdb's sqlite extension story);
  chartering from memory is how dead endpoints get documented as live.
- **Activation is part of every release:** marketplace source Update,
  Uninstall → Install, cache-slot verify, app relaunch, canary dispatch,
  and the full model re-pin (a reinstall wipes every pin). The pass is
  Brandon's; the release is not done until it has happened.
- **Roster candidates go through charter-architect.** When a candidate's
  entry condition fires, dispatch the architect to scorecard it and
  draft the kit; no charter gets hand-written in the main thread
  anymore.

## Completed

- [x] v0.1.0 and v0.1.1 (2026-09-03): plugin bootstrap, six core agents,
      the marketplace refresh procedure proven.
- [x] v0.2.0 and v0.2.1 (2026-09-20): ten agents from the workspace
      blitz retrospective (roster 16); CI hardened to the house shape;
      patchnotes and the full-entry tag procedure adopted.
- [x] v0.3.0 (2026-10-05): stock-broker, the first non-repo researcher;
      keyless source ladder verified live (EDGAR via data+efts, Yahoo
      chart, Nasdaq, FRED; Stooq and the www host documented dead).
- [x] v0.4.0 (2026-10-05): ledger-analyst, librarian, data-analyst,
      security-auditor from the researched scorecard (roster 21); the
      duckdb sqlite extension pre-installed so read-only attaches work
      offline; slop-reader precision fixes folded in before tagging.
- [x] v0.5.0 (2026-10-05): charter-architect, the meta lane (roster
      22). It drafts new agents and their release kits; from here,
      roster candidates dispatch through it before any charter is
      hand-written.
- [x] v0.6.0 (2026-10-05): syshealth-auditor, the machine lane
      (roster 23), drafted by charter-architect on its first live
      dispatch. Both entry conditions settled by live probing:
      `borg info` is passphrase-gated in agent shells (state reads
      chartered instead, the rbw passcommand fenced), and the
      sentinel mode-vs-agent call resolved to a new agent (repo-state
      and machine-state triggers share no corpus or allowlist).

## Dependencies that unlock existing agents (Brandon's moves, not waves)

- [ ] A hledger journal exists outside the encrypted-finance fence:
      ledger-analyst goes from "no readable journal" to live briefs.
- [ ] `~/.config/refs/portfolio.md` carries real positions: stock-broker
      gains portfolio-relative guidance.
- [x] The v0.3.0 + v0.4.0 + v0.5.0 activation pass (one reinstall
      covers all three). *(Completed 2026-10-05: install, relaunch,
      canaries all passing; pins were retained that time, only the new
      agents needed setting.)*
- [ ] The v0.6.0 activation pass (same procedure, whenever convenient;
      pins retained last time, so likely just the one new agent).

## v0.5+ candidates (each fires on its own green light)

- [ ] **ctf-recon**: research assistant over the local CTF stack
      (pwntools, checksec, radare2, Ghidra). Entry condition: a CTF
      season actually starts. The charter needs local-and-CTF-platform
      framing that stays inside the read-only line (analysis of given
      artifacts, never external targets).
- [ ] **log-miner**: journalctl and audit-log root-cause researcher for
      "what happened on this machine" questions. Entry condition: a real
      incident where manual journalctl grepping fumbled. The dispatch
      split from ci-triage must stay crisp (system state versus CI runs).

## Watch list (recorded, not committed)

- [ ] **web-researcher**: the stock-broker cited-web pattern generalized,
      with monolith for page archiving. Fires only if a second recurring
      web-research need appears; until then the main thread's WebSearch
      owns the space and a general charter invites description
      collisions.
- [ ] **schedule-analyst**: a td + gcalcli weekly digest. Cheap but low
      volume; ActivityWatch exports are already data-analyst surface via
      named endpoints. Fires only if weekly planning becomes a recurring
      ask.

## Declined (with reasons, so it stays decided)

- **Builders, language specialists, infra executors** (the bulk of
  community rosters): excluded by the read-only research charter, and the
  practitioner evidence says they duplicate what the main model already
  does well.
- **Orchestrators and context-managers**: the no-nesting charter excludes
  them, and the one meta-agent kept by the practitioner filter carried
  the worst token-budget risk of his dozen.
- **perf-benchmarker**: meaningful benchmarking needs builds, which the
  charters forbid.
- **activity-analyst as its own agent**: folded into data-analyst's
  named-endpoint allowance rather than doubled.

## Records kept here

- **Wave-selection evidence (2026-10-05).** Anthropic's multi-agent
  research write-up (90.2% research-eval gain for orchestrator-worker,
  roughly 15x chat token cost, explicitly a poor fit where subagents need
  shared context, "e.g. most coding"); Microsoft's guidance (go
  multi-agent only once single-agent limits are demonstrated); the
  practitioner who built 100 subagents and kept 12 (keepers are context
  wins; "defined by a job title, not a context win" never triggers;
  fuzzy overlapping descriptions made the orchestrator pick the wrong
  agent or none, so his filter cut them; he runs 3 daily); the VoltAgent
  awesome-list and the hesreallyhim
  directory (their additive roles over this roster are execution-shaped).
  Conclusion: the role axis is saturated at twenty-one; growth is
  domain-axis and scorecard-gated.
- **Dead or blocked surfaces, verified:** Stooq CSV endpoints
  (JavaScript proof-of-work wall), `www.sec.gov/files/*` (network block;
  use data.sec.gov plus efts), hledger `--lots` (does not exist in
  1.52.4), OSV's query API (POST; use `gh api /advisories` GETs),
  agent-shell system-mode `systemctl` (D-Bus connect times out,
  sandboxed and not; user mode works, system failed units ride one
  boot-scoped `journalctl -b --grep` pass), `borg info`/`list` in agent
  shells (passphrase-gated; use sys-maintain timestamps, cache mtimes,
  and repo state reads).
- **The usage-measurement gap:** ZCode session logs cannot measure
  dispatch counts (7-day retention, tool_use inputs not greppable), so
  roster-pruning calls ride judgment rather than telemetry. Revisit if
  the platform ever exposes dispatch counts.
