# Sync Models Guide

Model lists change often. Use `scripts/sync_models.py` to refresh `data/models.json`.

## What it does

1. Reads all providers from `data/providers.json`
2. Fetches **live** model catalogs where possible
3. Falls back to `data/static_models.json` when live fetch is unavailable
4. Writes merged results to `data/models.json`

## Run a sync

```bash
python scripts/sync_models.py
```

Example output:

```
Synced 97 providers, 945 total model IDs
  Live catalogs: 3
  Written to: data/models.json
```

## Live sources (no API key needed)

| Provider slug | API |
|---------------|-----|
| `openrouter` | `https://openrouter.ai/api/v1/models` |
| `deepinfra` | `https://api.deepinfra.com/v1/openai/models` |
| `huggingface` | `https://router.huggingface.co/v1/models` |

## Live sources (API key required)

Set the env variable, then run sync:

| Provider | Env variable |
|----------|--------------|
| OpenAI | `OPENAI_API_KEY` |
| Groq | `GROQ_API_KEY` |
| Together AI | `TOGETHER_API_KEY` |
| Fireworks | `FIREWORKS_API_KEY` |
| Mistral | `MISTRAL_API_KEY` |
| DeepSeek | `DEEPSEEK_API_KEY` |
| xAI | `XAI_API_KEY` |
| Cerebras | `CEREBRAS_API_KEY` |
| SambaNova | `SAMBANOVA_API_KEY` |
| Nebius | `NEBIUS_API_KEY` |

```powershell
$env:GROQ_API_KEY = "gsk_..."
python scripts/sync_models.py
```

## Update static model lists

Edit `data/static_models.json`:

```json
{
  "providers": {
    "groq": [
      "llama-3.3-70b-versatile",
      "llama-3.1-8b-instant"
    ]
  }
}
```

Then run `python scripts/sync_models.py` again.

## When to sync

- Before a release or PR that updates model data
- When a provider launches new models
- Weekly/monthly for gateway catalogs (OpenRouter, DeepInfra)

## Verify after sync

```bash
python llm_lookup.py openrouter --models
python llm_lookup.py --search-model gpt-5
```
