# Roadmap

Forward plan for the dragon-agents roster: what shipped, what could ship
next and under what conditions, and what was declined with reasons so no
future session re-litigates it. Updated as of v0.9.0.

## Standing rules (how this roster grows)

- **Research-first waves.** Every candidate faces the five-criterion
  scorecard before chartering: context win (keeps big output out of the
  main thread), trigger precision (sharp, non-overlapping description),
  frequency (roughly weekly real use), charter fit (read-only default;
  for a write seat, fence-fit: report-only default, a named scope, never
  a commit, no builds beyond dispatch consent), and source stability
  (the surface will not rot next quarter). Evidence base recorded under
  "Records kept here".
- **The non-negotiables hold at every version, as amended twice:**
  agents stay read-only by default, no nesting, and this repo stays
  stdlib-only markdown and JSON. Write capability is chartered only.
  claw (v0.8.0, Brandon's amendment of 2026-11-10) writes through
  tool-side structural gates (backup-dir outside the tree, an
  HMAC-sealed manifest the agent itself may never seal,
  refuse-beyond-the-approved-list, one rolled-back transaction) on
  loose-file blast radius, and the seal plus every ungated library write
  stay with the main thread. The five charter-fence seats (v0.9.0,
  Brandon's amendment of 2026-11-11: charter-architect,
  ci-posture-auditor, doc-drift-auditor, debt-census, test-gap-analyst)
  carry `tools: [Read, Edit, Write, Bash]` under the fence model:
  report-only default, a clean-tree precondition, a named write scope,
  never a commit, re-verification after applying, an itemized report.
  The six judges and gates (claim-verifier, shadow, code-reviewer,
  spec-compliance-reviewer, security-auditor, slop-reader) stay
  read-only; builders, executors, and orchestrators without fences
  remain excluded by charter, not by oversight.
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
- [x] v0.7.0 (2026-10-30): music-archivist, the second collection seat
      (roster 24), drafted by charter-architect; the librarian pattern
      applied to the music tree through lattice's read-only audits, with
      librarian reworked in the same wave to sharpen the trigger split.
      Probing fenced two default-write landmines (--extractArt,
      --genreTidy-build) and fixed the charter on `--output -`.
- [x] v0.7.1 (2026-10-30): portability hardening of the two collection
      seats (roster unchanged). librarian and music-archivist open with
      a rung 0 environment probe, resolve their library through the
      tools' own source-verified contracts (cquarry's find_db chain;
      lattice's config roots), return first-class not-applicable
      verdicts naming the providing packages, and carry generalized
      descriptions while this machine's paths stay the documented
      anchors. Probing fenced a real landmine: a non-TTY lattice with
      no root silently scans the current directory, and an unmounted
      configured root falls to that same fallback.
- [x] v0.8.2 (2026-11-11): workspace-sentinel learns the
      release-census check (pushed tags with no GitHub Release rank as
      findings; archived repos reported release-blocked), cited to the
      same-day 184-release backfill. The forward fix lives in the
      release skill's step 9 and the workspace tag procedure; the
      sentinel is the recurring guard.
- [x] v0.9.0 (2026-11-11): the second founding-rule amendment, Brandon's
      write-forward pass. Five audit-and-fix seats gain chartered write
      lanes under the fence model (report-only default, clean-tree
      precondition, named scope, never a commit, re-verify after
      applying, itemized report): charter-architect lands its own
      approved release kits, ci-posture-auditor writes the CI hardening
      (tightening only), doc-drift-auditor fixes mechanical drift,
      debt-census removes named census items, test-gap-analyst writes
      and runs the named missing tests (production code never touched).
      Roster unchanged at 26; the six judges and gates stay read-only;
      librarian and music-archivist stay fenced and the phase-3 decline
      stands. Model pins move with the writes: ci-posture-auditor,
      debt-census, and test-gap-analyst flip Flash to GLM-5.3 (the
      anything-that-writes rule). charter-architect's own upgrade was
      the one main-thread hand edit, applied first so the lane could
      exist.
- [x] v0.8.1 (2026-11-10): charter hardening before activation - claw's
      rung 0 becomes an explicit three-tool toolchain gate (REFUSED +
      install command on any miss), shadow carries the matching BLOCKED
      gate; library-side, the two skills name the delegation lane with
      their full bodies as the main-thread fallback.
- [x] v0.8.0 (2026-11-10): claw and shadow, the acquisition-pipeline
      seat (roster 26), drafted by charter-architect from Brandon's
      write-forward candidate and the split architecture agreed before
      dispatch. The founding read-only rule took its first recorded
      amendment, gated per the standing rules; a phase-3 write agent was
      scored and declined (ledger below); librarian's run-verb fence
      reworded in the same wave. Named for Wolfe's Shadow & Claw:
      shadow is the gate that watches, claw is the hand that executes.

## Dependencies that unlock existing agents (Brandon's moves, not waves)

- [ ] A hledger journal exists outside the encrypted-finance fence:
      ledger-analyst goes from "no readable journal" to live briefs.
- [ ] `~/.config/refs/portfolio.md` carries real positions: stock-broker
      gains portfolio-relative guidance.
- [x] The v0.3.0 + v0.4.0 + v0.5.0 activation pass (one reinstall
      covers all three). *(Completed 2026-10-05: install, relaunch,
      canaries all passing; pins were retained that time, only the new
      agents needed setting.)*
- [ ] The v0.6.0 through v0.8.0 activation pass (one reinstall covers
      all; pins were retained across the last reinstall, so expect to
      set claw and shadow and re-verify the rest).

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

- **A phase-3 write agent (raw WritableCalibreDB curation)**
  (2026-11-10): the write shape's human gate (audit, findings,
  Brandon's sign-off, bak, one transaction) sits between evidence and
  execution, so an agent either stops at findings (no win over
  shadow's pre-flight mode) or holds the pen unsupervised on the
  workspace's highest-blast-radius surface, with no seal or approved
  list to gate it. The library's own record decides it: agents are
  reliable on "contaminated" and unreliable on "fine" (21 overrides in
  49 on one wing), and five incidents of dropped or invented ids in
  agent record lists. The mechanical half ships as shadow's pre-flight
  and post-transaction modes; the judgment stays main-thread, and the
  phase-3 skill remains the judgment ledger. Unchanged by the v0.9.0
  amendment: it ruled judgment-heavy curation, not mechanically
  verifiable fixes, and librarian stays fenced.
- **Builders, language specialists, infra executors** (the bulk of
  community rosters): excluded by the read-only research charter, and the
  practitioner evidence says they duplicate what the main model already
  does well. (claw arrived v0.8.0 under tool-side structural gates, and
  v0.9.0 chartered five fence-gated audit-and-fix seats alongside it, a
  narrow deliberate slice. The bulk exclusion stands.)
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
