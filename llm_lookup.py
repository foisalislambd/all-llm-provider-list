#!/usr/bin/env python3
"""
LLM Provider Lookup — search by provider name or API endpoint.

Usage (Python):
    from llm_lookup import lookup, all_providers, get_models, search_models

    lookup("groq")                          # provider details
    get_models("groq")                      # all supported model IDs
    lookup("groq", include_models=True)     # details + models together
    search_models("llama")                  # find model across providers
    all_providers()                         # full list (114 providers)

Usage (CLI):
    python llm_lookup.py groq
    python llm_lookup.py groq --models
    python llm_lookup.py --search-model llama
    python llm_lookup.py --all
    python scripts/sync_models.py           # refresh live model catalogs
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

_DATA_FILE = Path(__file__).resolve().parent / "data" / "providers.json"
_MODELS_FILE = Path(__file__).resolve().parent / "data" / "models.json"
_PROVIDERS: list[dict[str, Any]] | None = None
_MODELS: dict[str, Any] | None = None


def _load() -> list[dict[str, Any]]:
    global _PROVIDERS
    if _PROVIDERS is None:
        with _DATA_FILE.open(encoding="utf-8") as f:
            _PROVIDERS = json.load(f)
    return _PROVIDERS


def _load_models_db() -> dict[str, Any]:
    global _MODELS
    if _MODELS is None:
        if not _MODELS_FILE.exists():
            _MODELS = {"providers": {}}
        else:
            with _MODELS_FILE.open(encoding="utf-8") as f:
                _MODELS = json.load(f)
    return _MODELS


def _slug_for_provider(provider: dict[str, Any]) -> str:
    return provider["slug"]


def get_models(query: str) -> dict[str, Any]:
    """
    Return the full model catalog for a provider.

    Example:
        get_models("groq")
        get_models("api.groq.com")
    """
    result = lookup(query)
    if isinstance(result, list):
        if len(result) != 1:
            raise ValueError(f"Multiple providers matched {query!r}; be more specific.")
        result = result[0]

    slug = result["slug"]
    db = _load_models_db()
    entry = db.get("providers", {}).get(slug)

    if entry:
        return {
            "provider": result["name"],
            "slug": slug,
            "count": entry["count"],
            "source": entry["source"],
            "models_endpoint": entry.get("models_endpoint"),
            "updated_at": entry.get("updated_at"),
            "models": entry["models"],
        }

    return {
        "provider": result["name"],
        "slug": slug,
        "count": len(result.get("popular_models", [])),
        "source": "popular_models-fallback",
        "models_endpoint": None,
        "updated_at": None,
        "models": result.get("popular_models", []),
    }


def search_models(text: str) -> list[dict[str, Any]]:
    """Find which providers offer models matching the query string."""
    q = text.strip().lower()
    if not q:
        return []

    hits: list[dict[str, Any]] = []
    db = _load_models_db()
    provider_by_slug = {p["slug"]: p for p in _load()}

    for slug, entry in db.get("providers", {}).items():
        matched = [m for m in entry.get("models", []) if q in m.lower()]
        if not matched:
            continue
        provider = provider_by_slug.get(slug, {})
        hits.append({
            "provider": entry.get("provider_name") or provider.get("name", slug),
            "slug": slug,
            "category": entry.get("category") or provider.get("category"),
            "api_base_url": entry.get("api_base_url") or provider.get("api_base_url"),
            "match_count": len(matched),
            "models": matched,
        })

    hits.sort(key=lambda x: (-x["match_count"], x["provider"]))
    return hits


def lookup_with_models(query: str) -> dict[str, Any]:
    """Provider details merged with full model list."""
    provider = lookup(query)
    if isinstance(provider, list):
        return {"providers": [lookup_with_models(p["slug"]) for p in provider]}

    models_info = get_models(provider["slug"])
    merged = dict(provider)
    merged["models_count"] = models_info["count"]
    merged["models_source"] = models_info["source"]
    merged["models"] = models_info["models"]
    merged["models_endpoint"] = models_info["models_endpoint"]
    return merged


def _normalize(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"^https?://", "", text)
    return text.rstrip("/")


def _provider_search_keys(provider: dict[str, Any]) -> set[str]:
    keys: set[str] = set()
    for field in ("name", "slug", "api_base_url"):
        val = provider.get(field)
        if val and isinstance(val, str) and val not in ("Custom endpoint", "Custom webhooks", "Region-dependent", "Self-hosted / enterprise"):
            keys.add(_normalize(val))

    for alias in provider.get("aliases") or []:
        keys.add(_normalize(alias))

    # domain-only key e.g. api.groq.com from full URL
    url = provider.get("api_base_url", "")
    if url.startswith("http"):
        parsed = urlparse(url if "://" in url else f"https://{url}")
        if parsed.netloc:
            keys.add(_normalize(parsed.netloc))

    return keys


def _build_index() -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = {}
    for provider in _load():
        for key in _provider_search_keys(provider):
            index.setdefault(key, []).append(provider)
    return index


_INDEX: dict[str, list[dict[str, Any]]] | None = None


def _get_index() -> dict[str, list[dict[str, Any]]]:
    global _INDEX
    if _INDEX is None:
        _INDEX = _build_index()
    return _INDEX


def lookup(
    query: str | None = None,
    *,
    include_models: bool = False,
) -> dict[str, Any] | list[dict[str, Any]]:
    """
    Look up provider(s) by name, slug, alias, or API endpoint.

    Set include_models=True to attach the full supported model list.

    Returns a single provider dict if one match, a list if multiple,
    or all providers when query is None / empty / "all".
    """
    if include_models and query and str(query).strip().lower() != "all":
        return lookup_with_models(query)
    if query is None or not str(query).strip() or str(query).strip().lower() == "all":
        return all_providers()

    q = _normalize(str(query))
    providers = _load()
    index = _get_index()

    # exact index hit
    if q in index:
        matches = index[q]
        return matches[0] if len(matches) == 1 else matches

    # partial match on name, slug, aliases, endpoint
    partial: list[dict[str, Any]] = []
    seen_ids: set[int] = set()
    for provider in providers:
        pid = provider["id"]
        if pid in seen_ids:
            continue
        haystack = " ".join(_provider_search_keys(provider))
        if q in haystack or any(q in k for k in _provider_search_keys(provider)):
            partial.append(provider)
            seen_ids.add(pid)

    if not partial:
        raise ValueError(f"No provider found for: {query!r}")

    return partial[0] if len(partial) == 1 else partial


def all_providers(
    category: str | None = None,
    openai_compatible: bool | None = None,
) -> list[dict[str, Any]]:
    """Return all providers, optionally filtered."""
    result = list(_load())

    if category:
        cat = category.strip().lower()
        result = [p for p in result if p["category"].lower().startswith(cat) or cat in p["category"].lower()]

    if openai_compatible is not None:
        result = [p for p in result if p["openai_compatible"] is openai_compatible]

    return result


def search(text: str) -> list[dict[str, Any]]:
    """Fuzzy search across name, models, notes, and endpoint."""
    q = text.strip().lower()
    if not q:
        return all_providers()

    hits: list[dict[str, Any]] = []
    for provider in _load():
        blob = json.dumps(provider, ensure_ascii=False).lower()
        if q in blob:
            hits.append(provider)
    return hits


def categories() -> dict[str, int]:
    """Count providers per category."""
    counts: dict[str, int] = {}
    for provider in _load():
        cat = provider["category"]
        counts[cat] = counts.get(cat, 0) + 1
    return counts


def format_provider(provider: dict[str, Any], *, show_all_models: bool = False) -> str:
    """Human-readable single provider summary."""
    lines = [
        f"#{provider['id']} {provider['name']} [{provider['category']}]",
        f"  Website:           {provider['website']}",
        f"  API Base URL:      {provider['api_base_url']}",
        f"  Env Variable:      {provider.get('env_variable') or 'N/A'}",
        f"  OpenAI Compatible: {provider['openai_compatible']}",
        f"  Notes:             {provider['notes']}",
    ]
    if provider.get("aliases"):
        lines.append(f"  Aliases:           {', '.join(provider['aliases'])}")

    if show_all_models or provider.get("models"):
        models = provider.get("models")
        if models is None and provider.get("slug"):
            models = get_models(provider["slug"])["models"]
        if models:
            source = provider.get("models_source") or get_models(provider["slug"])["source"]
            lines.append(f"  Models ({len(models)}, {source}):")
            for model in models:
                lines.append(f"    - {model}")
        else:
            popular = ", ".join(provider.get("popular_models", []))
            lines.append(f"  Popular Models:    {popular}")
    else:
        popular = ", ".join(provider.get("popular_models", []))
        lines.append(f"  Popular Models:    {popular}")

    return "\n".join(lines)


def _print_result(
    result: dict[str, Any] | list[dict[str, Any]],
    as_json: bool,
    *,
    show_all_models: bool = False,
) -> None:
    if as_json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    if isinstance(result, list):
        print(f"Found {len(result)} provider(s):\n")
        for i, provider in enumerate(result, 1):
            print(format_provider(provider, show_all_models=show_all_models))
            if i < len(result):
                print()
    else:
        print(format_provider(result, show_all_models=show_all_models))


def _print_model_search(hits: list[dict[str, Any]], as_json: bool) -> None:
    if as_json:
        print(json.dumps(hits, indent=2, ensure_ascii=False))
        return

    if not hits:
        print("No models matched.")
        return

    print(f"Found {len(hits)} provider(s) with matching models:\n")
    for hit in hits:
        print(f"{hit['provider']} [{hit['category']}] — {hit['match_count']} match(es)")
        print(f"  API: {hit['api_base_url']}")
        for model in hit["models"][:20]:
            print(f"    - {model}")
        if hit["match_count"] > 20:
            print(f"    ... and {hit['match_count'] - 20} more")
        print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Look up LLM API providers by name or endpoint URL.",
    )
    parser.add_argument("query", nargs="?", help="Provider name, slug, alias, or API endpoint")
    parser.add_argument("--all", action="store_true", help="List all providers")
    parser.add_argument("--category", "-c", help="Filter by category (Frontier, IaaS, Gateway, Local, ...)")
    parser.add_argument("--search", "-s", help="Search in all fields")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    parser.add_argument("--count", action="store_true", help="Show category counts")
    parser.add_argument("--models", "-m", action="store_true", help="Show all supported models")
    parser.add_argument("--search-model", help="Search model IDs across all providers")
    args = parser.parse_args(argv)

    try:
        if args.count:
            print(json.dumps(categories(), indent=2))
            return 0

        if args.search_model:
            hits = search_models(args.search_model)
            _print_model_search(hits, args.json)
            return 0 if hits else 1

        if args.search:
            result = search(args.search)
        elif args.all:
            result = all_providers(category=args.category)
            if args.models:
                result = [lookup_with_models(p["slug"]) for p in result]
        elif args.query:
            if args.models:
                result = lookup_with_models(args.query)
            else:
                result = lookup(args.query)
            if args.category:
                if isinstance(result, list):
                    result = [p for p in result if args.category.lower() in p["category"].lower()]
                elif args.category.lower() not in result["category"].lower():
                    result = []
        else:
            result = all_providers(category=args.category)
            if args.models:
                result = [lookup_with_models(p["slug"]) for p in result]

        if isinstance(result, list) and not result:
            print("No providers matched.", file=sys.stderr)
            return 1

        _print_result(result, args.json, show_all_models=args.models)
        return 0

    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
