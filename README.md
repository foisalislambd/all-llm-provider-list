# All LLM Providers — API Endpoints, Models & Integration Guide

A curated, developer-friendly directory of **95+ global LLM providers** — official frontier APIs, inference platforms, sovereign clouds, gateways, aggregators, and local runtimes.

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
- [Complete Provider Index](#complete-provider-index)
- [How Providers Are Organized](#how-providers-are-organized)
- [Official Frontier Model Developers](#official-frontier-model-developers)
- [High-Performance Inference Platforms (IaaS)](#high-performance-inference-platforms-iaas)
- [Decentralized, Sovereign & Enterprise Clouds](#decentralized-sovereign--enterprise-clouds)
- [Multi-Provider Gateways & Routers](#multi-provider-gateways--routers)
- [Aggregators & API Marketplaces](#aggregators--api-marketplaces)
- [Embeddings & Specialized APIs](#embeddings--specialized-apis)
- [Local & Self-Hosted Runtimes](#local--self-hosted-runtimes)
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

**Want one API key for many models?** Start with a gateway like [OpenRouter](https://openrouter.ai), [Portkey](https://portkey.ai), or [Opper](https://opper.ai).

---

## Complete Provider Index

| # | Provider | Category | API Base URL |
|---|----------|----------|--------------|
| 1 | OpenAI | Frontier | `https://api.openai.com/v1` |
| 2 | Anthropic | Frontier | `https://api.anthropic.com` |
| 3 | Google AI Studio | Frontier | `https://generativelanguage.googleapis.com` |
| 4 | DeepSeek | Frontier | `https://api.deepseek.com/v1` |
| 5 | Mistral AI | Frontier | `https://api.mistral.ai/v1` |
| 6 | xAI | Frontier | `https://api.x.ai/v1` |
| 7 | Cohere | Frontier | `https://api.cohere.com/v2` |
| 8 | AI21 Labs | Frontier | `https://api.ai21.com/studio/v1` |
| 9 | Baidu Qianfan | Frontier | `https://api.baiduqianfan.ai/v1` |
| 10 | StepFun | Frontier | `https://api.stepfun.com/v1` |
| 11 | Z.ai (Zhipu AI) | Frontier | `https://open.bigmodel.cn/api/paas/v4/` |
| 12 | Xiaomi | Frontier | Custom endpoint |
| 13 | Reka AI | Frontier | `https://api.reka.ai/v1` |
| 14 | Inflection | Frontier | Custom webhooks |
| 15 | MiniMax | Frontier | `https://api.minimax.io/v1` |
| 16 | Alibaba DashScope (Qwen) | Frontier | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| 17 | Upstage | Frontier | `https://api.upstage.ai/v1/solar` |
| 18 | Perplexity | Frontier | `https://api.perplexity.ai` |
| 19 | Voyage AI | Embeddings | `https://api.voyageai.com/v1` |
| 20 | Groq | IaaS | `https://api.groq.com/openai/v1` |
| 21 | Cerebras | IaaS | `https://api.cerebras.ai/v1` |
| 22 | SambaNova | IaaS | `https://api.sambanova.ai/v1` |
| 23 | Together AI | IaaS | `https://api.together.xyz/v1` |
| 24 | Fireworks AI | IaaS | `https://api.fireworks.ai/inference/v1` |
| 25 | DeepInfra | IaaS | `https://api.deepinfra.com/v1/openai` |
| 26 | Nebius AI Studio | IaaS | `https://api.studio.nebius.ai/v1` |
| 27 | SiliconFlow | IaaS | `https://api.siliconflow.cn/v1` |
| 28 | Inception | IaaS | `https://api.inceptionlabs.ai/v1` |
| 29 | Liquid AI | IaaS | Custom cluster endpoints |
| 30 | Friendli | IaaS | `https://api.friendli.ai/serverless/v1` |
| 31 | Inceptron | IaaS | Custom endpoint |
| 32 | Infermatic | IaaS | `https://api.totalgpt.ai` |
| 33 | Mancer | IaaS | `https://mancer.tech/oai/v1` |
| 34 | Morph | IaaS | `https://api.morphllm.com/v1` |
| 35 | AionLabs | IaaS | `https://api.aionlabs.ai/v1` |
| 36 | HuggingFace Inference | IaaS | `https://router.huggingface.co/v1` |
| 37 | NVIDIA NIM | IaaS | `https://integrate.api.nvidia.com/v1` |
| 38 | Hyperbolic | IaaS | `https://api.hyperbolic.xyz/v1` |
| 39 | Lepton AI | IaaS | `https://api.lepton.ai/v1` |
| 40 | Kluster.ai | IaaS | `https://api.kluster.ai/v1` |
| 41 | Anyscale Endpoints | IaaS | `https://api.endpoints.anyscale.com/v1` |
| 42 | Replicate | IaaS | `https://api.replicate.com/v1` |
| 43 | Inference.net | IaaS | `https://api.inference.net/v1` |
| 44 | Arcee AI | IaaS | `https://conductor.arcee.ai/v1` |
| 45 | Glhf.chat | IaaS | `https://glhf.chat/api/openai/v1` |
| 46 | AkashML | Sovereign / Cloud | `https://api.akashml.com/v1` |
| 47 | AtlasCloud | Sovereign / Cloud | `https://api.atlascloud.ai/v1` |
| 48 | Chutes | Sovereign / Cloud | `https://llm.chutes.ai/v1` |
| 49 | Cloudflare Workers AI | Sovereign / Cloud | `https://api.cloudflare.com/client/v4/accounts/{id}/ai/v1` |
| 50 | DigitalOcean | Sovereign / Cloud | `https://inference.do-ai.run/v1/` |
| 51 | GMICloud | Sovereign / Cloud | `https://api.gmi-serving.com/v1` |
| 52 | io.net | Sovereign / Cloud | `https://api.intelligence.io.solutions/api/v1` |
| 53 | NextBit | Sovereign / Cloud | `https://api.nextbit256.com/v1` |
| 54 | Novita | Sovereign / Cloud | `https://api.novita.ai/openai/v1` |
| 55 | Parasail | Sovereign / Cloud | `https://api.saas.parasail.io/v1` |
| 56 | Phala | Sovereign / Cloud | `POST /v1/chat/completions` |
| 57 | Poolside | Sovereign / Cloud | `https://divers.poolsi.de/openai/v1/` |
| 58 | Venice | Sovereign / Cloud | `https://api.venice.ai/api/v1` |
| 59 | Wafer | Sovereign / Cloud | `https://pass.wafer.ai/v1` |
| 60 | Azure OpenAI | Sovereign / Cloud | `https://<resource>.openai.azure.com/openai/v1` |
| 61 | Google Vertex AI | Sovereign / Cloud | Region-dependent |
| 62 | Amazon Bedrock | Sovereign / Cloud | `https://bedrock-runtime.<region>.amazonaws.com` |
| 63 | Baseten | Sovereign / Cloud | `https://model-{id}.api.baseten.co/v1` |
| 64 | Clarifai | Sovereign / Cloud | Custom endpoints |
| 65 | Scaleway | Sovereign / Cloud | `https://api.scaleway.ai/v1` |
| 66 | OVHcloud AI Endpoints | Sovereign / Cloud | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` |
| 67 | GitHub Models | Sovereign / Cloud | `https://models.inference.ai.azure.com` |
| 68 | Modal | Sovereign / Cloud | `https://<app>.modal.run/v1` |
| 69 | OpenRouter | Gateway | `https://openrouter.ai/api/v1` |
| 70 | Opper | Gateway | `https://api.opper.ai/v3/compat` |
| 71 | Axiom | Gateway | `https://cloud.axiomstudio.ai/rest/v1/llm-gateway/v1/` |
| 72 | Switchpoint | Gateway | `https://api.ppq.ai` |
| 73 | Relace | Gateway | `https://api.relace.ai/v1` |
| 74 | Moonshot AI | Gateway | `https://api.moonshot.ai/v1` |
| 75 | OpenInference | Gateway | Tracing / observability |
| 76 | Weights & Biases | Gateway | Evaluation registry |
| 77 | Perceptron | Gateway | Custom gateway |
| 78 | Portkey | Gateway | `https://api.portkey.ai/v1` |
| 79 | LiteLLM | Gateway | `http://localhost:4000/v1` (self-hosted) |
| 80 | Requesty | Gateway | `https://router.requesty.ai/v1` |
| 81 | Unify.ai | Gateway | `https://api.unify.ai/v0` |
| 82 | Helicone | Gateway | `https://ai-gateway.helicone.ai/v1` |
| 83 | Vercel AI Gateway | Gateway | `https://ai-gateway.vercel.sh/v1` |
| 84 | Cloudflare AI Gateway | Gateway | `https://gateway.ai.cloudflare.com/v1` |
| 85 | Kong AI Gateway | Gateway | Self-hosted / enterprise |
| 86 | AIMLAPI | Aggregator | `https://api.aimlapi.com/v1` |
| 87 | Eden AI | Aggregator | `https://api.edenai.co/v2` |
| 88 | LemonData | Aggregator | `https://api.lemondata.ai/v1` |
| 89 | Coze (ByteDance) | Aggregator | `https://api.coze.com/v1` |
| 90 | NLP Cloud | Specialized | `https://api.nlpcloud.io/v1` |
| 91 | Puter.js | Specialized | `https://api.puter.com/ai/chat` |
| 92 | Ollama | Local | `http://localhost:11434/v1` |
| 93 | LM Studio | Local | `http://localhost:1234/v1` |
| 94 | llama.cpp | Local | `http://localhost:8080/v1` |
| 95 | Jan.ai | Local | `http://localhost:1337/v1` |
| 96 | vLLM | Local | `http://localhost:8000/v1` |
| 97 | LocalAI | Local | `http://localhost:8080/v1` |

---

## How Providers Are Organized

```
┌─────────────────────────────────────────┐
│     Your App (OpenAI / Anthropic SDK)   │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│  Gateways (OpenRouter, Portkey, Opper)  │  ← optional routing layer
└─────────┬───────────┬───────────┬───────┘
          │           │           │
   ┌──────▼───┐ ┌─────▼─────┐ ┌──▼──────────┐
   │ Frontier │ │ IaaS /    │ │ Sovereign / │
   │ APIs     │ │ Inference │ │ Private     │
   │ OpenAI,  │ │ Groq, HF  │ │ Azure, AWS  │
   │ Claude,  │ │ Together  │ │ Vertex, EU  │
   │ Gemini   │ │ Fireworks │ │ clouds      │
   └──────────┘ └───────────┘ └─────────────┘
```

| Category | Count | Best for | Trade-off |
|----------|-------|----------|-----------|
| **Frontier APIs** | 18 | Best reasoning, agents, multimodal | Higher cost, vendor lock-in |
| **IaaS / Inference** | 26 | Speed, open-weight models, low cost | Model catalog varies by host |
| **Sovereign / Enterprise** | 23 | GDPR, VPC, compliance | More setup & procurement |
| **Gateways & Routers** | 18 | One key, failover, observability | Extra hop, gateway fees |
| **Aggregators** | 4 | Multi-vendor under one bill | Less control over routing |
| **Local / Self-hosted** | 6 | Privacy, unlimited, offline | You manage hardware |

---

## Official Frontier Model Developers

Companies that train and ship their own foundation models.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Google AI Studio** | [aistudio.google.com](https://aistudio.google.com) | `https://generativelanguage.googleapis.com` | Gemini 3.5, 3.1, 2.5 | Up to 2M context; free tier on Flash variants |
| **Anthropic** | [anthropic.com](https://www.anthropic.com) | `https://api.anthropic.com` | Claude Opus 4.8, Sonnet 4.6, Haiku 4.5 | Native Messages API (not OpenAI-compatible) |
| **OpenAI** | [platform.openai.com](https://platform.openai.com) | `https://api.openai.com/v1` | GPT-5.5, GPT-5.4, GPT-4.1, GPT-4o, o3-mini | Industry-standard SDK ecosystem |
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | `https://api.deepseek.com/v1` | DeepSeek-V4-Pro, V4-Flash, R1 | OpenAI + Anthropic format; context caching |
| **Mistral AI** | [console.mistral.ai](https://console.mistral.ai) | `https://api.mistral.ai/v1` | Mistral Medium 3.5, Small 4, Ministral 3 | EU-hosted; generous experiment tier |
| **xAI** | [x.ai](https://x.ai) | `https://api.x.ai/v1` | Grok-3, Grok-2 | Real-time streaming & agent workflows |
| **Cohere** | [cohere.com](https://cohere.com) | `https://api.cohere.com/v2` | Command R+, Embed v4, Rerank 3.5 | Enterprise search & RAG |
| **AI21 Labs** | [studio.ai21.com](https://studio.ai21.com) | `https://api.ai21.com/studio/v1` | Jamba 1.5 Large, Jamba 1.5 Mini | Long-context hybrid architecture |
| **Baidu Qianfan** | [cloud.baidu.com](https://cloud.baidu.com/product/wenxinworkshop) | `https://api.baiduqianfan.ai/v1` | ERNIE 4.0 Turbo, Speed, Lite | Chinese-language optimized |
| **StepFun** | [platform.stepfun.com](https://platform.stepfun.com) | `https://api.stepfun.com/v1` | Step 3.5 Flash, Step-series | Multilingual agent pipelines |
| **Z.ai (Zhipu AI)** | [open.bigmodel.cn](https://open.bigmodel.cn) | `https://open.bigmodel.cn/api/paas/v4/` | GLM-5, GLM-4.7, GLM-4.7-Flash | Strong bilingual CN/EN performance |
| **Xiaomi** | [xiaomi.com](https://xiaomi.com) | Custom endpoint | Mimo-v2-pro | On-device & edge deployments |
| **Reka AI** | [reka.ai](https://reka.ai) | `https://api.reka.ai/v1` | Reka Core, Reka Flash | Video, audio & text multimodal |
| **Inflection** | [inflection.ai](https://inflection.ai) | Custom webhooks | Pi-series | Conversational assistant focus |
| **MiniMax** | [platform.minimax.io](https://platform.minimax.io) | `https://api.minimax.io/v1` | MiniMax-M3, M2.1, M2 | OpenAI + Anthropic compatible; agentic |
| **Alibaba DashScope** | [alibabacloud.com](https://www.alibabacloud.com) | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | Qwen3-Max, Qwen-Plus, Qwen-Flash | Alibaba Cloud Model Studio; Qwen family |
| **Upstage** | [console.upstage.ai](https://console.upstage.ai) | `https://api.upstage.ai/v1/solar` | Solar Pro 3, Solar Mini | Korean AI lab; strong document AI |
| **Perplexity** | [docs.perplexity.ai](https://docs.perplexity.ai) | `https://api.perplexity.ai` | Sonar, Sonar Pro, Sonar Reasoning | Search-grounded answers with citations |

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
| **HuggingFace Inference** | [huggingface.co](https://huggingface.co) | `https://router.huggingface.co/v1` | Llama 3.3 70B, Qwen 2.5 72B | Huge model catalog; free tier available |
| **NVIDIA NIM** | [build.nvidia.com](https://build.nvidia.com) | `https://integrate.api.nvidia.com/v1` | Llama 3.3 70B, DeepSeek-R1 | NVIDIA inference microservices |
| **Hyperbolic** | [hyperbolic.xyz](https://app.hyperbolic.xyz) | `https://api.hyperbolic.xyz/v1` | DeepSeek-V3, Llama 3.3 70B | Decentralized GPU compute |
| **Lepton AI** | [lepton.ai](https://lepton.ai) | `https://api.lepton.ai/v1` | Llama 3.3 70B | Fast serverless inference |
| **Kluster.ai** | [kluster.ai](https://kluster.ai) | `https://api.kluster.ai/v1` | Llama 3.1 405B, Qwen 2.5 72B | Batch inference specialist |
| **Anyscale Endpoints** | [anyscale.com](https://app.endpoints.anyscale.com) | `https://api.endpoints.anyscale.com/v1` | Llama 3.3 70B, Mixtral 8x22B | Ray-based model serving |
| **Replicate** | [replicate.com](https://replicate.com) | `https://api.replicate.com/v1` | Open models, FLUX, video | Pay-per-run; image/audio/video too |
| **Inference.net** | [inference.net](https://inference.net) | `https://api.inference.net/v1` | DeepSeek-R1, Llama 3.1 70B | Decentralized inference network |
| **Arcee AI** | [arcee.ai](https://arcee.ai) | `https://conductor.arcee.ai/v1` | Trinity-Large, Caller-Large | Enterprise fine-tuned models |
| **Glhf.chat** | [glhf.chat](https://glhf.chat) | `https://glhf.chat/api/openai/v1` | Any HuggingFace model (`hf:` prefix) | vLLM-backed; run any HF model |

---

## Decentralized, Sovereign & Enterprise Clouds

Regional compliance, private networking, decentralized compute, and enterprise MLOps.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **AkashML** | [akash.network](https://akash.network) | `https://api.akashml.com/v1` | Llama 3, Qwen, DeepSeek | Decentralized GPU marketplace |
| **AtlasCloud** | [atlascloud.ai](https://atlascloud.ai) | `https://api.atlascloud.ai/v1` | DeepSeek-V3, Seedance 2.0, Kling 3.0 | Language + image + video APIs |
| **Chutes** | [chutes.ai](https://chutes.ai) | `https://llm.chutes.ai/v1` | Kimi, GLM, Qwen, MiniMax | Serverless custom model deploy |
| **Cloudflare Workers AI** | [cloudflare.com](https://cloudflare.com) | `https://api.cloudflare.com/client/v4/accounts/{id}/ai/v1` | Llama 3.3, Gemma 4, Kimi K2.5, FLUX | Edge inference; neuron-second billing |
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
| **Amazon Bedrock** | [aws.amazon.com/bedrock](https://aws.amazon.com/bedrock) | `https://bedrock-runtime.<region>.amazonaws.com` | Claude, Llama, Titan, Mistral | AWS-native; IAM & VPC integration |
| **Baseten** | [baseten.co](https://baseten.co) | `https://model-{id}.api.baseten.co/v1` | Llama 3.3, DeepSeek-R1, custom | MLOps with Truss packaging |
| **Clarifai** | [clarifai.com](https://clarifai.com) | Custom endpoints | Multimodal models | Data labeling & classification |
| **Scaleway** | [scaleway.com](https://console.scaleway.com) | `https://api.scaleway.ai/v1` | Llama 3.3 70B, DeepSeek-R1 | European cloud; GDPR-compliant |
| **OVHcloud AI** | [ovhcloud.com](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/) | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | Llama 3.1 70B, Qwen 2.5 72B | EU-hosted open models |
| **GitHub Models** | [github.com/marketplace/models](https://github.com/marketplace/models) | `https://models.inference.ai.azure.com` | GPT-4o, Llama 3.1 70B | Free tier with GitHub PAT |
| **Modal** | [modal.com](https://modal.com) | `https://<app>.modal.run/v1` | Any (self-deployed via vLLM) | Serverless GPU; deploy your own models |

---

## Multi-Provider Gateways & Routers

One API surface for many upstream providers — ideal for **failover**, **cost optimization**, and **reducing credential sprawl**.

| Provider | Website | API Base URL | What you get | Notes |
|----------|---------|--------------|--------------|-------|
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | `https://openrouter.ai/api/v1` | 300+ models from 60+ providers | Auto fallback & provider selection |
| **Opper** | [opper.ai](https://opper.ai) | `https://api.opper.ai/v3/compat` | 300+ routed models | EU-hosted; PII shielding |
| **Axiom** | [axiomstudio.ai](https://axiomstudio.ai) | `https://cloud.axiomstudio.ai/rest/v1/llm-gateway/v1/` | 18+ unified providers | Kubernetes-native enterprise routing |
| **Switchpoint** | [switchpoint.ai](https://switchpoint.ai) | `https://api.ppq.ai` | Intelligent router | Request-aware provider selection |
| **Relace** | [relace.ai](https://relace.ai) | `https://api.relace.ai/v1` | Apply 3, Search | Coding APIs; zero data retention default |
| **Moonshot AI** | [api.moonshot.ai](https://api.moonshot.ai/v1) | `https://api.moonshot.ai/v1` | Kimi K2.7 Code, K2.6 | First-party Kimi gateway |
| **Portkey** | [portkey.ai](https://portkey.ai) | `https://api.portkey.ai/v1` | 250+ models | Guardrails, caching, observability |
| **LiteLLM** | [github.com/BerriAI/litellm](https://github.com/BerriAI/litellm) | `http://localhost:4000/v1` | 100+ providers | Open-source; self-host or cloud |
| **Requesty** | [requesty.ai](https://requesty.ai) | `https://router.requesty.ai/v1` | Multi-provider routing | Auto-failover between providers |
| **Unify.ai** | [unify.ai](https://unify.ai) | `https://api.unify.ai/v0` | ML-based routing | Picks optimal provider per query |
| **Helicone** | [helicone.ai](https://helicone.ai) | `https://ai-gateway.helicone.ai/v1` | 100+ models | Observability-first AI gateway |
| **Vercel AI Gateway** | [vercel.com](https://vercel.com/docs/ai-gateway) | `https://ai-gateway.vercel.sh/v1` | All major providers | Bundled with Vercel platform |
| **Cloudflare AI Gateway** | [cloudflare.com](https://developers.cloudflare.com/ai-gateway/) | `https://gateway.ai.cloudflare.com/v1` | Any upstream provider | Edge caching; sits in front of APIs |
| **Kong AI Gateway** | [konghq.com](https://konghq.com/products/kong-ai-gateway) | Self-hosted | Enterprise routing | For existing Kong infrastructure |
| **OpenInference** | [openinference.ai](https://openinference.ai) | Tracing / observability | LLM telemetry | Execution graph tracing |
| **Weights & Biases** | [wandb.ai](https://wandb.ai) | Evaluation registry | Model benchmarking | Experiment tracking |
| **Perceptron** | [perceptron.ai](https://perceptron.ai) | Custom gateway | Enterprise routes | Custom middleware routing |

---

## Aggregators & API Marketplaces

Single API key to access models from multiple upstream vendors.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **AIMLAPI** | [aimlapi.com](https://aimlapi.com) | `https://api.aimlapi.com/v1` | GPT-4o, Claude 3.5, Gemini | 300+ models; free tier available |
| **Eden AI** | [edenai.co](https://edenai.co) | `https://api.edenai.co/v2` | OpenAI, Google, Anthropic routes | Multi-provider under one API |
| **LemonData** | [lemondata.ai](https://lemondata.ai) | `https://api.lemondata.ai/v1` | GPT-4o, Claude 3.5, open models | 300+ models; $1 free credits |
| **Coze (ByteDance)** | [coze.com](https://coze.com) | `https://api.coze.com/v1` | Via bots: GPT-4o, Gemini, Claude | Bot-builder platform with LLM backends |

---

## Embeddings & Specialized APIs

Providers focused on specific tasks rather than general chat.

| Provider | Website | API Base URL | Specialty | Notes |
|----------|---------|--------------|-----------|-------|
| **Voyage AI** | [voyageai.com](https://www.voyageai.com) | `https://api.voyageai.com/v1` | Embeddings & rerankers | Top-tier retrieval embeddings |
| **Perplexity** | [docs.perplexity.ai](https://docs.perplexity.ai) | `https://api.perplexity.ai` | Search-grounded chat | Real-time web search in responses |
| **NLP Cloud** | [nlpcloud.com](https://nlpcloud.com) | `https://api.nlpcloud.io/v1` | NER, summarization, chat | Custom API format; fine-tuned models |
| **Puter.js** | [puter.com](https://puter.com) | `https://api.puter.com/ai/chat` | Free GPT/Claude/Gemini access | No API key needed; web/Node.js SDK |

---

## Local & Self-Hosted Runtimes

Run models on your own machine — **free, private, and unlimited**.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Ollama** | [ollama.com](https://ollama.com) | `http://localhost:11434/v1` | Llama 3.3, Qwen 2.5, Gemma | Easiest local setup; 50+ models |
| **LM Studio** | [lmstudio.ai](https://lmstudio.ai) | `http://localhost:1234/v1` | Any GGUF from HuggingFace | Best GUI; drag-and-drop models |
| **llama.cpp** | [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | `http://localhost:8080/v1` | Any GGUF model | Foundation for most local tools |
| **Jan.ai** | [jan.ai](https://jan.ai) | `http://localhost:1337/v1` | Supported local models | 100% offline desktop app |
| **vLLM** | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) | `http://localhost:8000/v1` | Any compatible checkpoint | Production-grade local serving |
| **LocalAI** | [localai.io](https://localai.io) | `http://localhost:8080/v1` | OpenAI-compatible local stack | Drop-in OpenAI API replacement |

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
| Portkey | `PORTKEY_API_KEY` | `https://api.portkey.ai/v1` |
| Morph | `MORPH_API_KEY` | `https://api.morphllm.com/v1` |
| MiniMax | `MINIMAX_API_KEY` | `https://api.minimax.io/v1` |
| Alibaba DashScope | `DASHSCOPE_API_KEY` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| HuggingFace | `HUGGINGFACE_API_KEY` | `https://router.huggingface.co/v1` |
| NVIDIA NIM | `NVIDIA_API_KEY` | `https://integrate.api.nvidia.com/v1` |
| Perplexity | `PERPLEXITY_API_KEY` | `https://api.perplexity.ai` |
| Moonshot / Kimi | `MOONSHOT_API_KEY` | `https://api.moonshot.ai/v1` |
| GitHub Models | `GITHUB_TOKEN` | `https://models.inference.ai.azure.com` |

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

### Alibaba Qwen via OpenAI SDK (Python)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen3-max",
    messages=[{"role": "user", "content": "Hello from Qwen!"}],
)
print(response.choices[0].message.content)
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
| EU data residency | Mistral, Nebius, NextBit, Scaleway, OVHcloud, Opper |
| One API for everything | OpenRouter, Portkey, Opper, AIMLAPI |
| Code generation | Poolside, Morph, Moonshot Kimi |
| Privacy / no logging | Venice, Relace (ZDR), Phala (TEE), Local (Ollama) |
| Enterprise & compliance | Azure OpenAI, Google Vertex AI, Amazon Bedrock |
| Free tier / prototyping | Groq, Gemini, GitHub Models, HuggingFace, OpenRouter |
| Chinese models | DeepSeek, Qwen (DashScope), Zhipu, MiniMax, StepFun |
| Search-grounded answers | Perplexity Sonar |
| Self-hosted / offline | Ollama, LM Studio, vLLM, LocalAI |

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
