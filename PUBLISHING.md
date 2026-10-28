# Publishing Brainattic on the Cursor Marketplace

## 1. Preflight

From the repository root:

```bash
python3 tests/validate_manifest.py
gh auth status
```

Open `https://brainattic.ai/assets/icon-512.png` in a normal browser and confirm the image is a square, public image that fits Cursor's logotype requirement. If it is not, replace the URL in `.cursor-plugin/plugin.json` and in the form with a working public square asset.

## 2. Local Cursor smoke test

The code and JSON structure can be validated without Cursor, but OAuth must be tested in Cursor itself. Follow `README.md` to install locally. Verify plugin discovery, OAuth sign-in, tool discovery, and a read-only Brainattic search. Keep any tokens and other customer data out of this repository.

## 3. Create a public GitHub repository

```bash
git init -b main
git add .
git commit -m "feat: add Brainattic remote MCP plugin for Cursor"
gh repo create rutash/brainattic-cursor-plugin --public --source=. --remote=origin --push
gh repo edit rutash/brainattic-cursor-plugin --add-topic cursor-plugin --homepage https://brainattic.ai
```

If GitHub reports that the repository already exists, do not re-create it: inspect its contents before pushing.

## 4. Fill the Cursor publishing form

- Organization name: `Finite Software Systems Ltd.`
- Organization handle: `finite-software-systems-ltd` (or choose a branded handle if available and preferred)
- Contact email: `tashev@finite-soft.com`
- Logotype URL: `https://brainattic.ai/assets/icon-512.png` (after the visual check)
- Description: `Brainattic connects Cursor agents to an EU-hosted, governed knowledge base via MCP. Search and retrieve trusted project information, maintain versioned documentation, and create or update knowledge under workspace permissions and agent rules. Sign in securely through OAuth; no local backend or bundled API keys are required.`
- GitHub repository: `https://github.com/rutash/brainattic-cursor-plugin`
- Website: `https://brainattic.ai`

**Do not paste the repository URL until it exists and contains the `.cursor-plugin/plugin.json` and `mcp.json` files.** Cursor reviews the actual public repo and manually approves plugins.

## 5. After submission

Save the confirmation and application/reference number, if provided. The application is not an approved marketplace listing until Cursor confirms it and publishes it. The plugin wrapper is MIT-licensed; Brainattic's hosted backend is proprietary.
