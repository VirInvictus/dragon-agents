# Patchnotes

Release notes for dragon-agents, newest at top.

## v0.8.2 (2026-11-11)

workspace-sentinel learns the release-census check: pushed tags with no
GitHub Release now rank as findings, alongside entry-without-tag. The
2026-11-11 backfill (184 missing releases across 20 repos; Hearth was
0/47, dragon-agents 1/12) is the cited incident; the release skill and
the workspace tag procedure carry the forward fix, and the sentinel is
the recurring guard. Archived repos are reported as
release-blocked-archived, not as clean.

## v0.8.1 (2026-11-10)

Charter hardening before activation (Brandon's pre-install check), both
acquisition-pipeline agents.

- claw's rung 0 is now an explicit toolchain gate: it names all three
  required tools (`cquarry` from calibrequarry, `bindery` from
  bindery-cli, and the companion-script venv python), probes
  `command -v` + `--version` on each, and on any miss reports
  `REFUSED: toolchain missing (<what failed>) - install with uv tool
  install <pkg>@latest --force` and stops. No improvising around a
  half-installed lane.
- shadow carries the matching gate: `BLOCKED: toolchain missing` and
  stop, for its own cquarry-read and library-validator needs.
- Library-side wiring shipped the same day (not repo code): the two
  import skills now name the delegation lane (claw for phases 1-2,
  shadow for phase audits) and keep their full bodies as the canonical
  main-thread fallback; the library's AGENTS.md pathway section names
  both agents and its header's stale Claude Code references were
  updated to the AGENTS.md-era paths.

## v0.8.0 (2026-11-10)

Twenty-fifth and twenty-sixth agents: **claw**, the roster's first
gated execution seat (import runner), and **shadow**, its read-only
phase gate (import auditor). The Calibre acquisition pipeline's
file-side halves (phases 1 and 2) move out of the main thread; phase 3
stays there, declined with reasons recorded in the roadmap. Named for
Wolfe's Shadow & Claw.

- Founding-rule amendment, recorded: every prior agent is read-only by
  charter; Brandon amended that on 2026-11-10 for one narrow lane.
  What makes the lane chartered rather than a broken seal: every
  phase-1 write is to loose files under the dispatched batch directory
  through tools that demand backups outside the tree; phase 2 is one
  verb whose own gates do the work (refuses an unsigned manifest,
  refuses a missing --backup-dir outside the library, refuses files
  beyond the approved list, one all-or-nothing transaction with
  rollback); the agent never runs `cquarry run sign` or `approve`,
  never resolves a decision on its own, and never opens metadata.db
  directly. The seal moved one step closer to Brandon: the main thread
  signs.
- claw is trained to find the procedure, not to remember it: the
  charter mandates a runtime read of the phase-1 skill every run (the
  skills accrete traps weekly) and carries only the stable fence and
  decision-point core (duplicate and related overrides, lossy consent
  with the image-carrier check, edition and binding calls, stub and
  monolithic triage, provenance verify). Stamp research returns as
  evidence slices for the main thread's fleet; the runner spawns
  nothing.
- shadow audits one phase cold against the manifest and the two skills
  before sign or commit: approved-versus-staged path sets, verdicts
  versus decisions, stamp read-backs, imported ID sets, bak diffs, and
  the validator line, reporting CLEAR TO SIGN / CLEAR TO COMMIT /
  CLEAR TO CLOSE or BLOCKED with evidence.
- Phase 3 was scored and declined an agent (see the roadmap ledger):
  its write shape has a human gate between findings and execution, its
  judgment is house-voice prose and precedent tagging against a
  467-tag taxonomy, and this library carries five documented incidents
  of agent-produced record lists dropping or inventing ids plus a
  21-of-49 override rate on agent pass-verdicts. shadow's pre-flight
  and post-transaction modes carry the mechanical half instead.
- Probed live before chartering (2026-11-10, cquarry 3.86.0, bindery
  1.1.0; versions deliberately unpinned in the charters): the run-verb
  help pages for phase1, sign, approve, and phase2; the companion
  script set; the manifest schema read from that day's live batch; the
  Calibre-closed guard; and the external CLI set. Nothing probed
  turned up dead.
- Toolchain gate hardened in both charters (Brandon's pre-activation
  check): claw's rung 0 names all three tools (cquarry/calibrequarry,
  bindery-cli, and the companion-script venv python) and on any miss
  reports `REFUSED: toolchain missing` with the exact install command
  and stops; shadow carries the matching BLOCKED gate for its own
  reads.
- librarian's run-verb fence reworded to route the acquisition verbs
  to claw's lane; every librarian fence of its own is unchanged.

## v0.7.1 (2026-10-30)

Portability hardening of the two collection seats; roster unchanged at
twenty-four. librarian and music-archivist were machine-bound: their
ladders hardcoded Brandon's paths and assumed his toolchain. Both now
open with a rung 0 environment probe and resolve their library through
the tool's own discovery contract, so the same charters work on any
machine that has the underlying packages (a calibrequarry, bindery-cli,
or lattice-music user), while the v0.7.0 fences, verified quirks, and
output contracts carry forward unchanged.

- **librarian**: discovery rides cquarry's own chain, verified from
  source: the --db flag (a metadata.db path or its library directory),
  the saved ~/.config/cquarry/config.json, then the tool's defaults
  (./metadata.db, ~/Calibre Library/metadata.db, ~/calibre/metadata.db);
  a non-TTY miss raises FileNotFoundError rather than prompting, so the
  absent behavior is documented from source, never manufactured. Two
  probed tool-side effects are carried honestly: a defaults-chain hit
  saves itself into the config, and bindery resolves its library only
  from its own directory and the cwd, so it runs from the library root.
  A new absolute fence bans hunting the filesystem for a metadata.db
  outside the chain: a wrong library answered confidently is the worst
  failure the seat knows.
- **music-archivist**: the root comes from the dispatch (--root, or the
  positional the export modes take) or lattice's saved config
  (library_roots else library_root), nothing else. Probing exposed a
  real landmine, now fenced absolutely: with no --root and no config, a
  non-TTY lattice silently scans the current directory, and a
  configured root that is unmounted is silently dropped before that
  same fallback fires. The charter never rides that fallback; no
  dispatch root and no config root is a stop-and-report.
- The not-applicable verdict is a first-class output for both seats:
  which surface is missing, the probes tried, and the providing package
  (calibrequarry, bindery-cli, lattice-music on pip and uv), reporting
  only; installing stays the dispatcher's move and outside the
  read-only allowlist.
- Descriptions generalized: the frontmatter no longer promises
  ~/docs/Calibre Library or /mnt/SharedData/Music, keeping the
  books/Calibre/cquarry versus music/albums/lattice trigger split.
  This machine's paths stay in the charters as the documented,
  verified-here anchors, and the README table rows never carried the
  paths, so they are unchanged. No roster, validator, or AGENTS.md
  change.

## v0.7.0 (2026-10-30)

Twenty-fourth agent: **music-archivist**, the librarian pattern applied to
the music collection: lattice's read-only audit surface over
/mnt/SharedData/Music in place of cquarry over metadata.db. The same wave
reworks **librarian** so the two collection seats stay crisply separable at
dispatch time: books, Calibre, and cquarry on one side; music, albums, and
lattice on the other.

- Probing before chartering caught two default-write landmines and fenced
  them absolutely: `--extractArt` writes cover images with no output flag
  at all, and `--genreTidy-build` writes its map on every run with no
  dry-run gate (the dropped genre_map.tsv was already sitting in the
  library root). Every other write mode, the nine repo scripts/
  companions, and the update_docs catalog refresh are fenced the same
  way, and the charter standardizes on `--output -` because default
  output paths are report files in the current directory.
- Verified quirks the charter carries: `--where` scopes the read exports
  and audits with exact case-sensitive genre and artist strings and no
  format field; `--json` rides stats, health, and the six gateable audits;
  only 4-star and 5-star ratings exist, so `rating >= 5` is the real
  best-of filter; the collection holds zero FLAC, so taxonomy §7's FLAC
  talk is historical; playlists, play counts, and listening history do
  not exist, and the charter says the what-did-I-listen-to question is
  unanswerable rather than approximating it.
- Every count in the conventions layer is a dated snapshot (taxonomy §11
  2026-08-06, catalogs 2026-10-17, live tree 2026-10-30); the charter
  makes live lattice output win and every reported number carry its
  as-of.
- **librarian rechartered** (roster unchanged): the v0.4.0 charter
  sketched five modes of what was already CalibreQuarry's CLI under the
  name "cquarry"; v2 names the binary truthfully and rides a fully
  verified surface ladder. Scope is books-core per Brandon's lock: the
  Calibre library proper plus its taxonomy, catalog, and acquisition
  cluster, with music handed to music-archivist and the
  comics/audiobooks/games trees carried as mount-state pointers. Depth is
  hybrid: the library's own law corpus (CLAUDE.md NON-NEGOTIABLES,
  TAXONOMY.md and taxonomy.yaml, the catalogs runbook, refresh.md §8) is
  read at dispatch time, while the load-bearing rules moved inline (one
  hierarchical tag per book, generated exports never hand-edited, ID-set
  reconciliation over counts, the ownership predicate, dated counts,
  drift flagged instead of silently fixed).
- The librarian rework's live probes forced real corrections: duckdb 1.5.5
  attaches SQLite natively (the v0.4.0 "pre-installed extension" framing
  retired; the never-INSTALL fence stands), bare `cquarry` launches the
  TUI even in a non-TTY agent shell, the file-writing "read" modes
  (`--audit`, `--catalog`, `--export`, `--all-wings`) are fenced in favor
  of stdout counterparts, bindery's library mode requires the shell to
  sit in the library root, ADVISORY findings do not trip bindery's exit-1
  contract, and `validate_library.py` runs sub-second with allowlisted
  findings suppressed on a clean pass. The dated-snapshot rule earned its
  place live: the library header said 10,031 books (dated 2026-10-21)
  against a live 10,189, and Unsorted went from 9 books to 0 between the
  morning research sweep and the afternoon charter probes while both
  spec docs said empty throughout.
- Packaging: roster check extends to twenty-four; README, AGENTS.md, both
  manifests, and the roadmap synced; the pending v0.6.0 activation pass
  is subsumed into this wave's activation. First charter rework on the
  roster: librarian's name, color, tools, and model pin are unchanged.

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
