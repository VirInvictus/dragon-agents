# evals/

The standing eval convention (v1.6.0): one directory per seat, holding
a realistic dispatch prompt and the output-shape assertions a grader
checks the dispatch's final message against.

- `evals/<seat>/prompt.md`: the dispatch prompt, exactly as a
  dispatcher would send it, self-contained (paths, scope, standing,
  the no-subagents line).
- `evals/<seat>/graders.md`: what the output must contain for the
  dispatch to pass, derived from that charter's Output section: fixed
  table columns, verdict vocabularies, refusal lines, and the fences
  the charter forbids crossing (a grader that watches for the fence
  being crossed is part of the eval).

Seeding is incremental: an absent evals/ directory or a seat without
an entry passes validation. `python3 scripts/validate.py` parse-checks
whatever exists (every seeded seat needs its prompt.md). Grading
itself is a dispatch-time act: run the prompt against the seat, then
check the final message against graders.md — before charter-changing
releases for the seats whose charters moved, and as the canary when a
seat lands.

The prompts here double as the activation canary ladder: a fresh
conversation, one dispatch per seat, the grader checklist as the
acceptance bar.
