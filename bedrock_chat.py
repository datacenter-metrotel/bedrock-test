#!/usr/bin/env python3
"""
Bedrock Chat - Script interactivo para probar credenciales AWS Bedrock

Configurar credenciales via variables de entorno:
    export AWS_ACCESS_KEY_ID="tu-access-key"
    export AWS_SECRET_ACCESS_KEY="tu-secret-key"
    export AWS_DEFAULT_REGION="us-east-1"

O crear archivo .env en el mismo directorio.
"""

import boto3
import json
import sys
import os

# === CONFIGURACIÓN ===
# Cargar desde .env si existe
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip().strip('"\''))

load_env()

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')

# Modelo por defecto (usar inference profile, no model ID directo)
DEFAULT_MODEL = os.environ.get('BEDROCK_DEFAULT_MODEL', 'us.anthropic.claude-sonnet-5')


def get_bedrock_client():
    """Crear cliente de Bedrock Runtime"""
    return boto3.client(
        'bedrock-runtime',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )


def get_bedrock_management_client():
    """Crear cliente de Bedrock Management"""
    return boto3.client(
        'bedrock',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )


def verify_credentials():
    """Verificar que las credenciales son válidas"""
    print("🔐 Verificando credenciales AWS...")
    try:
        sts = boto3.client(
            'sts',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        identity = sts.get_caller_identity()
        print(f"   ✅ Account: {identity['Account']}")
        print(f"   ✅ User: {identity['Arn'].split('/')[-1]}")
        return True
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def extract_response_text(response):
    """Extraer texto de la respuesta, manejando diferentes formatos de modelo"""
    content = response['output']['message']['content']

    # Primero buscar texto directo (prioridad para Grok, OpenAI, Anthropic, etc.)
    for item in content:
        if 'text' in item:
            return item['text']

    # Si no hay texto directo, buscar en reasoningContent (DeepSeek R1)
    for item in content:
        if 'reasoningContent' in item:
            reasoning = item['reasoningContent']
            if 'reasoningText' in reasoning:
                text = reasoning['reasoningText'].get('text', '')
                # Buscar respuesta final después de </think> o similar
                if '</think>' in text:
                    parts = text.split('</think>')
                    return parts[-1].strip() if len(parts) > 1 else text
                return text

    # Fallback
    return "[Respuesta no disponible en formato texto]"


def test_model_connection(model_id):
    """Probar conexión con un modelo específico"""
    print(f"\n🤖 Probando conexión con: {model_id}")
    try:
        client = get_bedrock_client()
        # Usar maxTokens suficientes para modelos de razonamiento (Grok, DeepSeek)
        response = client.converse(
            modelId=model_id,
            messages=[{"role": "user", "content": [{"text": "Responde solo OK"}]}],
            inferenceConfig={"maxTokens": 256}
        )
        output = extract_response_text(response)
        # Limpiar output para mostrar solo lo relevante
        output_clean = output.strip().replace('\n', ' ')[:80]
        print(f"   ✅ Modelo responde: {output_clean}")
        return True
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def chat(model_id, message, conversation_history=None):
    """Enviar mensaje al modelo y obtener respuesta"""
    client = get_bedrock_client()

    if conversation_history is None:
        conversation_history = []

    conversation_history.append({
        "role": "user",
        "content": [{"text": message}]
    })

    response = client.converse(
        modelId=model_id,
        messages=conversation_history,
        inferenceConfig={"maxTokens": 4096}
    )

    assistant_message = extract_response_text(response)
    usage = response['usage']

    # Para el historial, guardar solo el texto limpio
    clean_message = assistant_message.replace("[Razonamiento]: ", "")
    conversation_history.append({
        "role": "assistant",
        "content": [{"text": clean_message}]
    })

    return assistant_message, usage, conversation_history


def interactive_chat(model_id=DEFAULT_MODEL):
    """Modo chat interactivo"""
    print("\n" + "=" * 60)
    print(f"💬 Chat interactivo con: {model_id}")
    print("=" * 60)
    print("Comandos especiales:")
    print("  /salir    - Terminar chat")
    print("  /nuevo    - Nueva conversación")
    print("  /modelo   - Cambiar modelo")
    print("  /tokens   - Mostrar uso de tokens")
    print("=" * 60 + "\n")

    conversation_history = []
    total_input_tokens = 0
    total_output_tokens = 0

    while True:
        try:
            user_input = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 ¡Hasta luego!")
            break

        if not user_input:
            continue

        if user_input.lower() == '/salir':
            print("\n👋 ¡Hasta luego!")
            break

        if user_input.lower() == '/nuevo':
            conversation_history = []
            total_input_tokens = 0
            total_output_tokens = 0
            print("🔄 Nueva conversación iniciada.\n")
            continue

        if user_input.lower() == '/tokens':
            print(f"\n📊 Tokens usados en esta sesión:")
            print(f"   Entrada: {total_input_tokens}")
            print(f"   Salida: {total_output_tokens}")
            print(f"   Total: {total_input_tokens + total_output_tokens}\n")
            continue

        if user_input.lower() == '/modelo':
            new_model = input("Nuevo modelo (Enter para cancelar): ").strip()
            if new_model:
                model_id = new_model
                conversation_history = []
                print(f"✅ Modelo cambiado a: {model_id}\n")
            continue

        try:
            response, usage, conversation_history = chat(model_id, user_input, conversation_history)
            total_input_tokens += usage['inputTokens']
            total_output_tokens += usage['outputTokens']
            print(f"\nAI: {response}\n")
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


def list_available_models():
    """Listar modelos disponibles con sus inference profiles"""
    print("\n📋 Listando inference profiles disponibles...")
    try:
        client = get_bedrock_management_client()
        response = client.list_inference_profiles()
        profiles = response.get('inferenceProfileSummaries', [])

        print(f"\nEncontrados {len(profiles)} inference profiles:\n")

        by_provider = {}
        for p in profiles:
            profile_id = p.get('inferenceProfileId', '')
            provider = profile_id.split('.')[1] if '.' in profile_id else 'unknown'
            if provider not in by_provider:
                by_provider[provider] = []
            by_provider[provider].append(profile_id)

        for provider, models in sorted(by_provider.items()):
            print(f"--- {provider.upper()} ---")
            for m in sorted(models):
                print(f"  {m}")
            print()

    except Exception as e:
        print(f"❌ Error: {e}")


def check_credentials():
    """Verificar que las credenciales están configuradas"""
    if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
        print("❌ Error: Credenciales AWS no configuradas.\n")
        print("Configura las siguientes variables de entorno:")
        print("  export AWS_ACCESS_KEY_ID='tu-access-key'")
        print("  export AWS_SECRET_ACCESS_KEY='tu-secret-key'")
        print("  export AWS_DEFAULT_REGION='us-east-1'")
        print("\nO crea un archivo .env con:")
        print("  AWS_ACCESS_KEY_ID=tu-access-key")
        print("  AWS_SECRET_ACCESS_KEY=tu-secret-key")
        print("  AWS_DEFAULT_REGION=us-east-1")
        return False
    return True


def main():
    print("=" * 60)
    print("       BEDROCK CHAT - Test de Credenciales")
    print("=" * 60)

    if not check_credentials():
        sys.exit(1)

    if not verify_credentials():
        print("\n❌ Las credenciales no son válidas. Verifica la configuración.")
        sys.exit(1)

    if not test_model_connection(DEFAULT_MODEL):
        print(f"\n⚠️  No se pudo conectar con {DEFAULT_MODEL}")
        print("Puedes intentar con otro modelo usando /modelo en el chat.")

    while True:
        print("\n📌 Menú principal:")
        print("  1. Chat interactivo")
        print("  2. Listar modelos disponibles")
        print("  3. Probar otro modelo")
        print("  4. Salir")

        try:
            choice = input("\nOpción: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 ¡Hasta luego!")
            break

        if choice == '1':
            interactive_chat()
        elif choice == '2':
            list_available_models()
        elif choice == '3':
            model = input("ID del modelo a probar: ").strip()
            if model:
                if test_model_connection(model):
                    start_chat = input("¿Iniciar chat con este modelo? (s/n): ").strip().lower()
                    if start_chat == 's':
                        interactive_chat(model)
        elif choice == '4':
            print("\n👋 ¡Hasta luego!")
            break


if __name__ == '__main__':
    main()
