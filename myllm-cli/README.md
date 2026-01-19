# MyLLM CLI

A powerful command-line tool for managing and interacting with local LLM models (GGUF format).

## Features

- 🚀 **Load and manage local GGUF models**
- 💬 **Interactive chat sessions** with markdown support
- 🌐 **Local API server** (OpenAI-compatible)
- ⚙️ **Flexible configuration** management
- 🎨 **Beautiful CLI interface** with Rich
- 🔧 **GPU acceleration** support

## Installation

### Prerequisites

- Python 3.8 or higher
- (Optional) CUDA-enabled GPU for GPU acceleration

### Install from source

```bash
# Clone or navigate to the project directory
cd myllm-cli

# Install in development mode
pip install -e .

# Or install normally
pip install .
```

### Install dependencies only

```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Configure your models directory

```bash
# Set the directory where your GGUF models are stored
myllm config set models_directory "C:\progeto\lmstudio-community"
```

### 2. List available models

```bash
myllm ls
```

### 3. Load a model

```bash
# Load by full path
myllm load "C:\progeto\lmstudio-community\gpt-oss-20b-GGUF\gpt-oss-20b.gguf"

# Or load by name (if in models directory)
myllm load gpt-oss-20b

# With custom settings
myllm load gpt-oss-20b --identifier my-model --gpu 1.0 --context-length 4096
```

### 4. Start chatting

```bash
myllm chat
```

### 5. Start API server

```bash
myllm server start
```

## Commands Reference

### Model Management

#### `myllm ls`
List all available models in your models directory.

```bash
myllm ls
```

#### `myllm load <model>`
Load a model into memory.

```bash
# Basic load
myllm load gpt-oss-20b

# With options
myllm load gpt-oss-20b \
  --identifier my-gpt \
  --gpu 1.0 \
  --context-length 4096
```

**Options:**
- `--identifier, -i`: Custom name for the model
- `--gpu, -g`: GPU offload (0.0-1.0, or "max" for full offload)
- `--context-length, -c`: Context window size (default: 2048)

#### `myllm unload <identifier>`
Unload a model from memory.

```bash
# Unload specific model
myllm unload my-gpt

# Unload all models
myllm unload --all
```

#### `myllm ps`
List currently loaded models.

```bash
myllm ps
```

### Chat

#### `myllm chat [model]`
Start an interactive chat session.

```bash
# Use first loaded model
myllm chat

# Use specific model
myllm chat my-gpt
```

**Chat Commands:**
- `/clear` - Clear conversation history
- `/system <prompt>` - Set system prompt
- `/exit` or `/quit` - Exit chat

### Server Management

#### `myllm server start`
Start the local API server.

```bash
# Start with default settings
myllm server start

# Start with custom host/port
myllm server start --host 0.0.0.0 --port 8080
```

#### `myllm server stop`
Stop the API server.

```bash
myllm server stop
```

#### `myllm server status`
Check server status.

```bash
myllm server status
```

### Configuration

#### `myllm config show`
Show current configuration.

```bash
myllm config show
```

#### `myllm config set <key> <value>`
Set a configuration value.

```bash
# Set models directory
myllm config set models_directory "/path/to/models"

# Set server port
myllm config set server.port 8080

# Set default GPU layers
myllm config set default_model_params.gpu_layers -1

# Set default context length
myllm config set default_model_params.context_length 4096

# Set default temperature
myllm config set default_model_params.temperature 0.7
```

#### `myllm config get <key>`
Get a configuration value.

```bash
myllm config get models_directory
```

## API Server

The API server provides OpenAI-compatible endpoints:

### Endpoints

#### GET `/v1/models`
List available models.

```bash
curl http://localhost:8080/v1/models
```

#### POST `/v1/chat/completions`
Chat completions (OpenAI-compatible).

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "my-gpt",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "temperature": 0.7,
    "max_tokens": 512
  }'
```

#### POST `/v1/completions`
Text completions (OpenAI-compatible).

```bash
curl http://localhost:8080/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "my-gpt",
    "prompt": "Once upon a time",
    "temperature": 0.7,
    "max_tokens": 512
  }'
```

## Configuration File

Configuration is stored in `~/.myllm/config.json`:

```json
{
  "models_directory": "C:\\progeto\\lmstudio-community",
  "server": {
    "host": "127.0.0.1",
    "port": 8080
  },
  "default_model_params": {
    "gpu_layers": -1,
    "context_length": 2048,
    "temperature": 0.7,
    "top_p": 0.9,
    "max_tokens": 512
  }
}
```

## Examples

### Example 1: Quick Chat

```bash
# Set up models directory
myllm config set models_directory "C:\progeto\lmstudio-community"

# Load your model
myllm load gpt-oss-20b-GGUF/gpt-oss-20b.gguf --gpu max

# Start chatting
myllm chat
```

### Example 2: Run API Server

```bash
# Load multiple models
myllm load gpt-oss-20b --identifier gpt-20b
myllm load llama-7b --identifier llama-7b

# Start server
myllm server start

# In another terminal, test the API
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-20b",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### Example 3: Use with OpenAI SDK

```python
from openai import OpenAI

# Point to your local server
client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="not-needed"
)

# Chat
response = client.chat.completions.create(
    model="gpt-20b",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

## Troubleshooting

### Model not loading

- Ensure the model file is in GGUF format
- Check that the path is correct
- Try reducing `--context-length` if you run out of memory
- Reduce `--gpu` if you have limited VRAM

### Server won't start

- Check if the port is already in use
- Ensure at least one model is loaded
- Check server status: `myllm server status`

### GPU acceleration not working

- Ensure you have CUDA installed
- Install llama-cpp-python with CUDA support:
  ```bash
  CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
  ```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

Built with:
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Click](https://click.palletsprojects.com/)
- [Rich](https://rich.readthedocs.io/)
