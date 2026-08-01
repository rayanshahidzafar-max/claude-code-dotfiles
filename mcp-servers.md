# User-scope MCP servers

These are added with `-s user`, so they live in `~/.claude.json` (not `settings.json`) and aren't restored automatically by copying `settings.json`. Re-run these on a new device:

```
claude mcp add playwright -s user -- npx @playwright/mcp@latest
```
