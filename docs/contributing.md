# Contributing

Thank you for helping keep this provider list accurate and up to date.

## Ways to contribute

1. **Add a new provider** — see [Adding Providers](adding-providers.md)
2. **Fix an endpoint or model name** — edit `data/providers.json` + README
3. **Refresh model catalogs** — run `scripts/sync_models.py`, commit `data/models.json`
4. **Improve docs** — edit files in `docs/`
5. **Report issues** — open a GitHub issue with provider name and correct URL

## PR workflow

1. Fork the repository
2. Create a branch: `git checkout -b add-provider-xyz`
3. Make your changes
4. Test locally:
   ```bash
   python llm_lookup.py <slug> --models
   python scripts/sync_models.py
   ```
5. Commit with a clear message:
   ```
   Add Provider XYZ with API endpoint and model list
   ```
6. Open a pull request describing what changed and link to official docs

## What we need in every provider PR

- Official website URL
- Verified `api_base_url`
- At least 1 confirmed model ID
- Correct `category` and `openai_compatible` flag
- README table row

## What we don't accept

- Providers without a public API
- Scraped data without official source
- API keys or secrets in any file
- `.env` files (use `.gitignore`)

## Code style

- Python: standard library only for core scripts
- JSON: 2-space indent, UTF-8
- Docs: clear steps, copy-paste commands

## Questions?

Open an issue or start a discussion on GitHub.
