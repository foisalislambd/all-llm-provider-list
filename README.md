# All LLM providers

**441 providers** · 3,698 model IDs · API URLs, env vars, and model names in one place.

Always confirm endpoints against official docs. To add or correct a provider, see [docs/contributing.md](docs/contributing.md). Updated 2026-09-25.

## Quick start

Most APIs are OpenAI-compatible. You only change `base_url` and `api_key`:

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"],
)
print(client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}],
).choices[0].message.content)
```

Look up any provider from this repo (no extra packages):

```bash
python llm_lookup.py groq
python llm_lookup.py groq --models
python llm_lookup.py --category Gateway
python llm_lookup.py --search-model kimi
```

One key for many models: [OpenRouter](https://openrouter.ai), [Portkey](https://portkey.ai).

## Categories

| Category | Count |
|----------|-------|
| [Frontier labs](#frontier-labs) | 71 |
| [Inference platforms](#inference-platforms) | 53 |
| [Cloud and enterprise](#cloud-and-enterprise) | 40 |
| [Gateways and routers](#gateways-and-routers) | 117 |
| [Aggregators](#aggregators) | 17 |
| [OAuth and IDE](#oauth-and-ide) | 22 |
| [Public endpoints](#public-endpoints) | 10 |
| [Search APIs](#search-apis) | 19 |
| [Audio](#audio) | 12 |
| [Image and video](#image-and-video) | 17 |
| [Cloud agents](#cloud-agents) | 3 |
| [Embeddings](#embeddings) | 4 |
| [Specialized](#specialized) | 4 |
| [Local and self-hosted](#local-and-self-hosted) | 18 |
| Web cookie adapters (in data only) | 34 |
| **Total** | **441** |

Unofficial **web-cookie / browser-session** adapters (34) stay in `data/providers.json` so they do not clutter this page. List them with `python llm_lookup.py --category "Web Cookie"`.

## Frontier labs

Companies that train their own foundation models.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [OpenAI](https://platform.openai.com) | `https://api.openai.com/v1` | GPT-5.5, GPT-5.4, GPT-4.1 | `OPENAI_API_KEY` |
| [Anthropic](https://www.anthropic.com) | `https://api.anthropic.com` | Claude Opus 4.8, Claude Sonnet 4.6, Claude Haiku 4.5 | `ANTHROPIC_API_KEY` |
| [Google AI Studio](https://aistudio.google.com) | `https://generativelanguage.googleapis.com` | Gemini 3.5, Gemini 3.1, Gemini 2.5 | `GEMINI_API_KEY` |
| [DeepSeek](https://platform.deepseek.com) | `https://api.deepseek.com/v1` | DeepSeek-V4-Pro, DeepSeek-V4-Flash, DeepSeek-R1 | `DEEPSEEK_API_KEY` |
| [Mistral AI](https://console.mistral.ai) | `https://api.mistral.ai/v1` | Mistral Medium 3.5, Mistral Small 4, Ministral 3 | `MISTRAL_API_KEY` |
| [xAI](https://x.ai) | `https://api.x.ai/v1` | Grok-3, Grok-2 | `XAI_API_KEY` |
| [Cohere](https://cohere.com) | `https://api.cohere.com/v2` | Command R+, Embed v4, Rerank 3.5 | `COHERE_API_KEY` |
| [AI21 Labs](https://studio.ai21.com) | `https://api.ai21.com/studio/v1` | Jamba 1.5 Large, Jamba 1.5 Mini | `AI21_API_KEY` |
| [Baidu Qianfan](https://cloud.baidu.com/product/wenxinworkshop) | `https://api.baiduqianfan.ai/v1` | ERNIE 4.0 Turbo, ERNIE Speed, ERNIE Lite | `QIANFAN_API_KEY` |
| [StepFun](https://platform.stepfun.com) | `https://api.stepfun.com/v1` | Step 3.5 Flash, Step-series | `STEPFUN_API_KEY` |
| [Z.ai (Zhipu AI)](https://open.bigmodel.cn) | `https://open.bigmodel.cn/api/paas/v4/` | GLM-5, GLM-4.7, GLM-4.7-Flash | `ZHIPU_API_KEY` |
| [Xiaomi](https://xiaomi.com) | `https://api.xiaomimimo.com/v1` | Mimo-v2-pro | `XIAOMI_API_KEY` |
| [Reka AI](https://reka.ai) | `https://api.reka.ai/v1` | Reka Core, Reka Flash | `REKA_API_KEY` |
| [Inflection](https://inflection.ai) | Custom webhooks | Pi-series | — |
| [MiniMax](https://platform.minimax.io) | `https://api.minimax.io/v1` | MiniMax-M3, MiniMax-M2.1, MiniMax-M2 | `MINIMAX_API_KEY` |
| [Alibaba DashScope](https://www.alibabacloud.com) | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | qwen3-max, Qwen-Plus, Qwen-Flash | `DASHSCOPE_API_KEY` |
| [Upstage](https://console.upstage.ai) | `https://api.upstage.ai/v1/solar` | Solar Pro 3, Solar Mini | `UPSTAGE_API_KEY` |
| [Perplexity](https://docs.perplexity.ai) | `https://api.perplexity.ai` | Sonar, Sonar Pro, Sonar Reasoning | `PERPLEXITY_API_KEY` |
| [Pioneer AI](https://pioneer.ai) | `https://api.pioneer.ai/v1` | Qwen/Qwen3-32B, Qwen/Qwen3.6-27B, Qwen/Qwen3.5-9B | `PIONEER_API_KEY` |
| [UC Direct (uncensored.com)](https://uncensored.com) | `https://api.uncensored.com/api/v1` | claude-opus-5, claude-opus-5-fast, claude-fable-5 | `UC_DIRECT_API_KEY` |
| [Blackbox AI](https://blackbox.ai) | `https://api.blackbox.ai/v1` | claude-fable-5, claude-opus-4.8, claude-sonnet-5 | `BLACKBOX_API_KEY` |
| [Perplexity Agent](https://www.perplexity.ai) | `https://api.perplexity.ai/v1` | openai/gpt-5.6-sol, perplexity/kimi-k3 | `PERPLEXITY_AGENT_API_KEY` |
| [Meta Llama API](https://llama.developer.meta.com) | `https://api.llama.com/compat/v1` | — | `META_LLAMA_API_KEY` |
| [Galadriel](https://galadriel.com) | `https://api.galadriel.ai/v1` | — | `GALADRIEL_API_KEY` |
| [Codestral](https://mistral.ai) | `https://codestral.mistral.ai/v1` | — | `CODESTRAL_API_KEY` |
| [Maritalk](https://www.maritaca.ai) | `https://chat.maritaca.ai/api` | — | `MARITALK_API_KEY` |
| [Nous Research](https://portal.nousresearch.com/help) | `https://inference-api.nousresearch.com/v1` | Hermes-4-405B, Hermes-4-70B | `NOUS_RESEARCH_API_KEY` |
| [Writer](https://dev.writer.com) | `https://api.writer.com/v1` | palmyra-x5, palmyra-x4 | `WRITER_API_KEY` |
| [GLM Coding](https://z.ai/subscribe) | `https://api.z.ai/api/coding/paas/v4` | glm-5.3-flash, glm-5.3, glm-5.3-high | `GLM_API_KEY` |
| [GLM Coding (China)](https://open.bigmodel.cn) | `https://open.bigmodel.cn/api/coding/paas/v4` | glm-5.3-flash, glm-5.3, glm-5.3-high | `GLM_CN_API_KEY` |
| [Alibaba Token Plan](https://www.alibabacloud.com/help/en/model-studio/token-plan-overview) | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic/v1` | qwen3.8-max-preview, qwen3.7-max, qwen3.7-plus | `BAILIAN_CODING_PLAN_API_KEY` |
| [Qwen Cloud](https://www.qwencloud.com) | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | qwen3.8-max, qwen3.7-max-2026-06-08, qwen3.7-plus | `QWEN_CLOUD_API_KEY` |
| [Qwen Cloud Token Plan](https://www.qwencloud.com/pricing/token-plan) | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` | qwen3.8-max, qwen3.7-max, qwen3.7-plus | `QWEN_CLOUD_TOKEN_PLAN_API_KEY` |
| [Kimi Code API Key](https://www.kimi.com/code) | `https://api.kimi.com/coding/v1` | — | `KIMI_CODING_API_KEY` |
| [Minimax (China)](https://www.minimaxi.com) | `https://api.minimaxi.com/v1` | MiniMax-M3, MiniMax-M2.7, MiniMax-M2.7-highspeed | `MINIMAX_CN_API_KEY` |
| [Alibaba (China)](https://dashscope.console.aliyun.com) | `https://dashscope.aliyuncs.com/compatible-mode/v1` | — | `ALIBABA_CN_API_KEY` |
| [LongCat AI](https://longcat.chat/platform/docs) | `https://api.longcat.chat/openai/v1` | LongCat-2.0 | `LONGCAT_API_KEY` |
| [Volcengine Ark Agent Plan](https://console.volcengine.com/ark/region:cn-beijing/subscription/agent-plan) | `https://ark.cn-beijing.volces.com/api/plan/v3` | doubao-seed-evolving, doubao-seed-2-1-turbo-260628, doubao-seed-2-0-lite-260215 | `VOLCENGINE_AGENT_PLAN_API_KEY` |
| [Volcengine Ark Coding Plan](https://console.volcengine.com/ark/region:cn-beijing/subscription/coding-plan) | `https://ark.cn-beijing.volces.com/api/coding/v3` | doubao-seed-2-1-turbo, doubao-seed-2.0-lite, deepseek-v4-flash | `VOLCENGINE_CODING_PLAN_API_KEY` |
| [GigaChat (Sber)](https://developers.sber.ru) | `https://gigachat.devices.sberbank.ru/api/v1` | — | `GIGACHAT_API_KEY` |
| [Xiaomi MiMo Token Plan](https://mimo.mi.com) | `https://token-plan-sgp.xiaomimimo.com/v1` | mimo-v2.5-pro, mimo-v2.5 | `XIAOMI_MIMO_TOKEN_PLAN_API_KEY` |
| [Tencent Hunyuan](https://hunyuan.tencent.com) | `https://api.hunyuan.cloud.tencent.com/v1` | hunyuan-turbos-latest, hunyuan-t1-latest, hunyuan-pro | `TENCENT_API_KEY` |
| [iFlytek Spark](https://xinghuo.xfyun.cn) | `https://spark-api-open.xf-yun.com/v1` | 4.0Ultra, generalv3.5, max-32k | `IFLYTEK_API_KEY` |
| [Baichuan](https://www.baichuan-ai.com) | `https://api.baichuan-ai.com/v1` | Baichuan4-Turbo, Baichuan4-Air, Baichuan4 | `BAICHUAN_API_KEY` |
| [Yi (01.AI)](https://01.ai) | `https://api.lingyiwanwu.com/v1` | yi-large | `YI_API_KEY` |
| [360 AI](https://ai.360.cn) | `https://api.360.cn/v1` | — | `AI360_API_KEY` |
| [Doubao](https://doubao.com) | `https://ark.cn-beijing.volces.com/api/v3` | doubao-seed-2-0-pro-260215, doubao-seed-2-0-lite-260215, doubao-seed-2-0-mini-260215 | `DOUBAO_API_KEY` |
| [SenseNova](https://platform.sensenova.cn) | `https://token.sensenova.cn/v1` | sensenova-6.7-flash-lite, deepseek-v4-flash, glm-5.2 | `SENSENOVA_API_KEY` |
| [Huancheng Public API](https://api.hcnsec.cn) | `https://api.hcnsec.cn/v1` | — | `HCNSEC_API_KEY` |
| [SEA-LION](https://sea-lion.ai) | `https://api.sea-lion.ai/v1` | aisingapore/Llama-SEA-LION-v3.5-70B-R, aisingapore/Llama-SEA-LION-v3-70B-IT, aisingapore/Gemma-SEA-LION-v4-27B-IT | `SEALION_API_KEY` |
| [Naver CLOVA Studio](https://api.ncloud-docs.com/docs/en/ai-naver-clovastudio-summary) | `https://clovastudio.stream.ntruss.com/v3/chat-completions` | HCX-007, HCX-005, HCX-DASH-002 | `CLOVA_STUDIO_API_KEY` |
| [InternLM (Intern-S1)](https://internlm.intern-ai.org.cn) | `https://chat.intern-ai.org.cn/api/v1` | intern-s1-pro, intern-s1, intern-s1-mini | `INTERNLM_API_KEY` |
| [Ant Ling / Ring (inclusionAI)](https://developer.ant-ling.com/en/docs) | `https://api.ant-ling.com/v1` | Ling-2.6-1T, Ring-2.6-1T, Ling-2.6-flash | `ANT_LING_API_KEY` |
| [Sarvam AI](https://docs.sarvam.ai) | `https://api.sarvam.ai/v1` | sarvam-105b, sarvam-30b | `SARVAM_API_KEY` |
| [PLaMo](https://plamo.preferredai.jp/api) | `https://api.platform.preferredai.jp/v1` | plamo-3.0-prime | `PLAMO_API_KEY` |
| [Typhoon](https://docs.opentyphoon.ai) | `https://api.opentyphoon.ai/v1` | typhoon-v2.5-30b-a3b-instruct | `TYPHOON_API_KEY` |
| [Amazon Nova](https://nova.amazon.com) | `https://api.nova.amazon.com/v1` | nova-2-pro-v1, nova-2-lite-v1 | `NOVA_API_KEY` |
| [Meta AI](https://dev.meta.ai) | `https://api.meta.ai/v1` | muse-spark-1.3, muse-spark-1.1, muse-spark-1.2 | `META_MODEL_API_KEY` |
| [Moonshot AI (China)](https://platform.moonshot.cn) | `https://api.moonshot.cn/v1` | kimi-k2.7-code, kimi-k2.6, kimi-k2.7-code-highspeed | `MOONSHOT_CN_API_KEY` |
| [Thinking Machines](https://tinker-docs.thinkingmachines.ai/tinker/compatible-apis/anthropic/) | `https://tinker.thinkingmachines.dev/services/tinker-prod/anthropic/api/v1` | thinkingmachines/Inkling:peft:262144, thinkingmachines/Inkling | `TINKER_API_KEY` |
| [Krutrim](https://cloud.olakrutrim.com) | `https://cloud.olakrutrim.com/v1` | krutrim-1, Meta-Llama-3-8B-Instruct | `KRUTRIM_API_KEY` |
| [Kimi For Coding](https://www.kimi.ai/code) | `https://api.kimi.ai/coding/v1` | kimi-for-coding-highspeed, kimi-for-coding, k3-256k | `KIMI_AI_API_KEY` |
| [Alibaba Coding Plan](https://www.alibabacloud.com/help/en/model-studio/coding-plan) | `https://coding-intl.dashscope.aliyuncs.com/v1` | qwen3.7-max, qwen3-coder-next, qwen3.5-plus | `ALIBABA_CODING_PLAN_API_KEY` |
| [Alibaba Coding Plan (China)](https://help.aliyun.com/zh/model-studio/coding-plan) | `https://coding.dashscope.aliyuncs.com/v1` | qwen3.7-max, qwen3-coder-next, qwen3.5-plus | `ALIBABA_CODING_PLAN_CN_API_KEY` |
| [Alibaba Token Plan (China)](https://www.alibabacloud.com/help/zh/model-studio/token-plan-overview) | `https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | qwen3.8-max, qwen3.7-max, deepseek-v4-flash-0731 | `ALIBABA_TOKEN_PLAN_CN_API_KEY` |
| [StepFun Step Plan (China)](https://platform.stepfun.com/docs/zh/step-plan/integrations/reasoning-api) | `https://api.stepfun.com/step_plan/v1` | step-5-preview, step-router-v1, step-3.5-flash-2603 | `STEPFUN_STEP_PLAN_API_KEY` |
| [StepFun Step Plan (Global)](https://platform.stepfun.ai/docs/en/step-plan/integrations/reasoning-api) | `https://api.stepfun.ai/step_plan/v1` | step-5-preview, step-3.5-flash-2603, step-3.5-flash | `STEPFUN_GLOBAL_STEP_PLAN_API_KEY` |
| [MiniMax Token Plan](https://platform.minimax.io/docs/token-plan/intro) | `https://api.minimax.io/anthropic/v1` | MiniMax-M3, MiniMax-M2.1, MiniMax-M2.5 | `MINIMAX_TOKEN_PLAN_API_KEY` |
| [MiniMax Token Plan (China)](https://platform.minimaxi.com/docs/token-plan/intro) | `https://api.minimax.cn/anthropic/v1` | MiniMax-M3, MiniMax-M2.1, MiniMax-M2.5 | `MINIMAX_CN_TOKEN_PLAN_API_KEY` |
| [Tencent TokenHub](https://cloud.tencent.com/document/product/1823/130050) | `https://tokenhub.tencentmaas.com/v1` | hy3-preview, hy3, hy4-preview | `TENCENT_TOKENHUB_API_KEY` |
| [Tencent Token Plan](https://cloud.tencent.com/document/product/1823/130060) | `https://api.lkeap.cloud.tencent.com/plan/v3` | hy3, hy4-preview | `TENCENT_TOKEN_PLAN_API_KEY` |

## Inference platforms

Hosted open-weight models — usually cheaper and faster.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Groq](https://console.groq.com) | `https://api.groq.com/openai/v1` | llama-3.3-70b-versatile, llama-3.1-8b-instant, Gemma 2 9B | `GROQ_API_KEY` |
| [Cerebras](https://cerebras.ai) | `https://api.cerebras.ai/v1` | Llama 3.3 70B, GPT-OSS 120B, Qwen 3 32B | `CEREBRAS_API_KEY` |
| [SambaNova](https://sambanova.ai) | `https://api.sambanova.ai/v1` | Llama 3.1 405B, Llama 3.3 70B, Qwen | `SAMBANOVA_API_KEY` |
| [Together AI](https://together.ai) | `https://api.together.xyz/v1` | Llama 3.3, DeepSeek-V4, Qwen | `TOGETHER_API_KEY` |
| [Fireworks AI](https://fireworks.ai) | `https://api.fireworks.ai/inference/v1` | Qwen 3.6 Plus, Kimi K2.6, Llama 4 Maverick | `FIREWORKS_API_KEY` |
| [DeepInfra](https://deepinfra.com) | `https://api.deepinfra.com/v1/openai` | Llama 3.3, Qwen 3, DeepSeek-V4 | `DEEPINFRA_API_KEY` |
| [Nebius AI Studio](https://studio.nebius.ai) | `https://api.studio.nebius.ai/v1` | DeepSeek-R1-0528, Llama 3.3 70B | `NEBIUS_API_KEY` |
| [SiliconFlow](https://siliconflow.com) | `https://api.siliconflow.cn/v1` | DeepSeek-R1-0528, MiniMax-M2, Qwen3-VL | `SILICONFLOW_API_KEY` |
| [Inception](https://inceptionlabs.ai) | `https://api.inceptionlabs.ai/v1` | Mercury-2, Mercury-Edit-2 | `INCEPTION_API_KEY` |
| [Liquid AI](https://liquid.ai) | `https://inference.liquid.ai/v1` | LFM2.5 Instruct, LFM2-24B | `LIQUID_API_KEY` |
| [Friendli](https://friendli.ai) | `https://api.friendli.ai/serverless/v1` | Llama 3.1 8B, DeepSeek-R1 | `FRIENDLI_API_KEY` |
| [Inceptron](https://inceptron.io) | Custom endpoint | Open-weight LLMs | — |
| [Infermatic](https://infermatic.ai) | `https://api.totalgpt.ai` | Rocinante, Midnight Miqu, Llama | `INFERMATIC_API_KEY` |
| [Mancer](https://mancer.tech) | `https://mancer.tech/oai/v1` | Goliath 120B, MythoMax, LumiMaid | `MANCER_API_KEY` |
| [Morph](https://morphllm.com) | `https://api.morphllm.com/v1` | morph-qwen35-397b, morph-qwen36-27b | `MORPH_API_KEY` |
| [AionLabs](https://aionlabs.ai) | `https://api.aionlabs.ai/v1` | Aion 2.0, Aion-RP | `AION_API_KEY` |
| [HuggingFace Inference](https://huggingface.co) | `https://router.huggingface.co/v1` | meta-llama/Llama-3.3-70B-Instruct, Qwen/Qwen2.5-72B-Instruct | `HUGGINGFACE_API_KEY` |
| [NVIDIA NIM](https://build.nvidia.com) | `https://integrate.api.nvidia.com/v1` | meta/llama-3.3-70b-instruct, deepseek-ai/deepseek-r1 | `NVIDIA_API_KEY` |
| [Hyperbolic](https://app.hyperbolic.xyz) | `https://api.hyperbolic.xyz/v1` | DeepSeek-V3, Llama 3.3 70B | `HYPERBOLIC_API_KEY` |
| [Lepton AI](https://lepton.ai) | `https://api.lepton.ai/v1` | Llama 3.3 70B | `LEPTON_API_KEY` |
| [Kluster.ai](https://kluster.ai) | `https://api.kluster.ai/v1` | Llama 3.1 405B, Qwen 2.5 72B | `KLUSTER_API_KEY` |
| [Anyscale Endpoints](https://app.endpoints.anyscale.com) | `https://api.endpoints.anyscale.com/v1` | Llama 3.3 70B, Mixtral 8x22B | `ANYSCALE_API_KEY` |
| [Replicate](https://replicate.com) | `https://api.replicate.com/v1` | Open models, FLUX, video models | `REPLICATE_API_TOKEN` |
| [Inference.net](https://inference.net) | `https://api.inference.net/v1` | DeepSeek-R1, Llama 3.1 70B | `INFERENCE_NET_API_KEY` |
| [Arcee AI](https://arcee.ai) | `https://conductor.arcee.ai/v1` | Trinity-Large, Caller-Large | `ARCEE_API_KEY` |
| [Glhf.chat](https://glhf.chat) | `https://glhf.chat/api/openai/v1` | hf:meta-llama/Llama-3.3-70B-Instruct, hf:Qwen/Qwen2.5-72B-Instruct | `GLHF_API_KEY` |
| [Ollama Cloud](https://ollama.com) | `https://ollama.com/api` | gpt-oss:20b-cloud, gpt-oss:120b | `OLLAMA_API_KEY` |
| [OpenVecta](https://openvecta.com) | `https://api.openvecta.com/v1` | glm-4.7-flash, claude-sonnet-4.6, deepseek-v4-flash | `OPENVECTA_API_KEY` |
| [Openference API](https://openference.com) | `https://api.openference.com/v1` | GLM-5.2 | `OPENFERENCE_API_KEY` |
| [Nube.sh](https://nube.sh) | `https://ai.nube.sh/api/v1` | — | `NUBE_API_KEY` |
| [Lambda AI](https://lambda.ai) | `https://api.lambda.ai/v1` | — | `LAMBDA_AI_API_KEY` |
| [nScale](https://nscale.com) | `https://inference.api.nscale.com/v1` | — | `NSCALE_API_KEY` |
| [PublicAI](https://publicai.co) | `https://api.publicai.co/v1` | — | `PUBLICAI_API_KEY` |
| [Featherless AI](https://featherless.ai) | `https://api.featherless.ai/v1` | — | `FEATHERLESS_AI_API_KEY` |
| [Predibase](https://predibase.com) | `https://serving.app.predibase.com/v1` | — | `PREDIBASE_API_KEY` |
| [Bytez](https://bytez.com) | `https://api.bytez.com/models/v2/openai/v1` | — | `BYTEZ_API_KEY` |
| [MonsterAPI](https://monsterapi.ai) | `https://api.monsterapi.ai/v1` | meta-llama/Meta-Llama-3.1-8B-Instruct, meta-llama/Llama-3.3-70B-Instruct | `MONSTERAPI_KEY` |
| [ModelScope](https://modelscope.cn) | `https://api-inference.modelscope.cn/v1` | — | `MODELSCOPE_API_KEY` |
| [BytePlus ModelArk](https://console.byteplus.com/ark) | `https://ark.ap-southeast.bytepluses.com/api/v3` | seed-2.0, kimi-k2-thinking, glm-4.7 | `BYTEPLUS_API_KEY` |
| [Pollinations AI](https://pollinations.ai) | `https://gen.pollinations.ai/v1` | openai, openai-fast, openai-large | `POLLINATIONS_API_KEY` |
| [Crusoe](https://docs.crusoecloud.com/managed-inference/overview) | `https://api.inference.crusoecloud.com/v1` | zai/GLM-5.1, zai/GLM-5.2, meta-llama/Llama-3.3-70B-Instruct | `CRUSOE_API_KEY` |
| [Vultr Inference](https://www.vultr.com) | `https://api.vultrinference.com/v1` | deepseek-v4-flash-0731, deepseek-v4.1-flash, glm-5.2 | `VULTR_API_KEY` |
| [CoralBricks](https://www.coralbricks.ai) | `https://inference.coralbricks.ai/v1` | glm-5.3-fp4, glm-5.3-flash-fp4, gpt-oss-120b | `CORAL_API_KEY` |
| [Jalapeno Cloud](https://www.jalapeno-cloud.ai) | `https://api.jalapeno-cloud.ai/v1` | Qwen3-VL-235B-A22B-Instruct, MiniMax-M3, Qwen3-Next-80B-A3B-Instruct | `JALAPENO_API_KEY` |
| [Berget.AI](https://berget.ai) | `https://api.berget.ai/v1` | Qwen/Qwen3.8-27B-FP8, mistralai/Mistral-Small-3.2-24B-Instruct-2506, zai-org/GLM-5.3-Flash | `BERGET_API_KEY` |
| [AMD Token Factory](https://developer.amd.com.cn/radeon/tokenfactory) | `https://developer.amd.com.cn/radeon/api/v1` | Qwen3.8-27B, DeepSeek-V4.1-Flash, DeepSeek-V4-Flash | `AMD_API_KEY` |
| [EBCloud](https://www.ebcloud.com) | `https://maas-api.ebcloud.com/v1` | Kimi-K2.6, GLM-5.1, DeepSeek-V4-Flash | `EBCLOUD_API_KEY` |
| [D.Run](https://www.d.run) | `https://chat.d.run/v1` | public/deepseek-v3, public/minimax-m25, public/deepseek-r1 | `DRUN_API_KEY` |
| [Lilac](https://docs.getlilac.com/inference/models) | `https://api.getlilac.com/v1` | google/gemma-4-31b-it, minimaxai/minimax-m3, moonshotai/kimi-k2.6 | `LILAC_API_KEY` |
| [RunInfra](https://runinfra.ai) | `https://api.runinfra.ai/v1` | Inferact/Qwen3.8-2.4T-A95B-NVFP4, Qwen/Qwen3.8-27B, deepseek-ai/DeepSeek-V4-Flash-0731 | `RUNINFRA_GATEWAY_KEY` |
| [AKI.IO](https://aki.io) | `https://aki.io/v1` | qwen3.8-27b, deepseek-v4-flash-0731-284b, qwen3.6-35b | `AKI_IO_API_KEY` |
| [DInference](https://dinference.com) | `https://api.dinference.com/v1` | glm-5, minimax-m2.5, glm-4.7 | `DINFERENCE_API_KEY` |
| [Ambient](https://ambient.xyz) | `https://api.ambient.xyz/v1` | z-ai/glm-5.2, qwen/qwen3.6-27b, qwen/qwen3.8-27b | `AMBIENT_API_KEY` |

## Cloud and enterprise

Azure, Bedrock, Vertex, and regional clouds.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [AkashML](https://akash.network) | `https://api.akashml.com/v1` | Llama 3, Qwen, DeepSeek | `AKASHML_API_KEY` |
| [AtlasCloud](https://atlascloud.ai) | `https://api.atlascloud.ai/v1` | DeepSeek-V3, Seedance 2.0, Kling 3.0 | `ATLASCLOUD_API_KEY` |
| [Chutes](https://chutes.ai) | `https://llm.chutes.ai/v1` | Kimi, GLM, Qwen | `CHUTES_API_KEY` |
| [Cloudflare Workers AI](https://cloudflare.com) | `https://api.cloudflare.com/client/v4/accounts/{id}/ai/v1` | @cf/meta/llama-3.3-70b-instruct-fp8-fast, Gemma 4, Kimi K2.5 | `CLOUDFLARE_API_TOKEN` |
| [DigitalOcean](https://digitalocean.com) | `https://inference.do-ai.run/v1/` | Llama 3 8B Instruct | `DIGITALOCEAN_API_KEY` |
| [GMICloud](https://gmicloud.ai) | `https://api.gmi-serving.com/v1` | GLM-5.1-FP8, DeepSeek-V3.2 | `GMI_API_KEY` |
| [io.net](https://io.net) | `https://api.intelligence.io.solutions/api/v1` | GLM-4.5-Air, GPT-OSS 120B, Llama 3.3 | `IO_NET_API_KEY` |
| [NextBit](https://nextbit256.com) | `https://api.nextbit256.com/v1` | qwen:3.5-35b, qwen3:30b, qwen3:14b | `NEXTBIT_API_KEY` |
| [Novita](https://novita.ai) | `https://api.novita.ai/openai/v1` | Kimi K2.5, Llama, Qwen | `NOVITA_API_KEY` |
| [Parasail](https://parasail.io) | `https://api.saas.parasail.io/v1` | DeepSeek-R1, QwenCoder 32B | `PARASAIL_API_KEY` |
| [Phala](https://phala.network) | POST /v1/chat/completions | unsloth/Qwen2.5-72B-Instruct | `PHALA_API_KEY` |
| [Poolside](https://poolside.ai) | `https://divers.poolsi.de/openai/v1/` | Laguna XS.2, Laguna M.1 | `POOLSIDE_API_KEY` |
| [Venice](https://venice.ai) | `https://api.venice.ai/api/v1` | llama-3.3-70b, fluently-xl | `VENICE_API_KEY` |
| [Wafer](https://wafer.ai) | `https://pass.wafer.ai/v1` | Qwen3.5-397B-A17B, GLM-5.1 | `WAFER_API_KEY` |
| [Azure OpenAI](https://azure.microsoft.com) | `https://<resource>.openai.azure.com/openai/v1` | GPT-5, Claude, Llama | `AZURE_OPENAI_API_KEY` |
| [Google Vertex AI](https://cloud.google.com/vertex-ai) | `https://us-central1-aiplatform.googleapis.com/v1/projects` | Gemini, Claude, partner models | `GOOGLE_APPLICATION_CREDENTIALS` |
| [Amazon Bedrock](https://aws.amazon.com/bedrock) | `https://bedrock-runtime.<region>.amazonaws.com` | Claude, Llama, Titan | `AWS_ACCESS_KEY_ID` |
| [Baseten](https://baseten.co) | `https://model-{id}.api.baseten.co/v1` | Llama 3.3, DeepSeek-R1 | `BASETEN_API_KEY` |
| [Clarifai](https://clarifai.com) | Custom endpoints | Multimodal models | `CLARIFAI_API_KEY` |
| [Scaleway](https://console.scaleway.com) | `https://api.scaleway.ai/v1` | Llama 3.3 70B, DeepSeek-R1 | `SCALEWAY_API_KEY` |
| [OVHcloud AI](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/) | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | Meta-Llama-3_1-70B-Instruct, Qwen2.5-72B-Instruct | `OVH_AI_API_KEY` |
| [GitHub Models](https://github.com/marketplace/models) | `https://models.inference.ai.azure.com` | gpt-4o, Meta-Llama-3.1-70B-Instruct | `GITHUB_TOKEN` |
| [Modal](https://modal.com) | `https://<app>.modal.run/v1` | google/gemini-2.0-flash | `MODAL_TOKEN_ID` |
| [Azure Cognitive Services](https://azure.microsoft.com/products/ai-services) | `https://<resource>.cognitiveservices.azure.com/openai/v1` | gpt-4o, gpt-4.1, o3-mini | `AZURE_COGNITIVE_SERVICES_API_KEY` |
| [GitLab Duo](https://about.gitlab.com/gitlab-duo/) | `https://gitlab.com/api/v4/ai` | duo-chat-haiku-4-5, duo-chat-sonnet-4-5, duo-chat-opus-4-5 | `GITLAB_TOKEN` |
| [GitHub Copilot](https://github.com/features/copilot) | `https://api.githubcopilot.com` | gpt-4o, claude-sonnet-4, o3-mini | `GITHUB_TOKEN` |
| [SAP AI Core](https://www.sap.com/products/artificial-intelligence/ai-core.html) | `https://api.ai.<region>.<landscape>.ml.hana.ondemand.com/v2` | gpt-4o, claude-sonnet-4, gemini-2.5-pro | `AICORE_SERVICE_KEY` |
| [STACKIT AI Model Serving](https://www.stackit.de/en/product/stackit-ai-model-serving) | `https://api.openai-compat.model-serving.eu01.onstackit.cloud/v1` | qwen3-vl-235b, llama-3.3-70b, mistral-nemo-instruct | `STACKIT_API_KEY` |
| [Snowflake Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-llm-rest-api) | `https://<account>.snowflakecomputing.com/api/v2/cortex/v1` | claude-sonnet-4-6, claude-haiku-4-5, gpt-5 | `SNOWFLAKE_CORTEX_TOKEN` |
| [IBM watsonx.ai Gateway](https://www.ibm.com/products/watsonx-ai) | `https://us-south.ml.cloud.ibm.com/ml/v1` | — | `WATSONX_API_KEY` |
| [OCI Generative AI](https://www.oracle.com/artificial-intelligence/generative-ai) | `https://inference.generativeai.us-chicago-1.oci.oraclecloud.com` | — | `OCI_API_KEY` |
| [Vertex AI Partners](https://cloud.google.com/vertex-ai) | `https://us-central1-aiplatform.googleapis.com/v1/projects` | DeepSeek-V4-Flash, DeepSeek-V4-Pro, Qwen3.6-35B-A3B | `VERTEX_PARTNER_API_KEY` |
| [Heroku AI](https://www.heroku.com) | `https://us.inference.heroku.com/v1` | — | `HEROKU_API_KEY` |
| [Databricks](https://www.databricks.com) | `https://adb-0000000000000000.0.azuredatabricks.net/serving-endpoints` | — | `DATABRICKS_API_KEY` |
| [DataRobot](https://docs.datarobot.com) | `https://app.datarobot.com/api/v2` | — | `DATAROBOT_API_KEY` |
| [Dasha Compute](https://www.getdasha.com/compute) | Open alpha | qwen3-8b, gemma3-12b, gemma3-27b | — |
| [Hetzner](https://docs.hetzner.com/general/company-and-policy/experiments/inference/) | `https://inference.hetzner.com/api/v1` | Qwen3.8-27B, Qwen/Qwen3.6-35B-A3B-FP8 | `HETZNER_API_KEY` |
| [evroc](https://docs.evroc.com/products/think/) | `https://models.think.evroc.com/v1` | google/gemma-4-26B-A4B-it, Qwen/Qwen3.8-27B, Qwen/Qwen3.6-35B-A3B | `EVROC_API_KEY` |
| [CloudFerro Sherlock](https://docs.sherlock.cloudferro.com/) | `https://api-sherlock.cloudferro.com/openai/v1` | meta-llama/Llama-3.3-70B-Instruct, MiniMaxAI/MiniMax-M2.5, openai/gpt-oss-120b | `CLOUDFERRO_SHERLOCK_API_KEY` |
| [SCNet Token Plan](https://www.scnet.cn/ac/openapi/doc/2.0/moduleapi/plans/token-plan.html) | `https://api.scnet.cn/api/llm/v1` | DeepSeek-V4-Flash-0731, Kimi-K2.6, MiniMax-M3 | `SCNET_API_KEY` |

## Gateways and routers

One key, many upstream providers.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [OpenRouter](https://openrouter.ai) | `https://openrouter.ai/api/v1` | auto | `OPENROUTER_API_KEY` |
| [Opper](https://opper.ai) | `https://api.opper.ai/v3/compat` | — | `OPPER_API_KEY` |
| [Axiom](https://axiomstudio.ai) | `https://cloud.axiomstudio.ai/rest/v1/llm-gateway/v1/` | — | `AXIOM_API_KEY` |
| [Switchpoint](https://switchpoint.ai) | `https://api.ppq.ai` | switchpoint/router | `SWITCHPOINT_API_KEY` |
| [Relace](https://relace.ai) | `https://api.relace.ai/v1` | Relace Apply 3, Relace Search | `RELACE_API_KEY` |
| [Moonshot AI](https://api.moonshot.ai/v1) | `https://api.moonshot.ai/v1` | kimi-k2.7-code, kimi-k2.6 | `MOONSHOT_API_KEY` |
| [OpenInference](https://openinference.ai) | Tracing / observability | LLM telemetry | — |
| [Weights & Biases](https://wandb.ai) | `https://api.inference.wandb.ai/v1` | Model benchmarking | `WANDB_API_KEY` |
| [Perceptron](https://perceptron.ai) | Custom gateway | Enterprise routes | — |
| [Portkey](https://portkey.ai) | `https://api.portkey.ai/v1` | — | `PORTKEY_API_KEY` |
| [LiteLLM](https://github.com/BerriAI/litellm) | `http://localhost:4000/v1` | — | `LITELLM_MASTER_KEY` |
| [Requesty](https://requesty.ai) | `https://router.requesty.ai/v1` | Multi-provider routing | `REQUESTY_API_KEY` |
| [Unify.ai](https://unify.ai) | `https://api.unify.ai/v0` | ML-routed models | `UNIFY_API_KEY` |
| [Helicone](https://helicone.ai) | `https://ai-gateway.helicone.ai/v1` | — | `HELICONE_API_KEY` |
| [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) | `https://ai-gateway.vercel.sh/v1` | — | `VERCEL_AI_GATEWAY_KEY` |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) | `https://gateway.ai.cloudflare.com/v1` | — | `CLOUDFLARE_API_TOKEN` |
| [Kong AI Gateway](https://konghq.com/products/kong-ai-gateway) | Self-hosted / enterprise | Enterprise routing | — |
| [Cortecs](https://cortecs.ai) | `https://api.cortecs.ai/v1` | kimi-k2-instruct, gpt-5-mini | `CORTECS_API_KEY` |
| [OpenCode Zen](https://opencode.ai/zen) | `https://opencode.ai/zen/v1` | gpt-5.5, claude-sonnet-4-6, qwen3-coder-480b | `OPENCODE_API_KEY` |
| [OpenCode Go](https://opencode.ai/docs/go/) | `https://opencode.ai/zen/go/v1` | kimi-k2.7, glm-5.1, deepseek-v4-pro | `OPENCODE_API_KEY` |
| [LLM Gateway](https://llmgateway.io) | `https://api.llmgateway.io/v1` | gpt-4o, claude-3-5-sonnet, gemini-2.5-pro | `LLM_GATEWAY_API_KEY` |
| [ZenMux](https://zenmux.ai) | `https://zenmux.ai/api/v1` | openai/gpt-5, anthropic/claude-sonnet-4, google/gemini-2.5-pro | `ZENMUX_API_KEY` |
| [Sakana AI (Fugu)](https://console.sakana.ai) | `https://api.sakana.ai/v1` | fugu, fugu-ultra, fugu-ultra-20260615 | `SAKANA_API_KEY` |
| [Prism API](https://go165.github.io/prism-api-promo/) | `https://sub2api.558686.xyz/v1` | gpt-5.5, gpt-5.4, claude-sonnet-4 | `PRISM_API_KEY` |
| [DiscountedTokens](https://discountedtokens.com) | `https://discountedtokens.com/v1` | GPT-5.5, GPT-5.4, GPT-5.6 | `DISCOUNTEDTOKENS_API_KEY` |
| [XiuRouter](https://router.xiu.ai/) | `https://router-api.xiu.ai/v1` | gpt-5.6-sol, gpt-5.5, claude-opus-5 | `XIUROUTER_API_KEY` |
| [SAGG](https://api.privatedeskai.com) | `https://api.privatedeskai.com/v1` | deepseek-ai/DeepSeek-V4-Flash-0731 | `SAGG_API_KEY` |
| [AIWave](https://aiwave.live/) | `https://aiwave.live/v1` | deepseek-v4-pro, deepseek-v4-flash, deepseek-v3.2 | `AIWAVE_API_KEY` |
| [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | `http://localhost:8317/v1` | — | `CLIPROXYAPI_KEY` |
| [9router](https://www.npmjs.com/package/9router) | `http://localhost:20130/v1` | — | — |
| [1min.AI](https://1min.ai) | `https://api.1min.ai/api/chat-with-ai` | gpt-4o-mini | `ONEMINAI_API_KEY` |
| [Cheaper Inference](https://cheaperinference.com) | `https://api.cheaperinference.com/v1` | aion-labs.aion-2-0, claude-fable-5, claude-haiku-4.5 | `CHEAPERINFERENCE_API_KEY` |
| [Freebuff](https://freebuff.com) | `https://www.codebuff.com/api/v1` | deepseek/deepseek-v4-flash, deepseek/deepseek-v4-pro, openai/gpt-5.6-luna | `FREEBUFF_API_KEY` |
| [Charm Hyper](https://hyper.charm.land) | `https://hyper.charm.land/v1` | hyper/auto | `CHARM_HYPER_API_KEY` |
| [AgentRouter](https://agentrouter.org) | `https://agentrouter.org/v1` | claude-opus-4-8, claude-opus-5, gpt-5.6-sol | `AGENTROUTER_API_KEY` |
| [UnoRouter](https://unorouter.ai) | `https://api.unorouter.com/v1` | — | `UNOROUTER_API_KEY` |
| [Command Code](https://commandcode.ai) | `https://api.commandcode.ai` | claude-opus-4-7, claude-opus-4-6, claude-sonnet-4-6 | `COMMAND_CODE_API_KEY` |
| [Zylo API](https://zyloai.net) | `https://api.zyloai.net/v1` | — | `ZYLO_API_KEY` |
| [FastRouter](https://fastrouter.ai) | `https://api.fastrouter.ai/api/v1` | — | `FASTROUTER_API_KEY` |
| [LLM.Kiwi](https://llm.kiwi) | `https://api.llm.kiwi/v1` | auto, hrLLM | `LLM_KIWI_API_KEY` |
| [LiteRouter](https://literouter.com) | `https://api.literouter.com/v1` | — | `LITEROUTER_API_KEY` |
| [GreenPT](https://greenpt.com) | `https://api.greenpt.ai/v1` | — | `GREENPT_API_KEY` |
| [EURouter](https://eurouter.ai) | `https://api.eurouter.ai/v1` | — | `EUROUTER_API_KEY` |
| [MNN AI](https://mnnai.ru) | `https://api.mnnai.ru/v1` | — | `MNN_AI_API_KEY` |
| [MegaNova AI](https://meganova.ai) | `https://api.meganova.ai/v1` | — | `MEGANOVA_AI_API_KEY` |
| [Mixlayer](https://www.mixlayer.com) | `https://models.mixlayer.ai/v1` | qwen/qwen3.5-4b-free | `MIXLAYER_API_KEY` |
| [Speka AI](https://speka.me) | `https://speka.me/v1` | — | `SPEKA_API_KEY` |
| [TokenReply](https://www.tokenreply.com) | `https://api.tokenreply.com/v1` | — | `TOKENREPLY_API_KEY` |
| [Yolo-Auto](https://yolo-auto.com) | `https://yolo-auto.com/v1` | qwen3.6-35b-a3b | `YOLO_AUTO_API_KEY` |
| [DXNT / DX Token](https://www.dxnt.com) | `https://www.dxnt.com/v1` | — | `DXNT_API_KEY` |
| [CloudCode.ONE](https://cloudcode.one) | `https://api.cloudcode.one/v1` | glm-4.7-flash, glm-4.6v-flash | `CLOUDCODE_ONE_API_KEY` |
| [OfoxAI](https://ofox.ai) | `https://api.ofox.ai/v1` | — | `OFOXAI_API_KEY` |
| [ZeroLimitAI](https://www.zerolimitai.com) | `https://www.zerolimitai.com/api/v1` | — | `ZEROLIMITAI_API_KEY` |
| [Helyx AI](https://helyxai.space) | `https://helyxai.space/v1` | — | `HELYXAI_API_KEY` |
| [Auriko](https://www.auriko.ai) | `https://api.auriko.ai/v1` | — | `AURIKO_API_KEY` |
| [Poixe AI](https://poixe.com) | `https://api.poixe.com/v1` | — | `POIXE_AI_API_KEY` |
| [Chat Oripe](https://api.oriper.com) | `https://api.oriper.com/v1` | — | `CHAT_ORIPE_API_KEY` |
| [FreeInference](https://freeinference.org) | `https://freeinference.org/v1` | — | `FREEINFERENCE_API_KEY` |
| [Free.ai](https://free.ai) | `https://api.free.ai/v1/chat` | — | `FREE_AI_API_KEY` |
| [DGrid](https://dgrid.ai) | `https://api.dgrid.ai/v1` | dgridai/free | `DGRID_API_KEY` |
| [Qiniu](https://www.qiniu.com) | `https://api.qnaigc.com/v1` | — | `QINIU_API_KEY` |
| [OrcaRouter](https://www.orcarouter.ai) | `https://api.orcarouter.ai/v1` | orcarouter/auto, openai/gpt-5.5, google/gemini-3.6-flash | `ORCAROUTER_API_KEY` |
| [Api.airforce](https://api.airforce) | `https://api.airforce/v1` | x-ai/grok-3, x-ai/grok-2-1212, anthropic/claude-3.7-sonnet | `AIRFORCE_API_KEY` |
| [CrofAI](https://crof.ai) | `https://crof.ai/v1` | deepseek-v4-pro, deepseek-v4-flash, deepseek-v4-flash-0731 | `CROF_API_KEY` |
| [BazaarLink](https://bazaarlink.ai) | `https://bazaarlink.ai/api/v1` | auto:free, claude-opus-4.7, claude-sonnet-4.6 | `BAZAARLINK_API_KEY` |
| [Synthetic](https://synthetic.new) | `https://api.synthetic.new/openai/v1` | hf:openai/gpt-oss-120b, hf:zai-org/GLM-5.2, hf:moonshotai/Kimi-K2.7-Code | `SYNTHETIC_API_KEY` |
| [Kilo Gateway](https://kilo.ai) | `https://api.kilo.ai/api/gateway` | kilo-auto/frontier, kilo-auto/balanced, kilo-auto/free | `KILO_GATEWAY_API_KEY` |
| [Dahl](https://inference.dahl.global) | `https://inference.dahl.global/v1` | MiniMaxAI/MiniMax-M2.7, moonshotai/Kimi-K2.6 | `DAHL_API_KEY` |
| [FreeTheAi](https://freetheai.xyz) | `https://api.freetheai.xyz/v1` | gpt-4o-mini, llama-3.3-70b-instruct, deepseek-chat | `FREETHEAI_API_KEY` |
| [g4f.space — Groq](https://g4f.space) | `https://g4f.space/api/groq/v1` | llama-3.3-70b-versatile, llama-3.1-8b-instant | `G4F_GROQ_API_KEY` |
| [g4f.space — Gemini](https://g4f.space) | `https://g4f.space/api/gemini/v1` | models/gemini-2.5-flash, models/gemini-2.5-pro | `G4F_GEMINI_API_KEY` |
| [g4f.space — Pollinations](https://g4f.space) | `https://g4f.space/api/pollinations/v1` | openai, openai-fast | `G4F_POLLINATIONS_API_KEY` |
| [g4f.space — Ollama](https://g4f.space) | `https://g4f.space/api/ollama/v1` | gemma3:4b | `G4F_OLLAMA_API_KEY` |
| [g4f.space — NVIDIA](https://g4f.space) | `https://g4f.space/api/nvidia/v1` | nvidia/nemotron-3-nano-30b-a3b, z-ai/glm-5.2, minimaxai/minimax-m2.7 | `G4F_NVIDIA_API_KEY` |
| [LLM7.io](https://llm7.io) | `https://api.llm7.io/v1` | gpt-4o-mini-2024-07-18, gpt-4.1-nano-2025-04-14, deepseek-r1-0528 | `LLM7_API_KEY` |
| [LlamaGate](https://llamagate.ai) | `https://llamagate.ai/v1` | — | `LLAMAGATE_API_KEY` |
| [Gitlawb Opengateway (MiMo)](https://opengateway.gitlawb.com) | `https://opengateway.gitlawb.com/v1/xiaomi-mimo` | mimo-v2.5-pro, mimo-v2.5, mimo-v2-pro | `GITLAWB_API_KEY` |
| [Gitlawb Opengateway (GMI Cloud)](https://opengateway.gitlawb.com) | `https://opengateway.gitlawb.com/v1/gmi-cloud` | XiaomiMiMo/MiMo-V2.5-Pro, XiaomiMiMo/MiMo-V2.5, openai/gpt-5.5 | `GITLAWB_GMI_API_KEY` |
| [NanoGPT](https://nano-gpt.com) | `https://nano-gpt.com/api/v1` | — | `NANOGPT_API_KEY` |
| [LaoZhang AI](https://api.laozhang.ai) | `https://api.laozhang.ai/v1` | — | `LAOZHANG_API_KEY` |
| [b.ai](https://b.ai) | `https://api.b.ai/v1` | — | `BAI_API_KEY` |
| [FenayAI](https://fenayai.com) | `https://api.fenayai.com/v1` | — | `FENAYAI_API_KEY` |
| [Empower](https://docs.empower.dev) | `https://api.empower.dev/v1` | — | `EMPOWER_API_KEY` |
| [Factory](https://factory.ai) | `https://api.factory.ai/v1` | auto | `FACTORY_API_KEY` |
| [BluesMinds](https://www.bluesminds.com) | `https://api.bluesminds.com/v1` | gpt-4o, gpt-4o-mini, gpt-4.1 | `BLUESMINDS_API_KEY` |
| [FreeModel.dev](https://freemodel.dev) | `https://api.freemodel.dev/v1` | gpt-5.5, gpt-5.4, gpt-5.4-mini | `FREEMODEL_DEV_API_KEY` |
| [FreeAIAPIKey](https://freeaiapikey.com) | `https://api.freeaiapikey.com/v1` | openai/gpt-4o, openai/gpt-5.4, openai/gpt-5.5 | `FREEAI_API_KEY` |
| [OpenAdapter](https://openadapter.dev) | `https://api.openadapter.in/v1` | glm-4.7 | `OPENADAPTER_API_KEY` |
| [DIT.ai](https://dit.ai) | `https://api.dit.ai/v1` | gpt-5.4, claude-sonnet-4-6 | `DIT_API_KEY` |
| [TokenRouter](https://tokenrouter.com) | `https://api.tokenrouter.com/v1` | minimax-3, deepseek-v4-pro, deepseek-v4-flash | `TOKENROUTER_API_KEY` |
| [Token Kiosk](https://agent-router.gaib.ai) | `https://agent-router.gaib.ai/v1` | claude-3-5-sonnet, deepseek-v3, deepseek-r1 | `TOKEN_KIOSK_API_KEY` |
| [SumoPod](https://ai.sumopod.com) | `https://ai.sumopod.com/v1` | — | `SUMOPOD_API_KEY` |
| [X5Lab](https://x5lab.dev) | `https://api.x5lab.dev/v1` | — | `X5LAB_API_KEY` |
| [Chenzk API](https://chenzk.top) | `https://chenzk.top/v1` | — | `CHENZK_API_KEY` |
| [Kenari](https://kenari.id) | `https://kenari.id/v1` | — | `KENARI_API_KEY` |
| [NavyAI](https://api.navy) | `https://api.navy/v1` | llama-3.3-70b-instruct, gemma-4-31b-it, deepseek-v4-flash | `NAVY_API_KEY` |
| [AINative Studio](https://ainative.studio) | `https://api.ainative.studio/api/v1` | qwen3-235b-cerebras, qwen3-32b, qwen3-14b | `AINATIVE_API_KEY` |
| [Routeway](https://routeway.ai) | `https://api.routeway.ai/v1` | llama-3.3-70b-instruct:free, nemotron-3-nano-30b-a3b:free, nemotron-nano-9b-v2:free | `ROUTEWAY_API_KEY` |
| [NaraRouter](https://bynara.id) | `https://router.bynara.id/v1` | agnes-2.0-flash, agnes-2.5-flash, laguna-s-2.1 | `NARA_API_KEY` |
| [Regolo AI](https://regolo.ai) | `https://api.regolo.ai` | regolo-chat, regolo-fast | `REGOLO_API_KEY` |
| [Void AI](https://voidai.app) | `https://api.voidai.app/v1` | — | `VOID_AI_API_KEY` |
| [HelixMind](https://helixmind.online) | `https://helixmind.online/v1` | — | `HELIXMIND_API_KEY` |
| [Logfare](https://logfare.ai) | `https://logfare.ai/v1` | — | `LOGFARE_API_KEY` |
| [TabiToken](https://tabitoken.com) | `https://tabitoken.com/v1` | claude-opus-5, claude-opus-5-thinking, claude-opus-4-8 | `TABITOKEN_API_KEY` |
| [SeekAi](https://seekai.cc) | `https://seekai.cc/v1` | — | `SEEKAI_API_KEY` |
| [Cursor API](https://cursor.com/dashboard/api) | `https://api.cursor.com/v1` | — | `CURSOR_API_KEY` |
| [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | `http://localhost:3000/v1` | kimi-k2.7-code, claude-sonnet-4, gpt-5.5 | `OMNIROUTE_API_KEY` |
| [Bifrost](https://github.com/maximhq/bifrost) | `http://localhost:8080/v1` | — | — |
| [Abacus](https://abacus.ai) | `https://routellm.abacus.ai/v1` | route-llm-code, route-llm-code-low, route-llm | `ABACUS_API_KEY` |
| [Merge Gateway](https://docs.merge.dev/merge-gateway) | `https://api-gateway.merge.dev/v1` | openai/gpt-5.2, anthropic/claude-sonnet-5, google/gemini-3.6-flash | `MERGE_GATEWAY_API_KEY` |
| [NEAR AI Cloud](https://docs.near.ai/) | `https://cloud-api.near.ai/v1` | anthropic/claude-fable-5, anthropic/claude-fable-5-1, anthropic/claude-haiku-4-5 | `NEARAI_API_KEY` |
| [SCX.ai](https://platform.scx.ai) | `https://api.scx.ai/v1` | GLM-5.2, Qwen3.8-Max, MiniMax-M2.7 | `SCX_API_KEY` |
| [iFlow](https://platform.iflow.cn) | `https://apis.iflow.cn/v1` | qwen3-vl-plus, glm-4.6, qwen3-32b | `IFLOW_API_KEY` |
| [LLMTR](https://llmtr.com) | `https://llmtr.com/v1` | llmtr/gemma-4, llmtr/qwen3-6-35b, llmtr/trendyol-asure-12b | `LLMTR_API_KEY` |
| [ai&](https://docs.aiand.com/) | `https://api.aiand.com/v1` | zai-org/glm-5.3, qwen/qwen3.8-27b, moonshotai/kimi-k3 | `AIAND_API_KEY` |
| [Inco](https://platform.inco.ai) | `https://api.inco.ai/v1` | kimi-k3:fast, glm-5.3:fast, glm-5.3-flash:fast | `INCO_API_KEY` |
| [Pendra](https://pendra.ai) | `https://api.pendra.ai/api/v1` | llama3.3:70b, qwen3-coder:30b, gpt-oss:120b | `PENDRA_API_KEY` |

## Aggregators

Multi-vendor catalogs under one bill.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [AIMLAPI](https://aimlapi.com) | `https://api.aimlapi.com/v1` | gpt-4o, claude-3-5-sonnet, gemini | `AIMLAPI_KEY` |
| [Eden AI](https://edenai.co) | `https://api.edenai.co/v2` | OpenAI, Google, Anthropic routes | `EDENAI_API_KEY` |
| [LemonData](https://lemondata.ai) | `https://api.lemondata.ai/v1` | gpt-4o, claude-3.5, open models | `LEMONDATA_API_KEY` |
| [Coze (ByteDance)](https://coze.com) | `https://api.coze.com/v1` | Via bots: GPT-4o, Gemini, Claude | `COZE_API_KEY` |
| [302.AI](https://302.ai) | `https://api.302.ai/v1` | glm-5, gpt-4o, claude-sonnet-4 | `AI302_API_KEY` |
| [FrogBot](https://frogbot.ai) | `https://app.frogbot.ai/api` | claude-sonnet-4, gpt-4o, gemini-2.5-pro | `FROGBOT_API_KEY` |
| [AnyAPI AI](https://anyapi.ai) | `https://api.anyapi.ai/v1` | — | `ANYAPI_KEY` |
| [Electron Hub](https://www.electronhub.ai) | `https://api.electronhub.ai/v1` | — | `ELECTRONHUB_API_KEY` |
| [ChatAnywhere](https://chatanywhere.tech) | `https://api.chatanywhere.org/v1` | — | `CHATANYWHERE_API_KEY` |
| [PiAPI](https://piapi.ai) | `https://api.piapi.ai` | — | `PIAPI_KEY` |
| [GoAPI](https://api.getgoapi.com) | `https://api.getgoapi.com/v1` | — | `GETGOAPI_KEY` |
| [TheB.AI](https://theb.ai) | `https://api.theb.ai/v1` | — | `THEBAI_API_KEY` |
| [Poe](https://creator.poe.com/api-reference) | `https://api.poe.com` | gpt-5.2, claude-opus-4.8, gemini-3.0-pro | `POE_API_KEY` |
| [Naga.ac](https://naga.ac) | `https://api.naga.ac/v1` | — | `NAGA_AC_API_KEY` |
| [Jiekou.AI](https://docs.jiekou.ai) | `https://api.jiekou.ai/openai` | grok-4-1-fast-reasoning, grok-4-1-fast-non-reasoning, gpt-5.2-codex | `JIEKOU_API_KEY` |
| [AIHubMix](https://aihubmix.com) | `https://aihubmix.com/v1` | auto, claude-opus-5-5, gpt-6-luna | `AIHUBMIX_API_KEY` |
| [EmpirioLabs AI](https://docs.empiriolabs.ai) | `https://api.empiriolabs.ai/v1` | glm-5-3, kling-3-0-turbo, glm-5-3-flash | `EMPIRIOLABS_API_KEY` |

## OAuth and IDE

Claude Code, Codex, Cursor, Copilot, and similar subscriptions.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [GitHub Enterprise Copilot](https://docs.github.com/en/copilot) | GitHub Enterprise host (device-flow OAuth) | claude-fable-5, claude-opus-5, claude-opus-4.8-fast | — |
| [xAI OAuth (Grok)](https://x.ai) | OAuth (provider-specific) | grok-4.5 | — |
| [Openference](https://openference.com) | `https://api.openference.com/v1` | GLM-5.2 | — |
| [Grok Build](https://x.ai) | `https://cli-chat-proxy.grok.com/v1` | grok-4.6, grok-4.5, grok-composer-2.5-fast | — |
| [Qoder](https://qoder.com) | `https://api.qoder.com/v1` | qwen3.8-max-preview, qwen3.7-max, qwen3.7-plus | — |
| [Antigravity CLI](https://antigravity.google) | OAuth (provider-specific) | — | — |
| [Kiro AI](https://kiro.dev) | `https://codewhisperer.us-east-1.amazonaws.com/generateAssistantResponse` | claude-sonnet-5, claude-sonnet-4.5, claude-haiku-4.5 | — |
| [Amazon Q](https://aws.amazon.com/q/developer) | OAuth (provider-specific) | — | — |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | `https://api.anthropic.com/v1` | claude-fable-5-1, claude-fable-5, claude-opus-5 | — |
| [Antigravity](https://antigravity.google) | OAuth (provider-specific) | — | — |
| [OpenAI Codex](https://developers.openai.com/codex) | `https://chatgpt.com/backend-api/codex` | gpt-6-astra, gpt-6-astra-ultra, gpt-6-astra-max | — |
| [Cursor IDE](https://cursor.com) | `https://api2.cursor.sh` | auto, auto-cost, auto-balance | — |
| [Zed IDE](https://zed.dev) | OAuth (provider-specific) | — | — |
| [Zed Hosted Models](https://zed.dev) | `https://cloud.zed.dev` | — | — |
| [Trae](https://trae.ai) | `https://core-normal.trae.ai/api/remote/v1` | auto, work, gemini-3.1-pro | — |
| [Kimi Code CLI](https://www.kimi.com/code) | OAuth (provider-specific) | — | — |
| [Kilo Code](https://kilocode.ai) | `https://api.kilo.ai/api/openrouter` | openrouter/free, openai/gpt-5.6-sol, openai/gpt-5.6-terra | — |
| [Cline](https://cline.bot) | `https://api.cline.bot/api/v1` | z-ai/glm-5.2, x-ai/grok-4.5, openai/gpt-5.6-sol | — |
| [ClinePass](https://cline.bot/cline-pass) | `https://api.cline.bot/api/v1` | cline-pass/glm-5.2, cline-pass/minimax-m3, cline-pass/deepseek-v4-pro | — |
| [Devin Desktop](https://devin.ai) | `https://server.codeium.com` | — | — |
| [Devin CLI](https://cli.devin.ai) | OAuth (provider-specific) | — | — |
| [CodeBuddy CN](https://copilot.tencent.com) | `https://copilot.tencent.com/v2` | glm-5.2, glm-5.1, glm-5.0 | — |

## Public endpoints

Endpoints that work without an API key (rate limits apply).

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Devin CLI Agentic Bridge](https://docs.devin.ai/work-with-devin/devin-cli) | No-auth public endpoint | — | — |
| [OpenCode Free](https://opencode.ai) | `https://opencode.ai/zen/v1` | big-pickle, muse-spark-1.2, muse-spark-1.2-contributor-free | — |
| [DuckDuckGo AI Chat](https://duckduckgo.com/duckchat) | `https://duck.ai/duckchat/v1/chat` | gpt-5.4-mini, gpt-5.6-luna, claude-haiku-4-5 | — |
| [Cloudflare AI Playground](https://playground.ai.cloudflare.com) | `https://playground.ai.cloudflare.com` | zai-org/glm-5.2, moonshotai/kimi-k2.7-code, moonshotai/kimi-k2.6 | — |
| [Chipotle Pepper AI (Free)](https://amelia.chipotle.com) | `https://amelia.chipotle.com` | pepper-1 | — |
| [Augment (Auggie CLI)](https://augmentcode.com) | No-auth public endpoint | sonnet4.6, fable-5, haiku4.5 | — |
| [ZCode (GLM Coding Plan)](https://zcode.z.ai) | No-auth public endpoint | — | — |
| [OpenAI Codex (App-Server)](https://developers.openai.com/codex/cli) | No-auth public endpoint | — | — |
| [UncloseAI](https://uncloseai.com) | `https://hermes.ai.unturf.com/v1` | adamo1139/Hermes-3-Llama-3.1-8B-FP8-Dynamic, qwen3.6:27b, gemma4:31b | — |
| [AI Horde](https://aihorde.net) | `https://oai.aihorde.net/v1` | aphrodite/TheDrummer/Cydonia-24B-v4.3, aphrodite/TheDrummer/Skyfall-31B-v4.2, google/gemma-4-31b | — |

## Search APIs

Web search, fetch, and crawl.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Perplexity Search](https://docs.perplexity.ai/guides/search-quickstart) | `https://api.perplexity.ai` | — | `PERPLEXITY_SEARCH_API_KEY` |
| [Serper Search](https://serper.dev) | `https://google.serper.dev` | — | `SERPER_SEARCH_API_KEY` |
| [Brave Search](https://brave.com/search/api) | `https://api.search.brave.com/res/v1` | — | `BRAVE_SEARCH_API_KEY` |
| [Exa Search](https://exa.ai) | `https://api.exa.ai` | — | `EXA_SEARCH_API_KEY` |
| [Tavily Search](https://tavily.com) | `https://api.tavily.com` | — | `TAVILY_SEARCH_API_KEY` |
| [AnySearch](https://anysearch.com) | `https://api.anysearch.com` | — | `ANYSEARCH_SEARCH_API_KEY` |
| [Firecrawl](https://firecrawl.dev) | `https://api.firecrawl.dev/v1` | — | `FIRECRAWL_API_KEY` |
| [Google Programmable Search](https://developers.google.com/custom-search/v1/overview) | `https://www.googleapis.com/customsearch/v1` | — | `GOOGLE_PSE_SEARCH_API_KEY` |
| [Nimble Search](https://docs.nimbleway.com/nimble-sdk/web-tools/search) | `https://api.webit.live` | — | `NIMBLE_SEARCH_API_KEY` |
| [Linkup Search](https://docs.linkup.so) | `https://api.linkup.so` | — | `LINKUP_SEARCH_API_KEY` |
| [SearchAPI](https://www.searchapi.io/docs/google) | `https://www.searchapi.io/api/v1/search` | — | `SEARCHAPI_KEY` |
| [You.com Search](https://you.com/business/api) | `https://api.ydc-index.io` | — | `YOUCOM_SEARCH_API_KEY` |
| [SearXNG Search](https://docs.searxng.org) | `http://localhost:8080` | — | `SEARXNG_SEARCH_API_KEY` |
| [X Search (Grok)](https://docs.x.ai/developers/tools/x-search) | `https://api.x.ai/v1` | — | `X_SEARCH_API_KEY` |
| [Xquik X Search](https://docs.xquik.com) | `https://api.xquik.com` | — | `XQUIK_SEARCH_API_KEY` |
| [Ollama Search](https://ollama.com/settings/keys) | `https://ollama.com/api` | — | `OLLAMA_SEARCH_API_KEY` |
| [Context7 (library docs)](https://context7.com) | `https://context7.com` | — | `CONTEXT7_API_KEY` |
| [Jina Reader (r.jina.ai)](https://jina.ai/reader) | `https://r.jina.ai` | — | `JINA_READER_API_KEY` |
| [TinyFish Fetch](https://docs.tinyfish.ai/fetch-api) | `https://api.tinyfish.ai` | — | `TINYFISH_API_KEY` |

## Audio

Speech-to-text and text-to-speech.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Deepgram](https://deepgram.com) | `https://api.deepgram.com/v1` | — | `DEEPGRAM_API_KEY` |
| [AssemblyAI](https://assemblyai.com) | `https://api.assemblyai.com/v2` | — | `ASSEMBLYAI_API_KEY` |
| [Soniox](https://soniox.com) | `https://api.soniox.com` | — | `SONIOX_API_KEY` |
| [ElevenLabs](https://elevenlabs.io) | `https://api.elevenlabs.io/v1` | — | `ELEVENLABS_API_KEY` |
| [Cartesia](https://cartesia.ai) | `https://api.cartesia.ai` | — | `CARTESIA_API_KEY` |
| [Fish Audio](https://fish.audio) | `https://api.fish.audio` | — | `FISHAUDIO_API_KEY` |
| [PlayHT](https://play.ht) | `https://api.play.ht/api/v2` | — | `PLAYHT_API_KEY` |
| [Inworld](https://inworld.ai) | `https://api.inworld.ai` | — | `INWORLD_API_KEY` |
| [AWS Polly](https://aws.amazon.com/polly) | `https://polly.us-east-1.amazonaws.com` | — | `AWS_POLLY_API_KEY` |
| [Gladia](https://gladia.io) | `https://api.gladia.io/v2` | — | `GLADIA_API_KEY` |
| [Rev AI](https://www.rev.ai) | `https://api.rev.ai` | — | `REV_AI_API_KEY` |
| [Speechmatics](https://www.speechmatics.com) | `https://asr.api.speechmatics.com/v2` | — | `SPEECHMATICS_API_KEY` |

## Image and video

Image and video generation APIs.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Veo AI Free](https://veoaifree.com) | `https://veoaifree.com/wp-admin/admin-ajax.php` | veo, seedance | — |
| [Agnes AI](https://agnes-ai.com) | `https://apihub.agnes-ai.com/v1` | agnes-2.0-flash, agnes-2.5-flash, agnes-3.0-flash | `AGNES_API_KEY` |
| [Runway](https://docs.dev.runwayml.com) | `https://api.dev.runwayml.com/v1` | — | `RUNWAYML_API_KEY` |
| [KIE.AI](https://kie.ai) | `https://api.kie.ai/v1` | claude-fable-5, claude-opus-5, claude-sonnet-5 | `KIE_API_KEY` |
| [Haiper](https://haiper.ai) | `https://api.haiper.ai/v1` | gen2, gen2-image | `HAIPER_API_KEY` |
| [Leonardo AI](https://leonardo.ai) | `https://cloud.leonardo.ai/api/rest/v1` | phoenix, sdxl | `LEONARDO_API_KEY` |
| [Ideogram](https://ideogram.ai) | `https://api.ideogram.ai` | V_3, V_2A | `IDEOGRAM_API_KEY` |
| [Magnific](https://www.magnific.com) | `https://api.magnific.com/v1/ai/mystic` | realism, fluid, zen | `MAGNIFIC_API_KEY` |
| [Suno](https://suno.ai) | `https://studio-api.suno.ai/api/generate/v2` | chirp-fenix, chirp-crow, chirp-v4 | `SUNO_API_KEY` |
| [Udio](https://udio.com) | `https://www.udio.com/api/generate-proxy` | udio-default | `UDIO_API_KEY` |
| [Fal.ai](https://fal.ai) | `https://fal.run` | — | `FAL_AI_API_KEY` |
| [Stability AI](https://stability.ai) | `https://api.stability.ai` | — | `STABILITY_AI_API_KEY` |
| [Black Forest Labs](https://blackforestlabs.ai) | `https://api.bfl.ai` | — | `BLACK_FOREST_LABS_API_KEY` |
| [Recraft](https://recraft.ai) | `https://external.api.recraft.ai/v1` | — | `RECRAFT_API_KEY` |
| [Topaz](https://topazlabs.com) | `https://api.topazlabs.com` | — | `TOPAZ_API_KEY` |
| [Segmind](https://segmind.com) | `https://api.segmind.com/v1` | — | `SEGMIND_API_KEY` |
| [DeepAI](https://deepai.org) | `https://api.deepai.org` | text2img | `DEEPAI_API_KEY` |

## Cloud agents

Hosted coding agents (task-based, not a chat API).

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Google Jules](https://jules.google) | `https://jules.google` | — | `JULES_API_KEY` |
| [Devin](https://devin.ai) | `https://api.devin.ai` | — | `DEVIN_API_KEY` |
| [Codex Cloud](https://openai.com/codex) | `https://chatgpt.com/backend-api/codex` | — | `CODEX_CLOUD_API_KEY` |

## Embeddings

Retrieval embeddings and rerankers.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Voyage AI](https://www.voyageai.com) | `https://api.voyageai.com/v1` | voyage-3, voyage-3-lite, rerank-2 | `VOYAGE_API_KEY` |
| [Jina AI (Foundation API)](https://jina.ai) | `https://api.jina.ai/v1` | — | `JINA_AI_API_KEY` |
| [Nomic](https://nomic.ai) | `https://api-atlas.nomic.ai/v1` | — | `NOMIC_API_KEY` |
| [Mixedbread AI](https://www.mixedbread.com) | `https://api.mixedbread.com/v1` | — | `MIXEDBREAD_API_KEY` |

## Specialized

Task-specific APIs that do not fit the groups above.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [NLP Cloud](https://nlpcloud.com) | `https://api.nlpcloud.io/v1` | finetuned-llama-3-70b, chatdolphin | `NLP_CLOUD_API_KEY` |
| [Puter.js](https://puter.com) | `https://api.puter.com/ai/chat` | gpt-4o-mini, claude-3.5-sonnet, gemini | — |
| [v0 (Vercel)](https://v0.dev) | `https://api.v0.dev/v1` | — | `V0_VERCEL_API_KEY` |
| [Dify](https://dify.ai) | `https://api.dify.ai` | auto | `DIFY_API_KEY` |

## Local and self-hosted

Run models on your own machine.

| Provider | API Base URL | Models | Env |
|----------|--------------|--------|-----|
| [Ollama](https://ollama.com) | `http://localhost:11434/v1` | llama3.3, qwen2.5, gemma | — |
| [LM Studio](https://lmstudio.ai) | `http://localhost:1234/v1` | — | — |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | `http://localhost:8080/v1` | — | — |
| [Jan.ai](https://jan.ai) | `http://localhost:1337/v1` | — | — |
| [vLLM](https://github.com/vllm-project/vllm) | `http://localhost:8000/v1` | — | — |
| [LocalAI](https://localai.io) | `http://localhost:8080/v1` | OpenAI-compatible local stack | — |
| [Atomic Chat](https://atomicchat.ai) | `http://127.0.0.1:1337/v1` | qwen-coder, deepseek-coder | — |
| [MLX Gemma 26B](https://github.com/ml-explore/mlx) | `http://localhost:${MLX_GEMMA_PORT}/v1` | mlx-community/gemma-4-26B-A4B-it-qat-q4_0-mlx-aligned | — |
| [MLX Qwen 3.8 27B](https://github.com/ml-explore/mlx) | `http://localhost:${MLX_QWEN_PORT}/v1` | maglun/Qwen3.8-27B-MLX-Mixed-3.80bpw | — |
| [Lemonade Server](https://lemonade-server.ai) | `http://localhost:13305/api/v1` | — | — |
| [Llamafile](https://github.com/Mozilla-Ocho/llamafile) | `http://127.0.0.1:8080/v1` | — | — |
| [NVIDIA Triton](https://developer.nvidia.com/triton-inference-server) | `http://localhost:8000/v1` | — | — |
| [Docker Model Runner](https://docs.docker.com/ai/model-runner) | `http://localhost:12434/v1` | — | — |
| [XInference](https://inference.readthedocs.io) | `http://localhost:9997/v1` | — | — |
| [oobabooga](https://github.com/oobabooga/text-generation-webui) | `http://localhost:5000/v1` | — | — |
| [SD WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | `http://localhost:7860` | — | — |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | `http://localhost:8188` | — | — |
| [Muse Code (Meta)](https://github.com/meta-llama/llama-stack) | `http://localhost:8321/v1` | llama-4-maverick, llama-4-scout, llama-3.3-70b | — |

## Pick a provider

| Goal | Start here |
|------|------------|
| Best reasoning | OpenAI, Anthropic, Gemini |
| Low cost / open models | Groq, DeepInfra, Together, SiliconFlow |
| One API, many models | OpenRouter, Portkey |
| EU / GDPR | Mistral, Nebius, Scaleway, OVHcloud |
| Code agents | Claude Code, Codex, Cursor, Moonshot Kimi |
| Offline | Ollama, LM Studio, vLLM |

Env var names are in the tables above and in `python llm_lookup.py <slug>`.

## Contributing

PRs welcome for new endpoints or corrected model IDs. See [docs/contributing.md](docs/contributing.md).

```bash
python llm_lookup.py <slug> --models
python scripts/sync_models.py
```

## License

MIT. Not affiliated with any listed provider.
