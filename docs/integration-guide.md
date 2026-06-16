# Integration Guide

Most providers use the **OpenAI-compatible** format. Switching providers = change `base_url` + `api_key`.

## OpenAI SDK (Python)

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"],
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

### Provider → base_url quick map

| Provider | `base_url` |
|----------|------------|
| OpenAI | `https://api.openai.com/v1` |
| Groq | `https://api.groq.com/openai/v1` |
| Together | `https://api.together.xyz/v1` |
| Fireworks | `https://api.fireworks.ai/inference/v1` |
| DeepSeek | `https://api.deepseek.com/v1` |
| OpenRouter | `https://openrouter.ai/api/v1` |
| DashScope (Qwen) | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |

Use `python llm_lookup.py <provider> --json` to get the exact URL.

## Anthropic SDK (Node.js)

For gateways that translate to Anthropic format (e.g. Wafer):

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://pass.wafer.ai",
  apiKey: process.env.WAFER_API_KEY,
});

const msg = await client.messages.create({
  model: "Qwen3.5-397B-A17B",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hi" }],
});
```

## OpenRouter — one key, many models

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## List available models (OpenAI-compatible)

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.deepinfra.com/v1/openai", api_key="...")
for m in client.models.list():
    print(m.id)
```

Or use this repo:

```bash
python llm_lookup.py deepinfra --models
```

## Providers that are NOT OpenAI-compatible

| Provider | Use instead |
|----------|-------------|
| Anthropic | `@anthropic-ai/sdk` Messages API |
| Cohere | Cohere Python SDK v2 |
| Amazon Bedrock | `boto3` bedrock-runtime |
| NLP Cloud | Custom REST format |

Check `openai_compatible` field:

```python
from llm_lookup import lookup
print(lookup("anthropic")["openai_compatible"])  # False
```

## Production tips

1. **Pin model IDs** — providers update models silently
2. **Use a gateway for failover** — OpenRouter, Portkey, LiteLLM
3. **Enable caching** — Gemini, DeepSeek, Anthropic support context caching
4. **EU data** — route through Mistral, Nebius, NextBit, Scaleway

## Environment variables

See the cheat sheet in [README.md](../README.md#environment-variables-cheat-sheet) or:

```bash
python llm_lookup.py groq --json
# check "env_variable" field
```
