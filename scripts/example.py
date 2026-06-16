"""Quick examples for llm_lookup.py"""

from llm_lookup import all_providers, get_models, lookup, search_models

# --- Provider details ---
print("=== Groq provider ===")
print(lookup("groq"))

# --- All models for a provider ---
print("\n=== Groq — all supported models ===")
groq_models = get_models("groq")
print(f"Total: {groq_models['count']} models (source: {groq_models['source']})")
for model in groq_models["models"]:
    print(f"  - {model}")

# --- Provider + models in one call ---
print("\n=== OpenRouter with models ===")
openrouter = lookup("openrouter", include_models=True)
print(f"{openrouter['name']}: {openrouter['models_count']} models")

# --- Search model across all providers ---
print("\n=== Who has 'llama-3.3' models? ===")
for hit in search_models("llama-3.3")[:5]:
    print(f"  {hit['provider']}: {hit['match_count']} matches")

print(f"\n=== Total providers: {len(all_providers())} ===")
