# Patchnotes

Release notes for dragon-agents, newest at top.

## v0.6.0 (2026-10-05)

Twenty-third agent: **syshealth-auditor**, the machine lane from the
roadmap's v0.5+ candidates, drafted by charter-architect on its first
live dispatch. It censuses backup freshness and system health from
state reads: sys_maintain's per-component success timestamps against
their own cooldowns, failures from its rotated run log, borgmatic
config and borg repo state, failed user units plus one boot-scoped
journal pass for system failed units, disk space, and pending-reboot
flags.

- Both roadmap entry conditions were settled by live probing before
  chartering. `borg info` does not run in an agent shell (no BORG_*
  env; repokey repo; verified failure), so archive freshness comes
  from state reads: the borgmatic timestamp, borg cache mtimes, and
  repo segment listing. The borgmatic `encryption_passcommand`
  (`rbw get`) is fenced: documented, never executed.
- The mode-vs-agent call against workspace-sentinel resolved to a new
  agent: sentinel's trigger is repo state across the workspace;
  machine state shares no corpus and no allowlist with it, and folding
  it in would blur two clean triggers.
- Verified quirks the charter carries: system-mode `systemctl` times
  out from agent shells (sandboxed and not; user mode works), so
  system failed units ride one bounded journal query; `btrfs_health`
  needs root and is reported as a direction with its exact command,
  never run.
- Packaging: roster check extends to twenty-three; README, AGENTS.md,
  both manifests, and the roadmap synced, with the dead-surface
  record extended (agent-shell systemctl and passphrase-gated borg).

## v0.5.0 (2026-10-05)

Twenty-second agent: **charter-architect**, the roster's meta lane. It
designs new agents: scorecard verdict (declining is a valid outcome),
a charter draft in the house anatomy with every tool surface probed
live, and the complete release kit (validator diff, doc syncs,
patchnotes entry, roadmap tick, commit message, activation checklist
with canary dispatch prompts) returned as text for the main thread to
apply. Draft-only by the repo's read-only non-negotiable: the architect
composes, the main thread edits, gates, and releases. It is growth
tooling, not roster growth; the roadmap's domain-axis conclusion
stands, and this agent is the lane that enforces it.

- Method grounded in three research veins: the four keys from Claude's
  subagent design guidance (descriptions as the routing signal, defined
  output contracts, obstacle reporting, minimal tool access); the
  draft-test-refine loop and lean-prompt discipline of ZCode's own
  skill-creator, the house precedent for a tool that authors its own
  artifact type; and the ADAS meta-agent line, where new agent designs
  are generated against an archive of prior ones (this charter corpus
  and its git history are that archive).
- Future roster candidates dispatch through charter-architect first;
  the roadmap's v0.5+ lanes (syshealth-auditor, ctf-recon, log-miner)
  are its first customers when their entry conditions fire.
- Packaging: roster check extends to twenty-two; README, AGENTS.md,
  both manifests, and the roadmap synced. The roadmap itself was
  introduced this cycle (b04177e, docs-only), and this release is its
  first stamp-and-tick carrier sync.

## v0.4.0 (2026-10-05)

Four domain-research agents; the roster grows from seventeen to twenty-one.
Selection was evidence-driven: a sweep of the multi-agent literature and
community rosters (Anthropic's orchestrator-worker write-up, Microsoft's
single-vs-multi-agent guidance, the VoltAgent awesome-list, and a
practitioner's 100-built-12-kept cut list) kept pointing at read-only
research as where subagents pay off, and at personal-data surfaces nothing
in the roster wrapped. Tool surfaces were probed live during chartering;
the corrections that probing forced (a nonexistent hledger flag, duckdb's
extension story, the exact lockfiles this fleet pins with) were folded in
before release.

- **ledger-analyst**: hledger finance briefs (cashflow, budget vs actual,
  net worth, cost-basis extracts that can feed stock-broker guidance).
  Verification found no journal on this machine; the live finance data is
  GPG-encrypted org files under `~/org/finance/`. The charter is therefore
  hledger-ready with an absolute fence: it reports "no readable journal"
  until a readable journal exists outside the fence, and never decrypts or
  reads the encrypted files.
- **librarian**: Calibre library research through cquarry's read surface
  (analytics, audit, health, series, FTS) plus read-only duckdb joins; it
  obeys the library's own CLAUDE.md and never uses cquarry's write flags.
- **data-analyst**: read-only duckdb profiling of datasets named in the
  dispatch (schema, nulls, top-N, joins, anomaly counts); the duckdb binary
  installed 2026-09-20 for agent-side SQL gets its consumer.
- **security-auditor**: defensive review of owned repos only: gitleaks with
  `--redact`, risky-pattern review, dependency advisory cross-checks via
  `gh api` GETs; exposure-ranked findings, remediation as direction only,
  and the CTF toolkit explicitly outside the charter.
- Packaging: the roster check in `scripts/validate.py` extends to
  twenty-one; README, AGENTS.md, and both manifests updated to match.

## v0.3.0 (2026-10-05)

Seventeenth agent: **stock-broker**, the roster's first non-repo researcher.
It briefs companies, ETFs, their sectors and peers, and the surrounding
markets (rates, indices, inflation, FX, commodities) from keyless public
sources only, gives portfolio-relative guidance when
`~/.config/refs/portfolio.md` supplies context, and leaves the decision
explicitly with the dispatcher.

- **stock-broker**: SEC EDGAR filings and XBRL fundamentals via
  `data.sec.gov`, with CIK resolution through the efts full-text search API
  (the `www.sec.gov` mapping file is blocked from this network); quotes and
  history across asset classes via Yahoo's public chart endpoint, Nasdaq's
  quote API as the equity backup, FRED CSVs for macro series, sponsor pages
  and Wikipedia as the scrape fallback. Every rung was verified live before
  the charter was written, which is also why Stooq is documented as dead:
  its CSV endpoints now sit behind a JavaScript proof-of-work challenge
  curl cannot solve.
- Guidance voice per Brandon's call: cited analysis with explicit unknowns,
  advice only relative to the portfolio context file, never authentication,
  never trading, never portfolio details in outbound traffic.
- Packaging: the roster check in `scripts/validate.py` extends to seventeen;
  README, AGENTS.md, and both manifests updated to match.

## v0.2.1 (2026-09-20)

Maintenance release from the 2026-09-20 setup audit (ci-posture-auditor,
doc-drift-auditor, and claim-verifier findings, independently verified).
No roster or charter changes.

- **CI hardened to the house shape** (`ci.yml`): actions SHA-pinned
  (checkout v4.4.0, setup-python v5.6.0), top-level `permissions:
  contents: read`, `concurrency` with cancel-in-progress,
  `timeout-minutes: 10` on the validate job, and `python-version`
  pinned to 3.14 instead of a floating `3.x`. The repo that audits the
  fleet's CI now matches the shape it audits against.
- **README install docs fixed** (blocking doc-drift finding): the
  install section claimed new plugins are enabled by default; that
  holds only for bundled official marketplaces. Plugins from a local
  directory marketplace like this one install disabled until first
  enabled, which is exactly the trap behind the 2026-09-05
  silent-reload incident. The section now says so and points at the
  gotchas in AGENTS.md.

## v0.2.0 (2026-09-20)

Ten new read-only research agents; the roster grows from six to sixteen.
Selection was evidence-driven from the 2026-09-04 to 09-17 workspace blitz
retrospective: five VERSION-carrier incidents across 319 tags, five manual
catalog reconciliations, the CI-hardening shape propagating repo to repo by
hand, and a test suite that silently sat outside unittest discovery.

- **release-auditor**: pre-tag readiness and post-tag sweep; every VERSION
  carrier, patchnotes entry heading style, and annotated-tag message health
  (the sweep the global tag procedure already mandates).
- **workspace-sentinel**: one-dispatch sweep of all owned repos; dirty trees,
  unpushed commits and tags, untagged releases, stale catalog rows.
- **ci-posture-auditor**: workflows against the house-hardened CI shape
  (SHA-pinned actions, least permissions, concurrency, timeouts); finds the
  repos still behind.
- **debt-census**: TODO/FIXME/HACK and dead-reference census with blame
  dating, as a cleanup worklist.
- **code-reviewer**: bug-hunting diff review (correctness, edge cases, scope
  creep, userspace-break risk); distinct from spec-compliance-reviewer, which
  checks the contract.
- **git-archaeologist**: regression windows and provenance from log, blame,
  and pickaxe; returns bisect plans, never runs them.
- **claim-verifier**: independent re-verification of findings lists;
  confirmed / refuted / unverifiable per claim.
- **dependency-auditor**: declared vs imported, floors vs the APIs actually
  used, stdlib-purity verification, Flatpak vendor staleness, toolchain drift.
- **test-gap-analyst**: static coverage map and suite-discovery checks;
  never builds or executes tests.
- **duplication-scout**: cross-repo similar-module detection feeding the
  library-graduation rule; evidence only, never the recommendation.

Packaging: `patchnotes.md` introduced with this release. The v0.1.0 and
v0.1.1 tags carry one-line messages and predate it; from v0.2.0 on, tags
follow the full-entry procedure. `scripts/validate.py` roster check extended
to the sixteen agents; README and AGENTS.md updated to match.
