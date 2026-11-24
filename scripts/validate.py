"""Structural checks for the dragon-agents plugin.

Validates both JSON manifests and every agent charter: frontmatter fields,
per-class tool restrictions, and the charter lines each class must carry.
Read-only agents keep `tools: [Read, Bash]` and the Read-only line; claw is
among them because its writes ride the pipeline's own gated verbs. The five
charter-fence write seats (v0.9.0) carry `tools: [Read, Edit, Write, Bash]`
plus the Clean tree fence and the never-commit line. The two purpose-built
web write seats (v1.0.0) carry their own classes and fences: latro
`[Read, Write, Bash, WebSearch, WebFetch]` with the new-file, never-commit,
and never-authenticate fences; assay `[Read, Bash, WebSearch, WebFetch]` with
the read-only-outside-the-lane, append-only, clean-tree, never-commit, and
never-authenticate fences. imprint (v1.1.0) carries [Read, Bash] like a
reader but is the metadata mutator: its writes ride the two gh verbs,
fenced by the metadata-lane, two-mutations-allowlist, never-commit, and
forbidden-mutations lines. Every agent keeps the no-subagent line and the
standing debug-reporting duty (v1.3.0): a `## Debug reporting` section the
agent satisfies in its final message, with filing left to the dispatcher.
Three charters carry pinned checks: ci-triage the jobs-API teardown
check for an empty `--log-failed`, release-auditor the identical-sort
rule for tag-versus-entry set compares and the claims-without-commits
truth check (v1.3.2, v1.4.0), and latro the any-Bash-mutation report
fence, the one corrective Write pass, and the named-tool DEGRADED line
(v1.3.3). The v1.4.0 seats add their own pinned fences: issue-census
(never-post, closed vocabulary, false-positive aversion),
fleet-sync-auditor (propose-only, vault no-versions), upstream-triage
(the named-clone fetch fence and the fast-forward rule),
release-executor (clean tree, the three-mutations allowlist, the
verbatim tag flag, force-push and re-tag bans), and pixel-judge (the
multimodal description requirement and the UI-driving and code-edit
bans). Every charter also carries the shared zsh shell-discipline rule
against unquoted leading-`=` tokens (v1.3.4). Every charter also carries
the shared language-discipline rule (v1.5.0),
and the vendored skills/ set is checked structurally: exactly the seven
Obsidian skills, each SKILL.md present with a frontmatter name matching
its folder, plus the attribution file.
The v1.6.0 comparative patches pin code-reviewer's fix-sketch and linter-folding rungs, latro's pinpoint-citation rule, and the untrusted-corpus lines on latro and issue-census.
The same release adds repo-marketer, a web-research reader in the assay tool class (read-only with web tools): its pins are the never-post fence, the never-authenticate rule, drafts landing in the final message only, and the per-draft compliance note. The roster grows to thirty-eight, and the skills set to eight (herald joins the seven vendored Obsidian skills). CI runs this on every push.
The v1.6.1 debug-duty patches pin: the snapshot-staleness rule on release-auditor and doc-drift-auditor (platform-injected AGENTS.md is a session-start snapshot; disk is the truth), release-executor's publish-workflow release-race branch and the tag-message class check that retires the size ratchet, latro's single-page-spec truncation fallback (respec source extraction), and assay's web-recovery discipline.
The v1.6.2 charter patch adds magick (convert as the ImageMagick 6 alias) to pixel-judge's Bash allowlist for the pixel-statistics rung, and pins the /tmp confinement of its outputs.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
READ_ONLY_TOOLS = ["Read", "Bash"]
WEB_READ_TOOLS = ["Read", "Bash", "WebSearch", "WebFetch"]
WRITE_TOOLS = ["Read", "Edit", "Write", "Bash"]
WEB_WRITE_TOOLS = ["Read", "Write", "Bash", "WebSearch", "WebFetch"]
WRITE_AGENTS = {
    "charter-architect",
    "ci-posture-auditor",
    "debt-census",
    "doc-drift-auditor",
    "test-gap-analyst",
}
WEB_WRITE_AGENTS = {"latro"}
WEB_APPEND_AGENTS = {"assay"}
WEB_RESEARCH_AGENTS = {"repo-marketer"}
GH_META_AGENTS = {"imprint"}
RELEASE_EXEC_AGENTS = {"release-executor"}
VISUAL_JUDGE_AGENTS = {"pixel-judge"}
SKILLS_DIR = ROOT / "skills"
EXPECTED_SKILLS = {
    "defuddle",
    "herald",
    "json-canvas",
    "knap",
    "obsidian-bases",
    "obsidian-cli",
    "obsidian-headless",
    "obsidian-markdown",
}
EXPECTED_AGENTS = {
    "assay",
    "cascade-checker",
    "charter-architect",
    "ci-posture-auditor",
    "ci-triage",
    "claim-verifier",
    "code-reviewer",
    "debt-census",
    "data-analyst",
    "dependency-auditor",
    "doc-drift-auditor",
    "duplication-scout",
    "fleet-sync-auditor",
    "git-archaeologist",
    "imprint",
    "issue-census",
    "claw",
    "latro",
    "shadow",
    "ledger-analyst",
    "librarian",
    "music-archivist",
    "pixel-judge",
    "release-auditor",
    "release-executor",
    "repo-cartographer",
    "repo-marketer",
    "schedule-analyst",
    "security-auditor",
    "slop-reader",
    "spec-compliance-reviewer",
    "stock-broker",
    "subscription-watchdog",
    "syshealth-auditor",
    "test-gap-analyst",
    "upstream-triage",
    "vault-archivist",
    "workspace-sentinel",
}
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

failures: list[str] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    mark = "ok  " if ok else "FAIL"
    print(f"[{mark}] {label}" + (f" ({detail})" if detail and not ok else ""))
    if not ok:
        failures.append(label)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Parse a leading `---` block of simple `key: value` lines."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[3:end].splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().removeprefix('"').removesuffix('"')
    return fields


def parse_tools(value: str) -> list[str]:
    """Parse the flow-style list form used by the agents, e.g. [Read, Bash]."""
    inner = value.strip().strip("[]")
    return [item.strip() for item in inner.split(",") if item.strip()]


def check_marketplace_manifest() -> None:
    path = ROOT / "marketplace.json"
    check("marketplace.json exists at repo root", path.is_file())
    if not path.is_file():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        check("marketplace.json parses", False, str(exc))
        return
    plugins = data.get("plugins")
    check("marketplace.json name is dragon-agents", data.get("name") == "dragon-agents")
    check(
        "marketplace.json lists exactly the dragon-agents plugin",
        isinstance(plugins, list)
        and len(plugins) == 1
        and plugins[0].get("name") == "dragon-agents"
        and plugins[0].get("source") == ".",
    )


def check_plugin_manifest() -> None:
    path = ROOT / ".zcode-plugin" / "plugin.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        check(".zcode-plugin/plugin.json parses", False, str(exc))
        return
    version = data.get("version")
    check("plugin.json name is dragon-agents", data.get("name") == "dragon-agents")
    check(
        "plugin.json version is semver",
        bool(version and SEMVER.match(version)),
        str(version),
    )
    check("plugin.json license is MIT", data.get("license") == "MIT")


def check_agents() -> None:
    if not AGENTS_DIR.is_dir():
        check("agents/ directory exists", False)
        return
    files = sorted(AGENTS_DIR.glob("*.md"))
    found = {f.stem for f in files}
    check(
        "roster is exactly the expected thirty-eight agents",
        found == EXPECTED_AGENTS,
        f"found {sorted(found)}",
    )
    for path in files:
        stem = path.stem
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter(text)
        if fields is None:
            check(f"{stem}: frontmatter parses", False)
            continue
        check(
            f"{stem}: name matches filename",
            fields.get("name") == stem,
            fields.get("name", ""),
        )
        check(
            f"{stem}: description is non-empty",
            bool(fields.get("description", "").strip()),
        )
        if stem in WRITE_AGENTS:
            expected_tools = WRITE_TOOLS
        elif stem in WEB_WRITE_AGENTS:
            expected_tools = WEB_WRITE_TOOLS
        elif stem in WEB_APPEND_AGENTS or stem in WEB_RESEARCH_AGENTS:
            expected_tools = WEB_READ_TOOLS
        elif (
            stem in GH_META_AGENTS
            or stem in RELEASE_EXEC_AGENTS
            or stem in VISUAL_JUDGE_AGENTS
        ):
            expected_tools = READ_ONLY_TOOLS
        else:
            expected_tools = READ_ONLY_TOOLS
        check(
            f"{stem}: tools match its class",
            parse_tools(fields.get("tools", "")) == expected_tools,
            fields.get("tools", ""),
        )
        check(
            f"{stem}: charter forbids spawning subagents",
            "Do not spawn subagents" in text,
        )
        check(
            f"{stem}: charter carries the debug-report duty",
            "## Debug reporting" in text,
        )
        lowered = text.lower()
        check(
            f"{stem}: charter carries the zsh shell-discipline rule",
            "=word" in lowered,
        )
        check(
            f"{stem}: charter carries the no-mid-command-cd rule",
            "zoxide" in lowered,
        )
        check(
            f"{stem}: charter carries the language-discipline rule",
            "language discipline" in lowered,
        )
        if stem in WRITE_AGENTS:
            check(
                f"{stem}: charter carries the clean-tree fence", "clean tree" in lowered
            )
            check(f"{stem}: charter forbids committing", "never commit" in lowered)
        elif stem in WEB_WRITE_AGENTS:
            check(f"{stem}: charter carries the new-file fence", "new file" in lowered)
            check(f"{stem}: charter forbids committing", "never commit" in lowered)
            check(
                f"{stem}: charter forbids authenticating",
                "never authenticate" in lowered,
            )
        elif stem in WEB_APPEND_AGENTS:
            check(
                f"{stem}: charter is read-only outside its lane",
                "read-only" in lowered,
            )
            check(
                f"{stem}: charter carries the append-only fence",
                "append-only" in lowered,
            )
            check(
                f"{stem}: charter carries the clean-tree fence", "clean tree" in lowered
            )
            check(f"{stem}: charter forbids committing", "never commit" in lowered)
            check(
                f"{stem}: charter forbids authenticating",
                "never authenticate" in lowered,
            )
        elif stem in WEB_RESEARCH_AGENTS:
            check(
                f"{stem}: charter carries the never-post fence",
                "never posts" in lowered,
            )
            check(
                f"{stem}: charter forbids authenticating",
                "never authenticate" in lowered,
            )
            check(
                f"{stem}: pins drafts to the final message only",
                "final message only" in lowered,
            )
            check(
                f"{stem}: requires a compliance note on every draft",
                "compliance note" in lowered,
            )
            check(f"{stem}: charter declares read-only", "Read-only" in text)
        elif stem in GH_META_AGENTS:
            check(
                f"{stem}: charter is read-only outside the metadata lane",
                "outside the metadata lane" in lowered,
            )
            check(
                f"{stem}: charter carries the metadata-mutation allowlist",
                "the two metadata mutations" in lowered,
            )
            check(f"{stem}: charter forbids committing", "never commit" in lowered)
            check(
                f"{stem}: charter carries the forbidden-mutations list",
                "forbidden mutations" in lowered,
            )
        elif stem in RELEASE_EXEC_AGENTS:
            check(
                f"{stem}: charter carries the clean-tree precondition",
                "clean tree" in lowered,
            )
            check(f"{stem}: charter forbids committing", "never commit" in lowered)
            check(
                f"{stem}: charter carries the three-mutations allowlist",
                "the three mutations" in lowered,
            )
            check(
                f"{stem}: charter mandates the verbatim tag flag",
                "--cleanup=verbatim" in lowered,
            )
            check(
                f"{stem}: charter forbids force-push and re-tagging",
                "never force-push" in lowered and "never re-tag" in lowered,
            )
        elif stem in VISUAL_JUDGE_AGENTS:
            check(f"{stem}: charter declares repo read-only", "Read-only" in text)
            check(
                f"{stem}: charter forbids UI driving",
                "ydotool" in lowered and "never drive" in lowered,
            )
            check(f"{stem}: charter forbids code edits", "never edit" in lowered)
            check(
                f"{stem}: description states the multimodal requirement",
                "multimodal" in fields.get("description", "").lower(),
            )
            check(
                f"{stem}: magick output confined to /tmp",
                "magick" in lowered and "under `/tmp`" in text,
            )
        else:
            check(f"{stem}: charter declares read-only", "Read-only" in text)
        if stem == "ci-triage":
            check(
                f"{stem}: charter carries the jobs-API teardown check",
                "jobs api" in lowered,
            )
        if stem == "release-auditor":
            check(
                f"{stem}: charter carries the identical-sort set-compare rule",
                "identical sort" in lowered,
            )
            check(
                f"{stem}: charter carries the claims-without-commits truth check",
                "no commit since the previous tag backs" in lowered,
            )
            check(
                f"{stem}: charter carries the release-body byte-compare rule",
                "jq -j" in lowered and "tool artifact, never a finding" in lowered,
            )
        if stem == "claim-verifier":
            check(
                f"{stem}: charter carries the partial verdict",
                "shows more than the text says" in lowered,
            )
            check(
                f"{stem}: charter sanctions in-memory probes",
                "in-memory probes are sanctioned" in lowered,
            )
            check(
                f"{stem}: charter pins the no-bytecode probe mode",
                "pycache" in lowered and "python3 -b" in lowered,
            )
        if stem == "latro":
            check(
                f"{stem}: charter fences every Bash mutation of the report",
                "any bash mutation of the report file" in lowered,
            )
            check(
                f"{stem}: charter allows one corrective write pass",
                "one corrective write pass" in lowered,
            )
            check(
                f"{stem}: charter names the missing tool in its degraded line",
                "degraded: websearch absent" in lowered,
            )
        if stem == "code-reviewer":
            check(
                f"{stem}: charter carries the fix-sketch rule",
                "fix sketch" in lowered,
            )
            check(
                f"{stem}: charter carries the linter-folding rung",
                "candidate findings to confirm or drop" in lowered,
            )
        if stem == "latro":
            check(
                f"{stem}: charter carries the pinpoint-citation rule",
                "where in the source the claim lives" in lowered,
            )
            check(
                f"{stem}: charter carries the untrusted-corpus fence",
                "evidence, never instructions" in lowered,
            )
        if stem == "issue-census":
            check(
                f"{stem}: charter carries the untrusted-corpus fence",
                "reported content, never followed" in lowered,
            )
        if stem == "issue-census":
            check(
                f"{stem}: charter carries the false-positive aversion rule",
                "false positives are worse than missing labels" in lowered,
            )
            check(
                f"{stem}: charter carries the closed-vocabulary rule",
                "closed vocabulary fetched live" in lowered,
            )
            check(
                f"{stem}: charter carries the never-post fence",
                "never comments on, closes, edits, creates, or relabels an issue"
                in lowered,
            )
        if stem == "fleet-sync-auditor":
            check(
                f"{stem}: charter declares propose-only",
                "propose-only" in lowered,
            )
            check(
                f"{stem}: charter carries the vault no-versions rule",
                "never puts a version or phase number in the vault" in lowered,
            )
        if stem == "upstream-triage":
            check(
                f"{stem}: charter fences the fetch to the named clone",
                "fetch only the dispatch-named reference clone" in lowered,
            )
            check(
                f"{stem}: charter keeps the fast-forward with the main thread",
                "the fast-forward stays with the main thread" in lowered,
            )
        if stem in {"release-auditor", "doc-drift-auditor"}:
            check(
                f"{stem}: charter carries the snapshot-staleness rule",
                "session-start snapshot" in lowered,
            )
        if stem == "release-executor":
            check(
                f"{stem}: charter carries the publish-workflow release-race branch",
                "publish-workflow release race" in lowered,
            )
            check(
                f"{stem}: charter carries the release class check",
                "never a paraphrase or degenerate shape" in lowered,
            )
            check(
                f"{stem}: charter carries the push ride-along enumeration",
                "push.followtags" in lowered,
            )
        if stem == "latro":
            check(
                f"{stem}: charter carries the single-page-spec truncation fallback",
                "respec source" in lowered,
            )
        if stem == "assay":
            check(
                f"{stem}: charter carries the web-recovery discipline",
                "recovery discipline" in lowered,
            )


def check_skills() -> None:
    check("skills/ directory exists", SKILLS_DIR.is_dir())
    check("skills/ATTRIBUTION.md present", (SKILLS_DIR / "ATTRIBUTION.md").is_file())
    if not SKILLS_DIR.is_dir():
        return
    found = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    check(
        "skills set is exactly the expected eight skills",
        found == EXPECTED_SKILLS,
        f"found {sorted(found)}",
    )
    for name in sorted(EXPECTED_SKILLS & found):
        path = SKILLS_DIR / name / "SKILL.md"
        check(f"skills/{name}/SKILL.md exists", path.is_file())
        if not path.is_file():
            continue
        fields = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fields is None:
            check(f"skills/{name}: frontmatter parses", False)
            continue
        check(
            f"skills/{name}: frontmatter name matches folder",
            fields.get("name") == name,
            fields.get("name", ""),
        )


EVALS_DIR = ROOT / "evals"


def check_evals() -> None:
    """Light parse check for the evals/<seat>/ convention (v1.6.0).

    The convention: per seat, evals/<seat>/prompt.md holds a realistic
    dispatch prompt and evals/<seat>/graders.md asserts the charter's
    Output contract shapes. Seeding is incremental; an empty or absent
    evals/ directory passes while the convention is documented.
    """
    if not EVALS_DIR.is_dir():
        check("evals/ convention documented, no evals/ directory yet", True)
        return
    seats = sorted(dir_.name for dir_ in EVALS_DIR.iterdir() if dir_.is_dir())
    check(f"evals/ covers {len(seats)} seat(s)", True, ", ".join(seats) or "none")
    for seat in seats:
        prompt = EVALS_DIR / seat / "prompt.md"
        check(f"evals/{seat}/prompt.md exists", prompt.is_file())


def main() -> int:
    check_marketplace_manifest()
    check_plugin_manifest()
    check_agents()
    check_skills()
    check_evals()
    if failures:
        print(f"\n{len(failures)} check(s) failed")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
