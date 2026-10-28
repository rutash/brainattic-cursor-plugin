#!/usr/bin/env python3
"""Validate the static Brainattic Cursor plugin package without network access."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parent.parent
plugin_path = root / '.cursor-plugin' / 'plugin.json'
mcp_path = root / 'mcp.json'
plugin = json.loads(plugin_path.read_text(encoding='utf-8'))
mcp = json.loads(mcp_path.read_text(encoding='utf-8'))

assert re.fullmatch(r'[a-z0-9][a-z0-9.-]*[a-z0-9]', plugin['name'])
assert re.fullmatch(r'\d+\.\d+\.\d+', plugin['version'])
assert plugin['mcpServers'] == 'mcp.json'
assert plugin['author']['name'] == 'Finite Software Systems Ltd.'
assert plugin['license'] == 'MIT'
assert (root / 'LICENSE').is_file() and (root / 'README.md').is_file()
assert plugin['repository'] == 'https://github.com/rutash/brainattic-cursor-plugin'
assert plugin['logo'].startswith('https://brainattic.ai/')
assert list(mcp['mcpServers']) == ['brainattic']
server = mcp['mcpServers']['brainattic']
assert server == {'url': 'https://app.brainattic.ai/api/mcp'}
assert urlparse(server['url']).scheme == 'https'
assert not any(x in str(plugin).lower() for x in ('private_key', 'client_secret', 'api_key'))
print('PASS: Cursor manifest, MCP URL, repo metadata, and local packaging')
print('NOT TESTED: public logo availability, Cursor runtime, OAuth and MCP tool calls')
