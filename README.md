# dragon-agents

[![License: MIT](https://img.shields.io/github/license/VirInvictus/dragon-agents)](LICENSE)
[![Release](https://img.shields.io/github/v/tag/VirInvictus/dragon-agents)](https://github.com/VirInvictus/dragon-agents/releases)
[![ci](https://github.com/VirInvictus/dragon-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/VirInvictus/dragon-agents/actions/workflows/ci.yml)

A local ZCode plugin of research subagents: **thirty-eight agents** (twenty-seven read-only, ten chartered write seats, one multimodal judge) and **eight skills**, installed through a directory marketplace. Read-only agents gather and report; the main thread decides and edits. Write seats exist only under chartered fences: propose-first, enumerated apply, read-back verification, never a commit. No agent spawns subagents. Every dispatch ends with a debug report of the friction it hit, filed by the dispatcher as issues so the roster keeps a dated improvement record.

**Fleet at a glance**

| | |
|---|---|
| Read-only seats | 27 |
| Chartered write seats | 10 |
| Multimodal judge | 1 (pixel-judge) |
| Skills | 8 (7 vendored official Obsidian skills + herald) |
| Design doc | [docs/guide/](docs/guide/README.md): model routing, platform settings, fleet operations |

## The fleet

### Repos, code, and releases

| Agent | Job |
|---|---|
| `repo-cartographer` | Repo onboarding map before planning: layout, stack, conventions, tests, risks. |
| `code-reviewer` | Bug-hunting diff review: `[bug]`/`[risk]`/`[nit]` findings with fix sketches; runs the repo's linter as hints. |
| `spec-compliance-reviewer` | Diff versus `spec.md` contract; violations with evidence. |
| `doc-drift-auditor` ✍ | Docs versus code reality; apply mode fixes mechanical drift. |
| `release-auditor` | Pre-tag readiness gate and post-tag sweep; runs both ways on patchnotes claims. |
| `release-executor` ✍ | Cuts a ready release: verbatim tag, GitHub Release, every step read back. Propose-first. |
| `ci-triage` | Failed CI run to root cause; jobs-API teardown check for never-ran runs. |
| `ci-posture-auditor` ✍ | Workflows versus the hardened CI shape; apply mode tightens only. |
| `git-archaeologist` | Regression windows and provenance from history; bisect plans, never executed. |
| `test-gap-analyst` ✍ | Coverage map; write mode adds the named missing tests, production code untouched. |
| `dependency-auditor` | Declared versus imported, floors versus used APIs, toolchain drift. |
| `debt-census` ✍ | TODO/FIXME census dated by blame; apply mode removes named items. |
| `duplication-scout` | Cross-repo duplicate detection feeding the library-graduation rule. |
| `cascade-checker` | Downstream call-site inventory for a changed shared-library API. |
| `workspace-sentinel` | One sweep, every owned repo: dirty trees, unpushed commits and tags, untagged releases, stale catalog rows. |

### Issues, marketing, and the web

| Agent | Job |
|---|---|
| `issue-census` | Open-issue census: aging, duplicates, fix-already-landed, label verdicts, release batch. Never comments or closes. |
| `repo-marketer` | Launch desk: where a repo should be posted, channel-native drafts, where-not-to-post, paid-ad verdict. Never posts; you do. |
| `fleet-sync-auditor` | Four-tier propagation audit after a release or rename (repo docs, catalog, public surfaces, vault); propose-only. |
| `upstream-triage` | Reference-clone upstream windows into port/skip verdicts and a port worklist. |
| `latro` ✍ | Deep web research as one new cited report per dispatch; keyless sources only. |
| `stock-broker` | Markets briefs from keyless public data: equities, ETFs, rates, FX. |
| `charter-architect` ✍ | Designs new agents: scorecard, live-probed charter, full release kit; apply mode lands it. |

### Collections and life

| Agent | Job |
|---|---|
| `librarian` | Calibre library research through read-only tooling; never writes the database. |
| `music-archivist` | Music-collection audits through lattice's read-only surface. |
| `vault-archivist` | Obsidian vault hygiene audit; connections proposed, never applied; prose never rewritten. |
| `subscription-watchdog` | Renewal audit over exported statement CSVs; dormant until statements exist. |
| `ledger-analyst` | hledger finance briefs; dormant until a journal exists; encrypted files fenced. |
| `schedule-analyst` | Weekly planning digest from Todoist and calendar; recommendations only. |
| `data-analyst` | Read-only duckdb profiling of named datasets. |

### Machine, security, and the pipeline

| Agent | Job |
|---|---|
| `syshealth-auditor` | Backup freshness, failed units, disk space from state reads; root-gated checks reported as directions. |
| `security-auditor` | Defensive review of owned repos: gitleaks redacted, risky patterns, advisory checks. |
| `claw` ✍ | Calibre import phases 1 and 2 through the pipeline's own structural gates; the seal stays with the main thread. |
| `shadow` | Read-only phase gate over an import: verdicts versus manifest before sign or commit. |

### Judges and gates

| Agent | Job |
|---|---|
| `claim-verifier` | Independent re-verification of a findings list: confirmed, refuted, or unverifiable per claim. |
| `slop-reader` | AI-prose pass on commissioned text; flags quotes, never rewrites. |
| `pixel-judge` | Multimodal acceptance pass on app, game, and desktop captures; JSON verdicts against a stated bar. |
| `assay` ✍ | Five-metric repo report card; goals append to roadmap.md with zero deletions. Idea mode is read-only. |
| `imprint` ✍ | GitHub metadata tender: description and topics via two gh verbs, read back; never tags, releases, or issues. |

✍ = chartered write seat (10 total; every write fenced, read back, and reported; never a commit).

## Skills

Eight skills ship beside the agents and surface as `dragon-agents:<skill>`:

| Skill | Job |
|---|---|
| `herald` | Reddit presence drafts in the operator's voice: posts, replies, hostile-reply buffers. Drafts only; you post. |
| `obsidian-cli` | Drive a running Obsidian app from the shell; includes the community gotcha audit. |
| `obsidian-markdown` | Obsidian-flavored Markdown: wikilinks, embeds, callouts, properties. |
| `obsidian-bases` | Bases database views: filters, formulas, table and kanban views. |
| `json-canvas` | Canvas files: nodes, edges, groups, layout validation. |
| `obsidian-headless` | Obsidian Sync and Publish from a terminal (subscription required). |
| `defuddle` | Clean Markdown extraction from web pages. |
| `knap` | Markdown rendering from templates plus JSON/CSV data. |

The seven Obsidian skills are vendored verbatim from the official
[obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills)
repository (MIT); provenance, commit pins, and the vet record live in
[skills/ATTRIBUTION.md](skills/ATTRIBUTION.md).

## The design guide

[docs/guide/](docs/guide/README.md) carries the fleet's optimization
arsenal: model routing (which seat gets which model and why), GLM
platform settings, subagent charter design, fleet operations, and the
sourced research behind them (73 citations across two research passes,
plus the marketing and comparative-design passes for v1.6.0).

## Install

In ZCode: Settings → Plugin Management → Discover tab → `+` → add this
repository as a local marketplace → install **dragon-agents**.
Marketplace plugins install disabled until first enabled; after
enabling, trust the `enabledPlugins` key in `config.json` and a canary
dispatch over the UI toggle. The agent roster and skill set bake at app
boot: a roster change lands in conversations opened after the next
app restart.

## Model guidance

Any text model works; the roster was written for text-only subagents
(one seat, `pixel-judge`, is the exception and needs an image-capable
pin). The routing principle: fast-tier models for rubric-driven
sweeps, the strong tier for judgment that gates work and for anything
that writes. The full rationale lives in
[docs/guide/model-routing.md](docs/guide/model-routing.md); per-agent
picks live in Settings → Subagents.

## Development

`python3 scripts/validate.py` is the whole test suite and CI gate: it
checks both manifests, every charter's frontmatter and tool class, and
the pinned fence lines each charter must carry (read-only lines,
never-commit fences, the shell and language discipline rules, per-seat
method pins such as the census's never-post fence), the exact roster
of thirty-eight, the eight-skill set, and the evals convention. Run it
before committing; CI runs the same script on every push.

`evals/<seat>/` holds per-seat dispatch prompts and output-shape
graders; the convention is documented and seeded incrementally (the
directory does not exist yet; its absence passes validation).

`AGENTS.md` documents the plugin's rules, the marketplace mechanics,
and the runtime gotchas; read it before changing how the plugin is
packaged. The optimization guide under `docs/guide/` explains the
design decisions.

## License

MIT. See [LICENSE](LICENSE).
