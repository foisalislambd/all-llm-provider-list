# Getting Started

This repo is a **reference directory** of 97+ LLM API providers with endpoints, models, and integration notes.

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/all-llm-provider-list.git
cd all-llm-provider-list
```

No `pip install` required — only Python 3.10+ standard library.

## 2. Browse providers in README

Open [`README.md`](../README.md) for the full human-readable tables:

- Official frontier APIs (OpenAI, Anthropic, Gemini…)
- Inference platforms (Groq, Together, Fireworks…)
- Enterprise clouds (Azure, Bedrock, Vertex…)
- Gateways (OpenRouter, Portkey…)
- Local runtimes (Ollama, LM Studio…)

## 3. Look up a provider from the terminal

```bash
python llm_lookup.py groq
python llm_lookup.py api.openai.com/v1
python llm_lookup.py --all
```

## 4. See all models a provider supports

```bash
python llm_lookup.py groq --models
python llm_lookup.py deepinfra --models --json
```

## 5. Pick a provider for your app

| Goal | Start here |
|------|------------|
| Best reasoning | OpenAI, Anthropic, Gemini |
| Lowest cost | DeepInfra, Together, Groq |
| One API, many models | OpenRouter, Portkey |
| EU / GDPR | Mistral, Nebius, Scaleway |
| Offline / private | Ollama, LM Studio |

See [Integration Guide](integration-guide.md) for SDK setup.

## 6. Set your API key

```bash
# Windows PowerShell
$env:GROQ_API_KEY = "your-key-here"

# Linux / macOS
export GROQ_API_KEY="your-key-here"
```

Never commit `.env` files — they are listed in `.gitignore`.

## Next steps

- [Python Lookup](python-lookup.md) — full script API
- [Sync Models](sync-models.md) — update model lists
- [Adding Providers](adding-providers.md) — contribute new entries
