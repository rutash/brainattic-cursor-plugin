# Brainattic for Cursor

Connect Cursor agents to **Brainattic**, an EU-hosted, MCP-native knowledge base for teams. Search trusted project material and maintain versioned, governed documents across AI workflows. Brainattic's workspace permissions and agent rules continue to apply when using Cursor.

This open-source plugin is a **configuration wrapper for the hosted Brainattic MCP server**, not a copy of the Brainattic backend. The remote service is proprietary and operated by Finite Software Systems Ltd. This repository contains no application server source code or credentials.

- Product: https://brainattic.ai
- Connection guide: https://brainattic.ai/docs/connect
- Support: https://brainattic.ai/support
- MCP endpoint: https://app.brainattic.ai/api/mcp (Streamable HTTP)

## Contents

- `.cursor-plugin/plugin.json` — Cursor Marketplace plugin manifest.
- `mcp.json` — registers the Brainattic remote MCP endpoint.
- `tests/validate_manifest.py` — local structural smoke test.

## Requirements

- Cursor version supporting plugins and remote Streamable HTTP MCP servers.
- A Brainattic account with access to a workspace.
- Browser access to complete the OAuth authorization flow when prompted.

## Install and test locally

The Cursor Marketplace entry is subject to Cursor's manual review. Until approval, you can inspect and test this package locally:

1. Copy this repository's files into `~/.cursor/plugins/local/brainattic/` (ensure the manifest ends up at `~/.cursor/plugins/local/brainattic/.cursor-plugin/plugin.json`).
2. Reload Cursor using **Developer: Reload Window**, or restart Cursor.
3. Open **Customize -> Plugins** and find the Brainattic plugin. Connect or authorize its MCP server when prompted.
4. Authenticate to Brainattic using the browser-based OAuth flow. The plugin does **not** include an API key or a static OAuth client secret.
5. Confirm that Brainattic tools are available. First perform a read-only search of a document in a workspace you control.

**Important:** A local JSON schema/structure check is not proof of working OAuth. Validate a fresh Cursor OAuth connection and actual tool discovery before submitting to the Marketplace. If Cursor's OAuth onboarding does not work for your account, record the error and do not claim the integration has passed end-to-end testing.

## Security and privacy

- The MCP server is hosted at `https://app.brainattic.ai/api/mcp`.
- Authentication and access rights are enforced by the Brainattic service. Workspace admins control access; the installed plugin does not grant permissions.
- The connected server exposes both read and mutation tools; confirm intended workspace permissions and review proposed write actions before allowing them.
- The public plugin manifest contains no API tokens, passwords, OAuth client secrets, or customer data.

## Version and license

The plugin version `1.0.0` is independent of the hosted Brainattic MCP server version. The files in this repository are MIT-licensed (see `LICENSE`). The MIT license **does not apply to the hosted Brainattic service, its server source code, or other proprietary assets**.

Maintainer: Finite Software Systems Ltd. — https://brainattic.ai
