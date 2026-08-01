# claude-code-dotfiles

Personal Claude Code configuration, kept here so it can be restored on any device.

## What's here

- `settings.json` — global Claude Code settings: extra plugin marketplaces and which plugins are enabled.
- `.agents/skills/` — project-local skills installed via the [`skills` CLI](https://github.com/anthropics/skills) (`npx skills add <repo> --skill <name>`); `.claude/skills/` symlinks into it and `skills-lock.json` pins the installed versions.
- `mcp-servers.md` — user-scope MCP servers (added via `claude mcp add ... -s user`), since those live in `~/.claude.json` rather than `settings.json` and aren't picked up automatically.

Deliberately **not** included (machine-specific or sensitive, and not needed for setup):
- `.credentials.json` — OAuth token, never sync this
- `history.jsonl`, `cache/`, `plugins/cache`, `plugins/marketplaces` — local caches, rebuilt automatically
- `plugins/installed_plugins.json`, `plugins/known_marketplaces.json` — contain absolute local install paths
- `.claude/settings.local.json` — per-machine local permissions, gitignored globally

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
5. Re-run the commands in `mcp-servers.md` to restore user-scope MCP servers.

## Updating this repo

After installing/enabling a new plugin locally, copy the updated `settings.json` back into this repo and commit.

After adding a project-local skill with `npx skills add <repo> --skill <name>`, commit the resulting `.agents/skills/<name>/`, `.claude/skills/<name>` symlink, and updated `skills-lock.json`.

After adding a user-scope MCP server with `claude mcp add <name> -s user -- <command>`, add the same command to `mcp-servers.md`.

## Note on "cloud" sync

This repo syncs your **local Claude Code CLI config** across machines. It does not sync settings for claude.ai / Claude Code's web/cloud environments — those are managed separately in your claude.ai account settings and aren't stored in this file.
