# Patchnotes

Release notes for dragon-agents, newest at top.

## v1.6.0 (2026-11-18)

The comparative-design and marketing wave: one new read-only seat, the
fleet's first in-repo authored skill, four charter patches from the
comparative seat-design report, the evals convention, and a README
rebuilt for readability. Drafted by charter-architect from the
campaign's second research leg (the 37-source repo-marketing report;
the first leg's 69-source pair fed v1.5.0, and a 32-source comparative
seat-design report drove the patches). Roster thirty-eight:
twenty-seven read-only, ten write seats, one multimodal judge.

- **repo-marketer** (GLM-5.3-Flash): the launch desk, read-only with
  web tools (the assay tool class). Given a repository it returns a
  placement analysis across the earned channels (Show HN, language
  subreddits, Lobsters, curated newsletters, Discord and Matrix,
  dev.to cross-posts, awesome lists) judged against each channel's
  live rules, the repo's actual maturity, and the operator's stated
  standing; an explicit where-not-to-post list; channel-native drafts
  built from the repo's own artifacts on the demonstrate-don't-claim
  skeleton (the trurl shape: analogy, problem, copy-pasteable
  examples, honest-maturity section, roughly 400 words);
  similar-projects research on the live web; a paid-advertising
  worth-it verdict with the arithmetic shown (the honest baseline is
  that most pure OSS gains nothing; three defensible conditions and
  four burn patterns carry their numbers); and a measurability plan
  (HN's spike shape, the roughly 20:1 HN-to-Reddit volume ratio,
  GitHub's 14-day referrer panel, UTM conventions with the lossiness
  caveat). The fences are absolute and first: it never posts, never
  comments, never votes, never opens a browser session to any
  platform, never authenticates, never touches a social account;
  drafts land in the final message only and the human posts. The
  enforcement reason is documented, not theorized: the February 2026
  matplotlib incident, where an autonomous agent retaliated against a
  maintainer over a rejected PR with a fabricated-quote hit piece,
  makes drafts-only a structural requirement. Anti-hype guardrails are
  charter law (the Stenberg standard): every claim traces to a repo
  artifact, no invented traction, no star-count flexing, every launch
  draft carries an honest-maturity section, every draft carries its
  channel's compliance note. Live probing shaped four rungs: HN's
  rules pages and lobste.rs fetch clean keyless while Reddit's rules
  routes 302 to a login wall under curl (the charter pins the WebFetch
  route and the "rules unverified" marking instead of promising
  fetches); hn.algolia.com's search API verified keyless and instantly
  returned a direct comparable for the dry-run repo; the CalibreQuarry
  dry run surfaced the maturity gate's exact finding class, the
  README's own TODO admitting the missing TUI screenshot.
- **skills/herald**: the Reddit presence buffer, authored by the main
  thread in this same campaign and landing under skills/ beside the
  seven vendored Obsidian skills (validate.py grows the expected set
  to eight). Drafts posts and replies in the operator's voice, triages
  reply threads, and keeps hostile replies at a sanitized distance;
  like repo-marketer it drafts only and the human posts. repo-marketer
  is its research engine: placement and first drafts from the agent,
  ongoing presence from the skill.
- **Comparative charter patches**: code-reviewer's fix-sketch and
  linter-folding rungs, latro's pinpoint-citation rule, and the
  untrusted-corpus lines on latro and issue-census; four of the
  comparative-design report's five STEALs, landed in-tree before this
  release (the report: 32 sources, 25 delta rows, 9 CONSIDERs and 11
  SKIPs also recorded). The fifth STEAL is the evals convention below.
- **evals/ convention**: evals/<seat>/prompt.md holds a realistic
  dispatch prompt and evals/<seat>/graders.md asserts the Output
  contract's shapes; seeding is incremental and an empty evals/
  passes while the convention fills. validate.py carries the light
  parse check.
- **README rebuilt for readability**: the single-mega-paragraph intro
  and one thirty-eight-row table became grouped seat tables by lane, a
  fleet-at-a-glance block, a skills table, and a condensed model
  guidance section pointing at the design guide. Same facts, parseable
  layout.

validate.py grows the roster to thirty-eight, adds the web-research
reader class with its four pins (never posts, never authenticate,
final message only, compliance note), expects the eighth skill
(herald), and carries the v1.6.0 comparative pins and the evals check
landed earlier in the tree.

## v1.5.0 (2026-11-18)

The life-domains wave plus the fleet's first vendored skills: two new
read-only seats, one shared charter line on every charter, and skills/
in the repo. Drafted by charter-architect from the campaign's research
pair (a 37-source stealable-seats report and a 32-source
skills-ecosystem report, 69 sources total). Roster thirty-seven:
twenty-six read-only, ten write seats, one multimodal judge.

- **vault-archivist** (GLM-5.3-Flash): read-only hygiene audit of an
  Obsidian vault, the az9713 /vault-health pattern proven on a
  10,918-file vault (baseline ~4,979 unresolved links): unresolved
  wikilinks and dangling targets, orphan and dead-end notes judged
  against the vault's own linking conventions, frontmatter coverage
  and key consistency, tag-taxonomy drift against the vault's declared
  roots, duplicate and near-duplicate notes, unreferenced attachments,
  plus PROPOSED connections between related notes (the buildwithclaude
  connection-agent lane folded in as a proposals-only rung,
  modes-before-agents: a suggestion list, never an edit). Vault prose
  is never rewritten, and the vault's own guidance file outranks the
  charter (the librarian law-corpus rule). Live probing on the
  reference vault (730 notes by its own walk) pinned three charter
  rungs: the audit universe is reconciled across enumerators because
  the vault's .gitignore deliberately hides the daily journal and
  eight personal notes (fd 626, rg 633, the vault's own script 730;
  an audit trusting one enumerator silently skips the journal), the
  vault's own graph_audit.py is the alias-aware primary authority
  (live: 5 dangling links, 31 orphans under its no-in-and-out
  definition, 2 unreferenced assets), and raw rg extraction carries
  three traps (multi-file path prefixes without -I, 405 embeds and
  136 empty dataview constructs absorbed by a naive pattern, aliases
  and anchors needing strips). One live convention finding of the
  kind the seat exists for: the core daily-notes config carries a
  template path the vault's own law forbids (the Templater race);
  reported, never fixed.
- **subscription-watchdog** (GLM-5.3-Flash): the renewal audit over
  manually exported bank and card statement CSVs, the offline pattern
  community skills already shipped (dvcrn's subscription-audit; the
  agentusecases corpus records a $700 recovery from exactly this
  audit): merchant-stem clustering, cadence from date gaps,
  stable/price-change/missed-billing/trial-to-paid/promo-step flags,
  optional budget-line gate. Deterministic awk/sort work with
  judgment labeled; the fences are absolute: never a bank API, never
  Plaid, never mail (the OpenClaw inbox record is why), never ~/org/
  or anything .gpg/.asc. Dormant until data (the ledger-analyst
  precedent): no statements named returns a first-class
  not-applicable verdict naming the export convention, so the seat
  ships before the data exists. Probing on synthetic statements
  verified the whole rubric and two parse traps: gawk FPAT keeps its
  quotes (a quoted US date silently zeroed every gap until quotes
  were stripped first), and a missed month hides from the median (a
  31-day series carrying one 61-day gap needs the per-gap check, not
  the average).
- **Language discipline, all thirty-seven charters**: answer in the
  dispatch's language to the end of the report. The history is the
  optimization-guide self-audit's not-applied list: a mid-session
  switch to Chinese or another unrequested language is a GLM-lineage
  drift that survives context resets, so the line orders the drift
  named in the Debug Report and the report continued in the
  dispatch's language. Validator-pinned like the v1.3.4 shell line
  before it (issue #7's sibling, promoted from the v1.4.1 candidate
  slot into this wave), pin written first.
- **skills/ vendored**: the seven official Obsidian skills
  (obsidian-cli, obsidian-markdown, obsidian-bases, json-canvas,
  obsidian-headless, defuddle, knap) from obsidianmd/obsidian-skills
  commit 1c3f6df5, MIT, vendored verbatim with ATTRIBUTION.md
  (provenance, commit pins, license chain) and a vet record shaped by
  the Snyk ToxicSkills audit: 36.82 percent of 3,984 community skills
  carried flaws, 13.4 percent critical, 76 confirmed malicious (91
  percent prompt injection), which is why the set is
  official-source-only, license-checked, and source-read before
  vendoring. The community CLI-audit reference (the 57-scenario
  Obsidian CLI gotcha set) is merged per the skills README.

validate.py grows the roster to thirty-seven, pins the
language-discipline rule on every charter, and adds the skills/
structural check: exactly the seven expected skills, every SKILL.md
present with a frontmatter name matching its folder, ATTRIBUTION.md
present. A punctuation-hygiene sweep rode the same release: five
charters (repo-cartographer, doc-drift-auditor, code-reviewer,
spec-compliance-reviewer, claim-verifier) carried em-dashes in their
output templates from before the house prose rule existed; the
templates now use house punctuation, and no verdict vocabulary
changed.

## v1.4.0 (2026-11-18)

The issue-and-propagation wave: five new seats drafted by
charter-architect from the roster-expansion campaign (a 28-source
prior-art report, a full sweep of the workspace's workflow corpus, and
usage mining), riding one release with a release-auditor method patch.
Roster thirty-five: twenty-four read-only, ten write seats, one
multimodal judge.

- **issue-census** (GLM-5.3-Flash): the retrospective census of OPEN
  GitHub issues, one repo or the whole owned fleet, which nothing ships
  (first-party Copilot automations label new issues one at a time; the
  fleet view is unbuilt). Aging profile, open-vs-open duplicate
  clusters, fix-already-landed cross-checks against git log, tags, and
  patchnotes, label hygiene, needs-info zombies, then label-only triage
  verdicts taken from Anthropic's own triage-issue command design: a
  closed vocabulary fetched live from the repo's own labels, duplicates
  marked against open issues only, and the false-positive aversion rule
  ("false positives are worse than missing labels"). It ends with
  rule-based SemVer hints (never model-judged: rules already do it
  exactly) and a proposed release batch. Absolute fences: never
  comments, never closes, never writes a label, never posts anything;
  on-demand dispatch only, never a resident watcher. The 2026-11-11
  issues-triage decline carried its own revisit condition ("if the
  workflow ever moves to issue-driven"); it has fired (the v1.3.0
  debug-report duty files issues as a standing flow, CalibreQuarry's
  release log is issue-driven end to end, opends gates a release on two
  open issues), and the ledger entry records the supersession. Two gh
  quirks carried in the charter: `--json comments` embeds every full
  comment body (verified on opends #13), so comment fields are only
  read through a `--jq` projection, and the REST `open_issues_count`
  counter includes pull requests while `gh issue list` does not.
- **fleet-sync-auditor** (GLM-5.3-Flash): the four-tier propagation
  audit the sync-reference-docs skill has hand-walked after every
  release: the repo's own docs (VERSION carriers, patchnotes placement,
  roadmap ticks, shields.io badge URLs where the version hides inside
  the URL, AGENTS.md status headers, Flatpak runtime pins), the
  workspace catalog row, the public surfaces (the profile README's
  shipping tags, the site codex status spans), and the Obsidian vault's
  identity stubs, where versions are forbidden by design. Propose-only
  by charter: the catalog-reconciler decline stands, the public
  surfaces are push-gated, and the vault is Brandon's prose. The tree
  is the truth (a reference document is never evidence about another
  reference document); tier 3 is curated, so absence from the profile
  README is not drift while a stale listed version is. Trigger lines
  drawn against both neighbors: doc-drift-auditor keeps one repo's docs
  versus code, workspace-sentinel the git-state sweep.
- **upstream-triage** (GLM-5.3: its port/skip verdicts gate porting
  work): the weekly NetNewsWire window behind Viaduct, generalized to
  any dispatch-named reference clone. Reads the last recorded sync
  point from the parent repo's dated sync notes, enumerates the
  upstream window, clusters it into arcs (windows reach +352 commits),
  and returns port / skip / roadmap-candidate verdicts with reasons,
  conflict flags against the parent's local ports, an ordered port
  worklist, and a draft sync note in the parent's own format. Its one
  chartered mutation, pinned in validate.py, is the roster's narrowest
  fetch exception: fetch only the dispatch-named reference clone,
  because triage needs commit content and `git ls-remote` returns only
  the tip (verified live: the clone's origin/main last saw f3a0102c3 on
  2026-11-08 while the tip had already moved, and the window's size was
  unanswerable without the objects). The sentinel's never-fetch rule
  stands everywhere else; the fast-forward, the sync note, and the
  ports stay with the main thread. A clone not declared reference
  material in the parent's AGENTS.md or the catalog is a REFUSED.
- **release-executor** (GLM-5.3, the write axis's first
  post-saturation seat, chartered on Brandon's explicit 2026-11-18
  appetite): the mechanical half of cutting a release, taken out of the
  main thread after a failure history measured in the hundreds (91
  broken tags across 20 repos, 184 missing GitHub Releases backfilled
  in one day, whisker-street's empty-notes-file release, deadbeef-cui's
  four release-workflow fix cycles). Propose mode (the default) drafts
  the exact command plan; apply mode, enumerating repo, version, and
  release commit and carrying release-auditor's ready verdict, verifies
  CI green on the release commit, extracts the patchnotes entry
  verbatim into a scratch file, proofreads it (version, date, heading
  style, no em-dashes, no neighboring tails, never the whole file, body
  non-empty), cuts the annotated tag with --cleanup=verbatim, verifies
  the message with cat-file against the previous tag's detail, pushes
  only that tag, creates the GitHub Release from the same file with
  --verify-tag, reads back every mutation, and closes with the
  for-each-ref subject sweep. Its writes are the roster's second
  instantly-public class (after imprint's metadata): three mutations
  plus the tag push, never force-push, never re-tag, never a branch,
  issue, or file. release-auditor's description now draws its side of
  the line: it gates and sweeps; the executor runs.
- **pixel-judge** (GLM-5.3-Flash, the roster's first multimodal seat
  and first vision-dependent charter): non-document visuals (GTK/Qt
  windows, Godot game screens, the bar, Hyprland, terminals, theming
  changes) judged from handed-in PNG captures plus state text against
  the dispatch's acceptance bar, one JSON verdict line per capture with
  evidence-backed issues and recapture guidance; self-capture is
  chartered only as region-scoped grim to /tmp (verified live on this
  Hyprland session; Catagotchi's own gotcha table documents grim dead
  under KWin, where the repo's capture script is the dispatcher's
  path), and UI driving via ydotool is forbidden absolutely. Document
  deliverables stay with the four plugin visual-judge seats.
- **release-auditor truth patch** (v1.4.0): the pre-release commit
  cross-check now runs both ways. Step 4 caught commits the entry fails
  to mention; it now also catches any claim in the entry that no commit
  since the previous tag backs (an invented or aspirational entry is a
  finding), the notes-versus-diff truth audit prior art found shipped
  nowhere, folded in as a method extension rather than a seat
  (modes-before-agents). The patch grew one more leg during this very
  release's gate: the auditor's Bash allowlist never had gh, so it
  could not verify CI itself and reported it dispatcher-asserted; the
  allowlist now carries `gh run list`/`gh run view` as read-only CI
  queries, and a new pre-release step makes green CI its own check
  (red, pending, or absent is `not ready`; unverifiable is reported,
  never assumed).

validate.py grows the roster to thirty-five and pins the wave's
dangerous lines: issue-census's false-positive aversion, closed
vocabulary, and never-post fences; fleet-sync-auditor's propose-only
and vault no-versions fences; upstream-triage's named-clone fetch fence
and fast-forward rule; release-executor's clean-tree,
three-mutations-allowlist, verbatim-tag, and force-push/re-tag fences;
pixel-judge's multimodal-description, UI-driving, and code-edit
requirements; and release-auditor's claims-without-commits truth check.

## v1.3.4 (2026-11-18)

One shared charter line across all thirty agents, from the standing
debug-report duty (issue #7): zsh shell discipline. Two independent
dispatches on 2026-11-17 lost the tails of compound Bash commands to
zsh's `=word` expansion: an unquoted `echo ===` separator makes zsh
resolve `==` as a command name against PATH, the expansion fails with
`== not found`, and everything after it in the compound command never
runs. Every charter now carries the rule in its constraints: never
write an unquoted token beginning with an equals sign; quote separator
text (`echo '---'`) or use `printf`. charter-architect's drafting
requirements name the line so future charters inherit it, and
validate.py pins the rule on every charter (pin written first: thirty
failures against the old charters, thirty passes after), so a future
charter edit cannot silently drop it.

## v1.3.3 (2026-11-17)

Two latro charter patches from the standing debug-report duty, batched
under the charter-patch policy. The write fence (#5): "Bash never
writes the report" now states the exhaustive rule, any Bash mutation of
the report file in place or redirected, with the in-place editors named
(`sd`, `sed -i`, `perl -i`, `awk` redirects, `sponge`, heredocs,
`mv`/`cp` onto the file) so the old verb enumeration cannot read as the
complete list; and a self-caught draft defect now has a sanctioned fix
path, one corrective Write pass of the full file before the first
return, never Edit, never Bash, because Method step 6 said "fix what
you find" while the fence left no legal tool to fix with, which is the
gap an `sd` call slipped through. The degraded line (#6): an absent web
tool is now named in the marker (`DEGRADED: WebSearch absent`,
`DEGRADED: WebFetch absent`, or both gone), the toolset is documented
as fixed at dispatch so the agent plans around the absence instead of
re-probing, and the absence is carried into the Debug Report, making
future partial-drop observations precise enough to answer the open
platform question of whether background launches shed WebSearch.
validate.py pins all three lines (pins written first: all three failed
against the old charter, all pass after), and the AGENTS.md Validation
and Non-negotiables sentences and the README Development check
inventory name them.

## v1.3.2 (2026-11-16)

Two charter patches from dispatch Debug Reports, batched under the
charter-patch policy. ci-triage (issue #3): an empty `--log-failed` with
exit 0 on a failed run is not "log unavailable"; the method now checks
the jobs API first, where zero steps, no runner, and a BlobNotFound log
endpoint are the signature of a run that never executed (a queue
teardown), and the teardown, not code, is the root cause.
release-auditor (issue #4): the tag-versus-entry cross-check now
set-compares with one identical sort on both sides, an awk set-diff or
`comm` only over inputs pre-sorted identically, because `comm` over
version-sorted lists compares lexicographically, silently disagrees,
and buries its warning; its contradictory output is a tool artifact,
not a finding. validate.py pins both lines so a future charter edit
cannot silently drop them.

## v1.3.1 (2026-11-13)

workspace-sentinel charter patch from a dispatch Debug Report (issue
#2): a latest-tag pick that disagrees with the top patchnotes entry is
re-verified against the entry's version line before reporting, because
a retagged catch-up tag carries a newer tag-object date than a later
release and can win the creatordate sort; and tag findings are
reconciled at sweep end so a tag minted mid-sweep is never reported
missing.

## v1.3.0 (2026-11-11)

Every agent now closes every dispatch with a structured debug report,
and the dispatcher files actionable findings as GitHub issues in this
repo. Brandon's request: a two-week capture window (2026-11-11 to
2026-11-25) whose triage decides charter, validator, and tooling
improvements per agent and per model.

- The duty is always-on and baked into all thirty charters as a
  `## Debug reporting` section: the final message ends with a
  `## Debug Report` block, one bullet per friction point actually hit,
  never speculation, in six categories (tool, environment, model,
  charter, dispatch, idea), or exactly `- none` on a clean run. The
  block is meta: it never replaces mission findings and never enters a
  deliverable file.
- The separation is explicit: agents report, the dispatcher files. No
  agent creates, comments on, or labels a GitHub issue in any form, so
  imprint's forbidden-mutations fence and the declined issues-triage
  ledger entry stand unchanged.
- The dispatcher's filing contract lives in this repo's AGENTS.md: one
  issue per actionable finding, deduped against open `debug`-labeled
  issues, titled `[<agent>] <summary>`, the body carrying the dispatch
  date, the category, the evidence, and the model pin the agent ran
  under, so the triage can group improvements per agent and per model.
  A one-line pointer joined the global dispatch rules so dispatches
  made from other workspaces still file.
- validate.py enforces the section on every charter (thirty new
  checks); the roster stays thirty and no tool set changed.

## v1.2.0 (2026-11-11)

Thirtieth agent: **schedule-analyst**, the school-and-schedule lane,
promoted from the watch list by the suite-completion gap survey. The
survey's baseline named weekly school work (td as the task system,
gcalcli the calendar, the Sunday D2L sweep) as the one recurring domain
with no seat; the same survey found the write axis saturated, and its
other verdicts are recorded in the roadmap ledger and watch list.

- td 5.10.0 is the verified backbone (every rung probed live
  2026-11-11): today/upcoming/inbox, stats (live but absent from the
  top-level help listing), task list's filter surface with the
  results/nextCursor JSON pagination, the project/section/label
  structure rungs, and completed list. Two quirks carried in the
  charter: the JSON priority field is the API scale, inverted against
  the UI (4 is p1), and today and upcoming open with the same overdue
  block.
- gcalcli 4.5.1 is chartered in its verified state: `list` answers from
  local cache, but event queries currently fail with
  `RefreshError: invalid_grant` (the stored OAuth session cannot
  refresh; verified live). Until Brandon re-auths, the digest runs
  td-only and carries a calendar-unavailable line with the re-auth
  direction, the ledger-analyst precedent (chartered ready, the dormant
  dependency stated plainly). Re-authentication is never the agent's
  act.
- Read-only by charter: td's and gcalcli's read verbs only,
  recommendations never executed, recurrences kept visible in any
  suggestion because they are load-bearing. The modes-before-agents
  call is recorded: not data-analyst's named-endpoint lane (local
  datasets, not CLI state reads) and not syshealth-auditor's (machine
  state shares no corpus or allowlist with task and calendar APIs).
- Model pin: GLM-5.3-Flash, the rubric-driven evidence-gathering tier
  (syshealth-auditor precedent); the dispatcher can raise it if
  digests run thin.
- Packaging: roster check extends to thirty; README, AGENTS.md (whose
  agent list carried a stale twenty-eight count over twenty-nine
  names; fixed here), both manifests, and the roadmap synced. The
  roadmap records the survey's verdicts: catalog reconciler declined
  (no git baseline under the write target for the fence model's
  re-verify leg, verified live), dependency apply mode and kindle-sync
  deferred with entry conditions, emulation and ML seats declined as
  job-title candidates, and ctf-recon and log-miner keep their unfired
  conditions.

## v1.1.0 (2026-11-11)

Twenty-ninth agent: **imprint**, the GitHub-metadata seat (Brandon's
request). It tends a repository's public identity, the description and
GitHub Topics, through the gh CLI: a new validator class for Bash-verb
metadata mutators whose tools stay [Read, Bash] (no Write, no Edit).

- "GitHub tags" in the request's phrasing is read and stated in the
  charter as GitHub Topics, the repository's discovery labels, never git
  tags; tags, releases, and the release flow are forbidden surfaces.
- The write lane is exactly two mutations, `gh repo edit --description`
  and `--add-topic`/`--remove-topic` (plus `--homepage` only when a
  dispatch names it; a topics PUT only for wholesale replacement, which
  `gh repo edit` cannot express). Forbidden absolutely: visibility,
  archive, rename, default branch, collaborators, branch protection,
  repository creation or deletion, feature toggles, gists, issues and
  PRs, discussions, webhooks, secrets, actions runs; and never commit,
  stage, push, or tag (release-auditor and workspace-sentinel own tag
  and release health; doc fixes route to doc-drift-auditor).
- These are the roster's first writes that are external: they publish to
  github.com instantly with no local diff to review. The fence answer
  transposes the v0.9.0 default: propose mode is the charter's default,
  apply dispatches name their repos explicitly (a fleet apply must
  enumerate; "all repos" is a REFUSED), every mutation is followed by a
  read-back, and the itemized before/after report is the only audit
  trail, its before-state doubling as the rollback record. Fleet propose
  sweeps are chartered from the start; the fences are per-repo
  identical, and deferring would only re-charter the same lines later.
- Grounding is mandated before a word is proposed: README, spec,
  patchnotes, roadmap, git log and tag census. A description that
  outpaces the repo is metadata drift, the named failure class.
- Probed live before chartering (gh 2.97.0): the read side exercised
  (`gh repo view --json` fields, the topics endpoint, cwd repo
  resolution); the write side verified from the tool's help and
  GitHub's own docs, never exercised during design. Topic rules verified
  from the docs: lowercase letters, numbers, hyphens; 50 characters or
  fewer; at most 20 topics; names saved as lowercase; always public even
  from private repos; 422 means stop, not retry. The description field's
  platform cap is not published anywhere reachable read-only; the
  charter sets house discipline at one line, 200 characters or fewer.
- The docs-prose-writer decline stands: this seat writes two bounded
  metadata fields grounded in the repo's own documents, not commissioned
  prose. Where the judgment is wanted harder, an apply dispatch can
  carry Brandon's approved text and the charter writes it verbatim or
  refuses.
- Model pin per the anything-that-writes rule: GLM-5.3.
- Packaging: validate.py learns the GH_META_AGENTS class (metadata-lane,
  two-mutations, never-commit, forbidden-mutations fences) and moves the
  roster check to twenty-nine; README, AGENTS.md, both manifests, and
  the roadmap synced.

## v1.0.0 (2026-11-11)

The first drop of purpose-built write agents (Brandon's request; the
web-researcher watch-list condition fired): two new write seats under
purpose-built fences, roster twenty-eight. Two further candidates from the
same brief were scored and declined; reasons recorded in the roadmap ledger.

- **latro**, the research-report writer: deep multi-source web research on a
  dispatch-named topic (project technologies, book acquisition, papers,
  languages, web design), written as a cited markdown report at a
  dispatch-named path. Tools [Read, Write, Bash, WebSearch, WebFetch]: the
  harness's web tools are named in frontmatter (the app bundle's agent loader
  consumes frontmatter tools as the subagent allowlist; the runtime grant is
  proven by the activation canary), with a keyless curl ladder as the
  structured rungs (arXiv, Crossref, OpenLibrary, all verified live) and a
  DEGRADED fallback if the web tools are absent. The fence is structural: no
  Edit tool, exactly one Write per dispatch, and it must be a new file
  (occupied path is a REFUSED), so existing prose and the Obsidian vault are
  unreachable by construction; never a commit; never an authentication.
  Evidence discipline follows stock-broker (dated sources, dead-end log,
  unknowns stated as unknowns) and the output contract is written to pass the
  slop-reader gate, which gains compensation-pattern awareness in this same
  release.
- **assay**, the grader, two modes. Repo mode grades a repo on the five named
  metrics (code quality, code cleanliness, repo cleanliness, documentation,
  overall project cohesion) with anchored X/10 scores and derived goals; on an
  append dispatch it appends the dated goals block to roadmap.md through the
  safest append the shell offers (quoted heredoc via cat >>, O_APPEND), after a
  clean-tree check and a whole-file read, re-verified by `git diff --numstat`
  (additions only, zero deletions) plus a byte-identity hash of the original
  lines: the file only grows. Idea mode is read-only: an idea graded on the
  four criteria (prior art via web search, concept completeness, complexity
  done right, maintenance load) to a worth-it / not-worth-it /
  worth-it-with-changes verdict. The overwrite-destroys-roadmaps incident
  class is the fence this lane exists to make impossible.
- validate.py learns the two web-carrying classes with their own fence
  predicates (latro: new-file, never-commit, never-authenticate; assay:
  read-only-lane, append-only, clean-tree, never-commit,
  never-authenticate); every agent keeps the no-subagent line; the roster
  check moves to twenty-eight.
- Model pins per the anything-that-writes rule: both new seats on GLM-5.3.
- Declined from the same brief, reasons in the roadmap ledger: a docs-prose
  writer (judgment-shaped authorship outside the v0.9.0 fence line; release
  prose keeps its single owner) and a cascade-applier (production code with
  behavior risk; the builders bulk exclusion stands).

## v0.9.0 (2026-11-11)

The second founding-rule amendment (Brandon's write-forward pass): five
audit-and-fix seats gain chartered write lanes under the fence model.
The line the amendment draws is the phase-3 evidence's own: a write seat
is chartered where the fix is fully determined by what the audit found
and re-running the same audit verifies it. Roster unchanged at
twenty-six; twenty agents stay read-only.

- The fence model, enforced by validate.py: report-only by default (a
  write dispatch names the mode and the scope), a clean-tree
  precondition (REFUSED: dirty tree), writes confined to the charter's
  named scope, never a commit or any git state change, re-verification
  after applying, and an itemized before/after report for main-thread
  review. The five carry tools: [Read, Edit, Write, Bash]; every other
  agent keeps [Read, Bash].
- charter-architect gains an apply mode: it lands its own approved
  release kit in the plugin repo and runs validate.py; commit, push,
  tag, and release stay with the main thread.
- ci-posture-auditor applies the hardened CI shape to a named repo,
  tightening only: it never removes or weakens a pin, permission,
  timeout, or gate.
- doc-drift-auditor fixes the mechanical drift it found (version
  carriers, roadmap ticks, patchnotes hygiene, proved README facts);
  judgment findings stay findings, and release-notes prose is never
  its pen.
- debt-census removes only census items the dispatch names; no
  refactors, no reformatting drive-bys; build-class verification only
  on dispatch consent.
- test-gap-analyst flips from static-only to write-and-run on a write
  dispatch: it writes the named missing tests in the repo's own
  conventions, runs exactly what it wrote (never the full suite), and
  never edits production code; a failing test that exposes a product
  bug is a finding, not a patch.
- Model pins move with the writes per the anything-that-writes rule:
  ci-posture-auditor, debt-census, and test-gap-analyst flip
  GLM-5.3-Flash to GLM-5.3.
- The six judges and gates (claim-verifier, shadow, code-reviewer,
  spec-compliance-reviewer, security-auditor, slop-reader) stay
  read-only: a verifier that can edit is not a verifier. librarian and
  music-archivist stay fenced, and the phase-3 decline stands.

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
