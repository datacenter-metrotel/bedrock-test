# AWS Bedrock Test

Scripts para probar y utilizar modelos de AWS Bedrock con soporte para múltiples proveedores.

## Modelos Soportados

| Proveedor | Modelos Disponibles |
|-----------|---------------------|
| **Anthropic** | Claude Sonnet 5/5.5, Opus 4.x/5.x, Haiku 4.5/5.5, Fable 5/5.1 |
| **OpenAI** | GPT-5.4, 5.5, 5.6, 6-Astra, 6-Luna, 6-Sol |
| **Meta** | Llama 3.1, 3.2, 3.3, 4 (Scout, Maverick) |
| **DeepSeek** | R1 (reasoning model) |
| **xAI** | Grok 4.6, 4.7 |
| **Mistral** | Pixtral Large |
| **Amazon** | Nova Pro, Lite, Micro, Premier |
| **Google** | Gemma 3 (4B, 12B, 27B) |
| **Stability AI** | Image generation/editing models |
| + más | Cohere, Writer, Z.AI, Moonshot, NVIDIA, Qwen, TwelveLabs |

## Requisitos

- Python 3.8+
- boto3
- Credenciales AWS con acceso a Bedrock

```bash
pip install boto3
```

## Configuración

### Opción 1: Variables de entorno

```bash
export AWS_ACCESS_KEY_ID="tu-access-key"
export AWS_SECRET_ACCESS_KEY="tu-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

### Opción 2: Archivo .env

```bash
cp .env.example .env
# Editar .env con tus credenciales
```

## Uso

### Chat Interactivo

```bash
python3 bedrock_chat.py
```

**Comandos disponibles en el chat:**
- `/salir` - Terminar chat
- `/nuevo` - Nueva conversación
- `/modelo` - Cambiar modelo
- `/tokens` - Ver uso de tokens

### Catálogo de Modelos

```bash
# Listar todos los modelos con alias
python3 bedrock_models.py

# Obtener ID de un modelo específico
python3 bedrock_models.py claude-sonnet-5
# Output: us.anthropic.claude-sonnet-5

# Filtrar por proveedor
python3 bedrock_models.py --provider anthropic

# Listar todos los inference profiles
python3 bedrock_models.py --all
```

### Uso en código Python

```python
from bedrock_models import MODELS, get_model

# Obtener model ID por alias
model_id = get_model('claude-sonnet-5')  
# -> 'us.anthropic.claude-sonnet-5'

# Usar directamente el diccionario
model_id = MODELS['gpt-6-astra']  
# -> 'us.openai.gpt-6-astra'

# Chat programático
from bedrock_chat import chat, verify_credentials

if verify_credentials():
    response, usage, history = chat(
        'us.anthropic.claude-sonnet-5',
        'Hola, como estas?'
    )
    print(response)
```

## Estructura de Archivos

```
.
├── README.md              # Este archivo
├── .env.example           # Plantilla de configuración
├── .gitignore             # Archivos ignorados por git
├── bedrock_chat.py        # Chat interactivo
├── bedrock_models.py      # Catálogo de modelos
└── bedrock-models.md      # Lista de modelos en markdown
```

## Inference Profiles

AWS Bedrock requiere usar **Inference Profiles** en lugar de Model IDs directos para ciertos modelos. Los prefijos indican:

- `us.` - Cross-region inference (US)
- `global.` - Global inference

Ejemplo:
```python
# Correcto
model_id = 'us.anthropic.claude-sonnet-5'

# Incorrecto (puede fallar)
model_id = 'anthropic.claude-sonnet-5'
```

## Notas Técnicas

### Modelos de Razonamiento

DeepSeek R1 y Grok son modelos de razonamiento que devuelven `reasoningContent` antes del texto final. El script maneja esto automáticamente.

### Límites de Tokens

- OpenAI requiere `maxTokens >= 16`
- Para modelos de razonamiento se recomienda `maxTokens >= 256`

## Licencia

MIT
