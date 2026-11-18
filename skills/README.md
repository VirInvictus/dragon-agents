# skills/

Seven Obsidian skills vendored from the official Obsidian repository,
plus one community CLI-audit reference merged in. Provenance, commit
pins, the vet record, and the license chain live in
[ATTRIBUTION.md](ATTRIBUTION.md). Skills surface under this plugin's
namespace once installed; the roster bakes at app boot, and so does
the skill set.

| Skill | What it does | Local note |
|---|---|---|
| `obsidian-cli` | Drive a running Obsidian app from the shell: read, create, search, tasks, tags, properties, backlinks, plugin dev. | CLI is on PATH here; it needs the desktop app running, and it exits 0 on failure (verified live), so read output, never trust the code. Safety rules and per-command gotchas in [obsidian-cli/references/CLI_AGENT_NOTES.md](obsidian-cli/references/CLI_AGENT_NOTES.md). |
| `obsidian-markdown` | Obsidian-flavored Markdown: wikilinks, embeds, callouts, properties, tags, comments, highlights. | The core skill for vault work; agents read the vault as plain files, so this applies even with the app closed. |
| `obsidian-bases` | `.base` database views: filters, formulas, table/card/kanban views. | 601 lines (spec recommends under 500); deep material already split into references/. |
| `json-canvas` | `.canvas` files: nodes, edges, groups, layout, validation. | Includes the JSON-escaping and newline pitfalls. |
| `obsidian-headless` | Obsidian Sync and Publish from a terminal (`ob`). | Requires a paid Sync/Publish subscription; unused on this setup, vendored for completeness. |
| `defuddle` | Extract clean Markdown from web pages. | Complements the research seats' fetch ladder. |
| `knap` | Render Markdown from templates plus JSON/CSV data; pairs with defuddle. | Batch rendering with `--dry-run`. |

House law that outranks any of these skills: the vault is never
rewritten by agents (wikilink, tag, and append only), and deletes go
to trash, never `permanent`. The skills teach mechanics; the vault's
own rules govern writes.
