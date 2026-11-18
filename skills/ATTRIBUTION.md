# Attribution and provenance for skills/

Everything in this directory is vendored, not authored. This plugin
does not modify upstream skill bodies except where noted below.

## obsidianmd/obsidian-skills

- Source: https://github.com/obsidianmd/obsidian-skills (official
  Obsidian repository)
- Commit vendored: 1c3f6df5683588e39b12462a75d1d0fcf550f955
- Vendored on: 2026-11-18
- License: MIT (upstream LICENSE carried verbatim as
  `LICENSE.upstream` at this level)
- What was taken: the seven skill folders under
  `plugins/obsidian/skills/` (obsidian-bases, obsidian-cli,
  obsidian-headless, obsidian-markdown, json-canvas, defuddle, knap),
  each with its references/, byte-for-byte.
- The one local modification in this vendored copy: a single
  see-also line appended to the References section of
  `obsidian-cli/SKILL.md`, pointing at `references/CLI_AGENT_NOTES.md`
  (below). No upstream body text was changed or removed.

## jackal092927/obsidian-official-cli-skills

- Source: https://github.com/jackal092927/obsidian-official-cli-skills
- Commit vendored: ab6533943454abd5fe554b5a1550c0244d569d98
- Vendored on: 2026-11-18
- License: MIT (carried verbatim as
  `obsidian-cli/references/LICENSE.jackal`)
- What was taken: that repository's SKILL.md, stored unmodified as
  `obsidian-cli/references/CLI_AGENT_NOTES.md`. It is an independent
  57-scenario audit of Obsidian CLI 1.12 that found 13 silent failures
  (exit 0 with wrong or empty output) and 24 poor defaults, validated
  by a second user against an 18,876-file vault. Its content overlaps
  the official obsidian-cli skill's trigger surface, which is why it
  ships as a reference file rather than a second skill.

## Vet record (2026-11-18)

Every file was read end to end against the house vet checklist:
permissive licenses present; zero load-time execution syntax (every
`!` hit is Obsidian embed markup, `![[Note]]`); zero bundled scripts
inside skills/; no network calls, credential paths, or base64 blobs;
frontmatter is spec-minimal (`name` + `description`, no
`allowed-tools` self-grants); no trigger collisions with this plugin's
agent descriptions (skills are task-named, agents role-named). One
size note: `obsidian-bases/SKILL.md` runs 601 lines against the
spec's 500-line recommendation; its deep material is already split
into references/. The Obsidian CLI's exit-0-on-failure behavior was
verified live on this machine during vetting.

## Refresh policy

Re-vet on any upstream update: diff against the recorded commit,
re-run the checklist, and re-read anything that changed. Upstream is
pinned by commit here; updates do not flow automatically.
