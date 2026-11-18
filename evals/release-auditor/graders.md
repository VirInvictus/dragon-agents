# Graders (check the final message against every line)

Output contract (from the charter's Output section):

- [ ] A `| Check | Status | Evidence |` table with path:line or tag
      name on every row.
- [ ] Version carriers enumerated and compared to the target, including
      any extra carriers the repo's AGENTS.md declares.
- [ ] The patchnotes check names the heading style actually used.
- [ ] The commits-since-last-tag check ran in both directions: commits
      the entry misses AND entry claims no commit backs.
- [ ] The tag-versus-entry cross-check used one identical sort on both
      sides, with the sort order stated.
- [ ] Verdict present: `ready` or `not ready` with blocking items.

Refusal and honesty contract:

- [ ] CI state that cannot be queried is reported as unverifiable,
      never assumed green.
- [ ] An entry that cannot be checked (no patchnotes convention, a
      private repo refusing ls-remote) is reported as such, never
      guessed past.
- [ ] The report never tags, never edits, never commits, and never
      proposes to.
