# Python Lookup Guide

The `llm_lookup.py` script lets you search providers and models from Python or the command line.

## Import in your project

```python
from llm_lookup import lookup, get_models, search_models, all_providers
```

## Look up a provider

By name, slug, alias, or API URL:

```python
lookup("groq")
lookup("openrouter")
lookup("api.groq.com/openai/v1")
lookup("gemini")          # alias → Google AI Studio
```

Returns a dict with: `name`, `category`, `website`, `api_base_url`, `popular_models`, `env_variable`, `openai_compatible`, `notes`.

## Get all supported models

```python
info = get_models("groq")
print(info["count"])      # number of models
print(info["source"])     # static | live-public | live-auth
print(info["models"])     # list of model IDs
```

## Provider + models in one call

```python
full = lookup("openrouter", include_models=True)
print(full["models_count"])
print(full["models"][:5])
```

## Search models across all providers

```python
hits = search_models("deepseek-r1")
for hit in hits:
    print(hit["provider"], hit["models"])
```

## Filter all providers

```python
all_providers()                          # all 97
all_providers(category="Gateway")        # gateways only
all_providers(openai_compatible=True)    # OpenAI-compatible only
```

## CLI reference

| Command | Description |
|---------|-------------|
| `python llm_lookup.py groq` | Provider details |
| `python llm_lookup.py groq --models` | Details + full model list |
| `python llm_lookup.py groq --json` | JSON output |
| `python llm_lookup.py --all` | List every provider |
| `python llm_lookup.py --category IaaS` | Filter by category |
| `python llm_lookup.py --search qwen` | Fuzzy search providers |
| `python llm_lookup.py --search-model llama` | Find model across providers |
| `python llm_lookup.py --count` | Category counts |

## Example script

Run the included example:

```bash
python example.py
```

## Data files used

| File | Purpose |
|------|---------|
| `data/providers.json` | Provider metadata (97 entries) |
| `data/models.json` | Model catalogs per provider |
| `data/static_models.json` | Fallback static model lists |

See [Data Structure](data-structure.md) for field definitions.
