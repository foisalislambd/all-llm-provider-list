# Adding Providers

Follow these steps to add a new LLM API provider to the database.

## Checklist

- [ ] Provider has a public API with documented endpoint
- [ ] Official website / docs link available
- [ ] Model IDs verified from official docs or `/v1/models`
- [ ] `providers.json` updated
- [ ] `static_models.json` updated with model IDs
- [ ] `README.md` table row added
- [ ] `python scripts/sync_models.py` run (if live API exists)
- [ ] `python llm_lookup.py <slug> --models` verified

## Step 1 — Add to providers.json

Open `data/providers.json` and append a new entry:

```json
{
  "id": 98,
  "name": "New Provider",
  "slug": "new-provider",
  "aliases": ["np"],
  "category": "IaaS",
  "website": "https://example.com",
  "api_base_url": "https://api.example.com/v1",
  "popular_models": ["model-a", "model-b"],
  "env_variable": "NEW_PROVIDER_API_KEY",
  "openai_compatible": true,
  "notes": "Short description"
}
```

**Category options:** `Frontier`, `IaaS`, `Sovereign / Cloud`, `Gateway`, `Aggregator`, `Embeddings`, `Specialized`, `Local`

## Step 2 — Add models to static_models.json

```json
{
  "providers": {
    "new-provider": [
      "model-a",
      "model-b",
      "model-c"
    ]
  }
}
```

## Step 3 — Enable live sync (optional)

If the provider has a public `GET /v1/models` endpoint, add to `scripts/sync_models.py`:

```python
PUBLIC_MODEL_APIS = {
    ...
    "new-provider": "https://api.example.com/v1/models",
}
```

Or for auth-required APIs:

```python
AUTH_MODEL_APIS = {
    ...
    "new-provider": ("NEW_PROVIDER_API_KEY", "https://api.example.com/v1/models"),
}
```

## Step 4 — Update README.md

Add a row to the correct table section and to the **Complete Provider Index**.

## Step 5 — Sync and test

```bash
python scripts/sync_models.py
python llm_lookup.py new-provider --models
python llm_lookup.py new-provider --json
```

## Step 6 — Open a PR

See [Contributing](contributing.md).

## Updating an existing provider

1. Edit fields in `data/providers.json`
2. Update models in `data/static_models.json`
3. Update README row
4. Run `python scripts/sync_models.py`
5. Verify with `llm_lookup.py`

## Removing a provider

1. Remove from `providers.json` (re-number IDs optional)
2. Remove slug from `static_models.json`
3. Remove from README tables
4. Run `python scripts/sync_models.py`
