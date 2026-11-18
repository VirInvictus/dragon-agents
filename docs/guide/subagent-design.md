# Subagent design: charters, fences, and validation-as-CI

How the seats themselves are built. The environment consensus first,
because it justifies everything else: every major harness ships
read-only delegation as the safe default (built-in explorer seats deny
Write and Edit; reviewer examples deny edit and shell outright; one
harness documents read-only sandbox mode as the planning surface), and
the ecosystem observation on record is that most multi-agent setups are
limited to read-only subagents. A read-mostly fleet with a few
chartered write lanes is the mainstream shape.

## The fence model for write seats

The non-negotiable: **writes are chartered, never casual.** A write
seat exists only with all of the following, stated in its charter and
enforced structurally where the harness allows:

- **Report-only by default.** The seat's ordinary dispatch returns
  findings; a write dispatch must be explicitly ordered.
- **An enumerated scope.** The charter names the exact files, verbs, or
  fields it may touch; anything else refuses.
- **A precondition gate.** Clean tree, ready verdict, dispatch-enumerated
  target triple: the write refuses without its precondition, with
  evidence.
- **Read-back.** Every mutation is verified against the world after it
  lands, and the before-state is recorded as the rollback trail.
- **Never a commit.** Version control stays with the operator; the seat
  leaves a reviewable diff.
- **Validation after applying.** The seat re-runs the structural
  checker and reports pass/fail in its report.

The hard-won generalization behind all of it: **make the write path
structural, not rhetorical.** Harness guidance states it directly:
split instructions into deterministic layers the harness always applies
(permissions, deny rules, hooks, validators) and non-deterministic
layers the model weighs (rule files, charters). If a rule keeps getting
emphasized and keeps getting missed, it belongs in the deterministic
layer. A tool-restricted reviewer is a reviewer that cannot edit: the
harness enforces it, so the prompt does not have to beg. The canonical failure is on the public
record: an agent deleted a production database during an explicit code
freeze under prompt-level prohibition alone, then fabricated records
claiming it was fixed; only checkpoints and structural limits repaired
the situation.

## Validation-as-CI for prompt artifacts

Roster files are config, and config gets a schema check in CI. One
stdlib script, run on every push, checking: manifests parse; every
charter's frontmatter matches its filename; tool allowlists match the
seat's class; the class's fence lines are present as literal substrings
(so a future edit cannot silently drop a fence); and the roster is
exactly the expected set. This has public precedent in every
schema-checked agent-config surface, and it closes a documented trap:
harnesses silently ignore unrecognized frontmatter fields, with no
error and no signal. Silent acceptance means the validator, not the
platform, is the defense.

Two pins worth copying: the per-class fence-literal checks (each
dangerous charter line has a validator check that fails if the line is
removed), and the exact-roster check (a seat cannot be half-removed).

## Description precision: the routing contract

The seat description is the routing trigger the orchestrator reads to
pick a seat, and it is a standing tax: descriptions load into main
context, and a harness warns once the combined descriptions pass
fifteen thousand tokens. Two consequences:

- **Detail lives in the charter body** (which loads only when the seat
  runs); the description carries only what-and-when plus its tool
  class.
- **Trigger precision beats coverage.** Every seat answers one dispatch
  question, and overlapping triggers are a defect: the recorded
  practitioner failure is an orchestrator picking the wrong agent or
  none because fuzzy descriptions collided. The design gate used here
  is a collision check against every existing description before a new
  seat is chartered; a new seat whose trigger cannot be told apart from
  an existing one at dispatch time is a merge or a decline.

Related, from instruction-budget research: frontier thinking models
reliably follow roughly 150-200 instructions, and a harness system
prompt already spends about fifty of them. Rule files under two hundred
lines, split into topical files loaded on demand, with specific
verifiable rules ("run the test suite after changing this directory")
over abstractions. One empirical result beats intuition here: an
always-loaded compressed documentation index scored 100% on API-usage
evals while lazy-loaded skills maxed at 79% even when the agent was
explicitly told to consult them.

## Seat anatomy rules the roster enforces

- **Minimum tools.** A read seat gets exactly the tools it needs
  (typically read and shell with a command allowlist in the charter
  text). Every extra tool is a misfire surface and a fence gap.
- **Output contract.** The charter defines the output shape (tables,
  verdicts, refusal lines) and how obstacles are reported, so a seat
  never fails silently or invents past a gap.
- **No nesting.** Subagents never spawn subagents; the fleet stays one
  orchestrator deep (depth caps of three are the ecosystem default;
  this roster is stricter by charter).
- **A meta-report duty.** Every dispatch ends with a structured report
  of the friction it actually hit (tool, environment, model, charter,
  dispatch, idea), filed by the dispatcher as issues. This is the
  feedback loop that turns operator annoyances into charter patches
  with dates and evidence.
- **Modes before agents.** A candidate expressible as a mode of an
  existing seat prefers the mode unless trigger precision genuinely
  suffers; the roster's declined ledger exists so skipped ideas stay
  decided instead of re-proposed.

## The multi-agent applicability test

Before adding any seat, the question from the source literature:
does the task actually parallelize, and is the value high enough to pay
the token multiplier (on record: agents use roughly 4x chat tokens,
multi-agent roughly 15x)? Domains needing shared context between steps
are a poor fit, and most coding work parallelizes less than research
does. The seats that earn their cost are the ones whose job is
isolating verbose output from the main thread or condensing a large
search into a small report: subagents are compression engines that
return their most important tokens.
