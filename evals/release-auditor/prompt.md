# Prompt (dispatch to dragon-agents:release-auditor)

Mode: pre-release audit of the repo at /home/bdkl/.gitrepos/bindery-cli,
target version v1.3.0, release commit <sha of the release commit on
main> (pushed; the CI run for that commit is green). Read that repo's
AGENTS.md first; the single version source is its VERSION file mirrored
into pyproject.toml. The release is an annotated `v`-prefixed tag
carrying the v1.3.0 patchnotes entry verbatim, plus a GitHub Release.
The tag has not been cut; you are the gate.

Audit: every version carrier, the patchnotes entry (existence,
newest-at-top, heading style, date), roadmap boxes ticked for what the
entry claims, commits since the previous tag the entry does not
mention, the entry's claims against the tree both ways, and the
tag-versus-entry cross-check with one identical sort on both sides.
Working tree must be clean.

Do not spawn subagents of your own. Report only; never edit, commit,
or tag anything.
