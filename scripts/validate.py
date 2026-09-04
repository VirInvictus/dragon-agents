"""Structural checks for the dragon-agents plugin.

Validates both JSON manifests and every agent charter: frontmatter fields,
the Read+Bash tool restriction, the read-only and no-subagent charter lines,
and the six-agent roster. CI runs this on every push.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
EXPECTED_AGENTS = {
    "cascade-checker",
    "ci-triage",
    "doc-drift-auditor",
    "repo-cartographer",
    "slop-reader",
    "spec-compliance-reviewer",
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
        "roster is exactly the expected six agents",
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
        check(
            f"{stem}: tools are exactly Read and Bash",
            parse_tools(fields.get("tools", "")) == ["Read", "Bash"],
            fields.get("tools", ""),
        )
        check(
            f"{stem}: charter forbids spawning subagents",
            "Do not spawn subagents" in text,
        )
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
