# Contributing

The source of truth is `data/providers.json`. `README.md` is generated from it.

## Look up a provider

```bash
python llm_lookup.py groq
python llm_lookup.py groq --models
python llm_lookup.py --category Gateway
python llm_lookup.py --search-model kimi
```

Lookup order: exact slug, then exact name, then alias, then partial match.

## Add or update a provider

Edit `data/providers.json` (append a new object, do not reuse an existing `slug`, set `id` to one more than the current max):

```json
{
  "id": 398,
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

Categories: `Frontier`, `IaaS`, `Sovereign / Cloud`, `Gateway`, `Aggregator`, `OAuth`, `Web Cookie`, `No-auth`, `Search`, `Audio`, `Image / Video`, `Cloud Agent`, `Embeddings`, `Specialized`, `Local`.

Then add model IDs under that slug in `data/static_models.json`, regenerate the README, and refresh catalogs:

```bash
python scripts/generate_readme.py
python scripts/sync_models.py
python llm_lookup.py new-provider --models
```

Do not edit README tables by hand.

## PR checklist

- Official website and a verified `api_base_url`
- At least one real model ID
- Correct `category` and `openai_compatible`
- No API keys or `.env` files
- `python llm_lookup.py <slug>` works
