# Patchnotes

Release notes for dragon-agents, newest at top.

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
