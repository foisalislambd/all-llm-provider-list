# Documentation

Step-by-step guides for using and maintaining this repository.

| Guide | What you'll learn |
|-------|-------------------|
| [Getting Started](getting-started.md) | Clone repo, first lookup, choose a provider |
| [Python Lookup](python-lookup.md) | Use `llm_lookup.py` — search providers & models |
| [Sync Models](sync-models.md) | Refresh live model catalogs from provider APIs |
| [Integration Guide](integration-guide.md) | Connect OpenAI / Anthropic SDKs to any provider |
| [Data Structure](data-structure.md) | How `providers.json`, `models.json` are organized |
| [Adding Providers](adding-providers.md) | Add or update a provider in the database |
| [Contributing](contributing.md) | PR workflow, review checklist |

## Quick commands

```bash
# Look up a provider
python llm_lookup.py groq

# Show all models for a provider
python llm_lookup.py openrouter --models

# Search which providers have a model
python llm_lookup.py --search-model llama-3.3

# Refresh model catalogs
python scripts/sync_models.py
```
