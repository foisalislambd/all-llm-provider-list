#!/usr/bin/env python3
"""
Sync model catalogs into data/models.json.

Public APIs (no key): OpenRouter, DeepInfra, HuggingFace
Optional live fetch via env API keys: OPENAI_API_KEY, GROQ_API_KEY, etc.

Run:  python scripts/sync_models.py
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROVIDERS_FILE = ROOT / "data" / "providers.json"
STATIC_FILE = ROOT / "data" / "static_models.json"
OUTPUT_FILE = ROOT / "data" / "models.json"

# slug -> public GET /v1/models URL (no auth)
PUBLIC_MODEL_APIS: dict[str, str] = {
    "openrouter": "https://openrouter.ai/api/v1/models",
    "deepinfra": "https://api.deepinfra.com/v1/openai/models",
    "huggingface": "https://router.huggingface.co/v1/models",
}

# slug -> (env_var, models_url)
AUTH_MODEL_APIS: dict[str, tuple[str, str]] = {
    "openai": ("OPENAI_API_KEY", "https://api.openai.com/v1/models"),
    "groq": ("GROQ_API_KEY", "https://api.groq.com/openai/v1/models"),
    "together": ("TOGETHER_API_KEY", "https://api.together.xyz/v1/models"),
    "fireworks": ("FIREWORKS_API_KEY", "https://api.fireworks.ai/inference/v1/models"),
    "mistral": ("MISTRAL_API_KEY", "https://api.mistral.ai/v1/models"),
    "deepseek": ("DEEPSEEK_API_KEY", "https://api.deepseek.com/v1/models"),
    "xai": ("XAI_API_KEY", "https://api.x.ai/v1/models"),
    "cerebras": ("CEREBRAS_API_KEY", "https://api.cerebras.ai/v1/models"),
    "sambanova": ("SAMBANOVA_API_KEY", "https://api.sambanova.ai/v1/models"),
    "nebius": ("NEBIUS_API_KEY", "https://api.studio.nebius.ai/v1/models"),
    "openrouter": ("OPENROUTER_API_KEY", "https://openrouter.ai/api/v1/models"),
    "sakana-fugu": ("SAKANA_API_KEY", "https://api.sakana.ai/v1/models"),
}


def _http_get_json(url: str, api_key: str | None = None, timeout: int = 30) -> dict | list:
    headers = {"Accept": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _extract_model_ids(payload: dict | list) -> list[str]:
    if isinstance(payload, list):
        items = payload
    else:
        items = payload.get("data") or payload.get("models") or []
    ids: list[str] = []
    for item in items:
        if isinstance(item, str):
            ids.append(item)
        elif isinstance(item, dict):
            mid = item.get("id") or item.get("name") or item.get("model")
            if mid:
                ids.append(str(mid))
    return sorted(set(ids))


def _models_url_from_base(base: str) -> str | None:
    if not base.startswith("http"):
        return None
    base = base.rstrip("/")
    if base.endswith("/v1"):
        return f"{base}/models"
    if "/v1/" in base or base.endswith("/v1"):
        return f"{base.rstrip('/')}/models"
    return f"{base}/v1/models"


def load_providers() -> list[dict]:
    with PROVIDERS_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def load_static() -> dict[str, list[str]]:
    if not STATIC_FILE.exists():
        return {}
    with STATIC_FILE.open(encoding="utf-8") as f:
        data = json.load(f)
    return data.get("providers", data)


def fetch_live(slug: str) -> tuple[list[str], str]:
    if slug in PUBLIC_MODEL_APIS:
        try:
            payload = _http_get_json(PUBLIC_MODEL_APIS[slug])
            return _extract_model_ids(payload), "live-public"
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            return [], f"live-public-failed: {exc}"

    if slug in AUTH_MODEL_APIS:
        env_var, url = AUTH_MODEL_APIS[slug]
        key = os.environ.get(env_var)
        if not key:
            return [], "skipped-no-api-key"
        try:
            payload = _http_get_json(url, api_key=key)
            return _extract_model_ids(payload), "live-auth"
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            return [], f"live-auth-failed: {exc}"

    return [], "not-configured"


def sync() -> dict:
    providers = load_providers()
    static = load_static()
    catalog: dict[str, dict] = {}
    now = datetime.now(timezone.utc).isoformat()

    for provider in providers:
        slug = provider["slug"]
        live_ids, live_status = fetch_live(slug)
        static_ids = static.get(slug, provider.get("popular_models", []))

        if live_ids:
            models = live_ids
            source = live_status
        else:
            models = static_ids if isinstance(static_ids, list) else []
            source = "static" if models else "unavailable"

        catalog[slug] = {
            "provider_id": provider["id"],
            "provider_name": provider["name"],
            "category": provider["category"],
            "api_base_url": provider["api_base_url"],
            "models_endpoint": _models_url_from_base(provider.get("api_base_url", "")),
            "count": len(models),
            "source": source,
            "updated_at": now,
            "models": models,
        }

    output = {
        "updated_at": now,
        "total_providers": len(catalog),
        "total_models": sum(v["count"] for v in catalog.values()),
        "providers": catalog,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return output


def main() -> None:
    result = sync()
    live = sum(1 for p in result["providers"].values() if p["source"].startswith("live"))
    print(f"Synced {result['total_providers']} providers, {result['total_models']} total model IDs")
    print(f"  Live catalogs: {live}")
    print(f"  Written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
