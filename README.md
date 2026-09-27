# claude-code-dotfiles

Personal Claude Code configuration, kept here so it can be restored on any device.

## What's here

- `settings.json` — global Claude Code settings: extra plugin marketplaces and which plugins are enabled.
- `skills/` — seven fiction-writing skills built from seven craft books with a 70/30 rule, plus `writers-room`, one front door that fires them together with your social, persuasion and video skills (see [`skills/README.md`](skills/README.md)).
- `tools/check_70_30.py` — verifies each skill's 70/30 source ratio and ledger.

Deliberately **not** included (machine-specific or sensitive, and not needed for setup):
- `.credentials.json` — OAuth token, never sync this
- `history.jsonl`, `cache/`, `plugins/cache`, `plugins/marketplaces` — local caches, rebuilt automatically
- `plugins/installed_plugins.json`, `plugins/known_marketplaces.json` — contain absolute local install paths

## Setting up a new device

1. Install Claude Code.
2. Copy `settings.json` from this repo into your global config directory:
   - Windows: `%USERPROFILE%\.claude\settings.json`
   - macOS/Linux: `~/.claude/settings.json`
3. Start `claude`. It will read `extraKnownMarketplaces` and `enabledPlugins` from settings and fetch/enable the plugins listed there automatically.
4. If a plugin doesn't pick up automatically, add its marketplace manually, e.g.:
   ```
   /plugin marketplace add <git-url-from-extraKnownMarketplaces>
   /plugin enable <plugin-name>
   ```

## Writing skills

Install the skills by copying each skill directory into your personal skills folder. Claude Code picks them up in every project.

macOS/Linux (from the repo root):
```bash
mkdir -p ~/.claude/skills
for d in skills/*/; do cp -R "${d%/}" ~/.claude/skills/; done
```

Windows PowerShell (from the repo root):
```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Get-ChildItem .\skills -Directory | ForEach-Object { Copy-Item $_.FullName "$HOME\.claude\skills" -Recurse -Force }
```

Re-run the same command after pulling updates. After editing a skill, run `python3 tools/check_70_30.py --write` to refresh its source ledger, then `python3 tools/check_70_30.py` to confirm the 70/30 ratio still holds.

For cloud sessions (claude.ai/code), personal skills in `~/.claude/skills/` aren't available. Commit the skill directories to the project's own `.claude/skills/` instead; the `cybertron-chronicles` repo does this.

## Updating this repo

After installing/enabling a new plugin locally, copy the updated `settings.json` back into this repo and commit.

## Note on "cloud" sync

This repo syncs your **local Claude Code CLI config** across machines. It does not sync settings for claude.ai / Claude Code's web/cloud environments — those are managed separately in your claude.ai account settings and aren't stored in this file.
