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
never-authenticate fences. Every agent keeps the no-subagent line. CI runs
this on every push.
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
    "git-archaeologist",
    "claw",
    "latro",
    "shadow",
    "ledger-analyst",
    "librarian",
    "music-archivist",
    "release-auditor",
    "repo-cartographer",
    "security-auditor",
    "slop-reader",
    "spec-compliance-reviewer",
    "stock-broker",
    "syshealth-auditor",
    "test-gap-analyst",
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
        "roster is exactly the expected twenty-eight agents",
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
        elif stem in WEB_APPEND_AGENTS:
            expected_tools = WEB_READ_TOOLS
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
        lowered = text.lower()
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
        else:
            check(f"{stem}: charter declares read-only", "Read-only" in text)


def main() -> int:
    check_marketplace_manifest()
    check_plugin_manifest()
    check_agents()
    if failures:
        print(f"\n{len(failures)} check(s) failed")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
