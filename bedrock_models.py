#!/usr/bin/env python3
"""
Bedrock Models - Lista de modelos disponibles para invocar via AWS Bedrock
Region: us-east-1 (N. Virginia)

USO:
    from bedrock_models import MODELS, get_model, list_models

    # Obtener un modelo específico
    model_id = get_model('claude-sonnet-5')
    # -> 'us.anthropic.claude-sonnet-5'

    # Listar todos los modelos
    list_models()
"""

# =============================================================================
# INFERENCE PROFILES - Usar estos IDs para invocar modelos
# =============================================================================
# Prefijo "us." = Cross-region inference (US)
# Prefijo "global." = Global inference
# =============================================================================

MODELS = {
    # =========================================================================
    # ANTHROPIC - Claude
    # =========================================================================

    # Claude 5.x
    "claude-sonnet-5": "us.anthropic.claude-sonnet-5",
    "claude-sonnet-5-5": "us.anthropic.claude-sonnet-5-5",
    "claude-opus-5": "us.anthropic.claude-opus-5",
    "claude-opus-5-5": "us.anthropic.claude-opus-5-5",
    "claude-haiku-5-5": "us.anthropic.claude-haiku-5-5",
    "claude-fable-5": "us.anthropic.claude-fable-5",
    "claude-fable-5-1": "us.anthropic.claude-fable-5-1",

    # Claude 4.x
    "claude-sonnet-4": "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "claude-sonnet-4-5": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "claude-sonnet-4-6": "us.anthropic.claude-sonnet-4-6",
    "claude-opus-4-1": "us.anthropic.claude-opus-4-1-20250805-v1:0",
    "claude-opus-4-5": "us.anthropic.claude-opus-4-5-20251101-v1:0",
    "claude-opus-4-6": "us.anthropic.claude-opus-4-6-v1",
    "claude-opus-4-7": "us.anthropic.claude-opus-4-7",
    "claude-opus-4-8": "us.anthropic.claude-opus-4-8",
    "claude-haiku-4-5": "us.anthropic.claude-haiku-4-5-20251001-v1:0",

    # Claude 3.x (legacy)
    "claude-3-sonnet": "us.anthropic.claude-3-sonnet-20240229-v1:0",
    "claude-3-haiku": "us.anthropic.claude-3-haiku-20240307-v1:0",

    # =========================================================================
    # OPENAI - GPT
    # =========================================================================

    # GPT 6.x
    "gpt-6-astra": "us.openai.gpt-6-astra",
    "gpt-6-luna": "us.openai.gpt-6-luna",
    "gpt-6-sol": "us.openai.gpt-6-sol",
    "gpt-6.1-sol": "us.openai.gpt-6.1-sol",

    # GPT 5.x
    "gpt-5.4": "us.openai.gpt-5.4",
    "gpt-5.5": "us.openai.gpt-5.5",
    "gpt-5.6-luna": "us.openai.gpt-5.6-luna",
    "gpt-5.6-sol": "us.openai.gpt-5.6-sol",
    "gpt-5.6-terra": "us.openai.gpt-5.6-terra",

    # =========================================================================
    # META - Llama
    # =========================================================================

    # Llama 4
    "llama4-maverick": "us.meta.llama4-maverick-17b-instruct-v1:0",
    "llama4-scout": "us.meta.llama4-scout-17b-instruct-v1:0",

    # Llama 3.3
    "llama3-3-70b": "us.meta.llama3-3-70b-instruct-v1:0",

    # Llama 3.2
    "llama3-2-90b": "us.meta.llama3-2-90b-instruct-v1:0",
    "llama3-2-11b": "us.meta.llama3-2-11b-instruct-v1:0",
    "llama3-2-3b": "us.meta.llama3-2-3b-instruct-v1:0",
    "llama3-2-1b": "us.meta.llama3-2-1b-instruct-v1:0",

    # Llama 3.1
    "llama3-1-70b": "us.meta.llama3-1-70b-instruct-v1:0",
    "llama3-1-8b": "us.meta.llama3-1-8b-instruct-v1:0",

    # =========================================================================
    # DEEPSEEK
    # =========================================================================
    "deepseek-r1": "us.deepseek.r1-v1:0",

    # =========================================================================
    # XAI - Grok
    # =========================================================================
    "grok-4.6": "us.xai.grok-4.6",
    "grok-4.7": "us.xai.grok-4.7",

    # =========================================================================
    # MISTRAL
    # =========================================================================
    "pixtral-large": "us.mistral.pixtral-large-2502-v1:0",

    # =========================================================================
    # MOONSHOT - Kimi
    # =========================================================================
    "kimi-k3": "us.moonshotai.kimi-k3",

    # =========================================================================
    # WRITER - Palmyra
    # =========================================================================
    "palmyra-x4": "us.writer.palmyra-x4-v1:0",
    "palmyra-x5": "us.writer.palmyra-x5-v1:0",

    # =========================================================================
    # Z.AI - GLM
    # =========================================================================
    "glm-5.3": "us.zai.glm-5.3",

    # =========================================================================
    # AMAZON - Nova
    # =========================================================================
    "nova-pro": "us.amazon.nova-pro-v1:0",
    "nova-lite": "us.amazon.nova-lite-v1:0",
    "nova-micro": "us.amazon.nova-micro-v1:0",
    "nova-premier": "us.amazon.nova-premier-v1:0",
    "nova-2-lite": "us.amazon.nova-2-lite-v1:0",

    # =========================================================================
    # COHERE - Embeddings
    # =========================================================================
    "cohere-embed-v4": "us.cohere.embed-v4:0",

    # =========================================================================
    # TWELVELABS - Video
    # =========================================================================
    "pegasus-1.2": "us.twelvelabs.pegasus-1-2-v1:0",
    "marengo-embed-3.0": "us.twelvelabs.marengo-embed-3-0-v1:0",
    "marengo-embed-2.7": "us.twelvelabs.marengo-embed-2-7-v1:0",

    # =========================================================================
    # STABILITY - Image
    # =========================================================================
    "stable-upscale-creative": "us.stability.stable-creative-upscale-v1:0",
    "stable-upscale-conservative": "us.stability.stable-conservative-upscale-v1:0",
    "stable-upscale-fast": "us.stability.stable-fast-upscale-v1:0",
    "stable-inpaint": "us.stability.stable-image-inpaint-v1:0",
    "stable-outpaint": "us.stability.stable-outpaint-v1:0",
    "stable-remove-bg": "us.stability.stable-image-remove-background-v1:0",
    "stable-erase": "us.stability.stable-image-erase-object-v1:0",
    "stable-search-replace": "us.stability.stable-image-search-replace-v1:0",
    "stable-search-recolor": "us.stability.stable-image-search-recolor-v1:0",
    "stable-style-transfer": "us.stability.stable-style-transfer-v1:0",
    "stable-style-guide": "us.stability.stable-image-style-guide-v1:0",
    "stable-control-sketch": "us.stability.stable-image-control-sketch-v1:0",
    "stable-control-structure": "us.stability.stable-image-control-structure-v1:0",
}

# =============================================================================
# IDs COMPLETOS - Para referencia directa
# =============================================================================

ALL_INFERENCE_PROFILES = {
    "anthropic": [
        "us.anthropic.claude-sonnet-5",
        "us.anthropic.claude-sonnet-5-5",
        "us.anthropic.claude-opus-5",
        "us.anthropic.claude-opus-5-5",
        "us.anthropic.claude-haiku-5-5",
        "us.anthropic.claude-fable-5",
        "us.anthropic.claude-fable-5-1",
        "us.anthropic.claude-sonnet-4-20250514-v1:0",
        "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
        "us.anthropic.claude-sonnet-4-6",
        "us.anthropic.claude-opus-4-1-20250805-v1:0",
        "us.anthropic.claude-opus-4-5-20251101-v1:0",
        "us.anthropic.claude-opus-4-6-v1",
        "us.anthropic.claude-opus-4-7",
        "us.anthropic.claude-opus-4-8",
        "us.anthropic.claude-haiku-4-5-20251001-v1:0",
        "us.anthropic.claude-3-sonnet-20240229-v1:0",
        "us.anthropic.claude-3-haiku-20240307-v1:0",
        "global.anthropic.claude-sonnet-5",
        "global.anthropic.claude-sonnet-5-5",
        "global.anthropic.claude-opus-5",
        "global.anthropic.claude-opus-5-5",
        "global.anthropic.claude-haiku-5-5",
        "global.anthropic.claude-fable-5",
        "global.anthropic.claude-fable-5-1",
        "global.anthropic.claude-sonnet-4-20250514-v1:0",
        "global.anthropic.claude-sonnet-4-5-20250929-v1:0",
        "global.anthropic.claude-sonnet-4-6",
        "global.anthropic.claude-opus-4-5-20251101-v1:0",
        "global.anthropic.claude-opus-4-6-v1",
        "global.anthropic.claude-opus-4-7",
        "global.anthropic.claude-opus-4-8",
        "global.anthropic.claude-haiku-4-5-20251001-v1:0",
    ],
    "openai": [
        "us.openai.gpt-6-astra",
        "us.openai.gpt-6-luna",
        "us.openai.gpt-6-sol",
        "us.openai.gpt-6.1-sol",
        "us.openai.gpt-5.4",
        "us.openai.gpt-5.5",
        "us.openai.gpt-5.6-luna",
        "us.openai.gpt-5.6-sol",
        "us.openai.gpt-5.6-terra",
        "global.openai.gpt-6-astra",
        "global.openai.gpt-6-luna",
        "global.openai.gpt-6-sol",
        "global.openai.gpt-6.1-sol",
        "global.openai.gpt-5.4",
        "global.openai.gpt-5.5",
        "global.openai.gpt-5.6-luna",
        "global.openai.gpt-5.6-sol",
        "global.openai.gpt-5.6-terra",
    ],
    "meta": [
        "us.meta.llama4-maverick-17b-instruct-v1:0",
        "us.meta.llama4-scout-17b-instruct-v1:0",
        "us.meta.llama3-3-70b-instruct-v1:0",
        "us.meta.llama3-2-90b-instruct-v1:0",
        "us.meta.llama3-2-11b-instruct-v1:0",
        "us.meta.llama3-2-3b-instruct-v1:0",
        "us.meta.llama3-2-1b-instruct-v1:0",
        "us.meta.llama3-1-70b-instruct-v1:0",
        "us.meta.llama3-1-8b-instruct-v1:0",
    ],
    "deepseek": [
        "us.deepseek.r1-v1:0",
    ],
    "xai": [
        "us.xai.grok-4.6",
        "us.xai.grok-4.7",
        "global.xai.grok-4.6",
        "global.xai.grok-4.7",
    ],
    "mistral": [
        "us.mistral.pixtral-large-2502-v1:0",
    ],
    "moonshot": [
        "us.moonshotai.kimi-k3",
        "global.moonshotai.kimi-k3",
    ],
    "writer": [
        "us.writer.palmyra-x4-v1:0",
        "us.writer.palmyra-x5-v1:0",
    ],
    "zai": [
        "us.zai.glm-5.3",
        "global.zai.glm-5.3",
    ],
    "amazon": [
        "us.amazon.nova-pro-v1:0",
        "us.amazon.nova-lite-v1:0",
        "us.amazon.nova-micro-v1:0",
        "us.amazon.nova-premier-v1:0",
        "us.amazon.nova-2-lite-v1:0",
        "global.amazon.nova-2-lite-v1:0",
    ],
    "cohere": [
        "us.cohere.embed-v4:0",
        "global.cohere.embed-v4:0",
    ],
    "twelvelabs": [
        "us.twelvelabs.pegasus-1-2-v1:0",
        "us.twelvelabs.marengo-embed-3-0-v1:0",
        "us.twelvelabs.marengo-embed-2-7-v1:0",
        "global.twelvelabs.pegasus-1-2-v1:0",
    ],
    "stability": [
        "us.stability.stable-creative-upscale-v1:0",
        "us.stability.stable-conservative-upscale-v1:0",
        "us.stability.stable-fast-upscale-v1:0",
        "us.stability.stable-image-inpaint-v1:0",
        "us.stability.stable-outpaint-v1:0",
        "us.stability.stable-image-remove-background-v1:0",
        "us.stability.stable-image-erase-object-v1:0",
        "us.stability.stable-image-search-replace-v1:0",
        "us.stability.stable-image-search-recolor-v1:0",
        "us.stability.stable-style-transfer-v1:0",
        "us.stability.stable-image-style-guide-v1:0",
        "us.stability.stable-image-control-sketch-v1:0",
        "us.stability.stable-image-control-structure-v1:0",
    ],
}


def get_model(name: str) -> str:
    """
    Obtener el ID de inference profile para un modelo.

    Args:
        name: Nombre corto del modelo (ej: 'claude-sonnet-5', 'gpt-6-astra')

    Returns:
        ID completo del inference profile (ej: 'us.anthropic.claude-sonnet-5')

    Raises:
        KeyError: Si el modelo no existe
    """
    if name in MODELS:
        return MODELS[name]

    # Buscar coincidencia parcial
    matches = [k for k in MODELS.keys() if name.lower() in k.lower()]
    if len(matches) == 1:
        return MODELS[matches[0]]
    elif len(matches) > 1:
        raise KeyError(f"Modelo ambiguo '{name}'. Coincidencias: {matches}")

    raise KeyError(f"Modelo '{name}' no encontrado. Usa list_models() para ver disponibles.")


def list_models(provider: str = None):
    """
    Listar modelos disponibles.

    Args:
        provider: Filtrar por proveedor (anthropic, openai, meta, etc.)
    """
    print("\n" + "=" * 70)
    print("MODELOS DISPONIBLES - AWS Bedrock")
    print("=" * 70)

    if provider:
        provider = provider.lower()
        filtered = {k: v for k, v in MODELS.items() if provider in v.lower()}
        for name, model_id in sorted(filtered.items()):
            print(f"  {name:30} -> {model_id}")
    else:
        current_provider = None
        for name, model_id in sorted(MODELS.items(), key=lambda x: x[1]):
            parts = model_id.split('.')
            prov = parts[1] if len(parts) >= 2 else 'unknown'

            if prov != current_provider:
                current_provider = prov
                print(f"\n--- {prov.upper()} ---")

            print(f"  {name:30} -> {model_id}")

    print("\n" + "=" * 70)
    print(f"Total: {len(MODELS)} modelos con alias")
    print("=" * 70 + "\n")


def list_all_profiles():
    """Listar todos los inference profiles por proveedor"""
    print("\n" + "=" * 70)
    print("TODOS LOS INFERENCE PROFILES")
    print("=" * 70)

    total = 0
    for provider, profiles in sorted(ALL_INFERENCE_PROFILES.items()):
        print(f"\n--- {provider.upper()} ({len(profiles)}) ---")
        for p in sorted(profiles):
            print(f"  {p}")
        total += len(profiles)

    print("\n" + "=" * 70)
    print(f"Total: {total} inference profiles")
    print("=" * 70 + "\n")


# =============================================================================
# EJEMPLO DE USO
# =============================================================================

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == '--all':
            list_all_profiles()
        elif sys.argv[1] == '--provider' and len(sys.argv) > 2:
            list_models(sys.argv[2])
        else:
            try:
                model_id = get_model(sys.argv[1])
                print(f"\n{sys.argv[1]} -> {model_id}\n")
            except KeyError as e:
                print(f"\n❌ {e}\n")
    else:
        list_models()
        print("\nUso:")
        print("  python bedrock_models.py                    # Listar todos")
        print("  python bedrock_models.py --all              # Listar inference profiles")
        print("  python bedrock_models.py --provider anthropic  # Filtrar por proveedor")
        print("  python bedrock_models.py claude-sonnet-5    # Obtener ID de modelo")
