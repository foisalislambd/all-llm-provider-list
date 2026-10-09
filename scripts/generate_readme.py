#!/usr/bin/env python3
"""Rebuild README.md from data/providers.json."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROVIDERS_FILE = ROOT / "data" / "providers.json"
STATIC_FILE = ROOT / "data" / "static_models.json"
README_FILE = ROOT / "README.md"

PLACEHOLDER_URLS = {
    "",
    "custom endpoint",
    "custom endpoints",
    "custom webhooks",
    "custom cluster endpoints",
    "custom gateway",
    "tracing / observability",
    "evaluation registry",
    "self-hosted / enterprise",
    "region-dependent",
    "open alpha",
    "oauth device flow (copilot subscription)",
    "post /v1/chat/completions",
}

CATEGORY_SECTIONS = [
    ("Frontier", "Frontier labs", "Companies that train their own foundation models."),
    ("IaaS", "Inference platforms", "Hosted open-weight models — usually cheaper and faster."),
    ("Sovereign / Cloud", "Cloud and enterprise", "Azure, Bedrock, Vertex, and regional clouds."),
    ("Gateway", "Gateways and routers", "One key, many upstream providers."),
    ("Aggregator", "Aggregators", "Multi-vendor catalogs under one bill."),
    ("OAuth", "OAuth and IDE", "Claude Code, Codex, Cursor, Copilot, and similar subscriptions."),
    ("No-auth", "Public endpoints", "Endpoints that work without an API key (rate limits apply)."),
    ("Search", "Search APIs", "Web search, fetch, and crawl."),
    ("Audio", "Audio", "Speech-to-text and text-to-speech."),
    ("Image / Video", "Image and video", "Image and video generation APIs."),
    ("Cloud Agent", "Cloud agents", "Hosted coding agents (task-based, not a chat API)."),
    ("Embeddings", "Embeddings", "Retrieval embeddings and rerankers."),
    ("Specialized", "Specialized", "Task-specific APIs that do not fit the groups above."),
    ("Local", "Local and self-hosted", "Run models on your own machine."),
]
README_SKIP_CATEGORIES = {"Web Cookie"}


def is_real_url(url: str | None) -> bool:
    if not url:
        return False
    return url.strip().lower() not in PLACEHOLDER_URLS and url.strip().lower().startswith("http")


def slugify_name(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def md_cell(text: str | None, code: bool = False) -> str:
    if text is None:
        return ""
    s = str(text).replace("|", "\\|").replace("\n", " ").strip()
    if code:
        return f"`{s}`"
    return s


def website_link(name: str, url: str) -> str:
    if url.startswith("http"):
        return f"[{md_cell(name)}]({url})"
    return f"**{md_cell(name)}**"


def popular_cell(models: list) -> str:
    if not models:
        return "—"
    return ", ".join(str(m) for m in models[:3])


def render_category_table(providers: list[dict]) -> str:
    lines = [
        "| Provider | API Base URL | Models | Env |",
        "|----------|--------------|--------|-----|",
    ]
    for p in providers:
        url = p.get("api_base_url") or ""
        url_cell = f"`{url}`" if is_real_url(url) else md_cell(url)
        env = f"`{p['env_variable']}`" if p.get("env_variable") else "—"
        lines.append(
            f"| {website_link(p['name'], p.get('website', ''))} | {url_cell} | {md_cell(popular_cell(p.get('popular_models') or []))} | {env} |"
        )
    return "\n".join(lines)


def generate_readme(providers: list[dict], model_count: int) -> str:
    counts: dict[str, int] = defaultdict(int)
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for p in providers:
        counts[p["category"]] += 1
        by_cat[p["category"]].append(p)
    total = len(providers)
    cookie_n = counts.get("Web Cookie", 0)

    cat_rows = ["| Category | Count |", "|----------|-------|"]
    for key, title, _blurb in CATEGORY_SECTIONS:
        n = counts.get(key, 0)
        if n:
            cat_rows.append(f"| [{title}](#{slugify_name(title)}) | {n} |")
    if cookie_n:
        cat_rows.append(f"| Web cookie adapters (in data only) | {cookie_n} |")
    cat_rows.append(f"| **Total** | **{total}** |")

    sections = []
    for key, title, blurb in CATEGORY_SECTIONS:
        items = by_cat.get(key) or []
        if not items or key in README_SKIP_CATEGORIES:
            continue
        sections.append(f"## {title}\n\n{blurb}\n\n{render_category_table(items)}\n")

    cookie_note = ""
    if cookie_n:
        cookie_note = (
            f"\nUnofficial **web-cookie / browser-session** adapters ({cookie_n}) stay in "
            f"`data/providers.json` so they do not clutter this page. List them with "
            f"`python llm_lookup.py --category \"Web Cookie\"`.\n"
        )

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    models_bit = f"{model_count:,} model IDs · " if model_count else ""

    return f"""# All LLM providers

**{total} providers** · {models_bit}API URLs, env vars, and model names in one place.

Always confirm endpoints against official docs. To add or correct a provider, see [docs/contributing.md](docs/contributing.md). Updated {now}.

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
    messages=[{{"role": "user", "content": "Hello!"}}],
).choices[0].message.content)
```

Look up any provider from this repo (no extra packages):

```bash
python llm_lookup.py groq
python llm_lookup.py groq --models
python llm_lookup.py --category Gateway
python llm_lookup.py --search-model kimi
```

Hosted gateways that bill many models on one key: [OpenRouter](https://openrouter.ai), [Portkey](https://portkey.ai).

## Use these providers with one key

[WowRouter](https://github.com/foisalislambd/wowrouter) ([`wowrouter`](https://www.npmjs.com/package/wowrouter), [`@foisalislambd/wowrouter`](https://github.com/foisalislambd/wowrouter)) runs on your computer. You save each provider's API key in its local panel, turn models on, and create one router key. Cursor, Claude Code, Codex, Continue, Cline, and any other coding agent that accepts a custom OpenAI base URL then talk to that single address. Provider keys stay in WowRouter. The agent only sees the router key.

The router listens on this machine only, at `http://127.0.0.1:8787`. It does not sell model access. A call goes through after you have saved that provider's key and switched the model on. A public model id is `provider/model`, such as `openai/gpt-4o-mini`. WowRouter rewrites that to the id the provider expects.

Node.js 20 or newer:

```bash
npm install -g wowrouter
wowrouter
```

`npm install -g airoute` and the `airoute` command are the same program. The same release is also published as `@foisalislambd/wowrouter` and `@foisalislambd/airoute` on GitHub Packages. Desktop builds are on the [GitHub releases](https://github.com/foisalislambd/wowrouter/releases). Docker uses the same panel and API, still bound to this computer:

```bash
docker run -d --name wowrouter \\
  -p 127.0.0.1:8787:8787 \\
  -v wowrouter:/data \\
  foisalislambd/wowrouter:latest
```

Then:

1. Open the panel at `http://127.0.0.1:8787`.
2. Under **Providers**, paste a provider API key and turn on the models you want.
3. Under **API keys**, create a router key. It is shown once and starts with `sk-airoute-`.
4. In the coding agent, set the OpenAI base URL to `http://127.0.0.1:8787/v1` and the API key to that router key. Include `/v1`. The agent appends `/chat/completions` itself.

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8787/v1",
    api_key=os.environ["WOWROUTER_API_KEY"],
)
print(client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{{"role": "user", "content": "Hello!"}}],
).choices[0].message.content)
```

`WOWROUTER_API_KEY` is the router key from the panel, not a provider key. If the first chat model fails, a chain created on the **Fallback** page is called as `fallback/your-name`. Guides for the panel, Cursor, and the API are in the [WowRouter docs](https://github.com/foisalislambd/wowrouter/tree/main/docs).

## Categories

{chr(10).join(cat_rows)}
{cookie_note}
{chr(10).join(sections)}
## Pick a provider

| Goal | Start here |
|------|------------|
| Best reasoning | OpenAI, Anthropic, Gemini |
| Low cost / open models | Groq, DeepInfra, Together, SiliconFlow |
| One API, many models | WowRouter (local, your own keys), OpenRouter, Portkey |
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
"""


def load_static() -> dict[str, list[str]]:
    if not STATIC_FILE.exists():
        return {}
    data = json.loads(STATIC_FILE.read_text(encoding="utf-8"))
    return data.get("providers", data)


def main() -> int:
    providers = json.loads(PROVIDERS_FILE.read_text(encoding="utf-8"))
    static = load_static()
    model_count = 0
    for row in providers:
        ids = static.get(row["slug"]) or row.get("popular_models") or []
        model_count += len(ids)

    README_FILE.write_text(generate_readme(providers, model_count), encoding="utf-8")
    print(f"Wrote {README_FILE} ({len(providers)} providers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
