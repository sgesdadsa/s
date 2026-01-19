# Quick Start Guide

Get up and running with MyLLM CLI in 5 minutes!

## Installation

### Windows

```cmd
# Run the installation script
install.bat

# Or install manually
pip install -e .
```

### Linux/Mac

```bash
# Make the script executable
chmod +x install.sh

# Run the installation script
./install.sh

# Or install manually
pip install -e .
```

## First Time Setup

### 1. Set your models directory

This is where your GGUF model files are stored:

```bash
# Windows
myllm config set models_directory "C:\progeto\lmstudio-community"

# Linux/Mac
myllm config set models_directory "/home/user/models"
```

### 2. Verify your models are detected

```bash
myllm ls
```

You should see a list of `.gguf` files in your models directory.

### 3. Load a model

```bash
# Load by name (from myllm ls output)
myllm load gpt-oss-20b

# Load with full GPU offload
myllm load gpt-oss-20b --gpu max

# Load with custom settings
myllm load gpt-oss-20b \
  --identifier my-model \
  --gpu 1.0 \
  --context-length 4096
```

### 4. Start chatting!

```bash
myllm chat
```

## Common Tasks

### Check what's loaded

```bash
myllm ps
```

### Start the API server

```bash
# Start server
myllm server start

# Check status
myllm server status

# Stop server
myllm server stop
```

### Test the API

```bash
# List models
curl http://localhost:8080/v1/models

# Chat
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "my-model",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### Use with Python

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="my-model",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

## Configuration

### View current config

```bash
myllm config show
```

### Change settings

```bash
# Server port
myllm config set server.port 8080

# Default context length
myllm config set default_model_params.context_length 4096

# Default temperature
myllm config set default_model_params.temperature 0.7
```

## Tips

1. **GPU Memory**: Use `--gpu` to control how much of the model runs on GPU
   - `--gpu max` or `--gpu 1.0` = Full GPU offload (fastest)
   - `--gpu 0.5` = Half GPU, half CPU
   - `--gpu 0` = CPU only

2. **Context Length**: Larger context = more memory needed
   - Start with 2048 and increase if needed
   - Maximum depends on your hardware

3. **Multiple Models**: You can load multiple models and switch between them
   ```bash
   myllm load model1 --identifier m1
   myllm load model2 --identifier m2
   myllm chat m1  # Chat with model1
   ```

4. **API Compatibility**: The server is OpenAI-compatible, so you can use it with:
   - OpenAI Python SDK
   - Any tool that supports OpenAI API
   - Your own applications

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out the [examples](examples/) folder for code samples
- Explore advanced configuration options

## Getting Help

```bash
# General help
myllm --help

# Command-specific help
myllm load --help
myllm chat --help
myllm server --help
```

## Common Issues

### "No models found"
- Check your models directory: `myllm config get models_directory`
- Make sure `.gguf` files are in that directory
- Update the path: `myllm config set models_directory /correct/path`

### "Failed to load model"
- Not enough memory? Try reducing `--context-length`
- GPU issues? Try `--gpu 0` for CPU-only mode
- Wrong file format? Only `.gguf` files are supported

### "Server won't start"
- Port already in use? Change it: `myllm config set server.port 8081`
- No models loaded? Load a model first: `myllm load <model>`
- Check status: `myllm server status`

For more troubleshooting, see the full README.
