# All AI and LLM Providers list — API Endpoints, Models & Integration Guide

A curated, developer-friendly directory of **402 global LLM providers** — official frontier APIs, inference platforms, sovereign clouds, gateways, aggregators, local runtimes, OAuth/IDE subscriptions, search, audio, and media APIs.

Catalog aligned with [OmniRoute](https://github.com/diegosouzapw/OmniRoute) (351+ registered providers) plus extra listings maintained in this repo. Use this as a single reference when you need:

- Official website & documentation links
- Standard API base URLs
- Popular model families per provider
- Environment variable names for quick setup
- Copy-paste integration patterns (OpenAI & Anthropic SDKs)

> **Note:** Model names and API URLs change frequently. Always verify against the provider's official docs before production use. Machine-readable data lives in [`data/`](data/) — see the [Documentation](docs/README.md). Last catalog merge: 2026-09-15.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Complete Provider Index](#complete-provider-index)
- [How Providers Are Organized](#how-providers-are-organized)
- [Official Frontier Model Developers](#official-frontier-model-developers)
- [High-Performance Inference Platforms (IaaS)](#high-performance-inference-platforms-iaas)
- [Decentralized, Sovereign & Enterprise Clouds](#decentralized-sovereign-enterprise-clouds)
- [Multi-Provider Gateways & Routers](#multi-provider-gateways-routers)
- [Aggregators & API Marketplaces](#aggregators-api-marketplaces)
- [Discount & Budget APIs](#discount-budget-apis)
- [OAuth & IDE Subscriptions](#oauth-ide-subscriptions)
- [Web Cookie / Browser Sessions](#web-cookie-browser-sessions)
- [No-auth & Public Endpoints](#no-auth-public-endpoints)
- [Search APIs](#search-apis)
- [Audio (TTS / STT)](#audio-tts-stt)
- [Image & Video APIs](#image-video-apis)
- [Cloud Coding Agents](#cloud-coding-agents)
- [Embeddings & Rerankers](#embeddings-rerankers)
- [Other Specialized APIs](#other-specialized-apis)
- [Local & Self-Hosted Runtimes](#local-self-hosted-runtimes)
- [Environment Variables Cheat Sheet](#environment-variables-cheat-sheet)
- [Integration Examples](#integration-examples)
- [Choosing the Right Provider](#choosing-the-right-provider)
- [Documentation](#documentation)
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

**Want one API key for many models?** Start with a gateway like [OpenRouter](https://openrouter.ai), [Portkey](https://portkey.ai), [OmniRoute](https://github.com/diegosouzapw/OmniRoute), or [Opper](https://opper.ai).

Look up any provider from this repo:

```bash
python llm_lookup.py groq
python llm_lookup.py --category Gateway
python llm_lookup.py --search-model kimi
```

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
| 12 | Xiaomi | Frontier | `https://api.xiaomimimo.com/v1` |
| 13 | Reka AI | Frontier | `https://api.reka.ai/v1` |
| 14 | Inflection | Frontier | Custom webhooks |
| 15 | MiniMax | Frontier | `https://api.minimax.io/v1` |
| 16 | Alibaba DashScope | Frontier | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
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
| 29 | Liquid AI | IaaS | `https://inference.liquid.ai/v1` |
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
| 56 | Phala | Sovereign / Cloud | POST /v1/chat/completions |
| 57 | Poolside | Sovereign / Cloud | `https://divers.poolsi.de/openai/v1/` |
| 58 | Venice | Sovereign / Cloud | `https://api.venice.ai/api/v1` |
| 59 | Wafer | Sovereign / Cloud | `https://pass.wafer.ai/v1` |
| 60 | Azure OpenAI | Sovereign / Cloud | `https://<resource>.openai.azure.com/openai/v1` |
| 61 | Google Vertex AI | Sovereign / Cloud | `https://us-central1-aiplatform.googleapis.com/v1/projects` |
| 62 | Amazon Bedrock | Sovereign / Cloud | `https://bedrock-runtime.<region>.amazonaws.com` |
| 63 | Baseten | Sovereign / Cloud | `https://model-{id}.api.baseten.co/v1` |
| 64 | Clarifai | Sovereign / Cloud | Custom endpoints |
| 65 | Scaleway | Sovereign / Cloud | `https://api.scaleway.ai/v1` |
| 66 | OVHcloud AI | Sovereign / Cloud | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` |
| 67 | GitHub Models | Sovereign / Cloud | `https://models.inference.ai.azure.com` |
| 68 | Modal | Sovereign / Cloud | `https://<app>.modal.run/v1` |
| 69 | OpenRouter | Gateway | `https://openrouter.ai/api/v1` |
| 70 | Opper | Gateway | `https://api.opper.ai/v3/compat` |
| 71 | Axiom | Gateway | `https://cloud.axiomstudio.ai/rest/v1/llm-gateway/v1/` |
| 72 | Switchpoint | Gateway | `https://api.ppq.ai` |
| 73 | Relace | Gateway | `https://api.relace.ai/v1` |
| 74 | Moonshot AI | Gateway | `https://api.moonshot.ai/v1` |
| 75 | OpenInference | Gateway | Tracing / observability |
| 76 | Weights & Biases | Gateway | `https://api.inference.wandb.ai/v1` |
| 77 | Perceptron | Gateway | Custom gateway |
| 78 | Portkey | Gateway | `https://api.portkey.ai/v1` |
| 79 | LiteLLM | Gateway | `http://localhost:4000/v1` |
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
| 98 | 302.AI | Aggregator | `https://api.302.ai/v1` |
| 99 | Atomic Chat | Local | `http://127.0.0.1:1337/v1` |
| 100 | Azure Cognitive Services | Sovereign / Cloud | `https://<resource>.cognitiveservices.azure.com/openai/v1` |
| 101 | Cortecs | Gateway | `https://api.cortecs.ai/v1` |
| 102 | FrogBot | Aggregator | `https://app.frogbot.ai/api` |
| 103 | GitLab Duo | Sovereign / Cloud | `https://gitlab.com/api/v4/ai` |
| 104 | GitHub Copilot | Sovereign / Cloud | `https://api.githubcopilot.com` |
| 105 | Ollama Cloud | IaaS | `https://ollama.com/api` |
| 106 | OpenCode Zen | Gateway | `https://opencode.ai/zen/v1` |
| 107 | OpenCode Go | Gateway | `https://opencode.ai/zen/go/v1` |
| 108 | LLM Gateway | Gateway | `https://api.llmgateway.io/v1` |
| 109 | SAP AI Core | Sovereign / Cloud | `https://api.ai.<region>.<landscape>.ml.hana.ondemand.com/v2` |
| 110 | STACKIT AI Model Serving | Sovereign / Cloud | `https://api.openai-compat.model-serving.eu01.onstackit.cloud/v1` |
| 111 | Snowflake Cortex | Sovereign / Cloud | `https://<account>.snowflakecomputing.com/api/v2/cortex/v1` |
| 112 | ZenMux | Gateway | `https://zenmux.ai/api/v1` |
| 113 | Sakana AI (Fugu) | Gateway | `https://api.sakana.ai/v1` |
| 114 | Prism API | Gateway | `https://sub2api.558686.xyz/v1` |
| 115 | DiscountedTokens | Discount / Budget API | `https://discountedtokens.com/v1` |
| 116 | XiuRouter | Gateway | `https://router-api.xiu.ai/v1` |
| 117 | SAGG | Gateway | `https://api.privatedeskai.com/v1` |
| 118 | AIWave | Gateway | `https://aiwave.live/v1` |
| 119 | Devin CLI Agentic Bridge | No-auth | No-auth public endpoint |
| 120 | OpenCode Free | No-auth | `https://opencode.ai/zen/v1` |
| 121 | DuckDuckGo AI Chat | No-auth | `https://duck.ai/duckchat/v1/chat` |
| 122 | Cloudflare AI Playground | No-auth | `https://playground.ai.cloudflare.com` |
| 123 | Chipotle Pepper AI (Free) | No-auth | `https://amelia.chipotle.com` |
| 124 | Veo AI Free | Image / Video | `https://veoaifree.com/wp-admin/admin-ajax.php` |
| 125 | Augment (Auggie CLI) | No-auth | No-auth public endpoint |
| 126 | ZCode (GLM Coding Plan) | No-auth | No-auth public endpoint |
| 127 | OpenAI Codex (App-Server) | No-auth | No-auth public endpoint |
| 128 | UncloseAI | No-auth | `https://hermes.ai.unturf.com/v1` |
| 129 | AI Horde | No-auth | `https://oai.aihorde.net/v1` |
| 130 | GitHub Enterprise Copilot | OAuth | `https://api.githubcopilot.com` |
| 131 | xAI OAuth (Grok) | OAuth | OAuth (provider-specific) |
| 132 | Openference | OAuth | `https://api.openference.com/v1` |
| 133 | Grok Build | OAuth | `https://cli-chat-proxy.grok.com/v1` |
| 134 | Qoder | OAuth | `https://api.qoder.com/v1` |
| 135 | Antigravity CLI | OAuth | OAuth (provider-specific) |
| 136 | Kiro AI | OAuth | `https://codewhisperer.us-east-1.amazonaws.com/generateAssistantResponse` |
| 137 | Amazon Q | OAuth | OAuth (provider-specific) |
| 138 | Claude Code | OAuth | `https://api.anthropic.com/v1` |
| 139 | Antigravity | OAuth | OAuth (provider-specific) |
| 140 | OpenAI Codex | OAuth | `https://chatgpt.com/backend-api/codex` |
| 141 | Cursor IDE | OAuth | `https://api2.cursor.sh` |
| 142 | Zed IDE | OAuth | OAuth (provider-specific) |
| 143 | Zed Hosted Models | OAuth | `https://cloud.zed.dev` |
| 144 | Trae | OAuth | `https://core-normal.trae.ai/api/remote/v1` |
| 145 | Kimi Code CLI | OAuth | OAuth (provider-specific) |
| 146 | Kilo Code | OAuth | `https://api.kilo.ai/api/openrouter` |
| 147 | Cline | OAuth | `https://api.cline.bot/api/v1` |
| 148 | ClinePass | OAuth | `https://api.cline.bot/api/v1` |
| 149 | Devin Desktop | OAuth | `https://server.codeium.com` |
| 150 | Devin CLI | OAuth | OAuth (provider-specific) |
| 151 | CodeBuddy CN | OAuth | `https://copilot.tencent.com/v2` |
| 152 | ChatGPT Web (Clean Room) | Web Cookie | `https://chatgpt.com` |
| 153 | ChatGPT Web (Codex) | Web Cookie | `https://chatgpt.com` |
| 154 | Grok Web (Subscription) | Web Cookie | `https://grok.com/rest/app-chat/conversations/new` |
| 155 | Gemini Web (Free) | Web Cookie | `https://gemini.google.com/app` |
| 156 | Perplexity Web (Pro/Max) | Web Cookie | `https://www.perplexity.ai/rest/sse/perplexity_ask` |
| 157 | Blackbox Web (Subscription) | Web Cookie | `https://app.blackbox.ai/api/chat` |
| 158 | Muse Spark Web (Meta AI) | Web Cookie | `https://www.meta.ai/api/graphql` |
| 159 | Claude Web | Web Cookie | `https://claude.ai/api/organizations` |
| 160 | DeepSeek Web | Web Cookie | `https://chat.deepseek.com/api/v0/chat/completion` |
| 161 | Microsoft Copilot Web | Web Cookie | Web cookie / browser session |
| 162 | Microsoft 365 Copilot (BizChat) | Web Cookie | Web cookie / browser session |
| 163 | t3.chat (Pro/Free) | Web Cookie | `https://t3.chat/api/chat` |
| 164 | Inner.ai (Subscription) | Web Cookie | `https://chatapi.innerai.com/chat` |
| 165 | Adapta.org (Adapta One Web) | Web Cookie | `https://agent.adapta.one/api/chat/stream/v1` |
| 166 | Arena (Free) | Web Cookie | `https://arena.ai/nextjs-api/stream/create-evaluation` |
| 167 | Tencent Yuanbao (Free) | Web Cookie | `https://yuanbao.tencent.com/api/chat` |
| 168 | Tencent AI Studio (Free) | Web Cookie | `https://aistudio.tencent.ai/api/chat` |
| 169 | HuggingChat (Free) | Web Cookie | `https://huggingface.co/chat/conversation` |
| 170 | Poe Web (Subscription) | Web Cookie | Web cookie / browser session |
| 171 | Venice Web (Privacy) | Web Cookie | Web cookie / browser session |
| 172 | v0 Vercel Web (Code Gen) | Web Cookie | Web cookie / browser session |
| 173 | Kimi Web | Web Cookie | `https://www.kimi.ai` |
| 174 | Dola Web (ByteDance) | Web Cookie | `https://www.dola.com/chat/completion` |
| 175 | Gemini Business (Enterprise) | Web Cookie | `https://business.gemini.google/home` |
| 176 | ZenMux Free (Web) | Web Cookie | `https://zenmux.ai/api/anthropic/v1` |
| 177 | TinyCMS Web (Free/Sub) | Web Cookie | `https://gov.freegpt.win/api/openai/oneapi/v1` |
| 178 | Z.ai Web | Web Cookie | `https://chat.z.ai` |
| 179 | PromptQL (Unofficial/Experimental) | Web Cookie | `https://data.prompt.ql.app/promptql/playground-v2-hge/v1/graphql` |
| 180 | Notion AI Web (Unofficial/Experimental) | Web Cookie | `https://app.notion.com/api/v3/runInferenceTranscript` |
| 181 | Adobe Firefly (Image/Video) | Web Cookie | Web cookie / browser session |
| 182 | HyperAgent (Unofficial/Experimental) | Web Cookie | `https://hyperagent.com/api/threads` |
| 183 | Conol (Unofficial/Experimental) | Web Cookie | `https://conol.ai/api/sessions` |
| 184 | MaxAI | Web Cookie | `https://api.maxai.me` |
| 185 | UC (uncensored.com) | Web Cookie | `https://internal-6.pubyar.com` |
| 186 | MLX Gemma 26B | Local | `http://localhost:${MLX_GEMMA_PORT}/v1` |
| 187 | MLX Qwen 3.8 27B | Local | `http://localhost:${MLX_QWEN_PORT}/v1` |
| 188 | Lemonade Server | Local | `http://localhost:13305/api/v1` |
| 189 | Llamafile | Local | `http://127.0.0.1:8080/v1` |
| 190 | NVIDIA Triton | Local | `http://localhost:8000/v1` |
| 191 | Docker Model Runner | Local | `http://localhost:12434/v1` |
| 192 | XInference | Local | `http://localhost:9997/v1` |
| 193 | oobabooga | Local | `http://localhost:5000/v1` |
| 194 | SD WebUI | Local | `http://localhost:7860` |
| 195 | ComfyUI | Local | `http://localhost:8188` |
| 196 | Perplexity Search | Search | `https://api.perplexity.ai` |
| 197 | Serper Search | Search | `https://google.serper.dev` |
| 198 | Brave Search | Search | `https://api.search.brave.com/res/v1` |
| 199 | Exa Search | Search | `https://api.exa.ai` |
| 200 | Tavily Search | Search | `https://api.tavily.com` |
| 201 | AnySearch | Search | `https://api.anysearch.com` |
| 202 | Firecrawl | Search | `https://api.firecrawl.dev/v1` |
| 203 | Google Programmable Search | Search | `https://www.googleapis.com/customsearch/v1` |
| 204 | Nimble Search | Search | `https://api.webit.live` |
| 205 | Linkup Search | Search | `https://api.linkup.so` |
| 206 | SearchAPI | Search | `https://www.searchapi.io/api/v1/search` |
| 207 | You.com Search | Search | `https://api.ydc-index.io` |
| 208 | SearXNG Search | Search | `http://localhost:8080` |
| 209 | X Search (Grok) | Search | `https://api.x.ai/v1` |
| 210 | Xquik X Search | Search | `https://api.xquik.com` |
| 211 | Ollama Search | Search | `https://ollama.com/api` |
| 212 | Context7 (library docs) | Search | `https://context7.com` |
| 213 | Deepgram | Audio | `https://api.deepgram.com/v1` |
| 214 | AssemblyAI | Audio | `https://api.assemblyai.com/v2` |
| 215 | Soniox | Audio | `https://api.soniox.com` |
| 216 | ElevenLabs | Audio | `https://api.elevenlabs.io/v1` |
| 217 | Cartesia | Audio | `https://api.cartesia.ai` |
| 218 | Fish Audio | Audio | `https://api.fish.audio` |
| 219 | PlayHT | Audio | `https://api.play.ht/api/v2` |
| 220 | Inworld | Audio | `https://api.inworld.ai` |
| 221 | AWS Polly | Audio | `https://polly.us-east-1.amazonaws.com` |
| 222 | Gladia | Audio | `https://api.gladia.io/v2` |
| 223 | Rev AI | Audio | `https://api.rev.ai` |
| 224 | Speechmatics | Audio | `https://asr.api.speechmatics.com/v2` |
| 225 | Google Jules | Cloud Agent | `https://jules.google` |
| 226 | Devin | Cloud Agent | `https://api.devin.ai` |
| 227 | Codex Cloud | Cloud Agent | `https://chatgpt.com/backend-api/codex` |
| 228 | CLIProxyAPI | Gateway | `http://localhost:8317/v1` |
| 229 | 9router | Gateway | `http://localhost:20130/v1` |
| 230 | Pioneer AI | Frontier | `https://api.pioneer.ai/v1` |
| 231 | UC Direct (uncensored.com) | Frontier | `https://api.uncensored.com/api/v1` |
| 232 | Blackbox AI | Frontier | `https://api.blackbox.ai/v1` |
| 233 | Perplexity Agent | Frontier | `https://api.perplexity.ai/v1` |
| 234 | Meta Llama API | Frontier | `https://api.llama.com/compat/v1` |
| 235 | Galadriel | Frontier | `https://api.galadriel.ai/v1` |
| 236 | Codestral | Frontier | `https://codestral.mistral.ai/v1` |
| 237 | Maritalk | Frontier | `https://chat.maritaca.ai/api` |
| 238 | Nous Research | Frontier | `https://inference-api.nousresearch.com/v1` |
| 239 | Writer | Frontier | `https://api.writer.com/v1` |
| 240 | Muse Code (Meta) | Frontier | `https://llama-stack.readthedocs.io` |
| 241 | OpenVecta | IaaS | `https://api.openvecta.com/v1` |
| 242 | Openference API | IaaS | `https://api.openference.com/v1` |
| 243 | Nube.sh | IaaS | `https://ai.nube.sh/api/v1` |
| 244 | Lambda AI | IaaS | `https://api.lambda.ai/v1` |
| 245 | nScale | IaaS | `https://inference.api.nscale.com/v1` |
| 246 | PublicAI | IaaS | `https://api.publicai.co/v1` |
| 247 | Featherless AI | IaaS | `https://api.featherless.ai/v1` |
| 248 | Predibase | IaaS | `https://serving.app.predibase.com/v1` |
| 249 | Bytez | IaaS | `https://api.bytez.com/models/v2/openai/v1` |
| 250 | MonsterAPI | IaaS | `https://api.monsterapi.ai/v1` |
| 251 | ModelScope | IaaS | `https://api-inference.modelscope.cn/v1` |
| 252 | BytePlus ModelArk | IaaS | `https://ark.ap-southeast.bytepluses.com/api/v3` |
| 253 | 1min.AI | Gateway | `https://api.1min.ai/api/chat-with-ai` |
| 254 | Cheaper Inference | Gateway | `https://api.cheaperinference.com/v1` |
| 255 | Freebuff | Gateway | `https://www.codebuff.com/api/v1` |
| 256 | Charm Hyper | Gateway | `https://hyper.charm.land/v1` |
| 257 | AgentRouter | Gateway | `https://agentrouter.org/v1` |
| 258 | UnoRouter | Gateway | `https://api.unorouter.com/v1` |
| 259 | Command Code | Gateway | `https://api.commandcode.ai` |
| 260 | Zylo API | Gateway | `https://api.zyloai.net/v1` |
| 261 | FastRouter | Gateway | `https://api.fastrouter.ai/api/v1` |
| 262 | AnyAPI AI | Aggregator | `https://api.anyapi.ai/v1` |
| 263 | Electron Hub | Aggregator | `https://api.electronhub.ai/v1` |
| 264 | LLM.Kiwi | Gateway | `https://api.llm.kiwi/v1` |
| 265 | LiteRouter | Gateway | `https://api.literouter.com/v1` |
| 266 | GreenPT | Gateway | `https://api.greenpt.ai/v1` |
| 267 | EURouter | Gateway | `https://api.eurouter.ai/v1` |
| 268 | MNN AI | Gateway | `https://api.mnnai.ru/v1` |
| 269 | MegaNova AI | Gateway | `https://api.meganova.ai/v1` |
| 270 | Mixlayer | Gateway | `https://models.mixlayer.ai/v1` |
| 271 | Speka AI | Gateway | `https://speka.me/v1` |
| 272 | TokenReply | Gateway | `https://api.tokenreply.com/v1` |
| 273 | Yolo-Auto | Gateway | `https://yolo-auto.com/v1` |
| 274 | DXNT / DX Token | Gateway | `https://www.dxnt.com/v1` |
| 275 | CloudCode.ONE | Gateway | `https://api.cloudcode.one/v1` |
| 276 | OfoxAI | Gateway | `https://api.ofox.ai/v1` |
| 277 | ZeroLimitAI | Gateway | `https://www.zerolimitai.com/api/v1` |
| 278 | ChatAnywhere | Aggregator | `https://api.chatanywhere.org/v1` |
| 279 | Helyx AI | Gateway | `https://helyxai.space/v1` |
| 280 | Auriko | Gateway | `https://api.auriko.ai/v1` |
| 281 | Poixe AI | Gateway | `https://api.poixe.com/v1` |
| 282 | Naga AI | Aggregator | `https://api.naga.ac/v1` |
| 283 | Chat Oripe | Gateway | `https://api.oriper.com/v1` |
| 284 | FreeInference | Gateway | `https://freeinference.org/v1` |
| 285 | Free.ai | Gateway | `https://api.free.ai/v1/chat` |
| 286 | DGrid | Gateway | `https://api.dgrid.ai/v1` |
| 287 | Qiniu | Gateway | `https://api.qnaigc.com/v1` |
| 288 | OrcaRouter | Gateway | `https://api.orcarouter.ai/v1` |
| 289 | Api.airforce | Gateway | `https://api.airforce/v1` |
| 290 | CrofAI | Gateway | `https://crof.ai/v1` |
| 291 | BazaarLink | Gateway | `https://bazaarlink.ai/api/v1` |
| 292 | Synthetic | Gateway | `https://api.synthetic.new/openai/v1` |
| 293 | Kilo Gateway | Gateway | `https://api.kilo.ai/api/gateway` |
| 294 | Dahl | Gateway | `https://inference.dahl.global/v1` |
| 295 | FreeTheAi | Gateway | `https://api.freetheai.xyz/v1` |
| 296 | g4f.space — Groq | Gateway | `https://g4f.space/api/groq/v1` |
| 297 | g4f.space — Gemini | Gateway | `https://g4f.space/api/gemini/v1` |
| 298 | g4f.space — Pollinations | Gateway | `https://g4f.space/api/pollinations/v1` |
| 299 | g4f.space — Ollama | Gateway | `https://g4f.space/api/ollama/v1` |
| 300 | g4f.space — NVIDIA | Gateway | `https://g4f.space/api/nvidia/v1` |
| 301 | LLM7.io | Gateway | `https://api.llm7.io/v1` |
| 302 | LlamaGate | Gateway | `https://llamagate.ai/v1` |
| 303 | Gitlawb Opengateway (MiMo) | Gateway | `https://opengateway.gitlawb.com/v1/xiaomi-mimo` |
| 304 | Gitlawb Opengateway (GMI Cloud) | Gateway | `https://opengateway.gitlawb.com/v1/gmi-cloud` |
| 305 | NanoGPT | Gateway | `https://nano-gpt.com/api/v1` |
| 306 | PiAPI | Aggregator | `https://api.piapi.ai` |
| 307 | GoAPI | Aggregator | `https://api.getgoapi.com/v1` |
| 308 | LaoZhang AI | Gateway | `https://api.laozhang.ai/v1` |
| 309 | TheB.AI | Aggregator | `https://api.theb.ai/v1` |
| 310 | b.ai | Gateway | `https://api.b.ai/v1` |
| 311 | FenayAI | Gateway | `https://api.fenayai.com/v1` |
| 312 | Empower | Gateway | `https://api.empower.dev/v1` |
| 313 | Poe | Aggregator | `https://api.poe.com` |
| 314 | Factory | Gateway | `https://api.factory.ai/v1` |
| 315 | BluesMinds | Gateway | `https://api.bluesminds.com/v1` |
| 316 | FreeModel.dev | Gateway | `https://api.freemodel.dev/v1` |
| 317 | FreeAIAPIKey | Gateway | `https://api.freeaiapikey.com/v1` |
| 318 | OpenAdapter | Gateway | `https://api.openadapter.in/v1` |
| 319 | DIT.ai | Gateway | `https://api.dit.ai/v1` |
| 320 | TokenRouter | Gateway | `https://api.tokenrouter.com/v1` |
| 321 | Token Kiosk | Gateway | `https://agent-router.gaib.ai/v1` |
| 322 | SumoPod | Gateway | `https://ai.sumopod.com/v1` |
| 323 | X5Lab | Gateway | `https://api.x5lab.dev/v1` |
| 324 | Chenzk API | Gateway | `https://chenzk.top/v1` |
| 325 | Kenari | Gateway | `https://kenari.id/v1` |
| 326 | NavyAI | Gateway | `https://api.navy/v1` |
| 327 | AINative Studio | Gateway | `https://api.ainative.studio/api/v1` |
| 328 | Routeway | Gateway | `https://api.routeway.ai/v1` |
| 329 | NaraRouter | Gateway | `https://router.bynara.id/v1` |
| 330 | Regolo AI | Gateway | `https://api.regolo.ai` |
| 331 | Naga.ac | Aggregator | `https://api.naga.ac/v1` |
| 332 | Void AI | Gateway | `https://api.voidai.app/v1` |
| 333 | HelixMind | Gateway | `https://helixmind.online/v1` |
| 334 | Logfare | Gateway | `https://logfare.ai/v1` |
| 335 | TabiToken | Gateway | `https://tabitoken.com/v1` |
| 336 | SeekAi | Gateway | `https://seekai.cc/v1` |
| 337 | IBM watsonx.ai Gateway | Sovereign / Cloud | `https://us-south.ml.cloud.ibm.com/ml/v1` |
| 338 | OCI Generative AI | Sovereign / Cloud | `https://inference.generativeai.us-chicago-1.oci.oraclecloud.com` |
| 339 | Vertex AI Partners | Sovereign / Cloud | `https://us-central1-aiplatform.googleapis.com/v1/projects` |
| 340 | Heroku AI | Sovereign / Cloud | `https://us.inference.heroku.com/v1` |
| 341 | Databricks | Sovereign / Cloud | `https://adb-0000000000000000.0.azuredatabricks.net/serving-endpoints` |
| 342 | DataRobot | Sovereign / Cloud | `https://app.datarobot.com/api/v2` |
| 343 | GLM Coding | Frontier | `https://api.z.ai/api/coding/paas/v4` |
| 344 | GLM Coding (China) | Frontier | `https://open.bigmodel.cn/api/coding/paas/v4` |
| 345 | GLM Thinking | Frontier | `https://api.z.ai/api/coding/paas/v4` |
| 346 | Alibaba Token Plan | Frontier | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic/v1` |
| 347 | Qwen Cloud | Frontier | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| 348 | Qwen Cloud Token Plan | Frontier | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` |
| 349 | Kimi Code API Key | Frontier | `https://api.kimi.com/coding/v1` |
| 350 | Minimax (China) | Frontier | `https://api.minimaxi.com/v1` |
| 351 | Alibaba (China) | Frontier | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| 352 | LongCat AI | Frontier | `https://api.longcat.chat/openai/v1` |
| 353 | Volcengine | Frontier | `https://ark.cn-beijing.volces.com/api/v3` |
| 354 | Volcengine Ark Agent Plan | Frontier | `https://ark.cn-beijing.volces.com/api/plan/v3` |
| 355 | Volcengine Ark Coding Plan | Frontier | `https://ark.cn-beijing.volces.com/api/coding/v3` |
| 356 | GigaChat (Sber) | Frontier | `https://gigachat.devices.sberbank.ru/api/v1` |
| 357 | Xiaomi MiMo Token Plan | Frontier | `https://token-plan-sgp.xiaomimimo.com/v1` |
| 358 | Tencent Hunyuan | Frontier | `https://api.hunyuan.cloud.tencent.com/v1` |
| 359 | iFlytek Spark | Frontier | `https://spark-api-open.xf-yun.com/v1` |
| 360 | Baichuan | Frontier | `https://api.baichuan-ai.com/v1` |
| 361 | Yi (01.AI) | Frontier | `https://api.lingyiwanwu.com/v1` |
| 362 | 360 AI | Frontier | `https://api.360.cn/v1` |
| 363 | Doubao | Frontier | `https://ark.cn-beijing.volces.com/api/v3` |
| 364 | SenseNova | Frontier | `https://token.sensenova.cn/v1` |
| 365 | SparkDesk | Frontier | `https://spark-api-open.xf-yun.com/v1` |
| 366 | Huancheng Public API | Frontier | `https://api.hcnsec.cn/v1` |
| 367 | Agnes AI | Image / Video | `https://apihub.agnes-ai.com/v1` |
| 368 | SEA-LION | Frontier | `https://api.sea-lion.ai/v1` |
| 369 | Naver CLOVA Studio | Frontier | `https://clovastudio.stream.ntruss.com/v3/chat-completions` |
| 370 | InternLM (Intern-S1) | Frontier | `https://chat.intern-ai.org.cn/api/v1` |
| 371 | Ant Ling / Ring (inclusionAI) | Frontier | `https://api.ant-ling.com/v1` |
| 372 | Sarvam AI | Frontier | `https://api.sarvam.ai/v1` |
| 373 | PLaMo | Frontier | `https://api.platform.preferredai.jp/v1` |
| 374 | Typhoon | Frontier | `https://api.opentyphoon.ai/v1` |
| 375 | Runway | Image / Video | `https://api.dev.runwayml.com/v1` |
| 376 | KIE.AI | Image / Video | `https://api.kie.ai/v1` |
| 377 | Pollinations AI | Specialized | `https://gen.pollinations.ai/v1` |
| 378 | Haiper | Image / Video | `https://api.haiper.ai/v1` |
| 379 | Leonardo AI | Image / Video | `https://cloud.leonardo.ai/api/rest/v1` |
| 380 | Ideogram | Image / Video | `https://api.ideogram.ai` |
| 381 | Magnific | Image / Video | `https://api.magnific.com/v1/ai/mystic` |
| 382 | Suno | Image / Video | `https://studio-api.suno.ai/api/generate/v2` |
| 383 | Udio | Image / Video | `https://www.udio.com/api/generate-proxy` |
| 384 | v0 (Vercel) | Specialized | `https://api.v0.dev/v1` |
| 385 | GitLab Duo PAT | Specialized | `https://gitlab.com/api/v4/ai` |
| 386 | Jina AI (Foundation API) | Embeddings | `https://api.jina.ai/v1` |
| 387 | Fal.ai | Image / Video | `https://fal.run` |
| 388 | Stability AI | Image / Video | `https://api.stability.ai` |
| 389 | Black Forest Labs | Image / Video | `https://api.bfl.ai` |
| 390 | Recraft | Image / Video | `https://external.api.recraft.ai/v1` |
| 391 | Topaz | Image / Video | `https://api.topazlabs.com` |
| 392 | Segmind | Image / Video | `https://api.segmind.com/v1` |
| 393 | Dify | Specialized | `https://api.dify.ai` |
| 394 | Nomic | Embeddings | `https://api-atlas.nomic.ai/v1` |
| 395 | Mixedbread AI | Embeddings | `https://api.mixedbread.com/v1` |
| 396 | Jina Reader (r.jina.ai) | Search | `https://r.jina.ai` |
| 397 | TinyFish Fetch | Search | `https://api.tinyfish.ai` |
| 398 | DeepAI | Image / Video | `https://api.deepai.org` |
| 399 | Cursor API | Specialized | `https://api.cursor.com/v1` |
| 400 | OmniRoute | Gateway | `http://localhost:3000/v1` |
| 401 | Bifrost | Gateway | `http://localhost:8080/v1` |
| 402 | Dasha Compute | Sovereign / Cloud | Open alpha |

---

## How Providers Are Organized

```
┌─────────────────────────────────────────┐
│     Your App (OpenAI / Anthropic SDK)   │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ Gateways (OpenRouter, OmniRoute, Portkey)│  ← optional routing layer
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

| Category | Count |
|----------|-------|
| **Official Frontier Model Developers** | 60 |
| **High-Performance Inference Platforms** | 39 |
| **Decentralized, Sovereign & Enterprise Clouds** | 36 |
| **Multi-Provider Gateways & Routers** | 106 |
| **Aggregators & API Marketplaces** | 15 |
| **Discount & Budget APIs** | 1 |
| **OAuth & IDE Subscriptions** | 22 |
| **Web Cookie / Browser Sessions** | 34 |
| **No-auth & Public Endpoints** | 10 |
| **Search APIs** | 19 |
| **Audio** | 12 |
| **Image & Video APIs** | 17 |
| **Cloud Coding Agents** | 3 |
| **Embeddings & Rerankers** | 4 |
| **Other Specialized APIs** | 7 |
| **Local & Self-Hosted Runtimes** | 17 |
| **Total** | **402** |

---

## Official Frontier Model Developers

Companies that train and ship their own foundation models.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **OpenAI** | [platform.openai.com](https://platform.openai.com) | `https://api.openai.com/v1` | GPT-5.5, GPT-5.4, GPT-4.1, GPT-4o | Industry-standard SDK ecosystem |
| **Anthropic** | [www.anthropic.com](https://www.anthropic.com) | `https://api.anthropic.com` | Claude Opus 4.8, Claude Sonnet 4.6, Claude Haiku 4.5 | Native Messages API (not OpenAI-compatible) |
| **Google AI Studio** | [aistudio.google.com](https://aistudio.google.com) | `https://generativelanguage.googleapis.com` | Gemini 3.5, Gemini 3.1, Gemini 2.5 | Up to 2M context; free tier on Flash variants |
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | `https://api.deepseek.com/v1` | DeepSeek-V4-Pro, DeepSeek-V4-Flash, DeepSeek-R1 | OpenAI + Anthropic format; context caching |
| **Mistral AI** | [console.mistral.ai](https://console.mistral.ai) | `https://api.mistral.ai/v1` | Mistral Medium 3.5, Mistral Small 4, Ministral 3 | EU-hosted; generous experiment tier |
| **xAI** | [x.ai](https://x.ai) | `https://api.x.ai/v1` | Grok-3, Grok-2 | Real-time streaming & agent workflows |
| **Cohere** | [cohere.com](https://cohere.com) | `https://api.cohere.com/v2` | Command R+, Embed v4, Rerank 3.5 | Enterprise search & RAG |
| **AI21 Labs** | [studio.ai21.com](https://studio.ai21.com) | `https://api.ai21.com/studio/v1` | Jamba 1.5 Large, Jamba 1.5 Mini | Long-context hybrid architecture |
| **Baidu Qianfan** | [cloud.baidu.com](https://cloud.baidu.com/product/wenxinworkshop) | `https://api.baiduqianfan.ai/v1` | ERNIE 4.0 Turbo, ERNIE Speed, ERNIE Lite | Chinese-language optimized |
| **StepFun** | [platform.stepfun.com](https://platform.stepfun.com) | `https://api.stepfun.com/v1` | Step 3.5 Flash, Step-series | Multilingual agent pipelines |
| **Z.ai (Zhipu AI)** | [open.bigmodel.cn](https://open.bigmodel.cn) | `https://open.bigmodel.cn/api/paas/v4/` | GLM-5, GLM-4.7, GLM-4.7-Flash | Strong bilingual CN/EN performance |
| **Xiaomi** | [xiaomi.com](https://xiaomi.com) | `https://api.xiaomimimo.com/v1` | Mimo-v2-pro | On-device & edge deployments |
| **Reka AI** | [reka.ai](https://reka.ai) | `https://api.reka.ai/v1` | Reka Core, Reka Flash | Video, audio & text multimodal |
| **Inflection** | [inflection.ai](https://inflection.ai) | Custom webhooks | Pi-series | Conversational assistant focus |
| **MiniMax** | [platform.minimax.io](https://platform.minimax.io) | `https://api.minimax.io/v1` | MiniMax-M3, MiniMax-M2.1, MiniMax-M2 | OpenAI + Anthropic compatible; agentic |
| **Alibaba DashScope** | [www.alibabacloud.com](https://www.alibabacloud.com) | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | qwen3-max, Qwen-Plus, Qwen-Flash | Alibaba Cloud Model Studio; Qwen family |
| **Upstage** | [console.upstage.ai](https://console.upstage.ai) | `https://api.upstage.ai/v1/solar` | Solar Pro 3, Solar Mini | Korean AI lab; strong document AI |
| **Perplexity** | [docs.perplexity.ai](https://docs.perplexity.ai) | `https://api.perplexity.ai` | Sonar, Sonar Pro, Sonar Reasoning | Search-grounded answers with citations |
| **Pioneer AI** | [pioneer.ai](https://pioneer.ai) | `https://api.pioneer.ai/v1` | Qwen/Qwen3-32B, Qwen/Qwen3.6-27B, Qwen/Qwen3.5-9B, Qwen/Qwen3-8B | $75 free usage credits — no credit card required; Pioneer AI by Fastino Labs. Free $75 usage credits, no credit card required. Use API key auth with a pio_sk_... key. Only open-tier models (Qwen3, Llama, Gemma, SmolLM) work directly — gated models (Claude/GPT/Gemini) require prior fine-tuning via the Pioneer platform. |
| **UC Direct (uncensored.com)** | [uncensored.com](https://uncensored.com) | `https://api.uncensored.com/api/v1` | claude-opus-5, claude-opus-5-fast, claude-fable-5, claude-opus-4.8 | Use your uncensored.com Developer API key (uai_sk_live_...). OmniRoute sends it as the X-api-key header to the OpenAI-compatible https://api.uncensored.com/api/v1 endpoint. The key never expires. This is the metered/credits surface; the un-metered subscription chat is the separate 'uc' provider.; UC Direct is OpenAI-compatible on /api/v1. OmniRoute probes /api/v1/models (public) and routes chat traffic to /api/v1/… |
| **Blackbox AI** | [blackbox.ai](https://blackbox.ai) | `https://api.blackbox.ai/v1` | claude-fable-5, claude-opus-4.8, claude-sonnet-5, claude-sonnet-4.6 | Limited free access is available through Blackbox; model availability and account limits apply |
| **Perplexity Agent** | [www.perplexity.ai](https://www.perplexity.ai) | `https://api.perplexity.ai/v1` | openai/gpt-5.6-sol, perplexity/kimi-k3 | Use your Perplexity API key. OmniRoute routes Agent API model IDs through Perplexity's Responses-compatible endpoint.; Use Agent API model IDs with the pplx-agent/ prefix, for example pplx-agent/openai/gpt-5.6-sol or pplx-agent/anthropic/claude-opus-4-5. |
| **Meta Llama API** | [llama.developer.meta.com](https://llama.developer.meta.com) | `https://api.llama.com/compat/v1` | — | First-party model lab API. |
| **Galadriel** | [galadriel.com](https://galadriel.com) | `https://api.galadriel.ai/v1` | — | First-party model lab API. |
| **Codestral** | [mistral.ai](https://mistral.ai) | `https://codestral.mistral.ai/v1` | — | First-party model lab API. |
| **Maritalk** | [www.maritaca.ai](https://www.maritaca.ai) | `https://chat.maritaca.ai/api` | — | First-party model lab API. |
| **Nous Research** | [portal.nousresearch.com](https://portal.nousresearch.com/help) | `https://inference-api.nousresearch.com/v1` | Hermes-4-405B, Hermes-4-70B | Free tier: 50 RPM, 500,000 TPM — no credit card; Use your Nous Portal API key. OmniRoute targets the official OpenAI-compatible inference endpoint at https://inference-api.nousresearch.com/v1.; Nous exposes an OpenAI-compatible /v1 surface with a large remote /models catalog. The /chat/completions endpoint requires a valid API key for programmatic inference. |
| **Writer** | [dev.writer.com](https://dev.writer.com) | `https://api.writer.com/v1` | palmyra-x5, palmyra-x4 | Writer Palmyra is OpenAI-compatible at https://api.writer.com/v1. palmyra-x5 offers a 1M-token context window. |
| **Muse Code (Meta)** | [github.com](https://github.com/meta-llama/llama-stack) | `https://llama-stack.readthedocs.io` | llama-4-maverick, llama-4-scout, llama-3.3-70b, llama-3.1-405b | Use your META_API_KEY env var as a Bearer token. Muse Code CLI uses the OpenAI Responses API wire format (POST /responses).; Muse Code is OpenAI-compatible. OmniRoute routes chat traffic through the Responses API and exposes the proprietary model catalog at /v1/muse-code/models. |
| **GLM Coding** | [z.ai](https://z.ai/subscribe) | `https://api.z.ai/api/coding/paas/v4` | glm-5.3-flash, glm-5.3, glm-5.3-high, glm-5.3-low | First-party model lab API. |
| **GLM Coding (China)** | [open.bigmodel.cn](https://open.bigmodel.cn) | `https://open.bigmodel.cn/api/coding/paas/v4` | glm-5.3-flash, glm-5.3, glm-5.3-high, glm-5.3-low | First-party model lab API. |
| **GLM Thinking** | [open.bigmodel.cn](https://open.bigmodel.cn) | `https://api.z.ai/api/coding/paas/v4` | glm-5.3-flash, glm-5.3, glm-5.3-high, glm-5.3-low | Preset GLM profile with higher token budget, thinking enabled, and longer timeout. |
| **Alibaba Token Plan** | [www.alibabacloud.com](https://www.alibabacloud.com/help/en/model-studio/token-plan-overview) | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic/v1` | qwen3.8-max-preview, qwen3.7-max, qwen3.7-plus, qwen3.6-flash | Use an Alibaba Token Plan key and select its Singapore or Beijing region. |
| **Qwen Cloud** | [www.qwencloud.com](https://www.qwencloud.com) | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | qwen3.8-max, qwen3.7-max-2026-06-08, qwen3.7-plus, qwen3.6-plus | Use a Qwen Cloud API key and select its Global or Beijing region. |
| **Qwen Cloud Token Plan** | [www.qwencloud.com](https://www.qwencloud.com/pricing/token-plan) | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` | qwen3.8-max, qwen3.7-max, qwen3.7-plus, qwen3.6-flash | Use a Qwen Cloud Token Plan key and select its Singapore or Beijing region. |
| **Kimi Code API Key** | [www.kimi.com](https://www.kimi.com/code) | `https://api.kimi.com/coding/v1` | — | First-party model lab API. |
| **Minimax (China)** | [www.minimaxi.com](https://www.minimaxi.com) | `https://api.minimaxi.com/v1` | MiniMax-M3, MiniMax-M2.7, MiniMax-M2.7-highspeed, MiniMax-M2.5 | First-party model lab API. |
| **Alibaba (China)** | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) | `https://dashscope.aliyuncs.com/compatible-mode/v1` | — | First-party model lab API. |
| **LongCat AI** | [longcat.chat](https://longcat.chat/platform/docs) | `https://api.longcat.chat/openai/v1` | LongCat-2.0 | Free: one-time 10M-token grant after account signup + KYC verification (LongCat-2.0). One-time only — not a recurring daily/monthly allowance. |
| **Volcengine** | [www.volcengine.com](https://www.volcengine.com) | `https://ark.cn-beijing.volces.com/api/v3` | — | First-party model lab API. |
| **Volcengine Ark Agent Plan** | [console.volcengine.com](https://console.volcengine.com/ark/region:cn-beijing/subscription/agent-plan) | `https://ark.cn-beijing.volces.com/api/plan/v3` | doubao-seed-evolving, doubao-seed-2-1-turbo-260628, doubao-seed-2-0-lite-260215, doubao-seed-2-0-mini-260215 | Connect your Volcano Engine account or use an Ark Agent Plan subscription API key. |
| **Volcengine Ark Coding Plan** | [console.volcengine.com](https://console.volcengine.com/ark/region:cn-beijing/subscription/coding-plan) | `https://ark.cn-beijing.volces.com/api/coding/v3` | doubao-seed-2-1-turbo, doubao-seed-2.0-lite, deepseek-v4-flash, glm-5.2 | Connect your Volcano Engine account or use an Ark Coding Plan subscription API key. |
| **GigaChat (Sber)** | [developers.sber.ru](https://developers.sber.ru) | `https://gigachat.devices.sberbank.ru/api/v1` | — | First-party model lab API. |
| **Xiaomi MiMo Token Plan** | [mimo.mi.com](https://mimo.mi.com) | `https://token-plan-sgp.xiaomimimo.com/v1` | mimo-v2.5-pro, mimo-v2.5 | First-party model lab API. |
| **Tencent Hunyuan** | [hunyuan.tencent.com](https://hunyuan.tencent.com) | `https://api.hunyuan.cloud.tencent.com/v1` | hunyuan-turbos-latest, hunyuan-t1-latest, hunyuan-pro, hunyuan-vision | Free Hunyuan Lite models. WeChat ecosystem.; Get API key at console.cloud.tencent.com |
| **iFlytek Spark** | [xinghuo.xfyun.cn](https://xinghuo.xfyun.cn) | `https://spark-api-open.xf-yun.com/v1` | 4.0Ultra, generalv3.5, max-32k, generalv3 | Spark Lite is free (2 QPS rate-limited), but iFlytek ToS §2.4(3) prohibits programmatic extraction and requires Chinese real-name auth — use with caution.; Get API key at console.xfyun.cn |
| **Baichuan** | [www.baichuan-ai.com](https://www.baichuan-ai.com) | `https://api.baichuan-ai.com/v1` | Baichuan4-Turbo, Baichuan4-Air, Baichuan4, Baichuan3-Turbo | Free Baichuan models. Popular Chinese LLM startup.; Get API key at platform.baichuan-ai.com |
| **Yi (01.AI)** | [01.ai](https://01.ai) | `https://api.lingyiwanwu.com/v1` | yi-large | No free API tier (2026) — Yi-Light retired; platform.01.ai is pay-as-you-go (Yi-Lightning paid). Open weights are download-only.; Get API key at platform.lingyiwanwu.com |
| **360 AI** | [ai.360.cn](https://ai.360.cn) | `https://api.360.cn/v1` | — | Free 360 AI Brain models. Major Chinese security company.; Get API key at ai.360.cn |
| **Doubao** | [doubao.com](https://doubao.com) | `https://ark.cn-beijing.volces.com/api/v3` | doubao-seed-2-0-pro-260215, doubao-seed-2-0-lite-260215, doubao-seed-2-0-mini-260215, doubao-seed-2-0-code-preview-260215 | Free Doubao models. ByteDance's chatbot.; Get API key at console.volcengine.com |
| **SenseNova** | [platform.sensenova.cn](https://platform.sensenova.cn) | `https://token.sensenova.cn/v1` | sensenova-6.7-flash-lite, deepseek-v4-flash, glm-5.2 | Free SenseTime models. Computer vision leader.; Get API key at platform.sensenova.cn; SenseNova registration appears to require a Chinese (+86) phone number for SMS verification — no international sign-up path is documented, so users outside mainland China may be unable to obtain an API key. |
| **SparkDesk** | [xinghuo.xfyun.cn](https://xinghuo.xfyun.cn) | `https://spark-api-open.xf-yun.com/v1` | 4.0Ultra, generalv3, pro-128k, lite | Spark Lite free (alias for iflytek), but ToS restricts to personal/non-commercial use and prohibits relaying access to third parties — use with caution.; Get API key at console.xfyun.cn |
| **Huancheng Public API** | [api.hcnsec.cn](https://api.hcnsec.cn) | `https://api.hcnsec.cn/v1` | — | Xinjiang Huancheng Cybersecurity public LLM API platform: free credits with daily check-ins.; Get API key at api.hcnsec.cn |
| **SEA-LION** | [sea-lion.ai](https://sea-lion.ai) | `https://api.sea-lion.ai/v1` | aisingapore/Llama-SEA-LION-v3.5-70B-R, aisingapore/Llama-SEA-LION-v3-70B-IT, aisingapore/Gemma-SEA-LION-v4-27B-IT, aisingapore/Qwen-SEA-LION-v4.5-27B-IT | Permanently free at 10 RPM — AI Singapore's Southeast-Asian models (Llama/Qwen/Gemma SEA-LION).; Sign in at sea-lion.ai with Google (no card, no region wall), create an API key, then paste it here. |
| **Naver CLOVA Studio** | [api.ncloud-docs.com](https://api.ncloud-docs.com/docs/en/ai-naver-clovastudio-summary) | `https://clovastudio.stream.ntruss.com/v3/chat-completions` | HCX-007, HCX-005, HCX-DASH-002 | OmniRoute routes chat traffic to the native Chat Completions v3 API (/v3/chat-completions/{model}), not the OpenAI-compatibility shim. All three v3 models are served: HCX-007 (reasoning, text only), HCX-005 (vision — accepts both public image URLs and inline base64 images), and HCX-DASH-002 (lightweight, text only). Requests stream upstream and are accumulated into a JSON body when the client asks for a non-stream… |
| **InternLM (Intern-S1)** | [internlm.intern-ai.org.cn](https://internlm.intern-ai.org.cn) | `https://chat.intern-ai.org.cn/api/v1` | intern-s1-pro, intern-s1, intern-s1-mini, internvl3.5-latest | Free monthly quota ~1M input / 3M output tokens (~10 RPM) |
| **Ant Ling / Ring (inclusionAI)** | [developer.ant-ling.com](https://developer.ant-ling.com/en/docs) | `https://api.ant-ling.com/v1` | Ling-2.6-1T, Ring-2.6-1T, Ling-2.6-flash | 500,000 free tokens per day per account (resets 02:00 UTC+8, no rollover); Register and create an API key at the Ant Ling API console (https://chat.ant-ling.com/open), then paste it here. OmniRoute routes chat traffic to https://api.ant-ling.com/v1/chat/completions; the provider is OpenAI-compatible and also exposes an Anthropic-compatible surface. |
| **Sarvam AI** | [docs.sarvam.ai](https://docs.sarvam.ai) | `https://api.sarvam.ai/v1` | sarvam-105b, sarvam-30b | ₹1,000 in free signup credits — never expire; Sarvam AI is OpenAI-compatible on /v1. OmniRoute probes /v1/models and routes chat traffic to /v1/chat/completions. Models are tuned for Indic languages. |
| **PLaMo** | [plamo.preferredai.jp](https://plamo.preferredai.jp/api) | `https://api.platform.preferredai.jp/v1` | plamo-3.0-prime | PLaMo is OpenAI-compatible at https://api.platform.preferredai.jp/v1. Built by Preferred Networks and optimized for Japanese. Docs are primarily in Japanese. |
| **Typhoon** | [docs.opentyphoon.ai](https://docs.opentyphoon.ai) | `https://api.opentyphoon.ai/v1` | typhoon-v2.5-30b-a3b-instruct | Free API key with a 5 req/s and 200 req/m rate limit.; Typhoon is OpenAI-compatible on /v1. Built by SCB 10X (Thailand); typhoon-v2.5-30b-a3b-instruct is a thai-first, multilingual model. |

## High-Performance Inference Platforms (IaaS)

Hosted open-weight models on optimized hardware — great for **low latency** and **low cost per token**.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Groq** | [console.groq.com](https://console.groq.com) | `https://api.groq.com/openai/v1` | llama-3.3-70b-versatile, llama-3.1-8b-instant, Gemma 2 9B | LPU hardware; extremely fast TTFT |
| **Cerebras** | [cerebras.ai](https://cerebras.ai) | `https://api.cerebras.ai/v1` | Llama 3.3 70B, GPT-OSS 120B, Qwen 3 32B | Wafer-scale engine throughput |
| **SambaNova** | [sambanova.ai](https://sambanova.ai) | `https://api.sambanova.ai/v1` | Llama 3.1 405B, Llama 3.3 70B, Qwen | RDU serving for large models |
| **Together AI** | [together.ai](https://together.ai) | `https://api.together.xyz/v1` | Llama 3.3, DeepSeek-V4, Qwen, FLUX.1 | Large catalog + fine-tuning |
| **Fireworks AI** | [fireworks.ai](https://fireworks.ai) | `https://api.fireworks.ai/inference/v1` | Qwen 3.6 Plus, Kimi K2.6, Llama 4 Maverick | Serverless low-latency serving |
| **DeepInfra** | [deepinfra.com](https://deepinfra.com) | `https://api.deepinfra.com/v1/openai` | Llama 3.3, Qwen 3, DeepSeek-V4, Mistral | Aggressive open-model pricing |
| **Nebius AI Studio** | [studio.nebius.ai](https://studio.nebius.ai) | `https://api.studio.nebius.ai/v1` | DeepSeek-R1-0528, Llama 3.3 70B | EU infrastructure; Token Factory |
| **SiliconFlow** | [siliconflow.com](https://siliconflow.com) | `https://api.siliconflow.cn/v1` | DeepSeek-R1-0528, MiniMax-M2, Qwen3-VL | Excellent cost/performance (CN) |
| **Inception** | [inceptionlabs.ai](https://inceptionlabs.ai) | `https://api.inceptionlabs.ai/v1` | Mercury-2, Mercury-Edit-2 | Diffusion language models (dLLMs) |
| **Liquid AI** | [liquid.ai](https://liquid.ai) | `https://inference.liquid.ai/v1` | LFM2.5 Instruct, LFM2-24B | Hybrid efficient architectures |
| **Friendli** | [friendli.ai](https://friendli.ai) | `https://api.friendli.ai/serverless/v1` | Llama 3.1 8B, DeepSeek-R1 | Custom checkpoints & private instances |
| **Inceptron** | [inceptron.io](https://inceptron.io) | Custom endpoint | Open-weight LLMs | Self-configured model hosting |
| **Infermatic** | [infermatic.ai](https://infermatic.ai) | `https://api.totalgpt.ai` | Rocinante, Midnight Miqu, Llama | Flat-rate community checkpoints |
| **Mancer** | [mancer.tech](https://mancer.tech) | `https://mancer.tech/oai/v1` | Goliath 120B, MythoMax, LumiMaid | Creative / roleplay fine-tunes |
| **Morph** | [morphllm.com](https://morphllm.com) | `https://api.morphllm.com/v1` | morph-qwen35-397b, morph-qwen36-27b | Fast code editing & routing |
| **AionLabs** | [aionlabs.ai](https://aionlabs.ai) | `https://api.aionlabs.ai/v1` | Aion 2.0, Aion-RP | Creative multi-turn fine-tunes |
| **HuggingFace Inference** | [huggingface.co](https://huggingface.co) | `https://router.huggingface.co/v1` | meta-llama/Llama-3.3-70B-Instruct, Qwen/Qwen2.5-72B-Instruct | Huge model catalog; free tier available |
| **NVIDIA NIM** | [build.nvidia.com](https://build.nvidia.com) | `https://integrate.api.nvidia.com/v1` | meta/llama-3.3-70b-instruct, deepseek-ai/deepseek-r1 | NVIDIA inference microservices |
| **Hyperbolic** | [app.hyperbolic.xyz](https://app.hyperbolic.xyz) | `https://api.hyperbolic.xyz/v1` | DeepSeek-V3, Llama 3.3 70B | Decentralized GPU compute |
| **Lepton AI** | [lepton.ai](https://lepton.ai) | `https://api.lepton.ai/v1` | Llama 3.3 70B | Fast serverless inference |
| **Kluster.ai** | [kluster.ai](https://kluster.ai) | `https://api.kluster.ai/v1` | Llama 3.1 405B, Qwen 2.5 72B | Batch inference specialist |
| **Anyscale Endpoints** | [app.endpoints.anyscale.com](https://app.endpoints.anyscale.com) | `https://api.endpoints.anyscale.com/v1` | Llama 3.3 70B, Mixtral 8x22B | Ray-based model serving |
| **Replicate** | [replicate.com](https://replicate.com) | `https://api.replicate.com/v1` | Open models, FLUX, video models | Pay-per-run; image/audio/video too |
| **Inference.net** | [inference.net](https://inference.net) | `https://api.inference.net/v1` | DeepSeek-R1, Llama 3.1 70B | Decentralized inference network |
| **Arcee AI** | [arcee.ai](https://arcee.ai) | `https://conductor.arcee.ai/v1` | Trinity-Large, Caller-Large | Enterprise fine-tuned models |
| **Glhf.chat** | [glhf.chat](https://glhf.chat) | `https://glhf.chat/api/openai/v1` | hf:meta-llama/Llama-3.3-70B-Instruct, hf:Qwen/Qwen2.5-72B-Instruct | vLLM-backed; run any HF model with hf: prefix |
| **Ollama Cloud** | [ollama.com](https://ollama.com) | `https://ollama.com/api` | gpt-oss:20b-cloud, gpt-oss:120b | OpenCode-supported; remote Ollama host; pull cloud models locally first |
| **OpenVecta** | [openvecta.com](https://openvecta.com) | `https://api.openvecta.com/v1` | glm-4.7-flash, claude-sonnet-4.6, deepseek-v4-flash, gpt-oss-120b | Free credits on signup for OpenAI-compatible inference across LLMs, embeddings, and reasoning models |
| **Openference API** | [openference.com](https://openference.com) | `https://api.openference.com/v1` | GLM-5.2 | Free plan: 3-day trial with open-source models — no credit card required |
| **Nube.sh** | [nube.sh](https://nube.sh) | `https://ai.nube.sh/api/v1` | — | OpenAI-compatible gateway (LiteLLM). Bring your own API key — models are resolved live from the account (passthrough). |
| **Lambda AI** | [lambda.ai](https://lambda.ai) | `https://api.lambda.ai/v1` | — | Hosted inference API for open-weight and partner models. |
| **nScale** | [nscale.com](https://nscale.com) | `https://inference.api.nscale.com/v1` | — | $5 free credits on signup for inference testing |
| **PublicAI** | [publicai.co](https://publicai.co) | `https://api.publicai.co/v1` | — | Requires an API key — one-time signup credit, then paid |
| **Featherless AI** | [featherless.ai](https://featherless.ai) | `https://api.featherless.ai/v1` | — | Free tier available — no credit card required |
| **Predibase** | [predibase.com](https://predibase.com) | `https://serving.app.predibase.com/v1` | — | $25 free trial credits (30-day validity) |
| **Bytez** | [bytez.com](https://bytez.com) | `https://api.bytez.com/models/v2/openai/v1` | — | $1 free credits, refreshes every 4 weeks |
| **MonsterAPI** | [monsterapi.ai](https://monsterapi.ai) | `https://api.monsterapi.ai/v1` | meta-llama/Meta-Llama-3.1-8B-Instruct, meta-llama/Llama-3.3-70B-Instruct | One-time signup trial credits for decentralized GPU inference (no recurring free plan). No credit card required.; Get API key at monsterapi.ai |
| **ModelScope** | [modelscope.cn](https://modelscope.cn) | `https://api-inference.modelscope.cn/v1` | — | Free tier via ModelScope API-Inference — Alibaba account required. |
| **BytePlus ModelArk** | [console.byteplus.com](https://console.byteplus.com/ark) | `https://ark.ap-southeast.bytepluses.com/api/v3` | seed-2.0, kimi-k2-thinking, glm-4.7, gpt-oss-120b | Free credits for new accounts. Seed 2.0, Kimi K2 Thinking, GLM 4.7, GPT-OSS-120B available. |

## Decentralized, Sovereign & Enterprise Clouds

Regional compliance, private networking, decentralized compute, and enterprise MLOps.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **AkashML** | [akash.network](https://akash.network) | `https://api.akashml.com/v1` | Llama 3, Qwen, DeepSeek | Decentralized GPU marketplace |
| **AtlasCloud** | [atlascloud.ai](https://atlascloud.ai) | `https://api.atlascloud.ai/v1` | DeepSeek-V3, Seedance 2.0, Kling 3.0 | Language + image + video APIs |
| **Chutes** | [chutes.ai](https://chutes.ai) | `https://llm.chutes.ai/v1` | Kimi, GLM, Qwen, MiniMax | Serverless custom model deploy |
| **Cloudflare Workers AI** | [cloudflare.com](https://cloudflare.com) | `https://api.cloudflare.com/client/v4/accounts/{id}/ai/v1` | @cf/meta/llama-3.3-70b-instruct-fp8-fast, Gemma 4, Kimi K2.5 | Edge inference; neuron-second billing; needs account ID |
| **DigitalOcean** | [digitalocean.com](https://digitalocean.com) | `https://inference.do-ai.run/v1/` | Llama 3 8B Instruct | Integrates with App Platform |
| **GMICloud** | [gmicloud.ai](https://gmicloud.ai) | `https://api.gmi-serving.com/v1` | GLM-5.1-FP8, DeepSeek-V3.2 | Enterprise H100 GPU cloud |
| **io.net** | [io.net](https://io.net) | `https://api.intelligence.io.solutions/api/v1` | GLM-4.5-Air, GPT-OSS 120B, Llama 3.3 | DePIN GPU clusters |
| **NextBit** | [nextbit256.com](https://nextbit256.com) | `https://api.nextbit256.com/v1` | qwen:3.5-35b, qwen3:30b, qwen3:14b | EU data centers (Spain) |
| **Novita** | [novita.ai](https://novita.ai) | `https://api.novita.ai/openai/v1` | Kimi K2.5, Llama, Qwen | Model APIs + agent sandboxes |
| **Parasail** | [parasail.io](https://parasail.io) | `https://api.saas.parasail.io/v1` | DeepSeek-R1, QwenCoder 32B | Serverless + dedicated instances |
| **Phala** | [phala.network](https://phala.network) | POST /v1/chat/completions | unsloth/Qwen2.5-72B-Instruct | TEE confidential execution |
| **Poolside** | [poolside.ai](https://poolside.ai) | `https://divers.poolsi.de/openai/v1/` | Laguna XS.2, Laguna M.1 | Code generation focus |
| **Venice** | [venice.ai](https://venice.ai) | `https://api.venice.ai/api/v1` | llama-3.3-70b, fluently-xl | Privacy-first; web3 auth |
| **Wafer** | [wafer.ai](https://wafer.ai) | `https://pass.wafer.ai/v1` | Qwen3.5-397B-A17B, GLM-5.1 | Fast serverless; Claude Code compatible |
| **Azure OpenAI** | [azure.microsoft.com](https://azure.microsoft.com) | `https://<resource>.openai.azure.com/openai/v1` | GPT-5, Claude, Llama | Enterprise Microsoft integration |
| **Google Vertex AI** | [cloud.google.com](https://cloud.google.com/vertex-ai) | `https://us-central1-aiplatform.googleapis.com/v1/projects` | Gemini, Claude, partner models | VPC, IAM, enterprise procurement |
| **Amazon Bedrock** | [aws.amazon.com](https://aws.amazon.com/bedrock) | `https://bedrock-runtime.<region>.amazonaws.com` | Claude, Llama, Titan, Mistral | AWS-native; IAM & VPC integration |
| **Baseten** | [baseten.co](https://baseten.co) | `https://model-{id}.api.baseten.co/v1` | Llama 3.3, DeepSeek-R1, custom | MLOps with Truss packaging |
| **Clarifai** | [clarifai.com](https://clarifai.com) | Custom endpoints | Multimodal models | Data labeling & classification |
| **Scaleway** | [console.scaleway.com](https://console.scaleway.com) | `https://api.scaleway.ai/v1` | Llama 3.3 70B, DeepSeek-R1 | European cloud; GDPR-compliant |
| **OVHcloud AI** | [www.ovhcloud.com](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/) | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | Meta-Llama-3_1-70B-Instruct, Qwen2.5-72B-Instruct | EU-hosted open models |
| **GitHub Models** | [github.com](https://github.com/marketplace/models) | `https://models.inference.ai.azure.com` | gpt-4o, Meta-Llama-3.1-70B-Instruct | Free tier with GitHub PAT |
| **Modal** | [modal.com](https://modal.com) | `https://<app>.modal.run/v1` | Any (self-deployed via vLLM) | Serverless GPU; deploy your own models |
| **Azure Cognitive Services** | [azure.microsoft.com](https://azure.microsoft.com/products/ai-services) | `https://<resource>.cognitiveservices.azure.com/openai/v1` | gpt-4o, gpt-4.1, o3-mini | OpenCode-supported; separate from Azure OpenAI; set AZURE_COGNITIVE_SERVICES_RESOURCE_NAME |
| **GitLab Duo** | [about.gitlab.com](https://about.gitlab.com/gitlab-duo/) | `https://gitlab.com/api/v4/ai` | duo-chat-haiku-4-5, duo-chat-sonnet-4-5, duo-chat-opus-4-5 | OpenCode-supported; OAuth or PAT; Premium/Ultimate; set GITLAB_INSTANCE_URL for self-hosted |
| **GitHub Copilot** | [github.com](https://github.com/features/copilot) | `https://api.githubcopilot.com` | gpt-4o, claude-sonnet-4, o3-mini | OpenCode-supported; OAuth via /connect; separate from GitHub Models marketplace API |
| **SAP AI Core** | [www.sap.com](https://www.sap.com/products/artificial-intelligence/ai-core.html) | `https://api.ai.<region>.<landscape>.ml.hana.ondemand.com/v2` | gpt-4o, claude-sonnet-4, gemini-2.5-pro, llama-3.3-70b | OpenCode-supported; 40+ models via BTP; service key JSON auth |
| **STACKIT AI Model Serving** | [www.stackit.de](https://www.stackit.de/en/product/stackit-ai-model-serving) | `https://api.openai-compat.model-serving.eu01.onstackit.cloud/v1` | qwen3-vl-235b, llama-3.3-70b, mistral-nemo-instruct | OpenCode-supported; EU sovereign hosting for Llama, Mistral, Qwen |
| **Snowflake Cortex** | [docs.snowflake.com](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-llm-rest-api) | `https://<account>.snowflakecomputing.com/api/v2/cortex/v1` | claude-sonnet-4-6, claude-haiku-4-5, gpt-5 | OpenCode-supported; OAuth or PAT; Claude/OpenAI families with tool calling |
| **IBM watsonx.ai Gateway** | [www.ibm.com](https://www.ibm.com/products/watsonx-ai) | `https://us-south.ml.cloud.ibm.com/ml/v1` | — | Use your watsonx bearer token. Base URL can be https://<region>.ml.cloud.ibm.com/ml/gateway/v1/ or a self-managed /ml/gateway/v1 endpoint.; The watsonx model gateway exposes OpenAI-compatible /chat/completions and /models under /ml/gateway/v1. |
| **OCI Generative AI** | [www.oracle.com](https://www.oracle.com/artificial-intelligence/generative-ai) | `https://inference.generativeai.us-chicago-1.oci.oraclecloud.com` | — | Use your OCI Generative AI API key or IAM bearer token. Base URL can be https://inference.generativeai.<region>.oci.oraclecloud.com/openai/v1/.; OCI exposes OpenAI-compatible chat and responses endpoints. Project ID is optional in OmniRoute but may be required for Responses and agentic workflows. |
| **Vertex AI Partners** | [cloud.google.com](https://cloud.google.com/vertex-ai) | `https://us-central1-aiplatform.googleapis.com/v1/projects` | DeepSeek-V4-Flash, DeepSeek-V4-Pro, Qwen3.6-35B-A3B, GLM-5.1-FP8 | Provide the same Service Account JSON used for Vertex AI partner models. |
| **Heroku AI** | [www.heroku.com](https://www.heroku.com) | `https://us.inference.heroku.com/v1` | — | Enterprise or regional cloud inference. |
| **Databricks** | [www.databricks.com](https://www.databricks.com) | `https://adb-0000000000000000.0.azuredatabricks.net/serving-endpoints` | — | Enterprise or regional cloud inference. |
| **DataRobot** | [docs.datarobot.com](https://docs.datarobot.com) | `https://app.datarobot.com/api/v2` | — | Use your DataRobot API token. Optional Base URL can be the account root (for LLM Gateway) or a deployment URL under /api/v2/deployments/<id>.; The default gateway catalogs active models from /genai/llmgw/catalog/. Deployment URLs are also supported for direct OpenAI-compatible chat requests. |
| **Dasha Compute** | [www.getdasha.com](https://www.getdasha.com/compute) | Open alpha | qwen3-8b, gemma3-12b, gemma3-27b | OpenAI-compatible API on a network of Apple-silicon Macs; providers paid per job in USDC. |

## Multi-Provider Gateways & Routers

One API surface for many upstream providers — ideal for **failover**, **cost optimization**, and **reducing credential sprawl**.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | `https://openrouter.ai/api/v1` | 300+ models from 60+ providers | Auto fallback & provider selection |
| **Opper** | [opper.ai](https://opper.ai) | `https://api.opper.ai/v3/compat` | 300+ routed models | EU-hosted; PII shielding |
| **Axiom** | [axiomstudio.ai](https://axiomstudio.ai) | `https://cloud.axiomstudio.ai/rest/v1/llm-gateway/v1/` | 18+ unified providers | Kubernetes-native enterprise routing |
| **Switchpoint** | [switchpoint.ai](https://switchpoint.ai) | `https://api.ppq.ai` | switchpoint/router | Request-aware provider selection |
| **Relace** | [relace.ai](https://relace.ai) | `https://api.relace.ai/v1` | Relace Apply 3, Relace Search | Coding APIs; zero data retention default |
| **Moonshot AI** | [api.moonshot.ai](https://api.moonshot.ai/v1) | `https://api.moonshot.ai/v1` | kimi-k2.7-code, kimi-k2.6 | First-party Kimi gateway |
| **OpenInference** | [openinference.ai](https://openinference.ai) | Tracing / observability | LLM telemetry | Execution graph tracing |
| **Weights & Biases** | [wandb.ai](https://wandb.ai) | `https://api.inference.wandb.ai/v1` | Model benchmarking | Experiment tracking |
| **Perceptron** | [perceptron.ai](https://perceptron.ai) | Custom gateway | Enterprise routes | Custom middleware routing |
| **Portkey** | [portkey.ai](https://portkey.ai) | `https://api.portkey.ai/v1` | 250+ models | Guardrails, caching, observability |
| **LiteLLM** | [github.com](https://github.com/BerriAI/litellm) | `http://localhost:4000/v1` | 100+ providers | Open-source; self-host or cloud |
| **Requesty** | [requesty.ai](https://requesty.ai) | `https://router.requesty.ai/v1` | Multi-provider routing | Auto-failover between providers |
| **Unify.ai** | [unify.ai](https://unify.ai) | `https://api.unify.ai/v0` | ML-routed models | Picks optimal provider per query |
| **Helicone** | [helicone.ai](https://helicone.ai) | `https://ai-gateway.helicone.ai/v1` | 100+ models | Observability-first AI gateway |
| **Vercel AI Gateway** | [vercel.com](https://vercel.com/docs/ai-gateway) | `https://ai-gateway.vercel.sh/v1` | All major providers | Bundled with Vercel platform |
| **Cloudflare AI Gateway** | [developers.cloudflare.com](https://developers.cloudflare.com/ai-gateway/) | `https://gateway.ai.cloudflare.com/v1` | Any upstream provider | Edge caching; sits in front of APIs |
| **Kong AI Gateway** | [konghq.com](https://konghq.com/products/kong-ai-gateway) | Self-hosted / enterprise | Enterprise routing | For existing Kong infrastructure |
| **Cortecs** | [cortecs.ai](https://cortecs.ai) | `https://api.cortecs.ai/v1` | kimi-k2-instruct, gpt-5-mini | OpenCode-supported; EU GDPR-compliant LLM router with speed/cost/balanced routing |
| **OpenCode Zen** | [opencode.ai](https://opencode.ai/zen) | `https://opencode.ai/zen/v1` | gpt-5.5, claude-sonnet-4-6, qwen3-coder-480b | OpenCode-curated models verified for coding agents; use opencode/<model-id> prefix |
| **OpenCode Go** | [opencode.ai](https://opencode.ai/docs/go/) | `https://opencode.ai/zen/go/v1` | kimi-k2.7, glm-5.1, deepseek-v4-pro, qwen3.6-plus | OpenCode-supported; low-cost subscription for open coding models; use opencode-go/<model-id> |
| **LLM Gateway** | [llmgateway.io](https://llmgateway.io) | `https://api.llmgateway.io/v1` | gpt-4o, claude-3-5-sonnet, gemini-2.5-pro, glm-4.7 | OpenCode-supported; unified API with provider/model routing |
| **ZenMux** | [zenmux.ai](https://zenmux.ai) | `https://zenmux.ai/api/v1` | openai/gpt-5, anthropic/claude-sonnet-4, google/gemini-2.5-pro | OpenCode-supported; enterprise routing across 200+ models |
| **Sakana AI (Fugu)** | [console.sakana.ai](https://console.sakana.ai) | `https://api.sakana.ai/v1` | fugu, fugu-ultra, fugu-ultra-20260615 | Trained multi-agent orchestrator; routes to frontier LLM pool via single OpenAI-compatible API |
| **Prism API** | [go165.github.io](https://go165.github.io/prism-api-promo/) | `https://sub2api.558686.xyz/v1` | gpt-5.5, gpt-5.4, claude-sonnet-4, gemini-2.5-pro | Independent OpenAI-compatible gateway for overseas developers; low-cost GPT-5.5 access and crypto-friendly recharge/voucher options |
| **XiuRouter** | [router.xiu.ai](https://router.xiu.ai/) | `https://router-api.xiu.ai/v1` | gpt-5.6-sol, gpt-5.5, claude-opus-5, gpt-5.4 | Usage-based gateway with OpenAI Chat Completions and Responses, Anthropic Messages, Gemini GenerateContent, scoped keys, and request-level usage and cost records |
| **SAGG** | [api.privatedeskai.com](https://api.privatedeskai.com) | `https://api.privatedeskai.com/v1` | deepseek-ai/DeepSeek-V4-Flash-0731 | Multi-provider failover gateway; a flat-rate Super Deal tier ($0.028/1M tokens, separate key) is also available |
| **AIWave** | [aiwave.live](https://aiwave.live/) | `https://aiwave.live/v1` | deepseek-v4-pro, deepseek-v4-flash, deepseek-v3.2, kimi-k3 | Chinese AI providers with USD billing, dated pricing, and request-level usage records |
| **CLIProxyAPI** | [github.com](https://github.com/router-for-me/CLIProxyAPI) | `http://localhost:8317/v1` | — | OpenAI-compatible multi-provider gateway or local proxy. |
| **9router** | [www.npmjs.com](https://www.npmjs.com/package/9router) | `http://localhost:20130/v1` | — | OpenAI-compatible multi-provider gateway or local proxy. |
| **1min.AI** | [1min.ai](https://1min.ai) | `https://api.1min.ai/api/chat-with-ai` | gpt-4o-mini | Create an API key at https://docs.1min.ai/docs/api/create-api-key, then paste it here.; 1min.ai uses a proprietary chat API (single prompt string + SSE) instead of OpenAI chat/completions. OmniRoute flattens OpenAI messages into a labeled prompt and translates the SSE stream. |
| **Cheaper Inference** | [cheaperinference.com](https://cheaperinference.com) | `https://api.cheaperinference.com/v1` | aion-labs.aion-2-0, claude-fable-5, claude-haiku-4.5, claude-opus-4-7-fast | Create an API key at https://cheaperinference.com/?utm_source=omniroute (needs the `inference` scope), then paste the ir_live_… token here. |
| **Freebuff** | [freebuff.com](https://freebuff.com) | `https://www.codebuff.com/api/v1` | deepseek/deepseek-v4-flash, deepseek/deepseek-v4-pro, openai/gpt-5.6-luna, minimax/minimax-m3 | Free Codebuff / Freebuff AI models.; Enter Freebuff / Codebuff Auth Token (obtained via CLI login or automated harvester).; Token is authenticated against Codebuff upstream session pool. |
| **Charm Hyper** | [hyper.charm.land](https://hyper.charm.land) | `https://hyper.charm.land/v1` | hyper/auto | 100 free monthly Hypercredits on signup; Create an API key at https://hyper.charm.land, then paste it here as a Bearer token. |
| **AgentRouter** | [agentrouter.org](https://agentrouter.org) | `https://agentrouter.org/v1` | claude-opus-4-8, claude-opus-5, gpt-5.6-sol | $200 free credits on signup - multi-model routing gateway; Get $200 free credits at https://agentrouter.org/register — no credit card required. |
| **UnoRouter** | [unorouter.ai](https://unorouter.ai) | `https://api.unorouter.com/v1` | — | Models with the :free suffix do not debit balance; limit is 1 request/minute per free model per user.; Create an API key at https://unorouter.ai, then paste it here as a Bearer token. |
| **Command Code** | [commandcode.ai](https://commandcode.ai) | `https://api.commandcode.ai` | claude-opus-4-7, claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5-20251001 | Use a Command Code API key. Requests are sent to Command Code's /provider/v1/chat/completions endpoint.; Create or copy an API key from Command Code, then paste it here as a Bearer token. |
| **Zylo API** | [zyloai.net](https://zyloai.net) | `https://api.zyloai.net/v1` | — | Basic plan: 10 RPM, 7,200 requests/day and 200,000 tokens/day; limited to Basic text models.; Create a free Zylo API key at https://zyloai.net, then use https://api.zyloai.net/v1 as the OpenAI-compatible base URL. |
| **FastRouter** | [fastrouter.ai](https://fastrouter.ai) | `https://api.fastrouter.ai/api/v1` | — | Models with the :free suffix allow 10 requests/day per organization and model; availability may change.; Create a FastRouter API key, then use https://api.fastrouter.ai/api/v1 as the OpenAI-compatible base URL. |
| **LLM.Kiwi** | [llm.kiwi](https://llm.kiwi) | `https://api.llm.kiwi/v1` | auto, hrLLM | Free plan exposes auto and hrLLM; the published 40 requests/hour limit applies to hrLLM.; Create a free LLM.Kiwi key, then use https://api.llm.kiwi/v1 as the OpenAI-compatible base URL. |
| **LiteRouter** | [literouter.com](https://literouter.com) | `https://api.literouter.com/v1` | — | Free model variants use the :free suffix; daily credit limits vary by model and free input is capped at 5,000 tokens.; Create a LiteRouter API key, then use https://api.literouter.com/v1 as the OpenAI-compatible base URL. |
| **GreenPT** | [greenpt.com](https://greenpt.com) | `https://api.greenpt.ai/v1` | — | API subscription is free to create; inference is billed per token. No free inference allowance is published.; Create a GreenPT API key, then use https://api.greenpt.ai/v1 as the OpenAI-compatible base URL. Review jurisdiction, privacy and regional data-transfer requirements before use. |
| **EURouter** | [eurouter.ai](https://eurouter.ai) | `https://api.eurouter.ai/v1` | — | Create an EURouter API key, then use https://api.eurouter.ai/v1 as the OpenAI-compatible base URL. Models are served by third-party upstreams listed per model in the EURouter catalog; check each upstream jurisdiction, privacy and data-transfer terms before use. |
| **MNN AI** | [mnnai.ru](https://mnnai.ru) | `https://api.mnnai.ru/v1` | — | Free plan: $1 monthly credits, 10 RPM and access only to models marked Free.; Create an MNN AI API key, then use the primary https://api.mnnai.ru/v1 OpenAI-compatible endpoint. Review jurisdiction, privacy and regional data-transfer requirements before use. |
| **MegaNova AI** | [meganova.ai](https://meganova.ai) | `https://api.meganova.ai/v1` | — | Free signup without a card. Published Tier 1 per-model quotas total 550 requests/day; they are not a shared global pool, and paid overage can apply if enabled.; Create a MegaNova API key, then use https://api.meganova.ai/v1 as the OpenAI-compatible base URL. |
| **Mixlayer** | [www.mixlayer.com](https://www.mixlayer.com) | `https://models.mixlayer.ai/v1` | qwen/qwen3.5-4b-free | The qwen/qwen3.5-4b-free model is free for prototyping and rate-limited; no fixed public RPM or daily quota is confirmed.; Create a Mixlayer API key, then use https://models.mixlayer.ai/v1 as the OpenAI-compatible base URL. |
| **Speka AI** | [speka.me](https://speka.me) | `https://speka.me/v1` | — | Free plan: $1 monthly usage, 10 RPM, one API key and access to open models and the playground; no card required.; Create a Speka API key, then use https://speka.me/v1 as the OpenAI-compatible base URL. Confirm current model availability and overage settings before use. |
| **TokenReply** | [www.tokenreply.com](https://www.tokenreply.com) | `https://api.tokenreply.com/v1` | — | Free-tagged models have model- and campaign-specific daily limits; no fixed global free quota is published.; Create a TokenReply token, then use https://api.tokenreply.com/v1 as the OpenAI-compatible base URL and confirm the selected model's current limit. |
| **Yolo-Auto** | [yolo-auto.com](https://yolo-auto.com) | `https://yolo-auto.com/v1` | qwen3.6-35b-a3b | Free API access is request-limited and intended for testing; no numeric daily quota is published and free access is not promised indefinitely.; Create a yolo_ API key, then use https://yolo-auto.com/v1 as the OpenAI-compatible base URL. |
| **DXNT / DX Token** | [www.dxnt.com](https://www.dxnt.com) | `https://www.dxnt.com/v1` | — | Free accounts are documented at 100 calls/day; the quota may increase through invitations and can vary by account.; Create a DXNT API key, then use https://www.dxnt.com/v1 as the OpenAI-compatible base URL. |
| **CloudCode.ONE** | [cloudcode.one](https://cloudcode.one) | `https://api.cloudcode.one/v1` | glm-4.7-flash, glm-4.6v-flash | Published free models include glm-4.7-flash and glm-4.6v-flash; no numeric quota is published, and key creation may require credit or a coupon.; Create a CloudCode.ONE key, then use https://api.cloudcode.one/v1 as the OpenAI-compatible base URL. Key issuance may require credit or a coupon. |
| **OfoxAI** | [ofox.ai](https://ofox.ai) | `https://api.ofox.ai/v1` | — | The current catalog advertises 10+ free models without a public numeric quota; review upstream provenance, retention and training terms before production use.; Create an OfoxAI Bearer key, then use https://api.ofox.ai/v1 as the OpenAI-compatible base URL. This integration covers the OpenAI surface only. |
| **ZeroLimitAI** | [www.zerolimitai.com](https://www.zerolimitai.com) | `https://www.zerolimitai.com/api/v1` | — | Temporary free trial is advertised, but official pages conflict between 3 and 7 days; a 100-calls/day claim is not treated as permanent.; Create a ZeroLimitAI Bearer token, then use https://www.zerolimitai.com/api/v1 as the OpenAI-compatible base URL. |
| **Helyx AI** | [helyxai.space](https://helyxai.space) | `https://helyxai.space/v1` | — | Operational Free plan documents 100,000 tokens/day; the site's separate 2M+ marketing claim conflicts and is not treated as a quota guarantee.; Create a Helyx AI Bearer key, then use https://helyxai.space/v1 as the OpenAI-compatible base URL. Review terms and data retention first. |
| **Auriko** | [www.auriko.ai](https://www.auriko.ai) | `https://api.auriko.ai/v1` | — | Free plan publishes 1,000 Platform RPM and 10,000 BYOK RPM. Platform inference still passes through provider cost; this is not a free-token pool or unlimited free inference.; Create an Auriko key with the ak_ prefix, then use https://api.auriko.ai/v1 as the OpenAI-compatible base URL. BYOK and platform credits have different cost semantics. |
| **Poixe AI** | [poixe.com](https://poixe.com) | `https://api.poixe.com/v1` | — | Current public free limits are small and model-group specific: 2 RPM/5 RPD for large-cup models and 20 RPM/50 RPD for small-cup models.; Create a Poixe Bearer key, then use https://api.poixe.com/v1 as the OpenAI-compatible base URL. Treat free model provenance and regional availability as experimental. |
| **Chat Oripe** | [api.oriper.com](https://api.oriper.com) | `https://api.oriper.com/v1` | — | Official metadata advertises 2M tokens/month, but the public site and documentation were blocked during audit; treat the quota and brand mapping as unconfirmed.; Use https://api.oriper.com/v1 only after confirming the provider's current documentation, terms and key issuance. No quota is guaranteed by this catalog. |
| **FreeInference** | [freeinference.org](https://freeinference.org) | `https://freeinference.org/v1` | — | Free research access without a card; non-Harvard applicants require manual approval and no numeric quota is publicly guaranteed.; Apply for a FreeInference key, then use https://freeinference.org/v1 as the OpenAI-compatible base URL. Terms allow prompt/response logging and possible publication of anonymized research data; never send sensitive or production data. |
| **Free.ai** | [free.ai](https://free.ai) | `https://api.free.ai/v1/chat` | — | 30,000 tokens/day cover self-hosted models after email verification. Usage beyond the pool can bill at raw cost, and premium external models are paid.; Create an sk-free- key, then use the nonstandard but OpenAI-shaped https://api.free.ai/v1/chat/ endpoint. Select a self-hosted zero-price model to stay within the free pool. |
| **DGrid** | [dgrid.ai](https://dgrid.ai) | `https://api.dgrid.ai/v1` | dgridai/free | DGrid Free Models Router: 10 requests/minute and 100 requests/day. A $5 lifetime top-up unlocks up to 20 requests/minute and 1,000 requests/day.; Create a DGrid API key at https://dgrid.ai, then use https://api.dgrid.ai/v1 as the OpenAI-compatible base URL. |
| **Qiniu** | [www.qiniu.com](https://www.qiniu.com) | `https://api.qnaigc.com/v1` | — | Create a Qiniu AI inference API key at https://portal.qiniu.com/ai-inference/api-key, then paste it here as a Bearer token. OpenAI-compatible endpoint at https://api.qnaigc.com/v1, proxying DeepSeek, Claude, Kimi and more behind one key. |
| **OrcaRouter** | [www.orcarouter.ai](https://www.orcarouter.ai) | `https://api.orcarouter.ai/v1` | orcarouter/auto, openai/gpt-5.5, google/gemini-3.6-flash, anthropic/claude-opus-4.8 | Create an API key (starts with sk-orca-) at https://www.orcarouter.ai, then paste it as a Bearer token. OpenAI-compatible endpoint at https://api.orcarouter.ai/v1. |
| **Api.airforce** | [api.airforce](https://api.airforce) | `https://api.airforce/v1` | x-ai/grok-3, x-ai/grok-2-1212, anthropic/claude-3.7-sonnet, qwen/qwen3-32b | 55 free tier models including Grok-3, Claude 3.7, Qwen3, Kimi-K2, Gemini 2.5 Flash, DeepSeek-V3; Get your API key from https://panel.api.airforce — OpenAI-compatible endpoint at https://api.airforce/v1 |
| **CrofAI** | [crof.ai](https://crof.ai) | `https://crof.ai/v1` | deepseek-v4-pro, deepseek-v4-flash, deepseek-v4-flash-0731, deepseek-v3.2 | OpenAI-compatible multi-provider gateway or local proxy. |
| **BazaarLink** | [bazaarlink.ai](https://bazaarlink.ai) | `https://bazaarlink.ai/api/v1` | auto:free, claude-opus-4.7, claude-sonnet-4.6, claude-haiku-4.5 | Free tier: 4M tokens/day per account with auto:free routing — zero-cost inference, no credit card required.; Use your BazaarLink API key (starts with sk-bl-) in Authorization: Bearer <key>. OpenAI SDK works with base URL https://bazaarlink.ai/api/v1. Models use provider/model-name format.; Create a free API key at https://bazaarlink.ai — model 'auto:free' routes to zero-cost inference. All models use the provider/… |
| **Synthetic** | [synthetic.new](https://synthetic.new) | `https://api.synthetic.new/openai/v1` | hf:openai/gpt-oss-120b, hf:zai-org/GLM-5.2, hf:moonshotai/Kimi-K2.7-Code, hf:Qwen/Qwen3.6-27B | OpenAI-compatible multi-provider gateway or local proxy. |
| **Kilo Gateway** | [kilo.ai](https://kilo.ai) | `https://api.kilo.ai/api/gateway` | kilo-auto/frontier, kilo-auto/balanced, kilo-auto/free, nvidia/nemotron-3-super-120b-a12b:free | OpenAI-compatible multi-provider gateway or local proxy. |
| **Dahl** | [inference.dahl.global](https://inference.dahl.global) | `https://inference.dahl.global/v1` | MiniMaxAI/MiniMax-M2.7, moonshotai/Kimi-K2.6 | Free — MiniMax M2.7, Kimi K2.6. Click 'Add Account' to auto-generate a token, or add your own API key.; Click 'Add Account' to auto-generate a token, or add a manual API key.; Auto-generate a token or paste your own API key.; Dahl auto-generates tokens via https://inference.dahl.global/tokens. No signup needed. Rate limits apply. You can also add your own API key. |
| **FreeTheAi** | [freetheai.xyz](https://freetheai.xyz) | `https://api.freetheai.xyz/v1` | gpt-4o-mini, llama-3.3-70b-instruct, deepseek-chat | Free OpenAI-compatible gateway — sign up via Discord for an API key.; Join the FreeTheAi Discord to get your free API key. |
| **g4f.space — Groq** | [g4f.space](https://g4f.space) | `https://g4f.space/api/groq/v1` | llama-3.3-70b-versatile, llama-3.1-8b-instant | Anonymous access to Groq requires proof-of-work cake credits from g4f.dev/chat; alternatively, use a g4f.dev member API key. Limits vary.; Bake anonymous cake credits at g4f.dev/chat, or use a g4f.dev member key (create one at g4f.dev/members.html).; Remote third-party gateway: prompts and request metadata leave OmniRoute and are handled by g4f.space. Its Terms and Privacy links were unavailable when last verified… |
| **g4f.space — Gemini** | [g4f.space](https://g4f.space) | `https://g4f.space/api/gemini/v1` | models/gemini-2.5-flash, models/gemini-2.5-pro | Anonymous access to Gemini requires proof-of-work cake credits from g4f.dev/chat; alternatively, use a g4f.dev member API key. Limits vary.; Bake anonymous cake credits at g4f.dev/chat, or use a g4f.dev member key (create one at g4f.dev/members.html).; Remote third-party gateway: prompts and request metadata leave OmniRoute and are handled by g4f.space. Its Terms and Privacy links were unavailable when last verifi… |
| **g4f.space — Pollinations** | [g4f.space](https://g4f.space) | `https://g4f.space/api/pollinations/v1` | openai, openai-fast | Anonymous access to Pollinations requires proof-of-work cake credits from g4f.dev/chat; alternatively, use a g4f.dev member API key. Limits vary.; Bake anonymous cake credits at g4f.dev/chat, or use a g4f.dev member key (create one at g4f.dev/members.html).; Remote third-party gateway: prompts and request metadata leave OmniRoute and are handled by g4f.space. Its Terms and Privacy links were unavailable when last… |
| **g4f.space — Ollama** | [g4f.space](https://g4f.space) | `https://g4f.space/api/ollama/v1` | gemma3:4b | Anonymous access to hosted Ollama requires proof-of-work cake credits from g4f.dev/chat; alternatively, use a g4f.dev member API key. Limits vary.; Bake anonymous cake credits at g4f.dev/chat, or use a g4f.dev member key (create one at g4f.dev/members.html).; Remote third-party gateway: prompts and request metadata leave OmniRoute and are handled by g4f.space. Its Terms and Privacy links were unavailable when last… |
| **g4f.space — NVIDIA** | [g4f.space](https://g4f.space) | `https://g4f.space/api/nvidia/v1` | nvidia/nemotron-3-nano-30b-a3b, z-ai/glm-5.2, minimaxai/minimax-m2.7 | Anonymous access to NVIDIA NIM requires proof-of-work cake credits from g4f.dev/chat; alternatively, use a g4f.dev member API key. Limits vary.; Bake anonymous cake credits at g4f.dev/chat, or use a g4f.dev member key (create one at g4f.dev/members.html).; Remote third-party gateway: prompts and request metadata leave OmniRoute and are handled by g4f.space. Its Terms and Privacy links were unavailable when last ve… |
| **LLM7.io** | [llm7.io](https://llm7.io) | `https://api.llm7.io/v1` | gpt-4o-mini-2024-07-18, gpt-4.1-nano-2025-04-14, deepseek-r1-0528, qwen2.5-coder-32b-instruct | No signup required - 2 req/s, 20 RPM, 100 req/hr free tier; Use any non-empty key (for example 'unused'). If older built-in models return model_unavailable, use Available Models → Import from /models or Auto-Sync; verified live model: gemini-3.1-flash-lite.; Works without API key (use 'unused' as key). Get free token at token.llm7.io for higher limits. |
| **LlamaGate** | [llamagate.ai](https://llamagate.ai) | `https://llamagate.ai/v1` | — | OpenAI-compatible multi-provider gateway or local proxy. |
| **Gitlawb Opengateway (MiMo)** | [opengateway.gitlawb.com](https://opengateway.gitlawb.com) | `https://opengateway.gitlawb.com/v1/xiaomi-mimo` | mimo-v2.5-pro, mimo-v2.5, mimo-v2-pro, mimo-v2-omni | Free MiMo (xiaomi/mimo-v2.5) revoked 2026-05 — Opengateway is now a pay-as-you-go credit gateway; no recurring free model.; Get your API key from Gitlawb Opengateway dashboard. |
| **Gitlawb Opengateway (GMI Cloud)** | [opengateway.gitlawb.com](https://opengateway.gitlawb.com) | `https://opengateway.gitlawb.com/v1/gmi-cloud` | XiaomiMiMo/MiMo-V2.5-Pro, XiaomiMiMo/MiMo-V2.5, openai/gpt-5.5, openai/gpt-5.4-pro | Free Nemotron promo ended 2026-06 — the GMI Cloud route is now pay-as-you-go credit only.; Get your API key from Gitlawb Opengateway dashboard. |
| **NanoGPT** | [nano-gpt.com](https://nano-gpt.com) | `https://nano-gpt.com/api/v1` | — | OpenAI-compatible multi-provider gateway or local proxy. |
| **LaoZhang AI** | [api.laozhang.ai](https://api.laozhang.ai) | `https://api.laozhang.ai/v1` | — | OpenAI-compatible multi-provider gateway or local proxy. |
| **b.ai** | [b.ai](https://b.ai) | `https://api.b.ai/v1` | — | Bearer API key for the b.ai OpenAI-compatible LLM gateway (distinct from TheB.AI). Create a key at https://docs.b.ai, then use https://api.b.ai/v1 as the OpenAI-compatible base URL. |
| **FenayAI** | [fenayai.com](https://fenayai.com) | `https://api.fenayai.com/v1` | — | Bearer API key for the FenayAI OpenAI-compatible gateway. |
| **Empower** | [docs.empower.dev](https://docs.empower.dev) | `https://api.empower.dev/v1` | — | Bearer API key for the Empower OpenAI-compatible endpoint.; Empower exposes OpenAI-compatible chat on https://app.empower.dev/api/v1 with tool-calling support on empower-functions. |
| **Factory** | [factory.ai](https://factory.ai) | `https://api.factory.ai/v1` | auto | Bearer API key for the Factory OpenAI-compatible gateway.; Get your Factory API key at https://app.factory.ai/settings/api-keys, then paste it as a Bearer token. OpenAI-compatible endpoint at https://api.factory.ai/v1. |
| **BluesMinds** | [www.bluesminds.com](https://www.bluesminds.com) | `https://api.bluesminds.com/v1` | gpt-4o, gpt-4o-mini, gpt-4.1, gpt-4.1-mini | Free daily pi credits — supports 200+ models including GPT-4o, GPT-4.1, Claude Sonnet 4.5, Gemini 2.0 Flash, DeepSeek V4, Qwen, Kimi K2; Get your API key at https://www.bluesminds.com — OpenAI-compatible endpoint at https://api.bluesminds.com/v1 with free daily credits. VIP models (Claude Opus 4.5, Gemini 2.5 Pro) consume pi credits. |
| **FreeModel.dev** | [freemodel.dev](https://freemodel.dev) | `https://api.freemodel.dev/v1` | gpt-5.5, gpt-5.4, gpt-5.4-mini, gpt-5.3-codex | $300 free credits on signup — no credit card required. Access GPT-5.4 and GPT-5.5 (OpenAI's latest flagship models) through an OpenAI-compatible API.; Get $300 free API credits at https://freemodel.dev — no payment info required. OpenAI-compatible endpoint. GPT-5.4 and GPT-5.5 models available. |
| **FreeAIAPIKey** | [freeaiapikey.com](https://freeaiapikey.com) | `https://api.freeaiapikey.com/v1` | openai/gpt-4o, openai/gpt-5.4, openai/gpt-5.5, openai/gpt-5.6-sol | Discounted API proxy for 40+ models including GPT-5, Claude Opus 4.6, Claude Sonnet 4.6, Qwen 3.5. Get your API key at https://freeaiapikey.com/dashboard. Base URL: https://freeaiapikey.com/v1. |
| **OpenAdapter** | [openadapter.dev](https://openadapter.dev) | `https://api.openadapter.in/v1` | glm-4.7 | Free tier with a generous quota and no credit card — 15+ open-source models with daily quota. Get your API key at https://dashboard.openadapter.in.; Use your OpenAdapter API key in Authorization: Bearer sk-cv-<key>. Fully OpenAI-compatible. API base URL: https://api.openadapter.in/v1.; OpenAdapter exposes an OpenAI-compatible chat completions endpoint at https://api.openadapter.in/v1/chat/completions, aggregating… |
| **DIT.ai** | [dit.ai](https://dit.ai) | `https://api.dit.ai/v1` | gpt-5.4, claude-sonnet-4-6 | Use your dit.ai API key in Authorization: Bearer <key>. Fully OpenAI-compatible — a drop-in replacement, just change the base URL to https://api.dit.ai/v1.; dit.ai (Distributed Intelligence Trade) is an OpenAI-compatible router/gateway with dynamic per-request pricing, exposing /v1/chat/completions at https://api.dit.ai/v1. OmniRoute uses the OpenAI protocol; spend/savings analytics live in the dit.ai dashboard. |
| **TokenRouter** | [tokenrouter.com](https://tokenrouter.com) | `https://api.tokenrouter.com/v1` | minimax-3, deepseek-v4-pro, deepseek-v4-flash | Free tier includes the MiniMax 3 model. Get your API key at https://tokenrouter.com.; Use your TokenRouter API key in Authorization: Bearer <key>. Fully OpenAI-compatible. API base URL: https://api.tokenrouter.com/v1.; TokenRouter exposes an OpenAI-compatible chat completions endpoint at https://api.tokenrouter.com/v1/chat/completions, plus a working /v1/models catalog. OmniRoute uses the OpenAI protocol. |
| **Token Kiosk** | [agent-router.gaib.ai](https://agent-router.gaib.ai) | `https://agent-router.gaib.ai/v1` | claude-3-5-sonnet, deepseek-v3, deepseek-r1, kimi-k1.5 | Use your Token Kiosk API key in Authorization: Bearer <key>. Fully OpenAI-compatible gateway. API base URL: https://agent-router.gaib.ai/v1.; Token Kiosk is a multi-provider agent LLM routing infrastructure exposing an OpenAI-compatible endpoint at https://agent-router.gaib.ai/v1/chat/completions with auto-fallback and latency routing. |
| **SumoPod** | [ai.sumopod.com](https://ai.sumopod.com) | `https://ai.sumopod.com/v1` | — | Use your SumoPod API key (sk-...) in Authorization: Bearer <key>. Fully OpenAI-compatible. API base URL: https://ai.sumopod.com/v1.; SumoPod exposes an OpenAI-compatible chat completions endpoint at https://ai.sumopod.com/v1/chat/completions, plus a live /v1/models catalog. OmniRoute uses the OpenAI protocol and lists models via passthrough. |
| **X5Lab** | [x5lab.dev](https://x5lab.dev) | `https://api.x5lab.dev/v1` | — | Use your X5Lab API key (x5-...) in Authorization: Bearer <key>. Fully OpenAI-compatible. API base URL: https://api.x5lab.dev/v1.; X5Lab exposes an OpenAI-compatible chat completions endpoint at https://api.x5lab.dev/v1/chat/completions, plus a live /v1/models catalog. OmniRoute uses the OpenAI protocol and lists models via passthrough. |
| **Chenzk API** | [chenzk.top](https://chenzk.top) | `https://chenzk.top/v1` | — | Create an API key at https://chenzk.top/token, then paste it here as a Bearer token. OpenAI-compatible endpoint at https://chenzk.top/v1, with a live /v1/models catalog. |
| **Kenari** | [kenari.id](https://kenari.id) | `https://kenari.id/v1` | — | Use your Kenari API key (kn-...) in Authorization: Bearer <key>. Fully OpenAI-compatible. API base URL: https://kenari.id/v1.; Kenari exposes an OpenAI-compatible chat completions endpoint at https://kenari.id/v1/chat/completions, plus a live /v1/models catalog covering Claude, GPT, DeepSeek, GLM, Kimi and more. OmniRoute uses the OpenAI protocol and lists models via passthrough. |
| **NavyAI** | [api.navy](https://api.navy) | `https://api.navy/v1` | llama-3.3-70b-instruct, gemma-4-31b-it, deepseek-v4-flash, deepseek-chat | Free plan is one shared 150K tokens/day pool at 20 RPM. Each model carries a token multiplier, so heavier models drain the pool faster (grok-4 at 10x is ~15K real tokens/day).; Create a free API key from the NavyAI dashboard, then paste it here as a Bearer token.; OpenAI-compatible endpoint at https://api.navy/v1 with a live /v1/models catalog that exposes per-model token_multiplier and premium flags. Upstream req… |
| **AINative Studio** | [ainative.studio](https://ainative.studio) | `https://api.ainative.studio/api/v1` | qwen3-235b-cerebras, qwen3-32b, qwen3-14b, qwen3-8b | Free tier ~10M tokens/month (claimed) across Qwen3, Llama 4, DeepSeek R1 and more.; Create a free API key at ainative.studio (no card), then paste it here as a Bearer token.; OpenAI-compatible endpoint at https://api.ainative.studio/api/v1 with a public /models catalog (84 models). OmniRoute lists models via passthrough. |
| **Routeway** | [routeway.ai](https://routeway.ai) | `https://api.routeway.ai/v1` | llama-3.3-70b-instruct:free, nemotron-3-nano-30b-a3b:free, nemotron-nano-9b-v2:free, step-3.7-flash:free | Free models (:free suffix) at ~5 RPM / 200 RPD across Llama, Nemotron, Step and Laguna.; Create a free API key at routeway.ai, then paste it here as a Bearer token.; OpenAI-compatible endpoint at https://api.routeway.ai/v1 with a public /models catalog (236 models). Cloudflare fronts the API and requires a browser-style User-Agent. |
| **NaraRouter** | [bynara.id](https://bynara.id) | `https://router.bynara.id/v1` | agnes-2.0-flash, agnes-2.5-flash, laguna-s-2.1, minimax-m3-free | Free plan: one 7M tokens/day bucket per account (15 req/min) across the plan's 8 models; others need credit.; Create a free NaraRouter account, link your Telegram (required before /v1 answers), then paste the key here as a Bearer token.; OpenAI-compatible endpoint at https://router.bynara.id/v1. Free-tier models are pinned; others need credit. |
| **Regolo AI** | [regolo.ai](https://regolo.ai) | `https://api.regolo.ai` | regolo-chat, regolo-fast | Get your Regolo API key from regolo.ai, then paste it here as a Bearer token.; OpenAI-compatible endpoint at https://api.regolo.ai/v1 with dynamic model discovery (19 models). |
| **Void AI** | [voidai.app](https://voidai.app) | `https://api.voidai.app/v1` | — | The public model catalog marks some models with a free plan requirement, but access is conditional and no numeric quota is confirmed.; Use https://api.voidai.app/v1 only after confirming authentication, account eligibility and terms. Treat this integration as experimental until the blocked documentation becomes public. |
| **HelixMind** | [helixmind.online](https://helixmind.online) | `https://helixmind.online/v1` | — | Previously circulated 3 RPM/50 RPD and no-card claims were not confirmed during the 2026-08-02 audit; current quota and billing require account verification.; Create a helix- key and use https://helixmind.online/v1. OpenAI requests use Bearer authentication; the Anthropic-compatible messages endpoint accepts x-api-key. |
| **Logfare** | [logfare.ai](https://logfare.ai) | `https://logfare.ai/v1` | — | Free OpenAI-compatible inference — no rate limits, no card. Logfare logs every request (prompts, completions, metadata) for internal research; opt out at /consent. Read https://logfare.ai/tos and https://logfare.ai/privacy before use.; Create a free account at https://logfare.ai/register (username/password, no email verification) to get an instant API key, then paste it here as a Bearer token.; Create a free API k… |
| **TabiToken** | [tabitoken.com](https://tabitoken.com) | `https://tabitoken.com/v1` | claude-opus-5, claude-opus-5-thinking, claude-opus-4-8, claude-opus-4-8-thinking | Create an sk- key at https://tabitoken.com and use https://tabitoken.com. The Anthropic-compatible /v1/messages endpoint (default) takes x-api-key; /v1/chat/completions takes Bearer. |
| **SeekAi** | [seekai.cc](https://seekai.cc) | `https://seekai.cc/v1` | — | Signup credit toward available models; amount and eligibility are set by SeekAi, not OmniRoute.; Create an API key at https://seekai.cc, then paste it here as a Bearer token.; Create an API key at https://seekai.cc, then paste it here as a Bearer token. OpenAI-compatible base URL: https://seekai.cc/v1. |
| **OmniRoute** | [github.com](https://github.com/diegosouzapw/OmniRoute) | `http://localhost:3000/v1` | kimi-k2.7-code, claude-sonnet-4, gpt-5.5, glm-5.3 | Open-source MIT AI gateway (352 providers, 1200+ models). Self-hosted OpenAI-compatible endpoint; quota-aware auto-fallback. |
| **Bifrost** | [github.com](https://github.com/maximhq/bifrost) | `http://localhost:8080/v1` | 1000+ models | Open-source Go gateway; adaptive load balancing, guardrails, virtual keys. |

## Aggregators & API Marketplaces

Single API key to access models from multiple upstream vendors.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **AIMLAPI** | [aimlapi.com](https://aimlapi.com) | `https://api.aimlapi.com/v1` | gpt-4o, claude-3-5-sonnet, gemini | 300+ models; free tier available |
| **Eden AI** | [edenai.co](https://edenai.co) | `https://api.edenai.co/v2` | OpenAI, Google, Anthropic routes | Multi-provider under one API |
| **LemonData** | [lemondata.ai](https://lemondata.ai) | `https://api.lemondata.ai/v1` | gpt-4o, claude-3.5, open models | 300+ models; $1 free credits |
| **Coze (ByteDance)** | [coze.com](https://coze.com) | `https://api.coze.com/v1` | Via bots: GPT-4o, Gemini, Claude | Bot-builder platform with LLM backends |
| **302.AI** | [302.ai](https://302.ai) | `https://api.302.ai/v1` | glm-5, gpt-4o, claude-sonnet-4 | OpenCode-supported; unified OpenAI-compatible gateway for 100+ models |
| **FrogBot** | [frogbot.ai](https://frogbot.ai) | `https://app.frogbot.ai/api` | claude-sonnet-4, gpt-4o, gemini-2.5-pro | OpenCode-supported; unified AI subscription for chat, embeddings, audio, and images |
| **AnyAPI AI** | [anyapi.ai](https://anyapi.ai) | `https://api.anyapi.ai/v1` | — | Free plan: 100,000 ANY Tokens/day and 100 RPM for eligible Free/Basic models; no credit card required.; Create and verify an AnyAPI account, then use https://api.anyapi.ai/v1 as the OpenAI-compatible base URL. |
| **Electron Hub** | [www.electronhub.ai](https://www.electronhub.ai) | `https://api.electronhub.ai/v1` | — | Free plan: 5 RPM, $0.25 weekly credits and 10 Neutrinos/day for :free models; family budgets also apply.; Create a free API key at https://app.electronhub.ai, then use https://api.electronhub.ai/v1 as the OpenAI-compatible base URL. |
| **ChatAnywhere** | [chatanywhere.tech](https://chatanywhere.tech) | `https://api.chatanywhere.org/v1` | — | Personal, educational or research use only: public documentation cites 10,000 points/day and 200 requests/day per IP/key; do not use for commercial traffic.; Create a ChatAnywhere key linked to GitHub, then use https://api.chatanywhere.org/v1 outside China. Review the non-commercial terms before enabling it. |
| **Naga AI** | [naga.ac](https://naga.ac) | `https://api.naga.ac/v1` | — | Models marked :free are publicly listed, but no numeric quota is confirmed. Naga's policy warns that free-tier prompts and outputs may be collected or used for training.; Create a Naga AI Bearer key, then use https://api.naga.ac/v1 as the OpenAI-compatible base URL. Never send sensitive data to the free tier without accepting its training policy. |
| **PiAPI** | [piapi.ai](https://piapi.ai) | `https://api.piapi.ai` | — | Multi-vendor model marketplace under one API key. |
| **GoAPI** | [api.getgoapi.com](https://api.getgoapi.com) | `https://api.getgoapi.com/v1` | — | Multi-vendor model marketplace under one API key. |
| **TheB.AI** | [theb.ai](https://theb.ai) | `https://api.theb.ai/v1` | — | Bearer API key for the TheB.AI OpenAI-compatible gateway. |
| **Poe** | [creator.poe.com](https://creator.poe.com/api-reference) | `https://api.poe.com` | gpt-5.2, claude-opus-4.8, gemini-3.0-pro | Bearer API key for the Poe OpenAI-compatible API.; Poe exposes OpenAI-compatible chat and responses on https://api.poe.com/v1, with authenticated balance checks on /usage/current_balance. |
| **Naga.ac** | [naga.ac](https://naga.ac) | `https://api.naga.ac/v1` | — | Free models include Nemotron 3 Ultra (free) and Llama 3.3 70B Instruct (Free). Paid models require credits. Google/GitHub/Discord signup.; Get API key at naga.ac — Google/GitHub/Discord signup available. |

## Discount & Budget APIs

Lower-cost resale or discounted access to frontier model families.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **DiscountedTokens** | [discountedtokens.com](https://discountedtokens.com) | `https://discountedtokens.com/v1` | GPT-5.5, GPT-5.4, GPT-5.6 | Budget resale of GPT-5.x family; OpenAI/Anthropic/Responses compatible; ~80% below retail |

## OAuth & IDE Subscriptions

Sign-in with an existing IDE or CLI subscription (Claude Code, Codex, Cursor, Copilot, …). No separate API key in many cases.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **GitHub Enterprise Copilot** | [docs.github.com](https://docs.github.com/en/copilot) | `https://api.githubcopilot.com` | claude-fable-5, claude-opus-5, claude-opus-4.8-fast, claude-opus-4.8 | Enter your GHE instance URL (e.g., https://ghe.company.com) in provider settings, then authenticate via device flow. |
| **xAI OAuth (Grok)** | [x.ai](https://x.ai) | OAuth (provider-specific) | grok-4.5 | Sign in with xAI to use api.x.ai models such as Grok 4.5. This is separate from Grok Build JWT sessions, which use cli-chat-proxy.grok.com and grok-build model aliases. |
| **Openference** | [openference.com](https://openference.com) | `https://api.openference.com/v1` | GLM-5.2 | Free plan: 3-day trial with open-source models — no credit card required; Sign in with your Openference account to route requests through api.openference.com. An active plan is required for inference — OAuth may authenticate but return 402 without one. |
| **Grok Build** | [x.ai](https://x.ai) | `https://cli-chat-proxy.grok.com/v1` | grok-4.6, grok-4.5, grok-composer-2.5-fast | Sign in with your browser, or paste your ~/.grok/auth.json (or the JWT access token) from the Grok Build CLI; refresh_token is rotated automatically either way. |
| **Qoder** | [qoder.com](https://qoder.com) | `https://api.qoder.com/v1` | qwen3.8-max-preview, qwen3.7-max, qwen3.7-plus, kimi-k3 | OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases. |
| **Antigravity CLI** | [antigravity.google](https://antigravity.google) | OAuth (provider-specific) | — | Import your Antigravity CLI (`agy`) login (paste/upload its token file), auto-detect a local CLI login, or sign in with Google. Shares the Antigravity backend (incl. Claude models). |
| **Kiro AI** | [kiro.dev](https://kiro.dev) | `https://codewhisperer.us-east-1.amazonaws.com/generateAssistantResponse` | claude-sonnet-5, claude-sonnet-4.5, claude-haiku-4.5, deepseek-3.2 | Free tier: 50 credits/month (~25K–100K tokens). ⚠️ Kiro ToS prohibits third-party proxy/harness use. |
| **Amazon Q** | [aws.amazon.com](https://aws.amazon.com/q/developer) | OAuth (provider-specific) | — | Uses the same AWS Builder ID or imported refresh-token flow as Kiro, but keeps Amazon Q connections separate. |
| **Claude Code** | [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code) | `https://api.anthropic.com/v1` | claude-fable-5-1, claude-fable-5, claude-opus-5, claude-opus-4-8 | OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases. |
| **Antigravity** | [antigravity.google](https://antigravity.google) | OAuth (provider-specific) | — | OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases. |
| **OpenAI Codex** | [developers.openai.com](https://developers.openai.com/codex) | `https://chatgpt.com/backend-api/codex` | gpt-6-astra, gpt-6-astra-ultra, gpt-6-astra-max, gpt-6-astra-xhigh | OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases. |
| **Cursor IDE** | [cursor.com](https://cursor.com) | `https://api2.cursor.sh` | auto, auto-cost, auto-balance, auto-intelligence | OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases. |
| **Zed IDE** | [zed.dev](https://zed.dev) | OAuth (provider-specific) | — | Zed stores LLM provider credentials (OpenAI, Anthropic, Google, Mistral, xAI) in the OS keychain. Use the Import button below to discover and import them automatically. |
| **Zed Hosted Models** | [zed.dev](https://zed.dev) | `https://cloud.zed.dev` | — | Sign in with your Zed account (native-app sign-in). OmniRoute generates a one-time RSA keypair and opens zed.dev to authorize it — on a remote/headless install, copy the resulting 127.0.0.1 callback URL from your browser's address bar and paste it back here. Distinct from the 'Zed IDE' credential-import entry above: this proxies chat completions through Zed's own hosted model aggregator (cloud.zed.dev), fronting A… |
| **Trae** | [trae.ai](https://trae.ai) | `https://core-normal.trae.ai/api/remote/v1` | auto, work, gemini-3.1-pro, gemini-3-flash-solo | Trae is an AI-native IDE by ByteDance (SOLO remote agent). Authorize via trae.ai in the popup, or sign in at solo.trae.ai and paste the Cloud-IDE-JWT (sent as 'Authorization: Cloud-IDE-JWT <token>', ~14-day lifetime) as the access token; web_id/biz_user_id/user_unique_id/scope/tenant/region propagate via providerSpecificData. No headless refresh for pasted tokens — re-paste on expiry. |
| **Kimi Code CLI** | [www.kimi.com](https://www.kimi.com/code) | OAuth (provider-specific) | — | Sign in with the same Kimi account used by Kimi Code CLI. OmniRoute uses the CLI OAuth flow and Kimi Coding Plan endpoints. |
| **Kilo Code** | [kilocode.ai](https://kilocode.ai) | `https://api.kilo.ai/api/openrouter` | openrouter/free, openai/gpt-5.6-sol, openai/gpt-5.6-terra, openai/gpt-5.6-luna | OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases. |
| **Cline** | [cline.bot](https://cline.bot) | `https://api.cline.bot/api/v1` | z-ai/glm-5.2, x-ai/grok-4.5, openai/gpt-5.6-sol, moonshotai/kimi-k3 | OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases. |
| **ClinePass** | [cline.bot](https://cline.bot/cline-pass) | `https://api.cline.bot/api/v1` | cline-pass/glm-5.2, cline-pass/minimax-m3, cline-pass/deepseek-v4-pro, cline-pass/deepseek-v4-flash | ClinePass is Cline's $9.99/mo subscription bundling 10 open coding models. Sign in with your Cline account (same login as the Cline CLI/IDE), or paste a direct ClinePass API key (app.cline.bot → Settings → API Keys). A ClinePass subscription unlocks the cline-pass/* models. Reuses the Cline WorkOS OAuth flow. |
| **Devin Desktop** | [devin.ai](https://devin.ai) | `https://server.codeium.com` | — | Paste an existing Devin API key from an authenticated Devin session. Key export availability and steps vary by Devin version and account. |
| **Devin CLI** | [cli.devin.ai](https://cli.devin.ai) | OAuth (provider-specific) | — | Requires the Devin CLI binary. Run `devin auth login` to authenticate, or provide your WINDSURF_API_KEY. Install: https://cli.devin.ai |
| **CodeBuddy CN** | [copilot.tencent.com](https://copilot.tencent.com) | `https://copilot.tencent.com/v2` | glm-5.2, glm-5.1, glm-5.0, glm-5.0-turbo | Tencent CodeBuddy CN (copilot.tencent.com). Sign in via the official CLI device-code flow, or paste a direct API key (sent as Authorization: Bearer). Catalog: GLM / Kimi / MiniMax / DeepSeek / Hunyuan. |

## Web Cookie / Browser Sessions

Unofficial adapters that reuse a signed-in web-app session. Treat these as personal-use integrations; they can break when the upstream UI changes.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **ChatGPT Web (Clean Room)** | [chatgpt.com](https://chatgpt.com) | `https://chatgpt.com` | gpt-5-6, gpt-5-6-thinking, gpt-5-6-pro, gpt-5.6-luna-free | Paste Playwright-compatible storage-state JSON exported from a logged-in chatgpt.com browser context. Cookie headers and individual token values are not accepted. |
| **ChatGPT Web (Codex)** | [chatgpt.com](https://chatgpt.com) | `https://chatgpt.com` | luna, think, instant, medium | Paste the full ChatGPT Cookie header. OmniRoute verifies it in an isolated headless browser profile. |
| **Grok Web (Subscription)** | [grok.com](https://grok.com) | `https://grok.com/rest/app-chat/conversations/new` | fast, expert, heavy, grok-420-computer-use-sa | Paste the full grok.com cookie line from DevTools → Application → Cookies. Include both `sso` and `sso-rw` (e.g. `sso=...; sso-rw=...`) — Grok's anti-bot rejects `sso` on its own. |
| **Gemini Web (Free)** | [gemini.google.com](https://gemini.google.com) | `https://gemini.google.com/app` | gemini-3.1-pro, gemini-3.7-flash, gemini-3.1-flash-lite | Paste the full cookie header, the __Secure-1PSID value, or the JSON export containing cookies from gemini.google.com. Include __Secure-1PSIDTS and __Secure-1PSIDCC when available. |
| **Perplexity Web (Pro/Max)** | [www.perplexity.ai](https://www.perplexity.ai) | `https://www.perplexity.ai/rest/sse/perplexity_ask` | pplx-auto, pplx-sonar, pplx-gpt-5.6-terra, pplx-gpt-5.6-sol | Paste your __Secure-next-auth.session-token cookie value from perplexity.ai |
| **Blackbox Web (Subscription)** | [app.blackbox.ai](https://app.blackbox.ai) | `https://app.blackbox.ai/api/chat` | gpt-4-turbo, gpt-4, gpt-3.5-turbo, claude-3-opus | Paste your __Secure-authjs.session-token value or full cookie header from app.blackbox.ai |
| **Muse Spark Web (Meta AI)** | [www.meta.ai](https://www.meta.ai) | `https://www.meta.ai/api/graphql` | muse-spark, muse-spark-thinking, muse-spark-contemplating | Free with login — Meta AI platform with Llama models.; Paste your ecto_1_sess cookie AND the ecto1:... WS auth token from meta.ai. Capture the ecto1: token in DevTools → Network → WS → the clippy request's Authorization query param. Example: ecto_1_sess=4240a308...NVDg0; ecto1:ABCD... |
| **Claude Web** | [claude.ai](https://claude.ai) | `https://claude.ai/api/organizations` | claude-fable-5-1, claude-fable-5, claude-opus-5, claude-opus-4-8 | Paste your session cookie from claude.ai |
| **DeepSeek Web** | [chat.deepseek.com](https://chat.deepseek.com) | `https://chat.deepseek.com/api/v0/chat/completion` | deepseek-v4-pro, deepseek-v4-pro-think, deepseek-v4-pro-search, deepseek-v4-pro-think-search | Paste your userToken from chat.deepseek.com — DevTools → Application → Local Storage → userToken |
| **Microsoft Copilot Web** | [copilot.microsoft.com](https://copilot.microsoft.com) | Web cookie / browser session | copilot-pro, gpt-4-turbo, gpt-4 | Paste the access_token from an authenticated copilot.microsoft.com request (DevTools → Network → Authorization), or export a HAR while logged in |
| **Microsoft 365 Copilot (BizChat)** | [m365.cloud.microsoft](https://m365.cloud.microsoft/chat) | Web cookie / browser session | copilot-m365, copilot-m365-claude-opus, copilot-m365-gpt-5-6-reasoning, copilot-m365-gpt-5-5-chat | Sign in at m365.cloud.microsoft/chat, then open DevTools → Network → filter 'WS' → click the Chathub WebSocket connection. Copy both the access_token query parameter AND the account-specific Chathub path segment from its request URL (wss://…/Chathub/<path>?…&access_token=…). It is NOT an Authorization: Bearer header on an XHR/Fetch request. The token is short-lived; this is an unofficial integration. Optional: sto… |
| **t3.chat (Pro/Free)** | [t3.chat](https://t3.chat) | `https://t3.chat/api/chat` | claude-opus-4, claude-sonnet-4, claude-haiku-4, claude-3.7 | Free tier gives limited model access. Pro ($8/month) unlocks 50+ models.; Open t3.chat in your browser, log in, then open DevTools → Application → Local Storage → https://t3.chat. Copy the value of 'convex-session-id'. Also open DevTools → Network, copy the Cookie header from any request. Paste both values here. See provider setup docs for a step-by-step guide. |
| **Inner.ai (Subscription)** | [app.innerai.com](https://app.innerai.com) | `https://chatapi.innerai.com/chat` | gpt-4o, gpt-4.1, gpt-4.1-mini, o3 | Paste your token cookie and email separated by a space: open DevTools → Application → Cookies → .innerai.com, copy the token value, then append a space and your Inner.ai login email. Example: eyJhbG... user@example.com |
| **Adapta.org (Adapta One Web)** | [agent.adapta.one](https://agent.adapta.one) | `https://agent.adapta.one/api/chat/stream/v1` | adapta-one, adapta-gpt, adapta-claude, adapta-gemini | Paste your __client cookie value from .clerk.agent.adapta.one (DevTools → Application → Cookies) |
| **Arena (Free)** | [arena.ai](https://arena.ai) | `https://arena.ai/nextjs-api/stream/create-evaluation` | — | Free model comparison platform (formerly LMArena) at arena.ai — Direct-chat catalog of chat models (GPT, Claude, Gemini, Llama, …). No subscription required.; Paste the full Cookie header from arena.ai (DevTools → Network → request → Cookie). Include arena-auth-prod-v1.0/.1… and cf_clearance/__cf_bm when present. OmniRoute uses Chrome TLS impersonation; if Arena still 403s, set providerSpecificData.recaptchaV3Toke… |
| **Tencent Yuanbao (Free)** | [yuanbao.tencent.com](https://yuanbao.tencent.com) | `https://yuanbao.tencent.com/api/chat` | deepseek-v3, deepseek-r1, hunyuan, hunyuan-t1 | Free consumer web session — DeepSeek V3/R1 and Hunyuan / Hunyuan-T1, optional web search. No subscription required. Rate limits apply.; Log in to yuanbao.tencent.com, then paste the full Cookie header (DevTools → Network → any /api request → Request Headers → Cookie). It must contain hy_user and hy_token. |
| **Tencent AI Studio (Free)** | [aistudio.tencent.ai](https://aistudio.tencent.ai) | `https://aistudio.tencent.ai/api/chat` | hy3-g, hunyuan-default, hunyuan-3d | Free web session on Tencent AI Studio (aistudio.tencent.ai) — Direct chat with Hunyuan models (hy3-g, HunyuanDefault, Hunyuan3D). Cookie authentication.; Log in to aistudio.tencent.ai, open DevTools -> Network, copy any request Cookie header containing session tokens. |
| **HuggingChat (Free)** | [huggingface.co](https://huggingface.co/chat) | `https://huggingface.co/chat/conversation` | baidu/ERNIE-4.5-VL-424B-A47B-Base-PT, CohereLabs/c4ai-command-r7b-12-2024, CohereLabs/command-a-reasoning-08-2025, CohereLabs/command-a-vision-07-2025 | Free LLM chat — no subscription required. Rate limits apply.; Paste the full Cookie header from huggingface.co/chat (DevTools → Network → /chat/conversation → Request Headers → Cookie). It should include hf-chat and may also include token / aws-waf-token. |
| **Poe Web (Subscription)** | [poe.com](https://poe.com) | Web cookie / browser session | — | Paste your p-b cookie value from poe.com (DevTools → Application → Cookies → p-b) |
| **Venice Web (Privacy)** | [venice.ai](https://venice.ai) | Web cookie / browser session | — | Paste your session cookie from venice.ai (DevTools → Application → Cookies) |
| **v0 Vercel Web (Code Gen)** | [v0.dev](https://v0.dev) | Web cookie / browser session | — | Paste your session cookie from v0.dev (DevTools → Application → Cookies) |
| **Kimi Web** | [www.kimi.ai](https://www.kimi.ai) | `https://www.kimi.ai` | k3, k2d6 | Paste access_token from www.kimi.ai DevTools → Application → Local Storage. A legacy kimi-auth cookie is also accepted. |
| **Dola Web (ByteDance)** | [www.dola.com](https://www.dola.com) | `https://www.dola.com/chat/completion` | dola-speed, dola-pro | Paste the full Cookie header from www.dola.com. It should include sessionid, ttwid, and s_v_web_id. If s_v_web_id is unavailable, fp=verify_... from a chat/completion request URL can be used as a fallback. |
| **Gemini Business (Enterprise)** | [business.gemini.google](https://business.gemini.google) | `https://business.gemini.google/home` | gemini-3-pro, gemini-3-ultra, gemini-3-flash, gemini-2.5-pro | Free for Google Workspace enterprise accounts — enterprise Gemini models (Pro, Flash, image, video) via direct StreamGenerate HTTP API. No subscription required, just enterprise SSO.; From your enterprise account: open business.gemini.google/home/cid/{your-cid}, then copy __Secure-1PSID and __Secure-1PSIDTS cookies from DevTools → Application → Cookies. Paste as a cookie header below. |
| **ZenMux Free (Web)** | [zenmux.ai](https://zenmux.ai) | `https://zenmux.ai/api/anthropic/v1` | deepseek/deepseek-chat, deepseek/deepseek-reasoner, deepseek/deepseek-v4-pro, kuaishou/kat-coder-pro-v1-free | Free tier (5 Flows/5h, 38.64 Flows/week) — DeepSeek V3.2, GLM 4.7 Flash Free and more. No subscription required.; Login at zenmux.ai, then export all cookies using EditThisCookie or Cookie-Editor and paste the full Cookie header string here. Refresh every ~30 days. |
| **TinyCMS Web (Free/Sub)** | [site.tinycms.xyz](https://site.tinycms.xyz) | `https://gov.freegpt.win/api/openai/oneapi/v1` | claude-fable-5, claude-opus-5, claude-sonnet-5, gpt-5.6-sol | Free tier has access to GPT 5.4, Gemini 3.5, and Grok 4.20 models. No login required. Subscription grants 300 requests/day for advanced models.; Go to site.tinycms.xyz, open DevTools → Application → Local Storage, copy the value of 'app-config-uuid' (starts with 'R'), and paste it here. |
| **Z.ai Web** | [chat.z.ai](https://chat.z.ai) | `https://chat.z.ai` | glm-5.3-flash, glm-5.3, glm-5.2 | Consumer web session for the four models currently visible in chat.z.ai. Distinct from the API-key zai/glm providers.; Copy the "token" value from chat.z.ai → DevTools → Application → Local Storage. Do not copy cookies; OmniRoute handles the per-request CAPTCHA through its browser transport. |
| **PromptQL (Unofficial/Experimental)** | [prompt.ql.app](https://prompt.ql.app) | `https://data.prompt.ql.app/promptql/playground-v2-hge/v1/graphql` | — | Paste the Bearer JWT from prompt.ql.app DevTools → Network → graphql → Authorization (token only). Optional projectId + session Cookie for refresh. |
| **Notion AI Web (Unofficial/Experimental)** | [www.notion.so](https://www.notion.so) | `https://app.notion.com/api/v3/runInferenceTranscript` | — | Paste only the token_v2 cookie VALUE from app.notion.com (DevTools → Application → Cookies → token_v2). Do not paste token_v2= or the full Cookie header. Workspace is auto-detected; space_id / notion_user_id are optional. |
| **Adobe Firefly (Image/Video)** | [firefly.adobe.com](https://firefly.adobe.com) | Web cookie / browser session | — | RECOMMENDED: firefly.adobe.com signed-in → F12 → Network → click firefly-3p.ff.adobe.io (generate-async or models/discovery) → Request Headers → Authorization → copy the token AFTER 'Bearer ' (starts with eyJ…). Cookie-only from firefly.adobe.com mints a GUEST token → 401/403; only multi-domain IMS cookies (adobelogin.com) or that Bearer JWT work. Unofficial/experimental media + Limits. |
| **HyperAgent (Unofficial/Experimental)** | [hyperagent.com](https://hyperagent.com) | `https://hyperagent.com/api/threads` | — | Paste the full Cookie header from hyperagent.com (DevTools → Network → any request → Request Headers → Cookie). Session cookies power chat + billing usage. |
| **Conol (Unofficial/Experimental)** | [conol.ai](https://conol.ai) | `https://conol.ai/api/sessions` | — | Use browser sign-in, or paste the full Cookie header from conol.ai. The __Secure-better-auth.session_token cookie is required. |
| **MaxAI** | [www.maxai.co](https://www.maxai.co) | `https://api.maxai.me` | — | Sign in once (email code or browser) to mint a MaxAI access token. OmniRoute signs each request, routes it through residential egress, and refreshes the token browserlessly, so a connection stays valid for about a year without re-login. |
| **UC (uncensored.com)** | [uncensored.com](https://uncensored.com) | `https://internal-6.pubyar.com` | — | Sign in once with an email code to bootstrap a UC (uncensored.com) subscription session. OmniRoute mints a fresh short-lived token per request browserlessly, so the connection renews on its own; you only re-run the email login about once a month when the subscription session rolls over. |

## No-auth & Public Endpoints

Public or anonymous endpoints that require no API key (rate limits usually apply).

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Devin CLI Agentic Bridge** | [docs.devin.ai](https://docs.devin.ai/work-with-devin/devin-cli) | No-auth public endpoint | — | Authentication is owned by the official Devin CLI in its isolated bridge volume.; This provider accepts only the official Devin CLI over local ACP stdio and never falls back to another provider. |
| **OpenCode Free** | [opencode.ai](https://opencode.ai) | `https://opencode.ai/zen/v1` | big-pickle, muse-spark-1.2, muse-spark-1.2-contributor-free, muse-spark-1.3 | No API key required — public OpenCode endpoint with Kimi, GLM, Qwen, MiMo, MiniMax models.; No API key required — uses OpenCode's public free endpoint.; OpenCode Free uses the public OpenCode endpoint (https://opencode.ai/zen/v1). No signup or API key needed. Rate limits apply. |
| **DuckDuckGo AI Chat** | [duckduckgo.com](https://duckduckgo.com/duckchat) | `https://duck.ai/duckchat/v1/chat` | gpt-5.4-mini, gpt-5.6-luna, claude-haiku-4-5, mistral-small-2603 | Free — anonymous access to multiple AI models via DuckDuckGo.; No credentials required — DuckDuckGo AI Chat is anonymous and free. |
| **Cloudflare AI Playground** | [playground.ai.cloudflare.com](https://playground.ai.cloudflare.com) | `https://playground.ai.cloudflare.com` | zai-org/glm-5.2, moonshotai/kimi-k2.7-code, moonshotai/kimi-k2.6, deepseek-ai/deepseek-v4-pro-0813 | Free — Cloudflare's AI Playground: GLM 5.2, Kimi K2.7 Code, DeepSeek V4 Pro, gpt-oss-120B and 16 more. No account, no API key.; No credentials required — anonymous browser sessions over a reverse-engineered cf_agent WebSocket protocol (Playwright transport).; Cloudflare AI Playground uses a reverse-engineered anonymous WebSocket protocol (no official API). Requires Playwright with a Chromium browser on first reque… |
| **Chipotle Pepper AI (Free)** | [amelia.chipotle.com](https://amelia.chipotle.com) | `https://amelia.chipotle.com` | pepper-1 | Free — Chipotle's Pepper AI (IPsoft Amelia). Anonymous sessions, no API key. Rate-limited.; No credentials required. Uses Chipotle's public support chatbot via reverse-engineered SockJS/STOMP protocol. |
| **Augment (Auggie CLI)** | [augmentcode.com](https://augmentcode.com) | No-auth public endpoint | sonnet4.6, fable-5, haiku4.5, sonnet4.5 | Local passthrough — runs the Augment CLI (`auggie`) on this machine. Auth is handled by `auggie login`, not OmniRoute.; No API key stored by OmniRoute. Install the Auggie CLI and run `auggie login` on this machine, then OmniRoute spawns it locally for each request.; Augment (Auggie CLI) requires the `auggie` binary installed and authenticated locally (`auggie login`). OmniRoute spawns it as a subprocess and never… |
| **ZCode (GLM Coding Plan)** | [zcode.z.ai](https://zcode.z.ai) | No-auth public endpoint | — | No API key stored by OmniRoute. The local ZCode app-server uses the existing builtin:zai-coding-plan login.; ZCode runs locally through its native app-server. OmniRoute never receives or stores the Z.ai credential. |
| **OpenAI Codex (App-Server)** | [developers.openai.com](https://developers.openai.com/codex/cli) | No-auth public endpoint | — | No token stored by OmniRoute. The Codex CLI app-server manages its own ChatGPT sign-in (~/.codex/auth.json, auto-refreshed). Use u201cSign in with ChatGPTu201d if the CLI is not yet authenticated.; OpenAI Codex (App-Server) drives the Codex CLI's local app-server (JSON-RPC over WebSocket). The CLI self-manages its OpenAI OAuth, so OmniRoute never sees or replays your token. Requires the codex CLI reachable at the… |
| **UncloseAI** | [uncloseai.com](https://uncloseai.com) | `https://hermes.ai.unturf.com/v1` | adamo1139/Hermes-3-Llama-3.1-8B-FP8-Dynamic, qwen3.6:27b, gemma4:31b | Free forever — no signup, no credit card. OpenAI-compatible endpoints.; No auth required. API accepts any non-empty string as key for identification. If older built-in models return 404, use Available Models → Import from /models or Auto-Sync; verified live model: solidrust/Hermes-3-Llama-3.1-8B-AWQ.; UncloseAI needs no API key. API accepts any non-empty string as key for identification. If older built-in models r… |
| **AI Horde** | [aihorde.net](https://aihorde.net) | `https://oai.aihorde.net/v1` | aphrodite/TheDrummer/Cydonia-24B-v4.3, aphrodite/TheDrummer/Skyfall-31B-v4.2, google/gemma-4-31b | Crowdsourced inference from volunteer GPUs. Throughput is a shared queue, not a quota: there is no RPM/RPD cap, but waits grow when the network is busy.; No API key required — uses AI Horde's documented anonymous key. Adding a free aihorde.net key is optional and only buys higher queue priority (kudos).; AI Horde routes to volunteer-run workers, so chat and image jobs can take minutes and tool calling is unavailab… |

## Search APIs

Web search, fetch, and crawl APIs used alongside LLM apps.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Perplexity Search** | [docs.perplexity.ai](https://docs.perplexity.ai/guides/search-quickstart) | `https://api.perplexity.ai` | — | Same API key as Perplexity (pplx-...) |
| **Serper Search** | [serper.dev](https://serper.dev) | `https://google.serper.dev` | — | API key from serper.dev dashboard |
| **Brave Search** | [brave.com](https://brave.com/search/api) | `https://api.search.brave.com/res/v1` | — | Subscription token from Brave Search API dashboard |
| **Exa Search** | [exa.ai](https://exa.ai) | `https://api.exa.ai` | — | API key from dashboard.exa.ai |
| **Tavily Search** | [tavily.com](https://tavily.com) | `https://api.tavily.com` | — | API key from app.tavily.com (format: tvly-...) |
| **AnySearch** | [anysearch.com](https://anysearch.com) | `https://api.anysearch.com` | — | Optional API key from anysearch.com (as_sk_...) - free 1000/day; keyless tier has lower limits |
| **Firecrawl** | [firecrawl.dev](https://firecrawl.dev) | `https://api.firecrawl.dev/v1` | — | API key from firecrawl.dev/app/api-keys (or set your self-hosted Firecrawl base URL); Free tier: 1,000 credits/month. Powers /v1/web/fetch and /v1/search. |
| **Google Programmable Search** | [developers.google.com](https://developers.google.com/custom-search/v1/overview) | `https://www.googleapis.com/customsearch/v1` | — | Requires a Google API key and your Programmable Search Engine ID (cx) |
| **Nimble Search** | [docs.nimbleway.com](https://docs.nimbleway.com/nimble-sdk/web-tools/search) | `https://api.webit.live` | — | Bearer API key from the Nimble dashboard |
| **Linkup Search** | [docs.linkup.so](https://docs.linkup.so) | `https://api.linkup.so` | — | Bearer API key from the Linkup dashboard |
| **SearchAPI** | [www.searchapi.io](https://www.searchapi.io/docs/google) | `https://www.searchapi.io/api/v1/search` | — | API key from SearchAPI (query param or Bearer auth) |
| **You.com Search** | [you.com](https://you.com/business/api) | `https://api.ydc-index.io` | — | X-API-Key from the You.com platform dashboard |
| **SearXNG Search** | [docs.searxng.org](https://docs.searxng.org) | `http://localhost:8080` | — | API key is optional. Set your SearXNG base URL. Some instances may require a bearer token for access. |
| **X Search (Grok)** | [docs.x.ai](https://docs.x.ai/developers/tools/x-search) | `https://api.x.ai/v1` | — | SuperGrok OAuth (xai-oauth) or xAI API key. This is Grok X Search, not the X Developer MCP. |
| **Xquik X Search** | [docs.xquik.com](https://docs.xquik.com) | `https://api.xquik.com` | — | Xquik API key (xq_...). Search is metered per returned post; the catalog estimate uses 5 results. |
| **Ollama Search** | [ollama.com](https://ollama.com/settings/keys) | `https://ollama.com/api` | — | Same API key as Ollama Cloud (from ollama.com/settings/keys) |
| **Context7 (library docs)** | [context7.com](https://context7.com) | `https://context7.com` | — | API key optional (ctx7sk-...) — anonymous tier works without a key; a key raises the rate limit |
| **Jina Reader (r.jina.ai)** | [jina.ai](https://jina.ai/reader) | `https://r.jina.ai` | — | Bearer API key for r.jina.ai URL-to-markdown (/v1/web/fetch only). Does not serve /v1/embeddings or /v1/rerank. The same Jina token as Foundation API works; OmniRoute reuses a jina-ai dashboard key or JINA_AI_API_KEY when this card is empty.; Reader / r.jina.ai only — not embeddings or rerank. Free tier: 1M fetches/month. |
| **TinyFish Fetch** | [docs.tinyfish.ai](https://docs.tinyfish.ai/fetch-api) | `https://api.tinyfish.ai` | — | X-API-Key from agent.tinyfish.ai/api-keys; Fetch does not use TinyFish credits. Submit up to 10 URLs per request (OmniRoute fetches one URL per call). |

## Audio (TTS / STT)

Speech-to-text and text-to-speech APIs.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Deepgram** | [deepgram.com](https://deepgram.com) | `https://api.deepgram.com/v1` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **AssemblyAI** | [assemblyai.com](https://assemblyai.com) | `https://api.assemblyai.com/v2` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **Soniox** | [soniox.com](https://soniox.com) | `https://api.soniox.com` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **ElevenLabs** | [elevenlabs.io](https://elevenlabs.io) | `https://api.elevenlabs.io/v1` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **Cartesia** | [cartesia.ai](https://cartesia.ai) | `https://api.cartesia.ai` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **Fish Audio** | [fish.audio](https://fish.audio) | `https://api.fish.audio` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **PlayHT** | [play.ht](https://play.ht) | `https://api.play.ht/api/v2` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **Inworld** | [inworld.ai](https://inworld.ai) | `https://api.inworld.ai` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **AWS Polly** | [aws.amazon.com](https://aws.amazon.com/polly) | `https://polly.us-east-1.amazonaws.com` | — | Use AWS Secret Access Key as API key; set providerSpecificData.accessKeyId and optional region. |
| **Gladia** | [gladia.io](https://gladia.io) | `https://api.gladia.io/v2` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **Rev AI** | [www.rev.ai](https://www.rev.ai) | `https://api.rev.ai` | — | Speech-to-text or text-to-speech API. See official docs for keys and model IDs. |
| **Speechmatics** | [www.speechmatics.com](https://www.speechmatics.com) | `https://asr.api.speechmatics.com/v2` | — | Free tier — 8 hours/month, no credit card required. Batch (async) mode only. |

## Image & Video APIs

Image generation, video generation, and related media APIs.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Veo AI Free** | [veoaifree.com](https://veoaifree.com) | `https://veoaifree.com/wp-admin/admin-ajax.php` | veo, seedance | Free video generation — VEO 3.1, Seedance. 6 requests/hour.; No auth required. Rate limited to 6 requests/hour per IP. |
| **Agnes AI** | [agnes-ai.com](https://agnes-ai.com) | `https://apihub.agnes-ai.com/v1` | agnes-2.0-flash, agnes-2.5-flash, agnes-3.0-flash | Permanently free API - no credit card required.; Get API key at agnes-ai.com |
| **Runway** | [docs.dev.runwayml.com](https://docs.dev.runwayml.com) | `https://api.dev.runwayml.com/v1` | — | Use your Runway API key in Authorization: Bearer <key>. OmniRoute targets the current Runway API at https://api.dev.runwayml.com/v1 and sends the required X-Runway-Version header automatically.; Runway video generation is task-based. OmniRoute submits text-to-video or image-to-video jobs, polls /v1/tasks/{id}, and normalizes the finished video outputs back into the OpenAI-like /v1/videos/generations response. |
| **KIE.AI** | [kie.ai](https://kie.ai) | `https://api.kie.ai/v1` | claude-fable-5, claude-opus-5, claude-sonnet-5, claude-haiku-4-5 | Image or video generation API. |
| **Haiper** | [haiper.ai](https://haiper.ai) | `https://api.haiper.ai/v1` | gen2, gen2-image | Get API key at haiper.ai/haiper-api |
| **Leonardo AI** | [leonardo.ai](https://leonardo.ai) | `https://cloud.leonardo.ai/api/rest/v1` | phoenix, sdxl | Get API key at leonardo.ai/developer |
| **Ideogram** | [ideogram.ai](https://ideogram.ai) | `https://api.ideogram.ai` | V_3, V_2A | Get API key at ideogram.ai/docs/api |
| **Magnific** | [www.magnific.com](https://www.magnific.com) | `https://api.magnific.com/v1/ai/mystic` | realism, fluid, zen, flexible | One-time ~€5 API credit for new accounts; pay-per-use afterward.; Get an API key at magnific.com/user/api-keys (header x-magnific-api-key). Legacy Freepik developer keys still work. |
| **Suno** | [suno.ai](https://suno.ai) | `https://studio-api.suno.ai/api/generate/v2` | chirp-fenix, chirp-crow, chirp-v4, chirp-v3-5 | Paste session cookie from suno.ai (Clerk auth) |
| **Udio** | [udio.com](https://udio.com) | `https://www.udio.com/api/generate-proxy` | udio-default | Paste session cookie from udio.com (Supabase auth) |
| **Fal.ai** | [fal.ai](https://fal.ai) | `https://fal.run` | — | Image or video generation API. |
| **Stability AI** | [stability.ai](https://stability.ai) | `https://api.stability.ai` | — | Image or video generation API. |
| **Black Forest Labs** | [blackforestlabs.ai](https://blackforestlabs.ai) | `https://api.bfl.ai` | — | Image or video generation API. |
| **Recraft** | [recraft.ai](https://recraft.ai) | `https://external.api.recraft.ai/v1` | — | Image or video generation API. |
| **Topaz** | [topazlabs.com](https://topazlabs.com) | `https://api.topazlabs.com` | — | Image or video generation API. |
| **Segmind** | [segmind.com](https://segmind.com) | `https://api.segmind.com/v1` | — | Free trial credits on signup, no credit card required (per Segmind's public docs).; Use your Segmind API key in the x-api-key header. OmniRoute targets https://api.segmind.com/v1/<model> and returns the generated image/video bytes directly.; Segmind exposes 200+ hosted image and video models (Flux, SDXL, SD3, Kandinsky, Wan, Hunyuan, LTX, Kling, ...) under a single POST /v1/<model> REST call per model. OmniRoute s… |
| **DeepAI** | [deepai.org](https://deepai.org) | `https://api.deepai.org` | text2img | Use your DeepAI API key. Get one at deepai.org — requires a Pro subscription ($9.99/mo).; DeepAI uses per-endpoint REST calls (e.g. /api/text2img) instead of OpenAI chat/completions. OmniRoute adapts OpenAI image generation requests to DeepAI's /api/{slug} endpoints. |

## Cloud Coding Agents

Long-running hosted coding agents (task-based, not a classic chat completions API).

| Provider | Website | API Base URL | Notes |
|----------|---------|--------------|-------|
| **Google Jules** | [Google Jules](https://jules.google) | `https://jules.google` | Jules API key for creating and managing cloud coding tasks. |
| **Devin** | [Devin](https://devin.ai) | `https://api.devin.ai` | Devin API key for cloud agent sessions. |
| **Codex Cloud** | [Codex Cloud](https://openai.com/codex) | `https://chatgpt.com/backend-api/codex` | OpenAI API key with Codex Cloud task access. |

## Embeddings & Rerankers

Providers focused on retrieval embeddings and reranking.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Voyage AI** | [www.voyageai.com](https://www.voyageai.com) | `https://api.voyageai.com/v1` | voyage-3, voyage-3-lite, rerank-2 | Top-tier retrieval embeddings & rerankers |
| **Jina AI (Foundation API)** | [jina.ai](https://jina.ai) | `https://api.jina.ai/v1` | — | 10M free tokens on signup (non-commercial), no credit card required; Bearer API key for api.jina.ai — embeddings, rerank, classify, segment, and search. Dashboard keys take precedence over JINA_AI_API_KEY. This is not the Reader / r.jina.ai card and does not fetch URLs. |
| **Nomic** | [nomic.ai](https://nomic.ai) | `https://api-atlas.nomic.ai/v1` | — | Free Nomic Embed API. Open-source embeddings, no credit card required.; Get API key at atlas.nomic.ai |
| **Mixedbread AI** | [www.mixedbread.com](https://www.mixedbread.com) | `https://api.mixedbread.com/v1` | — | Free-tier API key via signup, no credit card required.; Bearer API key for the Mixedbread embeddings API. |

## Other Specialized APIs

Providers focused on a specific task rather than general chat.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **NLP Cloud** | [nlpcloud.com](https://nlpcloud.com) | `https://api.nlpcloud.io/v1` | finetuned-llama-3-70b, chatdolphin | NER, summarization, chat; custom API format |
| **Puter.js** | [puter.com](https://puter.com) | `https://api.puter.com/ai/chat` | gpt-4o-mini, claude-3.5-sonnet, gemini | No API key needed; web/Node.js SDK |
| **Pollinations AI** | [pollinations.ai](https://pollinations.ai) | `https://gen.pollinations.ai/v1` | openai, openai-fast, openai-large, qwen-coder | Free keyless tier: openai, openai-fast, openai-large, qwen-coder, mistral, deepseek, grok, gemini-flash-lite-3.1, perplexity-fast, perplexity-reasoning. Premium models (claude, gemini, midijourney) require a Pollinations API key from enter.pollinations.ai.; Anonymous/keyless access to the documented free models is best-effort. Local v3.8.50 verification (2026-07-31) returned 401 via OmniRoute and Cloudflare 1010 o… |
| **v0 (Vercel)** | [v0.dev](https://v0.dev) | `https://api.v0.dev/v1` | — | Specialized API. See official docs for setup. |
| **GitLab Duo PAT** | [docs.gitlab.com](https://docs.gitlab.com/user/duo_agent_platform/code_suggestions) | `https://gitlab.com/api/v4/ai` | — | GitLab personal access token for the public Code Suggestions API. Configure a self-hosted base URL when not using gitlab.com. |
| **Dify** | [dify.ai](https://dify.ai) | `https://api.dify.ai` | auto | Free open-source AI app builder + RAG platform.; Get API key from your Dify instance. |
| **Cursor API** | [cursor.com](https://cursor.com/dashboard/api) | `https://api.cursor.com/v1` | — | Paste a Cursor user API key (crsr_...) from cursor.com/dashboard/api. OmniRoute exchanges it for a session token on demand; no IDE or cursor-agent install is needed. Usage bills to the Cursor plan that owns the key.; Same agent protocol and model catalog as the Cursor IDE provider. The Cursor CLI can also be pointed at /api/cursor-cli on this instance and authenticated with an OmniRoute API key. |

## Local & Self-Hosted Runtimes

Run models on your own machine — **free, private, and unlimited**.

| Provider | Website | API Base URL | Popular Models | Notes |
|----------|---------|--------------|----------------|-------|
| **Ollama** | [ollama.com](https://ollama.com) | `http://localhost:11434/v1` | llama3.3, qwen2.5, gemma | Easiest local setup; 50+ models |
| **LM Studio** | [lmstudio.ai](https://lmstudio.ai) | `http://localhost:1234/v1` | Any GGUF from HuggingFace | Best GUI; drag-and-drop models |
| **llama.cpp** | [github.com](https://github.com/ggml-org/llama.cpp) | `http://localhost:8080/v1` | Any GGUF model | Foundation for most local tools |
| **Jan.ai** | [jan.ai](https://jan.ai) | `http://localhost:1337/v1` | Supported local models | 100% offline desktop app |
| **vLLM** | [github.com](https://github.com/vllm-project/vllm) | `http://localhost:8000/v1` | Any compatible checkpoint | Production-grade local serving |
| **LocalAI** | [localai.io](https://localai.io) | `http://localhost:8080/v1` | OpenAI-compatible local stack | Drop-in OpenAI API replacement |
| **Atomic Chat** | [atomicchat.ai](https://atomicchat.ai) | `http://127.0.0.1:1337/v1` | qwen-coder, deepseek-coder | OpenCode-supported; desktop app with local OpenAI-compatible server |
| **MLX Gemma 26B** | [github.com](https://github.com/ml-explore/mlx) | `http://localhost:${MLX_GEMMA_PORT}/v1` | mlx-community/gemma-4-26B-A4B-it-qat-q4_0-mlx-aligned | No API key required. Runs mlx-lm server locally on port 11435. Requires uv and mlx-lm installed. Model: mlx-community/gemma-4-26B-A4B-it-qat-q4_0-mlx-aligned (~15.9GB peak memory). |
| **MLX Qwen 3.8 27B** | [github.com](https://github.com/ml-explore/mlx) | `http://localhost:${MLX_QWEN_PORT}/v1` | maglun/Qwen3.8-27B-MLX-Mixed-3.80bpw | No API key required. Runs mlx-lm server locally on port 11436. Requires uv and mlx-lm installed. Model: maglun/Qwen3.8-27B-MLX-Mixed-3.80bpw (~13.1GB peak memory). |
| **Lemonade Server** | [lemonade-server.ai](https://lemonade-server.ai) | `http://localhost:13305/api/v1` | — | API key optional. Configure the local Lemonade OpenAI-compatible base URL (default: http://localhost:13305/api/v1). |
| **Llamafile** | [github.com](https://github.com/Mozilla-Ocho/llamafile) | `http://127.0.0.1:8080/v1` | — | API key optional. Configure the local Llamafile OpenAI-compatible base URL (default: http://127.0.0.1:8080/v1). |
| **NVIDIA Triton** | [developer.nvidia.com](https://developer.nvidia.com/triton-inference-server) | `http://localhost:8000/v1` | — | API key optional. Configure the Triton OpenAI-compatible base URL (default: http://localhost:8000/v1). |
| **Docker Model Runner** | [docs.docker.com](https://docs.docker.com/ai/model-runner) | `http://localhost:12434/v1` | — | API key optional. Configure the local Docker Model Runner OpenAI-compatible base URL (default: http://localhost:12434/v1). |
| **XInference** | [inference.readthedocs.io](https://inference.readthedocs.io) | `http://localhost:9997/v1` | — | API key optional. Configure the local XInference OpenAI-compatible base URL (default: http://localhost:9997/v1). |
| **oobabooga** | [github.com](https://github.com/oobabooga/text-generation-webui) | `http://localhost:5000/v1` | — | API key optional. Configure the local oobabooga OpenAI-compatible base URL (default: http://localhost:5000/v1). |
| **SD WebUI** | [github.com](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | `http://localhost:7860` | — | No API key required. Configure the local WebUI base URL (default: http://localhost:7860). |
| **ComfyUI** | [github.com](https://github.com/comfyanonymous/ComfyUI) | `http://localhost:8188` | — | No API key required. Configure the local ComfyUI base URL (default: http://localhost:8188). |

## Environment Variables Cheat Sheet

Copy these into your `.env` file or secrets manager. Providers without a key (local, no-auth, many OAuth/cookie flows) are omitted.

| Provider | Env Variable | API Base URL |
|----------|--------------|--------------|
| OpenAI | `OPENAI_API_KEY` | `https://api.openai.com/v1` |
| Anthropic | `ANTHROPIC_API_KEY` | `https://api.anthropic.com` |
| Google AI Studio | `GEMINI_API_KEY` | `https://generativelanguage.googleapis.com` |
| DeepSeek | `DEEPSEEK_API_KEY` | `https://api.deepseek.com/v1` |
| Mistral AI | `MISTRAL_API_KEY` | `https://api.mistral.ai/v1` |
| xAI | `XAI_API_KEY` | `https://api.x.ai/v1` |
| Cohere | `COHERE_API_KEY` | `https://api.cohere.com/v2` |
| AI21 Labs | `AI21_API_KEY` | `https://api.ai21.com/studio/v1` |
| Baidu Qianfan | `QIANFAN_API_KEY` | `https://api.baiduqianfan.ai/v1` |
| StepFun | `STEPFUN_API_KEY` | `https://api.stepfun.com/v1` |
| Z.ai (Zhipu AI) | `ZHIPU_API_KEY` | `https://open.bigmodel.cn/api/paas/v4/` |
| Xiaomi | `XIAOMI_API_KEY` | `https://api.xiaomimimo.com/v1` |
| Reka AI | `REKA_API_KEY` | `https://api.reka.ai/v1` |
| MiniMax | `MINIMAX_API_KEY` | `https://api.minimax.io/v1` |
| Alibaba DashScope | `DASHSCOPE_API_KEY` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| Upstage | `UPSTAGE_API_KEY` | `https://api.upstage.ai/v1/solar` |
| Perplexity | `PERPLEXITY_API_KEY` | `https://api.perplexity.ai` |
| Voyage AI | `VOYAGE_API_KEY` | `https://api.voyageai.com/v1` |
| Groq | `GROQ_API_KEY` | `https://api.groq.com/openai/v1` |
| Cerebras | `CEREBRAS_API_KEY` | `https://api.cerebras.ai/v1` |
| SambaNova | `SAMBANOVA_API_KEY` | `https://api.sambanova.ai/v1` |
| Together AI | `TOGETHER_API_KEY` | `https://api.together.xyz/v1` |
| Fireworks AI | `FIREWORKS_API_KEY` | `https://api.fireworks.ai/inference/v1` |
| DeepInfra | `DEEPINFRA_API_KEY` | `https://api.deepinfra.com/v1/openai` |
| Nebius AI Studio | `NEBIUS_API_KEY` | `https://api.studio.nebius.ai/v1` |
| SiliconFlow | `SILICONFLOW_API_KEY` | `https://api.siliconflow.cn/v1` |
| Inception | `INCEPTION_API_KEY` | `https://api.inceptionlabs.ai/v1` |
| Liquid AI | `LIQUID_API_KEY` | `https://inference.liquid.ai/v1` |
| Friendli | `FRIENDLI_API_KEY` | `https://api.friendli.ai/serverless/v1` |
| Infermatic | `INFERMATIC_API_KEY` | `https://api.totalgpt.ai` |
| Mancer | `MANCER_API_KEY` | `https://mancer.tech/oai/v1` |
| Morph | `MORPH_API_KEY` | `https://api.morphllm.com/v1` |
| AionLabs | `AION_API_KEY` | `https://api.aionlabs.ai/v1` |
| HuggingFace Inference | `HUGGINGFACE_API_KEY` | `https://router.huggingface.co/v1` |
| NVIDIA NIM | `NVIDIA_API_KEY` | `https://integrate.api.nvidia.com/v1` |
| Hyperbolic | `HYPERBOLIC_API_KEY` | `https://api.hyperbolic.xyz/v1` |
| Lepton AI | `LEPTON_API_KEY` | `https://api.lepton.ai/v1` |
| Kluster.ai | `KLUSTER_API_KEY` | `https://api.kluster.ai/v1` |
| Anyscale Endpoints | `ANYSCALE_API_KEY` | `https://api.endpoints.anyscale.com/v1` |
| Replicate | `REPLICATE_API_TOKEN` | `https://api.replicate.com/v1` |
| Inference.net | `INFERENCE_NET_API_KEY` | `https://api.inference.net/v1` |
| Arcee AI | `ARCEE_API_KEY` | `https://conductor.arcee.ai/v1` |
| Glhf.chat | `GLHF_API_KEY` | `https://glhf.chat/api/openai/v1` |
| AkashML | `AKASHML_API_KEY` | `https://api.akashml.com/v1` |
| AtlasCloud | `ATLASCLOUD_API_KEY` | `https://api.atlascloud.ai/v1` |
| Chutes | `CHUTES_API_KEY` | `https://llm.chutes.ai/v1` |
| Cloudflare Workers AI | `CLOUDFLARE_API_TOKEN` | `https://api.cloudflare.com/client/v4/accounts/{id}/ai/v1` |
| DigitalOcean | `DIGITALOCEAN_API_KEY` | `https://inference.do-ai.run/v1/` |
| GMICloud | `GMI_API_KEY` | `https://api.gmi-serving.com/v1` |
| io.net | `IO_NET_API_KEY` | `https://api.intelligence.io.solutions/api/v1` |
| NextBit | `NEXTBIT_API_KEY` | `https://api.nextbit256.com/v1` |
| Novita | `NOVITA_API_KEY` | `https://api.novita.ai/openai/v1` |
| Parasail | `PARASAIL_API_KEY` | `https://api.saas.parasail.io/v1` |
| Phala | `PHALA_API_KEY` | POST /v1/chat/completions |
| Poolside | `POOLSIDE_API_KEY` | `https://divers.poolsi.de/openai/v1/` |
| Venice | `VENICE_API_KEY` | `https://api.venice.ai/api/v1` |
| Wafer | `WAFER_API_KEY` | `https://pass.wafer.ai/v1` |
| Azure OpenAI | `AZURE_OPENAI_API_KEY` | `https://<resource>.openai.azure.com/openai/v1` |
| Google Vertex AI | `GOOGLE_APPLICATION_CREDENTIALS` | `https://us-central1-aiplatform.googleapis.com/v1/projects` |
| Amazon Bedrock | `AWS_ACCESS_KEY_ID` | `https://bedrock-runtime.<region>.amazonaws.com` |
| Baseten | `BASETEN_API_KEY` | `https://model-{id}.api.baseten.co/v1` |
| Clarifai | `CLARIFAI_API_KEY` | Custom endpoints |
| Scaleway | `SCALEWAY_API_KEY` | `https://api.scaleway.ai/v1` |
| OVHcloud AI | `OVH_AI_API_KEY` | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` |
| GitHub Models | `GITHUB_TOKEN` | `https://models.inference.ai.azure.com` |
| Modal | `MODAL_TOKEN_ID` | `https://<app>.modal.run/v1` |
| OpenRouter | `OPENROUTER_API_KEY` | `https://openrouter.ai/api/v1` |
| Opper | `OPPER_API_KEY` | `https://api.opper.ai/v3/compat` |
| Axiom | `AXIOM_API_KEY` | `https://cloud.axiomstudio.ai/rest/v1/llm-gateway/v1/` |
| Switchpoint | `SWITCHPOINT_API_KEY` | `https://api.ppq.ai` |
| Relace | `RELACE_API_KEY` | `https://api.relace.ai/v1` |
| Moonshot AI | `MOONSHOT_API_KEY` | `https://api.moonshot.ai/v1` |
| Weights & Biases | `WANDB_API_KEY` | `https://api.inference.wandb.ai/v1` |
| Portkey | `PORTKEY_API_KEY` | `https://api.portkey.ai/v1` |
| LiteLLM | `LITELLM_MASTER_KEY` | `http://localhost:4000/v1` |
| Requesty | `REQUESTY_API_KEY` | `https://router.requesty.ai/v1` |
| Unify.ai | `UNIFY_API_KEY` | `https://api.unify.ai/v0` |
| Helicone | `HELICONE_API_KEY` | `https://ai-gateway.helicone.ai/v1` |
| Vercel AI Gateway | `VERCEL_AI_GATEWAY_KEY` | `https://ai-gateway.vercel.sh/v1` |
| Cloudflare AI Gateway | `CLOUDFLARE_API_TOKEN` | `https://gateway.ai.cloudflare.com/v1` |
| AIMLAPI | `AIMLAPI_API_KEY` | `https://api.aimlapi.com/v1` |
| Eden AI | `EDENAI_API_KEY` | `https://api.edenai.co/v2` |
| LemonData | `LEMONDATA_API_KEY` | `https://api.lemondata.ai/v1` |
| Coze (ByteDance) | `COZE_API_KEY` | `https://api.coze.com/v1` |
| NLP Cloud | `NLP_CLOUD_API_KEY` | `https://api.nlpcloud.io/v1` |
| 302.AI | `302AI_API_KEY` | `https://api.302.ai/v1` |
| Azure Cognitive Services | `AZURE_COGNITIVE_SERVICES_API_KEY` | `https://<resource>.cognitiveservices.azure.com/openai/v1` |
| Cortecs | `CORTECS_API_KEY` | `https://api.cortecs.ai/v1` |
| FrogBot | `FROGBOT_API_KEY` | `https://app.frogbot.ai/api` |
| GitLab Duo | `GITLAB_TOKEN` | `https://gitlab.com/api/v4/ai` |
| GitHub Copilot | `GITHUB_TOKEN` | `https://api.githubcopilot.com` |
| Ollama Cloud | `OLLAMA_API_KEY` | `https://ollama.com/api` |
| OpenCode Zen | `OPENCODE_API_KEY` | `https://opencode.ai/zen/v1` |
| OpenCode Go | `OPENCODE_API_KEY` | `https://opencode.ai/zen/go/v1` |
| LLM Gateway | `LLM_GATEWAY_API_KEY` | `https://api.llmgateway.io/v1` |
| SAP AI Core | `AICORE_SERVICE_KEY` | `https://api.ai.<region>.<landscape>.ml.hana.ondemand.com/v2` |
| STACKIT AI Model Serving | `STACKIT_API_KEY` | `https://api.openai-compat.model-serving.eu01.onstackit.cloud/v1` |
| Snowflake Cortex | `SNOWFLAKE_CORTEX_TOKEN` | `https://<account>.snowflakecomputing.com/api/v2/cortex/v1` |
| ZenMux | `ZENMUX_API_KEY` | `https://zenmux.ai/api/v1` |
| Sakana AI (Fugu) | `SAKANA_API_KEY` | `https://api.sakana.ai/v1` |
| Prism API | `PRISM_API_KEY` | `https://sub2api.558686.xyz/v1` |
| DiscountedTokens | `DISCOUNTEDTOKENS_API_KEY` | `https://discountedtokens.com/v1` |
| XiuRouter | `XIUROUTER_API_KEY` | `https://router-api.xiu.ai/v1` |
| SAGG | `SAGG_API_KEY` | `https://api.privatedeskai.com/v1` |
| AIWave | `AIWAVE_API_KEY` | `https://aiwave.live/v1` |
| Perplexity Search | `PERPLEXITY_SEARCH_API_KEY` | `https://api.perplexity.ai` |
| Serper Search | `SERPER_SEARCH_API_KEY` | `https://google.serper.dev` |
| Brave Search | `BRAVE_SEARCH_API_KEY` | `https://api.search.brave.com/res/v1` |
| Exa Search | `EXA_SEARCH_API_KEY` | `https://api.exa.ai` |
| Tavily Search | `TAVILY_SEARCH_API_KEY` | `https://api.tavily.com` |
| AnySearch | `ANYSEARCH_SEARCH_API_KEY` | `https://api.anysearch.com` |
| Firecrawl | `FIRECRAWL_API_KEY` | `https://api.firecrawl.dev/v1` |
| Google Programmable Search | `GOOGLE_PSE_SEARCH_API_KEY` | `https://www.googleapis.com/customsearch/v1` |
| Nimble Search | `NIMBLE_SEARCH_API_KEY` | `https://api.webit.live` |
| Linkup Search | `LINKUP_SEARCH_API_KEY` | `https://api.linkup.so` |
| SearchAPI | `SEARCHAPI_SEARCH_API_KEY` | `https://www.searchapi.io/api/v1/search` |
| You.com Search | `YOUCOM_SEARCH_API_KEY` | `https://api.ydc-index.io` |
| SearXNG Search | `SEARXNG_SEARCH_API_KEY` | `http://localhost:8080` |
| X Search (Grok) | `X_SEARCH_API_KEY` | `https://api.x.ai/v1` |
| Xquik X Search | `XQUIK_SEARCH_API_KEY` | `https://api.xquik.com` |
| Ollama Search | `OLLAMA_SEARCH_API_KEY` | `https://ollama.com/api` |
| Context7 (library docs) | `CONTEXT7_API_KEY` | `https://context7.com` |
| Deepgram | `DEEPGRAM_API_KEY` | `https://api.deepgram.com/v1` |
| AssemblyAI | `ASSEMBLYAI_API_KEY` | `https://api.assemblyai.com/v2` |
| Soniox | `SONIOX_API_KEY` | `https://api.soniox.com` |
| ElevenLabs | `ELEVENLABS_API_KEY` | `https://api.elevenlabs.io/v1` |
| Cartesia | `CARTESIA_API_KEY` | `https://api.cartesia.ai` |
| Fish Audio | `FISHAUDIO_API_KEY` | `https://api.fish.audio` |
| PlayHT | `PLAYHT_API_KEY` | `https://api.play.ht/api/v2` |
| Inworld | `INWORLD_API_KEY` | `https://api.inworld.ai` |
| AWS Polly | `AWS_POLLY_API_KEY` | `https://polly.us-east-1.amazonaws.com` |
| Gladia | `GLADIA_API_KEY` | `https://api.gladia.io/v2` |
| Rev AI | `REV_AI_API_KEY` | `https://api.rev.ai` |
| Speechmatics | `SPEECHMATICS_API_KEY` | `https://asr.api.speechmatics.com/v2` |
| Google Jules | `JULES_API_KEY` | `https://jules.google` |
| Devin | `DEVIN_API_KEY` | `https://api.devin.ai` |
| Codex Cloud | `CODEX_CLOUD_API_KEY` | `https://chatgpt.com/backend-api/codex` |
| CLIProxyAPI | `CLIPROXYAPI_API_KEY` | `http://localhost:8317/v1` |
| 9router | `P9ROUTER_API_KEY` | `http://localhost:20130/v1` |
| Pioneer AI | `PIONEER_API_KEY` | `https://api.pioneer.ai/v1` |
| UC Direct (uncensored.com) | `UC_DIRECT_API_KEY` | `https://api.uncensored.com/api/v1` |
| Blackbox AI | `BLACKBOX_API_KEY` | `https://api.blackbox.ai/v1` |
| Perplexity Agent | `PERPLEXITY_AGENT_API_KEY` | `https://api.perplexity.ai/v1` |
| Meta Llama API | `META_LLAMA_API_KEY` | `https://api.llama.com/compat/v1` |
| Galadriel | `GALADRIEL_API_KEY` | `https://api.galadriel.ai/v1` |
| Codestral | `CODESTRAL_API_KEY` | `https://codestral.mistral.ai/v1` |
| Maritalk | `MARITALK_API_KEY` | `https://chat.maritaca.ai/api` |
| Nous Research | `NOUS_RESEARCH_API_KEY` | `https://inference-api.nousresearch.com/v1` |
| Writer | `WRITER_API_KEY` | `https://api.writer.com/v1` |
| Muse Code (Meta) | `MUSE_CODE_API_KEY` | `https://llama-stack.readthedocs.io` |
| OpenVecta | `OPENVECTA_API_KEY` | `https://api.openvecta.com/v1` |
| Openference API | `OPENFERENCE_API_API_KEY` | `https://api.openference.com/v1` |
| Nube.sh | `NUBE_API_KEY` | `https://ai.nube.sh/api/v1` |
| Lambda AI | `LAMBDA_AI_API_KEY` | `https://api.lambda.ai/v1` |
| nScale | `NSCALE_API_KEY` | `https://inference.api.nscale.com/v1` |
| PublicAI | `PUBLICAI_API_KEY` | `https://api.publicai.co/v1` |
| Featherless AI | `FEATHERLESS_AI_API_KEY` | `https://api.featherless.ai/v1` |
| Predibase | `PREDIBASE_API_KEY` | `https://serving.app.predibase.com/v1` |
| Bytez | `BYTEZ_API_KEY` | `https://api.bytez.com/models/v2/openai/v1` |
| MonsterAPI | `MONSTERAPI_API_KEY` | `https://api.monsterapi.ai/v1` |
| ModelScope | `MODELSCOPE_API_KEY` | `https://api-inference.modelscope.cn/v1` |
| BytePlus ModelArk | `BYTEPLUS_API_KEY` | `https://ark.ap-southeast.bytepluses.com/api/v3` |
| 1min.AI | `ONEMINAI_API_KEY` | `https://api.1min.ai/api/chat-with-ai` |
| Cheaper Inference | `CHEAPERINFERENCE_API_KEY` | `https://api.cheaperinference.com/v1` |
| Freebuff | `FREEBUFF_API_KEY` | `https://www.codebuff.com/api/v1` |
| Charm Hyper | `CHARM_HYPER_API_KEY` | `https://hyper.charm.land/v1` |
| AgentRouter | `AGENTROUTER_API_KEY` | `https://agentrouter.org/v1` |
| UnoRouter | `UNOROUTER_API_KEY` | `https://api.unorouter.com/v1` |
| Command Code | `COMMAND_CODE_API_KEY` | `https://api.commandcode.ai` |
| Zylo API | `ZYLO_API_API_KEY` | `https://api.zyloai.net/v1` |
| FastRouter | `FASTROUTER_API_KEY` | `https://api.fastrouter.ai/api/v1` |
| AnyAPI AI | `ANYAPI_API_KEY` | `https://api.anyapi.ai/v1` |
| Electron Hub | `ELECTRONHUB_API_KEY` | `https://api.electronhub.ai/v1` |
| LLM.Kiwi | `LLM_KIWI_API_KEY` | `https://api.llm.kiwi/v1` |
| LiteRouter | `LITEROUTER_API_KEY` | `https://api.literouter.com/v1` |
| GreenPT | `GREENPT_API_KEY` | `https://api.greenpt.ai/v1` |
| EURouter | `EUROUTER_API_KEY` | `https://api.eurouter.ai/v1` |
| MNN AI | `MNN_AI_API_KEY` | `https://api.mnnai.ru/v1` |
| MegaNova AI | `MEGANOVA_AI_API_KEY` | `https://api.meganova.ai/v1` |
| Mixlayer | `MIXLAYER_API_KEY` | `https://models.mixlayer.ai/v1` |
| Speka AI | `SPEKA_API_KEY` | `https://speka.me/v1` |
| TokenReply | `TOKENREPLY_API_KEY` | `https://api.tokenreply.com/v1` |
| Yolo-Auto | `YOLO_AUTO_API_KEY` | `https://yolo-auto.com/v1` |
| DXNT / DX Token | `DXNT_API_KEY` | `https://www.dxnt.com/v1` |
| CloudCode.ONE | `CLOUDCODE_ONE_API_KEY` | `https://api.cloudcode.one/v1` |
| OfoxAI | `OFOXAI_API_KEY` | `https://api.ofox.ai/v1` |
| ZeroLimitAI | `ZEROLIMITAI_API_KEY` | `https://www.zerolimitai.com/api/v1` |
| ChatAnywhere | `CHATANYWHERE_API_KEY` | `https://api.chatanywhere.org/v1` |
| Helyx AI | `HELYXAI_API_KEY` | `https://helyxai.space/v1` |
| Auriko | `AURIKO_API_KEY` | `https://api.auriko.ai/v1` |
| Poixe AI | `POIXE_AI_API_KEY` | `https://api.poixe.com/v1` |
| Naga AI | `NAGA_AI_API_KEY` | `https://api.naga.ac/v1` |
| Chat Oripe | `CHAT_ORIPE_API_KEY` | `https://api.oriper.com/v1` |
| FreeInference | `FREEINFERENCE_API_KEY` | `https://freeinference.org/v1` |
| Free.ai | `FREE_AI_API_KEY` | `https://api.free.ai/v1/chat` |
| DGrid | `DGRID_API_KEY` | `https://api.dgrid.ai/v1` |
| Qiniu | `QINIU_API_KEY` | `https://api.qnaigc.com/v1` |
| OrcaRouter | `ORCAROUTER_API_KEY` | `https://api.orcarouter.ai/v1` |
| Api.airforce | `API_AIRFORCE_API_KEY` | `https://api.airforce/v1` |
| CrofAI | `CROF_API_KEY` | `https://crof.ai/v1` |
| BazaarLink | `BAZAARLINK_API_KEY` | `https://bazaarlink.ai/api/v1` |
| Synthetic | `SYNTHETIC_API_KEY` | `https://api.synthetic.new/openai/v1` |
| Kilo Gateway | `KILO_GATEWAY_API_KEY` | `https://api.kilo.ai/api/gateway` |
| Dahl | `DAHL_API_KEY` | `https://inference.dahl.global/v1` |
| FreeTheAi | `FREETHEAI_API_KEY` | `https://api.freetheai.xyz/v1` |
| g4f.space — Groq | `G4F_GROQ_API_KEY` | `https://g4f.space/api/groq/v1` |
| g4f.space — Gemini | `G4F_GEMINI_API_KEY` | `https://g4f.space/api/gemini/v1` |
| g4f.space — Pollinations | `G4F_POLLINATIONS_API_KEY` | `https://g4f.space/api/pollinations/v1` |
| g4f.space — Ollama | `G4F_OLLAMA_API_KEY` | `https://g4f.space/api/ollama/v1` |
| g4f.space — NVIDIA | `G4F_NVIDIA_API_KEY` | `https://g4f.space/api/nvidia/v1` |
| LLM7.io | `LLM7_API_KEY` | `https://api.llm7.io/v1` |
| LlamaGate | `LLAMAGATE_API_KEY` | `https://llamagate.ai/v1` |
| Gitlawb Opengateway (MiMo) | `GITLAWB_API_KEY` | `https://opengateway.gitlawb.com/v1/xiaomi-mimo` |
| Gitlawb Opengateway (GMI Cloud) | `GITLAWB_GMI_API_KEY` | `https://opengateway.gitlawb.com/v1/gmi-cloud` |
| NanoGPT | `NANOGPT_API_KEY` | `https://nano-gpt.com/api/v1` |
| PiAPI | `PIAPI_API_KEY` | `https://api.piapi.ai` |
| GoAPI | `GETGOAPI_API_KEY` | `https://api.getgoapi.com/v1` |
| LaoZhang AI | `LAOZHANG_API_KEY` | `https://api.laozhang.ai/v1` |
| TheB.AI | `THEBAI_API_KEY` | `https://api.theb.ai/v1` |
| b.ai | `BAI_API_KEY` | `https://api.b.ai/v1` |
| FenayAI | `FENAYAI_API_KEY` | `https://api.fenayai.com/v1` |
| Empower | `EMPOWER_API_KEY` | `https://api.empower.dev/v1` |
| Poe | `POE_API_KEY` | `https://api.poe.com` |
| Factory | `FACTORY_API_KEY` | `https://api.factory.ai/v1` |
| BluesMinds | `BLUESMINDS_API_KEY` | `https://api.bluesminds.com/v1` |
| FreeModel.dev | `FREEMODEL_DEV_API_KEY` | `https://api.freemodel.dev/v1` |
| FreeAIAPIKey | `FREEAIAPIKEY_API_KEY` | `https://api.freeaiapikey.com/v1` |
| OpenAdapter | `OPENADAPTER_API_KEY` | `https://api.openadapter.in/v1` |
| DIT.ai | `DIT_API_KEY` | `https://api.dit.ai/v1` |
| TokenRouter | `TOKENROUTER_API_KEY` | `https://api.tokenrouter.com/v1` |
| Token Kiosk | `TOKEN_KIOSK_API_KEY` | `https://agent-router.gaib.ai/v1` |
| SumoPod | `SUMOPOD_API_KEY` | `https://ai.sumopod.com/v1` |
| X5Lab | `X5LAB_API_KEY` | `https://api.x5lab.dev/v1` |
| Chenzk API | `CHENZK_API_KEY` | `https://chenzk.top/v1` |
| Kenari | `KENARI_API_KEY` | `https://kenari.id/v1` |
| NavyAI | `NAVY_API_KEY` | `https://api.navy/v1` |
| AINative Studio | `AINATIVE_API_KEY` | `https://api.ainative.studio/api/v1` |
| Routeway | `ROUTEWAY_API_KEY` | `https://api.routeway.ai/v1` |
| NaraRouter | `NARA_API_KEY` | `https://router.bynara.id/v1` |
| Regolo AI | `REGOLO_API_KEY` | `https://api.regolo.ai` |
| Naga.ac | `NAGA_AC_API_KEY` | `https://api.naga.ac/v1` |
| Void AI | `VOID_AI_API_KEY` | `https://api.voidai.app/v1` |
| HelixMind | `HELIXMIND_API_KEY` | `https://helixmind.online/v1` |
| Logfare | `LOGFARE_API_KEY` | `https://logfare.ai/v1` |
| TabiToken | `TABITOKEN_API_KEY` | `https://tabitoken.com/v1` |
| SeekAi | `SEEKAI_API_KEY` | `https://seekai.cc/v1` |
| IBM watsonx.ai Gateway | `WATSONX_API_KEY` | `https://us-south.ml.cloud.ibm.com/ml/v1` |
| OCI Generative AI | `OCI_API_KEY` | `https://inference.generativeai.us-chicago-1.oci.oraclecloud.com` |
| Vertex AI Partners | `VERTEX_PARTNER_API_KEY` | `https://us-central1-aiplatform.googleapis.com/v1/projects` |
| Heroku AI | `HEROKU_API_KEY` | `https://us.inference.heroku.com/v1` |
| Databricks | `DATABRICKS_API_KEY` | `https://adb-0000000000000000.0.azuredatabricks.net/serving-endpoints` |
| DataRobot | `DATAROBOT_API_KEY` | `https://app.datarobot.com/api/v2` |
| GLM Coding | `GLM_API_KEY` | `https://api.z.ai/api/coding/paas/v4` |
| GLM Coding (China) | `GLM_CN_API_KEY` | `https://open.bigmodel.cn/api/coding/paas/v4` |
| GLM Thinking | `GLMT_API_KEY` | `https://api.z.ai/api/coding/paas/v4` |
| Alibaba Token Plan | `BAILIAN_CODING_PLAN_API_KEY` | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic/v1` |
| Qwen Cloud | `QWEN_CLOUD_API_KEY` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| Qwen Cloud Token Plan | `QWEN_CLOUD_TOKEN_PLAN_API_KEY` | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` |
| Kimi Code API Key | `KIMI_CODING_APIKEY_API_KEY` | `https://api.kimi.com/coding/v1` |
| Minimax (China) | `MINIMAX_CN_API_KEY` | `https://api.minimaxi.com/v1` |
| Alibaba (China) | `ALIBABA_CN_API_KEY` | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| LongCat AI | `LONGCAT_API_KEY` | `https://api.longcat.chat/openai/v1` |
| Volcengine | `VOLCENGINE_API_KEY` | `https://ark.cn-beijing.volces.com/api/v3` |
| Volcengine Ark Agent Plan | `VOLCENGINE_AGENT_PLAN_API_KEY` | `https://ark.cn-beijing.volces.com/api/plan/v3` |
| Volcengine Ark Coding Plan | `VOLCENGINE_CODING_PLAN_API_KEY` | `https://ark.cn-beijing.volces.com/api/coding/v3` |
| GigaChat (Sber) | `GIGACHAT_API_KEY` | `https://gigachat.devices.sberbank.ru/api/v1` |
| Xiaomi MiMo Token Plan | `XIAOMI_MIMO_TOKEN_PLAN_API_KEY` | `https://token-plan-sgp.xiaomimimo.com/v1` |
| Tencent Hunyuan | `TENCENT_API_KEY` | `https://api.hunyuan.cloud.tencent.com/v1` |
| iFlytek Spark | `IFLYTEK_API_KEY` | `https://spark-api-open.xf-yun.com/v1` |
| Baichuan | `BAICHUAN_API_KEY` | `https://api.baichuan-ai.com/v1` |
| Yi (01.AI) | `YI_API_KEY` | `https://api.lingyiwanwu.com/v1` |
| 360 AI | `P360AI_API_KEY` | `https://api.360.cn/v1` |
| Doubao | `DOUBAO_API_KEY` | `https://ark.cn-beijing.volces.com/api/v3` |
| SenseNova | `SENSENOVA_API_KEY` | `https://token.sensenova.cn/v1` |
| SparkDesk | `SPARKDESK_API_KEY` | `https://spark-api-open.xf-yun.com/v1` |
| Huancheng Public API | `HCNSEC_API_KEY` | `https://api.hcnsec.cn/v1` |
| Agnes AI | `AGNES_API_KEY` | `https://apihub.agnes-ai.com/v1` |
| SEA-LION | `SEALION_API_KEY` | `https://api.sea-lion.ai/v1` |
| Naver CLOVA Studio | `CLOVA_STUDIO_API_KEY` | `https://clovastudio.stream.ntruss.com/v3/chat-completions` |
| InternLM (Intern-S1) | `INTERNLM_API_KEY` | `https://chat.intern-ai.org.cn/api/v1` |
| Ant Ling / Ring (inclusionAI) | `ANT_LING_API_KEY` | `https://api.ant-ling.com/v1` |
| Sarvam AI | `SARVAM_API_KEY` | `https://api.sarvam.ai/v1` |
| PLaMo | `PLAMO_API_KEY` | `https://api.platform.preferredai.jp/v1` |
| Typhoon | `TYPHOON_API_KEY` | `https://api.opentyphoon.ai/v1` |
| Runway | `RUNWAYML_API_KEY` | `https://api.dev.runwayml.com/v1` |
| KIE.AI | `KIE_API_KEY` | `https://api.kie.ai/v1` |
| Pollinations AI | `POLLINATIONS_API_KEY` | `https://gen.pollinations.ai/v1` |
| Haiper | `HAIPER_API_KEY` | `https://api.haiper.ai/v1` |
| Leonardo AI | `LEONARDO_API_KEY` | `https://cloud.leonardo.ai/api/rest/v1` |
| Ideogram | `IDEOGRAM_API_KEY` | `https://api.ideogram.ai` |
| Magnific | `MAGNIFIC_API_KEY` | `https://api.magnific.com/v1/ai/mystic` |
| Suno | `SUNO_API_KEY` | `https://studio-api.suno.ai/api/generate/v2` |
| Udio | `UDIO_API_KEY` | `https://www.udio.com/api/generate-proxy` |
| v0 (Vercel) | `V0_VERCEL_API_KEY` | `https://api.v0.dev/v1` |
| GitLab Duo PAT | `GITLAB_API_KEY` | `https://gitlab.com/api/v4/ai` |
| Jina AI (Foundation API) | `JINA_AI_API_KEY` | `https://api.jina.ai/v1` |
| Fal.ai | `FAL_AI_API_KEY` | `https://fal.run` |
| Stability AI | `STABILITY_AI_API_KEY` | `https://api.stability.ai` |
| Black Forest Labs | `BLACK_FOREST_LABS_API_KEY` | `https://api.bfl.ai` |
| Recraft | `RECRAFT_API_KEY` | `https://external.api.recraft.ai/v1` |
| Topaz | `TOPAZ_API_KEY` | `https://api.topazlabs.com` |
| Segmind | `SEGMIND_API_KEY` | `https://api.segmind.com/v1` |
| Dify | `DIFY_API_KEY` | `https://api.dify.ai` |
| Nomic | `NOMIC_API_KEY` | `https://api-atlas.nomic.ai/v1` |
| Mixedbread AI | `MIXEDBREAD_API_KEY` | `https://api.mixedbread.com/v1` |
| Jina Reader (r.jina.ai) | `JINA_READER_API_KEY` | `https://r.jina.ai` |
| TinyFish Fetch | `TINYFISH_API_KEY` | `https://api.tinyfish.ai` |
| DeepAI | `DEEPAI_API_KEY` | `https://api.deepai.org` |
| Cursor API | `CURSOR_API_API_KEY` | `https://api.cursor.com/v1` |
| OmniRoute | `OMNIROUTE_API_KEY` | `http://localhost:3000/v1` |

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
| One API for everything | OpenRouter, OmniRoute, Portkey, Opper, AIMLAPI |
| Code generation | Poolside, Morph, Moonshot Kimi, Claude Code / Codex |
| Privacy / no logging | Venice, Relace (ZDR), Phala (TEE), Local (Ollama) |
| Enterprise & compliance | Azure OpenAI, Google Vertex AI, Amazon Bedrock |
| Free tier / prototyping | Groq, Gemini, GitHub Models, HuggingFace, OpenRouter, Pollinations |
| Chinese models | DeepSeek, Qwen (DashScope), Zhipu, MiniMax, StepFun |
| Search-grounded answers | Perplexity Sonar, Exa, Tavily, Brave |
| Self-hosted / offline | Ollama, LM Studio, vLLM, LocalAI |
| IDE subscription reuse | Claude Code, Codex, Cursor, GitHub Copilot, Kimi Code |

### Production tips

1. **Use a gateway for HA** — Route across 2–3 providers so rate limits or outages don't take down your app.
2. **Pin model versions** — Providers silently update models. Pin explicit model IDs and monitor output quality.
3. **Enable context caching** — Gemini, DeepSeek, and Anthropic support caching that can cut costs significantly on repeated prompts.
4. **Respect data sovereignty** — Route PII and regulated data only through EU or private VPC endpoints.
5. **Treat cookie/OAuth unofficial adapters carefully** — Web-cookie providers can break when the upstream UI changes; prefer official APIs in production.

---

## Documentation

Step-by-step guides in [`docs/`](docs/README.md):

| Guide | Description |
|-------|-------------|
| [Getting Started](docs/getting-started.md) | Clone, first lookup, pick a provider |
| [Python Lookup](docs/python-lookup.md) | `llm_lookup.py` — search providers & models |
| [Sync Models](docs/sync-models.md) | Refresh live model catalogs |
| [Integration Guide](docs/integration-guide.md) | OpenAI / Anthropic SDK setup |
| [Data Structure](docs/data-structure.md) | `providers.json`, `models.json` format |
| [Adding Providers](docs/adding-providers.md) | Add or update a provider |
| [Contributing](docs/contributing.md) | PR workflow & checklist |

---

## Repository Structure

```
all-llm-provider-list/
├── README.md              ← Provider tables & quick reference
├── llm_lookup.py          ← Python lookup script
├── scripts/
│   ├── sync_models.py     ← Refresh model catalogs
│   ├── import_omniroute.py← Merge OmniRoute catalog
│   └── example.py         ← Usage examples
├── data/
│   ├── providers.json     ← 402 providers (source of truth)
│   ├── models.json        ← Model catalogs per provider
│   └── static_models.json ← Fallback model lists
└── docs/                  ← Step-by-step guides
```

---

## Contributing

Found a new provider, updated endpoint, or wrong model name? PRs welcome!

See [docs/contributing.md](docs/contributing.md) and [docs/adding-providers.md](docs/adding-providers.md) for the full workflow.

To refresh from [OmniRoute](https://github.com/diegosouzapw/OmniRoute):

```bash
git clone --depth 1 https://github.com/diegosouzapw/OmniRoute.git /tmp/omniroute
python scripts/import_omniroute.py --omniroute /tmp/omniroute
python scripts/sync_models.py
```

---

## Disclaimer

This list is maintained for **educational and integration reference** purposes. We are not affiliated with any listed provider. API endpoints, pricing, and model availability can change without notice. Always refer to official provider documentation for production deployments.

Web-cookie and some OAuth adapters are unofficial; using them may violate a provider's terms of service. Prefer official APIs whenever they exist.

---

## License

MIT — use freely, attribute when you share.
