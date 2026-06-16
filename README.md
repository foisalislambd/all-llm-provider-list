# All LLM Providers — API Endpoints, Models & Integration Guide

A curated, developer-friendly directory of **60+ global LLM providers** — official frontier APIs, high-speed inference platforms, sovereign clouds, and multi-provider gateways.

Use this repo as a single reference when you need:

- Official website & documentation links  
- Standard API base URLs  
- Popular model families per provider  
- Environment variable names for quick setup  
- Copy-paste integration patterns (OpenAI & Anthropic SDKs)

> **Note:** Model names and API URLs change frequently. Always verify against the provider's official docs before production use. Full raw reference data lives in [`docs/data.txt`](docs/data.txt).

---

## Table of Contents

- [Quick Start](#quick-start)
- [How Providers Are Organized](#how-providers-are-organized)
- [Official Frontier Model Developers](#official-frontier-model-developers)
- [High-Performance Inference Platforms (IaaS)](#high-performance-inference-platforms-iaas)
- [Decentralized, Sovereign & Enterprise Clouds](#decentralized-sovereign--enterprise-clouds)
- [Multi-Provider Gateways & Routers](#multi-provider-gateways--routers)
- [Environment Variables Cheat Sheet](#environment-variables-cheat-sheet)
- [Integration Examples](#integration-examples)
- [Choosing the Right Provider](#choosing-the-right-provider)
- [Contributing](#contributing)
- [License](#license)

---

## Quick Start

Most providers expose an **OpenAI-compatible** REST API. Switching providers usually means changing only two things:

1. `base_url` — the API endpoint  
2. `api_key` — your provider credential  

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

**Want one API key for many models?** Start with a gateway like [OpenRouter](https://openrouter.ai) or [Opper](https://opper.ai) — they route to dozens of upstream providers behind a single endpoint.

---

## How Providers Are Organized

```
┌─────────────────────────────────────────┐
│     Your App (OpenAI / Anthropic SDK)   │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│   Gateways (OpenRouter, Opper, Axiom)   │  ← optional routing layer
└─────────┬───────────┬───────────┬───────┘
          │           │           │
   ┌──────▼───┐ ┌─────▼─────┐ ┌──▼──────────┐
   │ Frontier │ │ IaaS /    │ │ Sovereign / │
   │ APIs     │ │ Inference │ │ Private     │
   │ OpenAI,  │ │ Groq,     │ │ Azure,      │
   │ Claude,  │ │ Together  │ │ Vertex, EU  │
   │ Gemini   │ │ Fireworks │ │ clouds      │
   └──────────┘ └───────────┘ └─────────────┘
```

| Category | Best for | Trade-off |
|----------|----------|-----------|
| **Frontier APIs** | Best reasoning, agents, multimodal | Higher cost, vendor lock-in |
| **IaaS / Inference** | Speed, open-weight models, low cost | Model catalog varies by host |
| **Sovereign / Enterprise** | GDPR, VPC, compliance | More setup & procurement |
| **Gateways** | One key, failover, cost routing | Extra hop, gateway fees |

---

## Official Frontier Model Developers

Companies that train and ship their own foundation models.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Google AI Studio** | [aistudio.google.com](https://aistudio.google.com) | `https://generativelanguage.googleapis.com` | Gemini 3.5, 3.1, 2.5 | Up to 2M context; free tier on Flash variants |
| **Anthropic** | [anthropic.com](https://www.anthropic.com) | `https://api.anthropic.com` | Claude Opus 4.8, Sonnet 4.6, Haiku 4.5 | Native Messages API (not OpenAI-compatible) |
| **OpenAI** | [platform.openai.com](https://platform.openai.com) | `https://api.openai.com/v1` | GPT-5.5, GPT-5.4, GPT-4.1, GPT-4o, o3-mini | Industry-standard SDK ecosystem |
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | `https://api.deepseek.com/v1` | DeepSeek-V4-Pro, V4-Flash, R1 | Strong price/performance; context caching |
| **Mistral AI** | [console.mistral.ai](https://console.mistral.ai) | `https://api.mistral.ai/v1` | Mistral Medium 3.5, Small 4, Ministral 3 | EU-hosted; generous experiment tier |
| **xAI** | [x.ai](https://x.ai) | `https://api.x.ai/v1` | Grok-3, Grok-2 | Real-time streaming & agent workflows |
| **Cohere** | [cohere.com](https://cohere.com) | `https://api.cohere.com/v2` | Command R+, Embed v4, Rerank 3.5 | Enterprise search & RAG |
| **AI21 Labs** | [studio.ai21.com](https://studio.ai21.com) | `https://api.ai21.com/studio/v1` | Jamba 1.5 Large, Jamba 1.5 Mini | Long-context hybrid architecture |
| **Baidu Qianfan** | [cloud.baidu.com](https://cloud.baidu.com/product/wenxinworkshop) | `https://api.baiduqianfan.ai/v1` | ERNIE 4.0 Turbo, Speed, Lite | Chinese-language optimized |
| **StepFun** | [platform.stepfun.com](https://platform.stepfun.com) | `https://api.stepfun.com/v1` | Step-series | Multilingual agent pipelines |
| **Z.ai (Zhipu AI)** | [open.bigmodel.cn](https://open.bigmodel.cn) | `https://open.bigmodel.cn/api/paas/v4/` | GLM-5, GLM-4.7, GLM-4.7-Flash | Strong bilingual CN/EN performance |
| **Xiaomi** | [xiaomi.com](https://xiaomi.com) | Custom endpoint | Mimo-v2-pro | On-device & edge deployments |
| **Reka AI** | [reka.ai](https://reka.ai) | `https://api.reka.ai/v1` | Reka Core, Reka Flash | Video, audio & text multimodal |
| **Inflection** | [inflection.ai](https://inflection.ai) | Custom webhooks | Pi-series | Conversational assistant focus |

---

## High-Performance Inference Platforms (IaaS)

Hosted open-weight models on optimized hardware — great for **low latency** and **low cost per token**.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Groq** | [console.groq.com](https://console.groq.com) | `https://api.groq.com/openai/v1` | Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B | LPU hardware; extremely fast TTFT |
| **Cerebras** | [cerebras.ai](https://cerebras.ai) | `https://api.cerebras.ai/v1` | Llama 3.3 70B, GPT-OSS 120B, Qwen 3 32B | Wafer-scale engine throughput |
| **SambaNova** | [sambanova.ai](https://sambanova.ai) | `https://api.sambanova.ai/v1` | Llama 3.1 405B, Llama 3.3 70B, Qwen | RDU serving for large models |
| **Together AI** | [together.ai](https://together.ai) | `https://api.together.xyz/v1` | Llama 3.3, DeepSeek-V4, Qwen, FLUX.1 | Large catalog + fine-tuning |
| **Fireworks AI** | [fireworks.ai](https://fireworks.ai) | `https://api.fireworks.ai/inference/v1` | Qwen 3.6 Plus, Kimi K2.6, Llama 4 Maverick | Serverless low-latency serving |
| **DeepInfra** | [deepinfra.com](https://deepinfra.com) | `https://api.deepinfra.com/v1/openai` | Llama 3.3, Qwen 3, DeepSeek-V4, Mistral | Aggressive open-model pricing |
| **Nebius AI Studio** | [studio.nebius.ai](https://studio.nebius.ai) | `https://api.studio.nebius.ai/v1` | DeepSeek-R1-0528, Llama 3.3 70B | EU infrastructure; Token Factory |
| **SiliconFlow** | [siliconflow.com](https://siliconflow.com) | `https://api.siliconflow.cn/v1` | DeepSeek-R1-0528, MiniMax-M2, Qwen3-VL | Excellent cost/performance (CN) |
| **Inception** | [inceptionlabs.ai](https://inceptionlabs.ai) | `https://api.inceptionlabs.ai/v1` | Mercury-2, Mercury-Edit-2 | Diffusion language models (dLLMs) |
| **Liquid AI** | [liquid.ai](https://liquid.ai) | Custom cluster endpoints | LFM2.5 Instruct, LFM2-24B | Hybrid efficient architectures |
| **Friendli** | [friendli.ai](https://friendli.ai) | `https://api.friendli.ai/serverless/v1` | Llama 3.1 8B, DeepSeek-R1 | Custom checkpoints & private instances |
| **Inceptron** | [inceptron.io](https://inceptron.io) | Custom endpoint | Open-weight LLMs | Self-configured model hosting |
| **Infermatic** | [infermatic.ai](https://infermatic.ai) | `https://api.totalgpt.ai` | Rocinante, Midnight Miqu, Llama | Flat-rate community checkpoints |
| **Mancer** | [mancer.tech](https://mancer.tech) | `https://mancer.tech/oai/v1` | Goliath 120B, MythoMax, LumiMaid | Creative / roleplay fine-tunes |
| **Morph** | [morphllm.com](https://morphllm.com) | `https://api.morphllm.com/v1` | morph-qwen35-397b, morph-qwen36-27b | Fast code editing & routing |
| **AionLabs** | [aionlabs.ai](https://aionlabs.ai) | `https://api.aionlabs.ai/v1` | Aion 2.0, Aion-RP | Creative multi-turn fine-tunes |

---

## Decentralized, Sovereign & Enterprise Clouds

Regional compliance, private networking, decentralized compute, and enterprise MLOps.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **AkashML** | [akash.network](https://akash.network) | `https://api.akashml.com/v1` | Llama 3, Qwen, DeepSeek | Decentralized GPU marketplace |
| **AtlasCloud** | [atlascloud.ai](https://atlascloud.ai) | `https://api.atlascloud.ai/v1` | DeepSeek-V3, Seedance 2.0, Kling 3.0 | Language + image + video APIs |
| **Chutes** | [chutes.ai](https://chutes.ai) | `https://llm.chutes.ai/v1` | Kimi, GLM, Qwen, MiniMax | Serverless custom model deploy |
| **Cloudflare Workers AI** | [cloudflare.com](https://cloudflare.com) | `https://api.cloudflare.com` | Llama 3.3, Gemma 4, Kimi K2.5, FLUX | Edge inference; neuron-second billing |
| **DigitalOcean** | [digitalocean.com](https://digitalocean.com) | `https://inference.do-ai.run/v1/` | Llama 3 8B Instruct | Integrates with App Platform |
| **GMICloud** | [gmicloud.ai](https://gmicloud.ai) | `https://api.gmi-serving.com/v1` | GLM-5.1-FP8, DeepSeek-V3.2 | Enterprise H100 GPU cloud |
| **io.net** | [io.net](https://io.net) | `https://api.intelligence.io.solutions/api/v1` | GLM-4.5-Air, GPT-OSS 120B, Llama 3.3 | DePIN GPU clusters |
| **NextBit** | [nextbit256.com](https://nextbit256.com) | `https://api.nextbit256.com/v1` | qwen:3.5-35b, qwen3:30b, qwen3:14b | EU data centers (Spain) |
| **Novita** | [novita.ai](https://novita.ai) | `https://api.novita.ai/openai/v1` | Kimi K2.5, Llama, Qwen | Model APIs + agent sandboxes |
| **Parasail** | [parasail.io](https://parasail.io) | `https://api.saas.parasail.io/v1` | DeepSeek-R1, QwenCoder 32B | Serverless + dedicated instances |
| **Phala** | [phala.network](https://phala.network) | `POST /v1/chat/completions` | Qwen2.5-72B-Instruct | TEE confidential execution |
| **Poolside** | [poolside.ai](https://poolside.ai) | `https://divers.poolsi.de/openai/v1/` | Laguna XS.2, Laguna M.1 | Code generation focus |
| **Venice** | [venice.ai](https://venice.ai) | `https://api.venice.ai/api/v1` | llama-3.3-70b, fluently-xl | Privacy-first; web3 auth |
| **Wafer** | [wafer.ai](https://wafer.ai) | `https://pass.wafer.ai/v1` | Qwen3.5-397B-A17B, GLM-5.1 | Fast serverless; Claude Code compatible |
| **Azure OpenAI** | [azure.microsoft.com](https://azure.microsoft.com) | `https://<resource>.openai.azure.com/openai/v1` | OpenAI, Anthropic, Llama | Enterprise Microsoft integration |
| **Google Vertex AI** | [cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai) | Region-dependent | Gemini, Claude, partners | VPC, IAM, enterprise procurement |
| **Baseten** | [baseten.co](https://baseten.co) | Custom model APIs | Open-weight & custom | MLOps with Truss packaging |
| **Clarifai** | [clarifai.com](https://clarifai.com) | Custom endpoints | Multimodal models | Data labeling & classification |

---

## Multi-Provider Gateways & Routers

One API surface for many upstream providers — ideal for **failover**, **cost optimization**, and **reducing credential sprawl**.

| Provider | Website | API Base URL | What you get | Notes |
|----------|---------|--------------|--------------|-------|
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | `https://openrouter.ai/api/v1` | Claude, GPT, Gemini, DeepSeek, Llama + more | Auto fallback & provider selection |
| **Opper** | [opper.ai](https://opper.ai) | `https://api.opper.ai/v3/compat` | 300+ routed models | EU-hosted; PII shielding |
| **Axiom** | [axiomstudio.ai](https://axiomstudio.ai) | `https://cloud.axiomstudio.ai/rest/v1/llm-gateway/v1/` | 18+ unified providers | Kubernetes-native enterprise routing |
| **Switchpoint** | [switchpoint.ai](https://switchpoint.ai) | `https://api.ppq.ai` | Intelligent router | Request-aware provider selection |
| **Relace** | [relace.ai](https://relace.ai) | `https://api.relace.ai/v1` | Apply 3, Search | Coding APIs; zero data retention default |
| **Moonshot AI** | [api.moonshot.ai](https://api.moonshot.ai/v1) | `https://api.moonshot.ai/v1` | Kimi K2.7 Code, K2.6 | First-party Kimi gateway |
| **OpenInference** | [openinference.ai](https://openinference.ai) | Tracing / observability | LLM telemetry | Execution graph tracing |
| **Weights & Biases** | [wandb.ai](https://wandb.ai) | Evaluation registry | Model benchmarking | Experiment tracking |
| **Perceptron** | [perceptron.ai](https://perceptron.ai) | Custom gateway | Enterprise routes | Custom middleware routing |

---

## Environment Variables Cheat Sheet

Copy these into your `.env` file or secrets manager:

| Provider | Env Variable | API Base URL |
|----------|--------------|--------------|
| Google AI Studio | `GEMINI_API_KEY` | `https://generativelanguage.googleapis.com` |
| Anthropic | `ANTHROPIC_API_KEY` | `https://api.anthropic.com` |
| OpenAI | `OPENAI_API_KEY` | `https://api.openai.com/v1` |
| DeepSeek | `DEEPSEEK_API_KEY` | `https://api.deepseek.com/v1` |
| Mistral AI | `MISTRAL_API_KEY` | `https://api.mistral.ai/v1` |
| xAI | `XAI_API_KEY` | `https://api.x.ai/v1` |
| Groq | `GROQ_API_KEY` | `https://api.groq.com/openai/v1` |
| Together AI | `TOGETHER_API_KEY` | `https://api.together.xyz/v1` |
| Fireworks AI | `FIREWORKS_API_KEY` | `https://api.fireworks.ai/inference/v1` |
| Nebius Studio | `NEBIUS_API_KEY` | `https://api.tokenfactory.nebius.com/v1/` |
| GMI Cloud | `GMI_API_KEY` | `https://api.gmi-serving.com/v1` |
| Wafer | `WAFER_API_KEY` | `https://pass.wafer.ai/v1` |
| OpenRouter | `OPENROUTER_API_KEY` | `https://openrouter.ai/api/v1` |
| Morph | `MORPH_API_KEY` | `https://api.morphllm.com/v1` |

---

## Integration Examples

### OpenAI SDK → Any OpenAI-Compatible Provider (Python)

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=os.environ["NEBIUS_API_KEY"],
)

stream = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-0528",
    messages=[{"role": "user", "content": "Explain quantum computing in one paragraph."}],
    temperature=0.1,
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

### Anthropic SDK → Compatible Gateway (Node.js)

```javascript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  baseURL: "https://pass.wafer.ai",
  apiKey: process.env.WAFER_API_KEY,
});

const message = await anthropic.messages.create({
  model: "Qwen3.5-397B-A17B",
  max_tokens: 4096,
  messages: [{ role: "user", content: "Write a hello world in Rust." }],
});

console.log(message.content[0].text);
```

### OpenRouter — One Key, Many Models

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

## Choosing the Right Provider

| Your goal | Start here |
|-----------|------------|
| Best overall reasoning & tools | OpenAI, Anthropic, Google Gemini |
| Lowest cost / open models | DeepInfra, Together, SiliconFlow, Groq |
| EU data residency | Mistral, Nebius, NextBit, Opper |
| One API for everything | OpenRouter, Opper, Axiom |
| Code generation | Poolside, Morph, Moonshot Kimi |
| Privacy / no logging | Venice, Relace (ZDR), Phala (TEE) |
| Enterprise & compliance | Azure OpenAI, Google Vertex AI |

### Production tips

1. **Use a gateway for HA** — Route across 2–3 providers so rate limits or outages don't take down your app.
2. **Pin model versions** — Providers silently update models. Pin explicit model IDs and monitor output quality.
3. **Enable context caching** — Gemini, DeepSeek, and Anthropic support caching that can cut costs significantly on repeated prompts.
4. **Respect data sovereignty** — Route PII and regulated data only through EU or private VPC endpoints.

---

## Repository Structure

```
all-llm-provider-list/
├── README.md          ← You are here (human-friendly guide)
└── docs/
    └── data.txt       ← Full reference database with extended notes
```

---

## Contributing

Found a new provider, updated endpoint, or wrong model name? PRs welcome!

1. Fork the repo  
2. Update the relevant table in `README.md` and/or `docs/data.txt`  
3. Include a link to the provider's official documentation  
4. Open a pull request with a short description of what changed  

---

## Disclaimer

This list is maintained for **educational and integration reference** purposes. We are not affiliated with any listed provider. API endpoints, pricing, and model availability can change without notice. Always refer to official provider documentation for production deployments.

---

## License

MIT — use freely, attribute when you share.
