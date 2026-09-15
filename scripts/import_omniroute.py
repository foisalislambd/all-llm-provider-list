#!/usr/bin/env python3
"""
Import OmniRoute's provider catalog into this repository.

Reads OmniRoute TypeScript catalog + registry files and merges missing
providers (plus models, endpoints, and notes) into:

  data/providers.json
  data/static_models.json
  README.md

Usage:
    python scripts/import_omniroute.py --omniroute /tmp/omniroute
    python scripts/import_omniroute.py --fix
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROVIDERS_FILE = ROOT / "data" / "providers.json"
STATIC_FILE = ROOT / "data" / "static_models.json"
README_FILE = ROOT / "README.md"

# OmniRoute catalog ID -> existing slug in this repo (avoid duplicates).
SLUG_MAP = {
    "gemini": "google-ai-studio",
    "github": "github-copilot",
    "ollama-local": "ollama",
    "voyage-ai": "voyage",
    "sap": "sap-ai-core",
    "vertex": "vertex-ai",
    "snowflake": "snowflake-cortex",
    "nvidia": "nvidia-nim",
    "friendliai": "friendli",
    "aion": "aionlabs",
    "qianfan": "baidu-qianfan",
    "zai": "zhipu",
    "llmgateway": "llm-gateway",
    "alibaba": "dashscope",
    "azure": "azure-openai",
    "azure-ai": "azure-cognitive-services",
    "cloudflare-ai": "cloudflare-workers-ai",
    "arcee-ai": "arcee",
    "xiaomi-mimo": "xiaomi",
    "wandb": "wandb",
    "302ai": "302-ai",
    "nlpcloud": "nlpcloud",
    "lmstudio": "lm-studio",
    "llamacpp": "llama-cpp",
    "llama.cpp": "llama-cpp",
    "kimi": "moonshot",
    "baidu": "baidu-qianfan",
}

# Official endpoints used when OmniRoute registry wraps helpers and omits a literal baseUrl.
KNOWN_BASE_URLS = {
    "jina-ai": "https://api.jina.ai/v1",
    "jina-reader": "https://r.jina.ai",
    "mixedbread": "https://api.mixedbread.com/v1",
    "nomic": "https://api-atlas.nomic.ai/v1",
    "watsonx": "https://us-south.ml.cloud.ibm.com/ml/v1",
    "deepgram": "https://api.deepgram.com/v1",
    "assemblyai": "https://api.assemblyai.com/v2",
    "elevenlabs": "https://api.elevenlabs.io/v1",
    "cartesia": "https://api.cartesia.ai",
    "playht": "https://api.play.ht/api/v2",
    "gladia": "https://api.gladia.io/v2",
    "brave-search": "https://api.search.brave.com/res/v1",
    "serper-search": "https://google.serper.dev",
    "exa-search": "https://api.exa.ai",
    "tavily-search": "https://api.tavily.com",
    "firecrawl": "https://api.firecrawl.dev/v1",
    "suno": "https://api.sunoapi.org",
    "fal-ai": "https://fal.run",
    "stability-ai": "https://api.stability.ai",
    "recraft": "https://external.api.recraft.ai/v1",
    "ideogram": "https://api.ideogram.ai",
    "runwayml": "https://api.dev.runwayml.com/v1",
    "deepai": "https://api.deepai.org",
    "perplexity-search": "https://api.perplexity.ai",
    "anysearch-search": "https://api.anysearch.com",
    "google-pse-search": "https://www.googleapis.com/customsearch/v1",
    "linkup-search": "https://api.linkup.so",
    "searchapi-search": "https://www.searchapi.io/api/v1/search",
    "youcom-search": "https://api.ydc-index.io",
    "searxng-search": "http://localhost:8080",
    "x-search": "https://api.x.ai/v1",
    "context7": "https://context7.com",
    "soniox": "https://api.soniox.com",
    "fishaudio": "https://api.fish.audio",
    "inworld": "https://api.inworld.ai",
    "rev-ai": "https://api.rev.ai",
    "speechmatics": "https://asr.api.speechmatics.com/v2",
    "cliproxyapi": "http://localhost:8317/v1",
    "9router": "http://localhost:20130/v1",
    "maritalk": "https://chat.maritaca.ai/api",
    "piapi": "https://api.piapi.ai",
    "getgoapi": "https://api.getgoapi.com/v1",
    "laozhang": "https://api.laozhang.ai/v1",
    "thebai": "https://api.theb.ai/v1",
    "poe": "https://api.poe.com",
    "kimi-coding-apikey": "https://api.kimi.com/coding/v1",
    "360ai": "https://api.360.cn/v1",
    "gitlab": "https://gitlab.com/api/v4/ai",
    "black-forest-labs": "https://api.bfl.ai",
    "segmind": "https://api.segmind.com/v1",
    "cursor-api": "https://api.cursor.com/v1",
    "datarobot": "https://app.datarobot.com/api/v2",
    "oci": "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
    "empower": "https://api.empower.dev/v1",
    "fenayai": "https://api.fenayai.com/v1",
    "topaz": "https://api.topazlabs.com",
    "nimble-search": "https://api.webit.live",
    "xquik-search": "https://api.xquik.com",
    "tinyfish": "https://api.tinyfish.ai",
    "aws-polly": "https://polly.us-east-1.amazonaws.com",
    "jules": "https://jules.google",
    "devin": "https://api.devin.ai",
    "codex-cloud": "https://chatgpt.com/backend-api/codex",
    "muse-code": "https://llama-stack.readthedocs.io",
    "ollama-search": "https://ollama.com/api",
}

WEBSITE_FALLBACKS = {
    "ghe-copilot": "https://docs.github.com/en/copilot",
    "grok-cli": "https://x.ai",
    "qoder": "https://qoder.com",
    "kiro": "https://kiro.dev",
    "claude": "https://docs.anthropic.com/en/docs/claude-code",
    "antigravity": "https://antigravity.google",
    "codex": "https://developers.openai.com/codex",
    "cursor": "https://cursor.com",
    "kilocode": "https://kilocode.ai",
    "cline": "https://cline.bot",
    "clinepass": "https://cline.bot/cline-pass",
}

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

# Existing IaaS names that live in OmniRoute's frontier-labs file.
IAAS_IDS = {
    "groq",
    "cerebras",
    "sambanova",
    "together",
    "fireworks",
    "deepinfra",
    "nebius",
    "siliconflow",
    "inception",
    "liquid",
    "friendliai",
    "huggingface",
    "nvidia",
    "hyperbolic",
    "kluster",
    "anyscale",
    "replicate",
    "inference-net",
    "arcee-ai",
}

AGGREGATOR_IDS = {
    "aimlapi",
    "coze",
    "eden-ai",
    "lemondata",
    "302ai",
    "frogbot",
    "poe",
    "piapi",
    "getgoapi",
    "thebai",
    "naga-ac",
    "naga-ai",
    "chatanywhere",
    "electronhub",
    "anyapi",
}

IMAGE_VIDEO_IDS = {
    "runwayml",
    "kie",
    "haiper",
    "leonardo",
    "ideogram",
    "magnific",
    "fal-ai",
    "stability-ai",
    "black-forest-labs",
    "recraft",
    "topaz",
    "segmind",
    "deepai",
    "agnes",
    "veoaifree-web",
    "suno",
    "udio",
}

EMBEDDING_IDS = {"voyage-ai", "jina-ai", "nomic", "mixedbread"}


# ---------------------------------------------------------------------------
# Minimal TypeScript object-literal parser
# ---------------------------------------------------------------------------

def _skip_ws_and_comments(src: str, i: int) -> int:
    n = len(src)
    while i < n:
        if src[i] in " \t\r\n":
            i += 1
            continue
        if src.startswith("//", i):
            nl = src.find("\n", i)
            i = n if nl < 0 else nl + 1
            continue
        if src.startswith("/*", i):
            end = src.find("*/", i + 2)
            i = n if end < 0 else end + 2
            continue
        break
    return i


def _parse_string(src: str, i: int) -> tuple[str, int]:
    quote = src[i]
    i += 1
    out: list[str] = []
    n = len(src)
    while i < n:
        ch = src[i]
        if ch == "\\":
            if i + 1 < n:
                nxt = src[i + 1]
                escapes = {"n": "\n", "t": "\t", "r": "\r", "\\": "\\", quote: quote}
                out.append(escapes.get(nxt, nxt))
                i += 2
                continue
        if ch == quote:
            return "".join(out), i + 1
        out.append(ch)
        i += 1
    return "".join(out), i


def _parse_value(src: str, i: int):
    i = _skip_ws_and_comments(src, i)
    if i >= len(src):
        return None, i
    ch = src[i]
    if ch in ('"', "'", "`"):
        s, i = _parse_string(src, i)
        i = _skip_ws_and_comments(src, i)
        while i < len(src) and src[i] == "+":
            i = _skip_ws_and_comments(src, i + 1)
            if i < len(src) and src[i] in ('"', "'", "`"):
                more, i = _parse_string(src, i)
                s += more
                i = _skip_ws_and_comments(src, i)
            else:
                break
        return s, i
    if src.startswith("true", i) and not src[i + 4 : i + 5].isalnum():
        return True, i + 4
    if src.startswith("false", i) and not src[i + 5 : i + 6].isalnum():
        return False, i + 5
    if src.startswith("null", i) and not src[i + 4 : i + 5].isalnum():
        return None, i + 4
    if ch == "[":
        return _parse_array(src, i)
    if ch == "{":
        return _parse_object(src, i)
    # identifier / number / call expression — capture raw token until , } ]
    start = i
    depth = 0
    while i < len(src):
        c = src[i]
        if c in ('"', "'", "`"):
            _, i = _parse_string(src, i)
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif c in "[{":
            depth += 1
        elif c in "]}":
            if depth == 0:
                break
            depth -= 1
        elif c == "," and depth == 0:
            break
        elif c == "}" and depth == 0:
            break
        i += 1
    raw = src[start:i].strip()
    if raw in {"undefined", "null", "void 0"}:
        return None, i
    if re.fullmatch(r"-?\d+(\.\d+)?", raw or ""):
        return float(raw) if "." in raw else int(raw), i
    return raw, i


def _parse_array(src: str, i: int) -> tuple[list, int]:
    assert src[i] == "["
    i += 1
    items: list = []
    while True:
        i = _skip_ws_and_comments(src, i)
        if i >= len(src):
            break
        if src[i] == "]":
            return items, i + 1
        if src[i] == ",":
            i += 1
            continue
        if src.startswith("...", i):
            i += 3
            val, i = _parse_value(src, i)
            items.append(("...", val))
            continue
        val, i = _parse_value(src, i)
        items.append(val)
    return items, i


def _parse_object(src: str, i: int) -> tuple[dict, int]:
    assert src[i] == "{"
    i += 1
    obj: dict = {}
    while True:
        i = _skip_ws_and_comments(src, i)
        if i >= len(src):
            break
        if src[i] == "}":
            return obj, i + 1
        if src[i] == ",":
            i += 1
            continue
        if src[i] in ('"', "'", "`"):
            key, i = _parse_string(src, i)
        else:
            m = re.match(r"[A-Za-z_$][\w$-]*", src[i:])
            if not m:
                i += 1
                continue
            key = m.group(0)
            i += m.end()
        i = _skip_ws_and_comments(src, i)
        if i < len(src) and src[i] == ":":
            i += 1
            val, i = _parse_value(src, i)
            obj[key] = val
        else:
            # shorthand or unexpected
            continue
    return obj, i


def parse_exported_object(src: str, export_name: str | None = None) -> dict:
    """Parse `export const NAME = { ... }` (optionally Object.freeze)."""
    if export_name:
        pat = rf"export\s+const\s+{re.escape(export_name)}\s*(?::[^=]+)?=\s*(?:Object\.freeze\()?"
        m = re.search(pat, src)
        if not m:
            return {}
        i = _skip_ws_and_comments(src, m.end())
        if i < len(src) and src[i] == "{":
            obj, _ = _parse_object(src, i)
            return obj
        return {}
    # First top-level exported object
    for m in re.finditer(r"export\s+const\s+\w+\s*(?::[^=]+)?=\s*(?:Object\.freeze\()?", src):
        i = _skip_ws_and_comments(src, m.end())
        if i < len(src) and src[i] == "{":
            obj, _ = _parse_object(src, i)
            return obj
    return {}


def flatten_catalog_entries(obj: dict) -> list[dict]:
    entries = []
    for key, val in obj.items():
        if isinstance(val, dict) and (val.get("id") or val.get("name")):
            entry = dict(val)
            entry.setdefault("id", key.strip('"'))
            entries.append(entry)
    return entries


# ---------------------------------------------------------------------------
# OmniRoute loaders
# ---------------------------------------------------------------------------

def load_catalog(omni: Path) -> list[dict]:
    catalog_dir = omni / "src" / "shared" / "constants" / "providers"
    files = [
        ("noauth.ts", "No-auth", "no-auth"),
        ("oauth.ts", "OAuth", "oauth"),
        ("web-cookie.ts", "Web Cookie", "web-cookie"),
        ("local.ts", "Local", "local"),
        ("search.ts", "Search", "search"),
        ("audio.ts", "Audio", "audio"),
        ("cloud-agent.ts", "Cloud Agent", "cloud-agent"),
        ("upstream-proxy.ts", "Gateway", "api-key"),
        ("apikey/frontier-labs.ts", None, "api-key"),
        ("apikey/inference-hosts.ts", "IaaS", "api-key"),
        ("apikey/gateways.ts", "Gateway", "api-key"),
        ("apikey/enterprise-cloud.ts", "Sovereign / Cloud", "api-key"),
        ("apikey/regional.ts", "Frontier", "api-key"),
        ("apikey/specialty-media.ts", None, "api-key"),
    ]
    providers: list[dict] = []
    seen: set[str] = set()
    for rel, default_cat, auth_type in files:
        path = catalog_dir / rel
        if not path.exists():
            continue
        obj = parse_exported_object(path.read_text(encoding="utf-8"))
        for entry in flatten_catalog_entries(obj):
            pid = str(entry.get("id") or "")
            if not pid or pid in seen or entry.get("systemOnly"):
                continue
            seen.add(pid)
            cat = assign_category(pid, entry, default_cat, rel)
            entry["_category"] = cat
            entry["_auth_type"] = auth_type
            entry["_source_file"] = rel
            providers.append(entry)
    return providers


def assign_category(pid: str, entry: dict, default_cat: str | None, rel: str) -> str:
    if pid in IMAGE_VIDEO_IDS:
        return "Image / Video"
    if pid in EMBEDDING_IDS:
        return "Embeddings"
    if pid in AGGREGATOR_IDS:
        return "Aggregator"
    if pid in IAAS_IDS or rel.endswith("inference-hosts.ts"):
        return "IaaS"
    kinds = entry.get("serviceKinds") or []
    if isinstance(kinds, list):
        kinds_s = {str(k) for k in kinds if not isinstance(k, tuple)}
        if kinds_s & {"image", "video"} and not (kinds_s & {"llm"}):
            return "Image / Video"
        if kinds_s & {"webSearch", "webFetch"} and "llm" not in kinds_s:
            return "Search"
    if default_cat:
        return default_cat
    if "frontier" in rel:
        return "Frontier"
    if "specialty" in rel:
        return "Specialized"
    return "Specialized"


def load_shared_model_tables(omni: Path) -> dict[str, list[str]]:
    """Parse CHAT_OPENAI_COMPAT_MODELS and named model arrays."""
    tables: dict[str, list[str]] = {}
    shared = omni / "open-sse" / "config" / "providers" / "shared.ts"
    if shared.exists():
        text = shared.read_text(encoding="utf-8")
        obj = parse_exported_object(text, "CHAT_OPENAI_COMPAT_MODELS")
        for key, val in obj.items():
            tables[key] = extract_model_ids(val)
    # Named frozen arrays used via spreads
    for path in (omni / "open-sse" / "config").rglob("*.ts"):
        text = path.read_text(encoding="utf-8")
        for m in re.finditer(r"export\s+const\s+(\w+_MODELS|\w+_SHARED_MODELS)\s*=", text):
            name = m.group(1)
            i = _skip_ws_and_comments(text, m.end())
            if text.startswith("Object.freeze(", i):
                i = _skip_ws_and_comments(text, i + len("Object.freeze("))
            if i < len(text) and text[i] == "[":
                arr, _ = _parse_array(text, i)
                tables[name] = extract_model_ids(arr)
    return tables


def extract_model_ids(value) -> list[str]:
    ids: list[str] = []

    def walk(node) -> None:
        if node is None:
            return
        if isinstance(node, str):
            if node and not node.startswith("...") and " " not in node[:2]:
                # skip raw identifiers like buildModels(...)
                if node.startswith("buildModels"):
                    return
                if re.match(r"^[\w./:+-]+$", node) and not node[0].isdigit() or "/" in node or "-" in node:
                    if node not in {"true", "false", "null"} and not node.endswith("("):
                        # only accept model-like strings when they came from arrays of strings
                        pass
            return
        if isinstance(node, tuple) and node and node[0] == "...":
            walk(node[1])
            return
        if isinstance(node, dict):
            mid = node.get("id")
            if isinstance(mid, str) and mid:
                ids.append(mid)
            return
        if isinstance(node, list):
            for item in node:
                if isinstance(item, str) and item and not item.startswith("buildModels"):
                    if re.match(r"^[\w./:+@-]+$", item):
                        ids.append(item)
                else:
                    walk(item)

    walk(value)
    # de-dupe preserve order
    out: list[str] = []
    seen: set[str] = set()
    for mid in ids:
        if mid not in seen:
            seen.add(mid)
            out.append(mid)
    return out


def _local_model_tables(text: str) -> dict[str, list[str]]:
    tables: dict[str, list[str]] = {}
    for m in re.finditer(r"export\s+const\s+(\w+)\s*(?::[^=]+)?=\s*", text):
        name = m.group(1)
        i = _skip_ws_and_comments(text, m.end())
        if text.startswith("Object.freeze(", i):
            i = _skip_ws_and_comments(text, i + len("Object.freeze("))
        if i < len(text) and text[i] == "[":
            arr, _ = _parse_array(text, i)
            ids = extract_model_ids(arr)
            if ids:
                tables[name] = ids
    return tables


def _skip_call_wrapper(text: str, i: int) -> int:
    """Handle `buildOpenAiCompatibleRegistryEntry({...})` wrappers."""
    i = _skip_ws_and_comments(text, i)
    m = re.match(r"[A-Za-z_$][\w$]*\s*\(", text[i:])
    if not m:
        return i
    i = _skip_ws_and_comments(text, i + m.end())
    return i


def load_registry(omni: Path, shared_tables: dict[str, list[str]]) -> dict[str, dict]:
    registry: dict[str, dict] = {}
    root = omni / "open-sse" / "config" / "providers" / "registry"
    if not root.exists():
        return registry
    for path in root.rglob("index.ts"):
        text = path.read_text(encoding="utf-8")
        local_tables = {**shared_tables, **_local_model_tables(text)}
        for m in re.finditer(r"export\s+const\s+\w+\s*(?::\s*RegistryEntry)?\s*=\s*", text):
            i = _skip_call_wrapper(text, m.end())
            if i >= len(text) or text[i] != "{":
                continue
            obj, _ = _parse_object(text, i)
            pid = obj.get("id")
            if not isinstance(pid, str) or not pid:
                continue
            models = resolve_registry_models(obj.get("models"), local_tables)
            base = normalize_base_url(obj.get("baseUrl") or "")
            if not base and isinstance(obj.get("baseUrls"), list) and obj["baseUrls"]:
                first = obj["baseUrls"][0]
                if isinstance(first, str):
                    base = normalize_base_url(first)
            if not base and isinstance(obj.get("modelsUrl"), str):
                base = normalize_base_url(obj["modelsUrl"].replace("/models", ""))
            if not base:
                base = KNOWN_BASE_URLS.get(pid, "")
            fmt = obj.get("format") if isinstance(obj.get("format"), str) else ""
            if not fmt and base:
                fmt = "openai"
            registry[pid] = {
                "id": pid,
                "alias": obj.get("alias") if isinstance(obj.get("alias"), str) else "",
                "format": fmt,
                "base_url": base,
                "models": models,
                "auth_type": obj.get("authType") if isinstance(obj.get("authType"), str) else "",
                "models_url": obj.get("modelsUrl") if isinstance(obj.get("modelsUrl"), str) else "",
            }
    return registry


def resolve_registry_models(models_val, shared_tables: dict[str, list[str]]) -> list[str]:
    if models_val is None:
        return []
    if isinstance(models_val, str):
        # CHAT_OPENAI_COMPAT_MODELS.foo or CHAT_OPENAI_COMPAT_MODELS["foo"] or GLM_SHARED_MODELS
        m = re.search(r'CHAT_OPENAI_COMPAT_MODELS(?:\[["\']([\w.-]+)["\']\]|\.([\w]+))', models_val)
        if m:
            key = m.group(1) or m.group(2)
            return list(shared_tables.get(key, []))
        ident = models_val.split(".")[-1].strip()
        if ident in shared_tables:
            return list(shared_tables[ident])
        return []
    ids = extract_model_ids(models_val)
    # resolve spreads of named constants mixed into arrays
    extra: list[str] = []
    if isinstance(models_val, list):
        for item in models_val:
            if isinstance(item, tuple) and item[0] == "...":
                extra.extend(resolve_registry_models(item[1], shared_tables))
            elif isinstance(item, str) and item in shared_tables:
                extra.extend(shared_tables[item])
    return dedupe(extra + ids)


def normalize_base_url(url: str) -> str:
    if not isinstance(url, str):
        return ""
    url = url.strip()
    if not url.startswith("http"):
        return ""
    for suffix in (
        "/chat/completions",
        "/messages",
        "/completions",
        "/responses",
    ):
        if url.endswith(suffix):
            url = url[: -len(suffix)]
    return url.rstrip("/")


def dedupe(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def is_real_url(url: str | None) -> bool:
    if not url:
        return False
    return url.strip().lower() not in PLACEHOLDER_URLS and url.strip().lower().startswith("http")


ENV_OVERRIDES = {
    "9router": None,
    "360ai": "AI360_API_KEY",
    "openference-api": "OPENFERENCE_API_KEY",
    "zylo-api": "ZYLO_API_KEY",
    "cursor-api": "CURSOR_API_KEY",
    "kimi-coding-apikey": "KIMI_CODING_API_KEY",
    "aimlapi": "AIMLAPI_KEY",
    "302-ai": "AI302_API_KEY",
    "searchapi-search": "SEARCHAPI_KEY",
    "cliproxyapi": "CLIPROXYAPI_KEY",
    "monsterapi": "MONSTERAPI_KEY",
    "anyapi": "ANYAPI_KEY",
    "api-airforce": "AIRFORCE_API_KEY",
    "piapi": "PIAPI_KEY",
    "getgoapi": "GETGOAPI_KEY",
    "freeaiapikey": "FREEAI_API_KEY",
}


def env_for_slug(slug: str, auth_type: str, existing: str | None = None) -> str | None:
    if slug in ENV_OVERRIDES:
        return ENV_OVERRIDES[slug]
    if existing:
        return existing
    if auth_type in {"no-auth", "web-cookie", "local", "oauth"}:
        return None
    ident = re.sub(r"[^A-Z0-9]+", "_", slug.upper()).strip("_")
    if not ident:
        return None
    if ident[0].isdigit():
        ident = "AI" + ident
    ident = ident.replace("APIKEY", "API_KEY")
    ident = re.sub(r"_+", "_", ident).strip("_")
    if ident.endswith("_API_KEY"):
        return ident
    if ident.endswith("API"):
        return f"{ident}_KEY"
    return f"{ident}_API_KEY"


def is_ugly_env(env: str | None) -> bool:
    if not env:
        return False
    return bool(
        re.search(r"API_API_KEY", env)
        or re.search(r"APIKEY_API_KEY", env)
        or re.match(r"^P\d", env)
        or env[0].isdigit()
    )


FALLBACK_NOTES = {
    "OAuth": "OAuth / IDE subscription. Sign in through the official CLI or app; no separate API key in most cases.",
    "Audio": "Speech-to-text or text-to-speech API. See official docs for keys and model IDs.",
    "Gateway": "OpenAI-compatible multi-provider gateway or local proxy.",
    "Frontier": "First-party model lab API.",
    "IaaS": "Hosted inference API for open-weight and partner models.",
    "Sovereign / Cloud": "Enterprise or regional cloud inference.",
    "Aggregator": "Multi-vendor model marketplace under one API key.",
    "Image / Video": "Image or video generation API.",
    "Search": "Web search, fetch, or crawl API.",
    "Specialized": "Specialized API. See official docs for setup.",
    "No-auth": "Public or anonymous endpoint; rate limits usually apply.",
    "Web Cookie": "Unofficial web-session adapter. Prefer official APIs in production.",
    "Local": "Runs on your machine. OpenAI-compatible local server.",
    "Cloud Agent": "Hosted coding agent. Task-based rather than a classic chat API.",
    "Embeddings": "Embeddings or rerank API.",
}


def notes_from(entry: dict, registry: dict | None) -> str:
    parts: list[str] = []
    for key in ("freeNote", "authHint", "apiHint"):
        val = entry.get(key)
        if isinstance(val, str) and val.strip():
            parts.append(val.strip())
    notice = entry.get("notice")
    if isinstance(notice, dict):
        text = notice.get("text")
        if isinstance(text, str) and text.strip():
            parts.append(text.strip())
    note = "; ".join(parts)
    note = re.sub(r"\s+", " ", note).strip()
    if len(note) > 420:
        note = note[:417].rstrip() + "…"
    return note


def openai_compatible(entry: dict, registry: dict | None) -> bool:
    if registry:
        fmt = (registry.get("format") or "").lower()
        if fmt in {"openai", "openai-completions", "openai-responses"}:
            return True
        if fmt in {"claude", "anthropic", "gemini"}:
            return False
        if is_real_url(registry.get("base_url")) and "/v1" in registry["base_url"]:
            return True
    local = entry.get("localDefault")
    if isinstance(local, str) and "/v1" in local:
        return True
    return False


def slugify_name(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def build_existing_index(existing: list[dict]) -> dict[str, dict]:
    index: dict[str, dict] = {}
    for p in existing:
        index[p["slug"].lower()] = p
        for alias in p.get("aliases") or []:
            index[str(alias).lower()] = p
        index[p["name"].lower()] = p
        index[slugify_name(p["name"])] = p
    return index


def find_existing(omni_id: str, entry: dict, by_slug: dict[str, dict], by_name: dict[str, dict]) -> dict | None:
    """Match only on canonical slug, explicit map, or exact display name.

    Alias matching is too lossy (Claude Code != Anthropic, OpenCode Free != Zen).
    """
    mapped = SLUG_MAP.get(omni_id)
    if mapped and mapped in by_slug:
        return by_slug[mapped]
    if omni_id in by_slug:
        return by_slug[omni_id]
    name = str(entry.get("name") or "").strip().lower()
    if name and name in by_name:
        return by_name[name]
    return None


def extra_hand_curated() -> list[dict]:
    return [
        {
            "name": "OmniRoute",
            "slug": "omniroute",
            "aliases": ["omni-route", "cheaper-inference-gateway"],
            "category": "Gateway",
            "website": "https://github.com/diegosouzapw/OmniRoute",
            "api_base_url": "http://localhost:3000/v1",
            "popular_models": ["kimi-k2.7-code", "claude-sonnet-4", "gpt-5.5", "glm-5.3"],
            "env_variable": "OMNIROUTE_API_KEY",
            "openai_compatible": True,
            "notes": "Open-source MIT AI gateway (352 providers, 1200+ models). Self-hosted OpenAI-compatible endpoint; quota-aware auto-fallback.",
        },
        {
            "name": "Bifrost",
            "slug": "bifrost",
            "aliases": ["maximhq-bifrost"],
            "category": "Gateway",
            "website": "https://github.com/maximhq/bifrost",
            "api_base_url": "http://localhost:8080/v1",
            "popular_models": ["1000+ models"],
            "env_variable": None,
            "openai_compatible": True,
            "notes": "Open-source Go gateway; adaptive load balancing, guardrails, virtual keys.",
        },
        {
            "name": "Dasha Compute",
            "slug": "dasha-compute",
            "aliases": ["dasha", "getdasha"],
            "category": "Sovereign / Cloud",
            "website": "https://www.getdasha.com/compute",
            "api_base_url": "Open alpha",
            "popular_models": ["qwen3-8b", "gemma3-12b", "gemma3-27b"],
            "env_variable": None,
            "openai_compatible": True,
            "notes": "OpenAI-compatible API on a network of Apple-silicon Macs; providers paid per job in USDC.",
        },
    ]


def _clean_website(url: str) -> str:
    if not isinstance(url, str) or not url.startswith("http"):
        return url or ""
    return url.split("?", 1)[0].rstrip("/") or url


def merge(existing: list[dict], catalog: list[dict], registry: dict[str, dict]) -> tuple[list[dict], dict[str, list[str]], dict]:
    static: dict[str, list[str]] = {}
    stats = {"kept": 0, "updated_urls": 0, "added": 0, "models_merged": 0}

    providers = [dict(p) for p in existing]
    by_slug = {p["slug"]: p for p in providers}
    by_name = {p["name"].strip().lower(): p for p in providers}
    next_id = max(p["id"] for p in providers) + 1

    stats["kept"] = len(providers)

    for entry in catalog:
        pid = str(entry["id"])
        reg = registry.get(pid)
        match = find_existing(pid, entry, by_slug, by_name)
        models = list((reg or {}).get("models") or [])
        popular_from_omni = models[:6]

        if match:
            slug = match["slug"]
            target = by_slug[slug]
            new_url = ""
            if reg and is_real_url(reg.get("base_url")):
                new_url = reg["base_url"]
            elif isinstance(entry.get("localDefault"), str) and is_real_url(entry["localDefault"]):
                new_url = entry["localDefault"].rstrip("/")
            elif pid in KNOWN_BASE_URLS:
                new_url = KNOWN_BASE_URLS[pid]
            if new_url and not is_real_url(target.get("api_base_url")):
                target["api_base_url"] = new_url
                stats["updated_urls"] += 1
                if "/v1" in new_url:
                    target["openai_compatible"] = True
                if not target.get("env_variable") and entry.get("_auth_type") == "api-key":
                    target["env_variable"] = env_for_slug(slug, "api-key")
            aliases = list(target.get("aliases") or [])
            taken = {s.lower() for s in by_slug}
            for extra in (entry.get("alias"),):
                if (
                    isinstance(extra, str)
                    and extra
                    and extra.lower() not in {"undefined", "null"}
                    and extra.lower() not in {a.lower() for a in aliases}
                    and extra != slug
                    and extra.lower() not in taken
                ):
                    aliases.append(extra)
            target["aliases"] = [a for a in aliases if a and str(a).lower() not in {"undefined", "null"}]
            if models:
                static[slug] = models
                stats["models_merged"] += 1
                if not target.get("popular_models"):
                    target["popular_models"] = popular_from_omni
            continue

        # New provider
        slug = pid
        if slug in by_slug:
            slug = f"{pid}-omni"
        website = _clean_website(entry.get("website") if isinstance(entry.get("website"), str) else "")
        if not website or "diegosouzapw/OmniRoute" in website:
            website = WEBSITE_FALLBACKS.get(pid) or website
        if not website:
            website = "https://github.com/diegosouzapw/OmniRoute"
        api_base = ""
        if reg and is_real_url(reg.get("base_url")):
            api_base = reg["base_url"]
        elif pid in KNOWN_BASE_URLS:
            api_base = KNOWN_BASE_URLS[pid]
        elif isinstance(entry.get("localDefault"), str) and is_real_url(entry["localDefault"]):
            api_base = entry["localDefault"].rstrip("/")
        elif isinstance(entry.get("defaultPort"), (int, float)):
            api_base = f"http://localhost:{int(entry['defaultPort'])}/v1"
        elif entry.get("_auth_type") == "oauth":
            api_base = "OAuth (provider-specific)"
        elif entry.get("_auth_type") == "web-cookie":
            api_base = "Web cookie / browser session"
        elif entry.get("_auth_type") == "no-auth":
            api_base = "No-auth public endpoint"
        else:
            api_base = "See official docs"

        aliases = []
        extra = entry.get("alias")
        if (
            isinstance(extra, str)
            and extra
            and extra != slug
            and extra.lower() not in {"undefined", "null"}
        ):
            aliases.append(extra)

        new = {
            "id": next_id,
            "name": str(entry.get("name") or slug),
            "slug": slug,
            "aliases": aliases,
            "category": entry["_category"],
            "website": website,
            "api_base_url": api_base,
            "popular_models": popular_from_omni,
            "env_variable": env_for_slug(slug, entry["_auth_type"]),
            "openai_compatible": openai_compatible(entry, reg),
            "notes": notes_from(entry, reg)
            or FALLBACK_NOTES.get(entry["_category"])
            or f"{entry['_category']} provider from the OmniRoute catalog.",
        }
        providers.append(new)
        by_slug[slug] = new
        by_name[new["name"].strip().lower()] = new
        if models:
            static[slug] = models
        next_id += 1
        stats["added"] += 1

    # Hand-curated extras (Bifrost, Dasha, OmniRoute) if still missing
    for extra in extra_hand_curated():
        if extra["slug"] in by_slug:
            continue
        extra_row = dict(extra)
        extra_row["id"] = next_id
        providers.append(extra_row)
        by_slug[extra["slug"]] = extra_row
        next_id += 1
        stats["added"] += 1

    providers.sort(key=lambda p: p["id"])
    return providers, static, stats


# ---------------------------------------------------------------------------
# Data cleanup (collisions, env names, leftover TS values)
# ---------------------------------------------------------------------------

SLUG_RENAMES = {
    "claude": "claude-code",
    "glm": "glm-coding",
}

# Fold duplicate listings of the same product into one row.
MERGE_SLUGS = {
    "gitlab": "gitlab-duo",
    "glmt": "glm-coding",
    "sparkdesk": "iflytek",
    "volcengine": "doubao",
    "naga-ai": "naga-ac",
}

CATEGORY_FIXES = {
    "discountedtokens": "Gateway",
    "cursor-api": "Gateway",
    "pollinations": "IaaS",
    "muse-code": "Local",
}

URL_FIXES = {
    "muse-code": "http://localhost:8321/v1",
    "ghe-copilot": "GitHub Enterprise host (device-flow OAuth)",
}

# Aliases that collide with another provider's slug or a more common meaning.
REMOVE_ALIASES = {
    "github-copilot": {"github"},
    "github-models": {"github"},
    "copilot-web": {"copilot"},
    "opencode-zen": {"opencode"},
    "piapi": {"pi"},
    "poe-web": {"poe"},
    "claude-code": {"claude"},
}

NO_KEY_CATEGORIES = {"Local", "Web Cookie", "No-auth"}


_PLACEHOLDER_MODEL = re.compile(
    r"(?i)^(any|all|supported)[- ]"
    r"|major-provider"
    r"|upstream-provider"
    r"|gguf-model"
    r"|compatible-checkpoint"
    r"|custom-deployed"
    r"|supported-local"
)


def _real_models(models: list | None) -> list[str]:
    out: list[str] = []
    for item in models or []:
        text = str(item).strip()
        if not text:
            continue
        low = text.lower()
        if "+" in text and any(word in low for word in ("model", "provider", "routed")):
            continue
        if low in {"custom", "n/a", "various"}:
            continue
        if _PLACEHOLDER_MODEL.search(text):
            continue
        if text not in out:
            out.append(text)
    return out


def _clean_notes(note: str | None) -> str:
    if not note:
        return ""
    parts = [p.strip() for p in re.split(r";\s*", str(note)) if p.strip()]
    seen: set[str] = set()
    out: list[str] = []
    for part in parts:
        key = part.lower()
        if key not in seen:
            seen.add(key)
            out.append(part)
    return "; ".join(out)


def _merge_provider(dst: dict, src: dict, static: dict[str, list[str]]) -> None:
    dst["aliases"] = dedupe(
        list(dst.get("aliases") or []) + list(src.get("aliases") or []) + [src["slug"]]
    )
    dst["popular_models"] = dedupe(
        list(dst.get("popular_models") or []) + list(src.get("popular_models") or [])
    )[:8]
    src_notes = (src.get("notes") or "").strip()
    dst_notes = (dst.get("notes") or "").strip()
    if src_notes and src_notes not in dst_notes and len(src_notes) > len(dst_notes):
        dst["notes"] = src_notes if not dst_notes else f"{dst_notes}; {src_notes}"
    if src["slug"] in static:
        static[dst["slug"]] = dedupe(list(static.get(dst["slug"], [])) + list(static.pop(src["slug"])))


def cleanup_providers(providers: list[dict], static: dict[str, list[str]] | None = None) -> list[dict]:
    static = static if static is not None else {}
    by_slug = {p["slug"]: p for p in providers}

    for old, new in SLUG_RENAMES.items():
        if old in by_slug and new not in by_slug:
            row = by_slug.pop(old)
            row["slug"] = new
            by_slug[new] = row
            if old in static:
                static[new] = dedupe(list(static.get(new, [])) + list(static.pop(old)))

    for src_slug, dst_slug in MERGE_SLUGS.items():
        if src_slug in by_slug and dst_slug in by_slug and src_slug != dst_slug:
            _merge_provider(by_slug[dst_slug], by_slug.pop(src_slug), static)

    taken_slugs = {p["slug"].lower() for p in by_slug.values()}
    for row in by_slug.values():
        slug = row["slug"]
        if slug in CATEGORY_FIXES:
            row["category"] = CATEGORY_FIXES[slug]
        if slug in URL_FIXES:
            row["api_base_url"] = URL_FIXES[slug]
        if slug in ENV_OVERRIDES:
            row["env_variable"] = ENV_OVERRIDES[slug]
        elif is_ugly_env(row.get("env_variable")):
            row["env_variable"] = env_for_slug(slug, "api-key")
        if row["category"] in NO_KEY_CATEGORIES and slug not in ENV_OVERRIDES:
            row["env_variable"] = None

        aliases = []
        banned = {a.lower() for a in REMOVE_ALIASES.get(slug, set())} | {"undefined", "null", "none"}
        for alias in row.get("aliases") or []:
            if not alias or not isinstance(alias, str):
                continue
            a = alias.strip()
            if not a or a.lower() in banned or a.lower() == slug:
                continue
            if a.lower() in taken_slugs:
                continue
            if a.lower() not in {x.lower() for x in aliases}:
                aliases.append(a)
        row["aliases"] = aliases

        popular = _real_models(row.get("popular_models"))
        if slug in static:
            static[slug] = _real_models(static[slug])
        if not popular and slug in static:
            popular = list(static[slug][:6])
        row["popular_models"] = popular

        row["notes"] = _clean_notes(row.get("notes")) or FALLBACK_NOTES.get(row["category"], "")

        url = row.get("api_base_url") or ""
        if row.get("openai_compatible") and not is_real_url(url):
            row["openai_compatible"] = False

    # One owner per alias; prefer an exact slug match, otherwise the oldest id.
    alias_owners: dict[str, list[dict]] = defaultdict(list)
    for row in by_slug.values():
        for alias in row.get("aliases") or []:
            alias_owners[alias.lower()].append(row)
    for alias, rows in alias_owners.items():
        if len(rows) < 2:
            continue
        keep = next((r for r in rows if r["slug"].lower() == alias), min(rows, key=lambda r: r["id"]))
        for row in rows:
            if row is keep:
                continue
            row["aliases"] = [a for a in row["aliases"] if a.lower() != alias]

    cleaned = sorted(by_slug.values(), key=lambda p: p["id"])
    for i, row in enumerate(cleaned, 1):
        row["id"] = i
    return cleaned


# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------

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

Includes the [OmniRoute](https://github.com/diegosouzapw/OmniRoute) catalog plus extra listings. Always confirm endpoints against official docs. To add or correct a provider, see [docs/contributing.md](docs/contributing.md). Updated {now}.

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

One key for many models: [OpenRouter](https://openrouter.ai), [OmniRoute](https://github.com/diegosouzapw/OmniRoute), [Portkey](https://portkey.ai).

## Categories

{chr(10).join(cat_rows)}
{cookie_note}
{chr(10).join(sections)}
## Pick a provider

| Goal | Start here |
|------|------------|
| Best reasoning | OpenAI, Anthropic, Gemini |
| Low cost / open models | Groq, DeepInfra, Together, SiliconFlow |
| One API, many models | OpenRouter, OmniRoute, Portkey |
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


def save_static(existing: dict[str, list[str]], incoming: dict[str, list[str]]) -> int:
    merged = dict(existing)
    added = 0
    for slug, models in incoming.items():
        prev = merged.get(slug, [])
        combined = dedupe(list(prev) + list(models))
        if combined != prev:
            added += 1
        merged[slug] = combined
    STATIC_FILE.write_text(
        json.dumps({"providers": merged}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return added


def write_catalog(providers: list[dict], static: dict[str, list[str]] | None = None) -> None:
    static = dict(static or load_static())
    providers = cleanup_providers(providers, static)
    PROVIDERS_FILE.write_text(
        json.dumps(providers, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    STATIC_FILE.write_text(
        json.dumps({"providers": static}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    model_count = 0
    for row in providers:
        ids = static.get(row["slug"]) or row.get("popular_models") or []
        model_count += len(ids)
    README_FILE.write_text(generate_readme(providers, model_count), encoding="utf-8")
    print(f"Wrote {len(providers)} providers → {PROVIDERS_FILE}")
    print(f"Wrote {README_FILE}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import OmniRoute providers into this repo.")
    parser.add_argument("--omniroute", default="/tmp/omniroute", help="Path to OmniRoute checkout")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Clean existing catalog + regenerate README (no OmniRoute clone needed)",
    )
    args = parser.parse_args()

    if args.fix:
        providers = json.loads(PROVIDERS_FILE.read_text(encoding="utf-8"))
        write_catalog(providers, load_static())
        return 0

    omni = Path(args.omniroute)
    if not omni.exists():
        raise SystemExit(f"OmniRoute path not found: {omni}")

    existing = json.loads(PROVIDERS_FILE.read_text(encoding="utf-8"))
    print(f"Existing providers: {len(existing)}")

    catalog = load_catalog(omni)
    print(f"OmniRoute catalog entries: {len(catalog)}")

    shared = load_shared_model_tables(omni)
    print(f"Shared model tables: {len(shared)}")

    registry = load_registry(omni, shared)
    print(f"Registry entries: {len(registry)}")

    providers, static_in, stats = merge(existing, catalog, registry)
    print(
        f"Merge: kept={stats['kept']} added={stats['added']} "
        f"urls_filled={stats['updated_urls']} model_catalogs={stats['models_merged']}"
    )
    prev_static = load_static()
    for slug, models in static_in.items():
        prev_static[slug] = dedupe(list(prev_static.get(slug, [])) + list(models))
    write_catalog(providers, prev_static)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
