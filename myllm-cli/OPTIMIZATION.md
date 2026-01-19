# Performance Optimization Guide

Tips and tricks to get the best performance from MyLLM CLI.

## GPU Optimization

### NVIDIA GPUs

1. **Install CUDA-enabled llama-cpp-python**
```bash
# Uninstall existing version
pip uninstall llama-cpp-python -y

# Install with CUDA support
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
```

2. **Check GPU is being used**
```bash
# On Windows
nvidia-smi

# You should see python process using GPU memory
```

3. **Optimize GPU offload**
```bash
# Full GPU offload (fastest)
myllm load model --gpu max

# Partial offload (if running out of VRAM)
myllm load model --gpu 0.7  # 70% on GPU
```

### AMD GPUs (ROCm)

```bash
# Install with ROCm support
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
```

### Apple Silicon (M1/M2/M3)

```bash
# Metal acceleration (built-in on macOS)
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python --force-reinstall --no-cache-dir

# Use maximum GPU
myllm load model --gpu max
```

## Memory Optimization

### Reduce Context Length

```bash
# Smaller context = less memory
myllm load model --context-length 2048  # Default
myllm load model --context-length 1024  # Smaller, uses less memory
```

### Use Quantized Models

Smaller quantized models use less memory:
- Q4_K_M: Good balance (recommended)
- Q5_K_M: Better quality, more memory
- Q3_K_M: Smaller, faster, lower quality
- Q2_K: Smallest, fastest, lowest quality

### Monitor Memory Usage

```bash
# Windows
taskmgr

# Linux
htop

# Check VRAM
nvidia-smi  # NVIDIA
rocm-smi    # AMD
```

## CPU Optimization

### Set Thread Count

```bash
# Use more CPU threads for faster inference
myllm config set advanced.threads 8  # For 8-core CPU
myllm config set advanced.threads 16 # For 16-core CPU
```

### CPU-Only Mode

```bash
# Force CPU mode (no GPU)
myllm load model --gpu 0

# Increase threads for CPU
myllm config set advanced.threads 16
```

## Model Selection

### Choose the Right Size

- **2-7B models**: Fast, good for simple tasks
- **13B models**: Balanced performance and quality
- **20B+ models**: Best quality, slower, needs more VRAM

### Example Models by Use Case

**Fast Responses (2-7B)**
```bash
myllm load llama-7b --gpu max --context-length 2048
```

**Balanced (13B)**
```bash
myllm load llama-13b --gpu max --context-length 4096
```

**Best Quality (20B+)**
```bash
myllm load gpt-oss-20b --gpu max --context-length 4096
```

## Configuration Presets

### For RTX 3060 (12GB VRAM)
```bash
myllm config set default_model_params.gpu_layers -1
myllm config set default_model_params.context_length 2048
myllm config set default_model_params.batch_size 512
```

### For RTX 4090 (24GB VRAM)
```bash
myllm config set default_model_params.gpu_layers -1
myllm config set default_model_params.context_length 8192
myllm config set default_model_params.batch_size 512
```

### For CPU Only (No GPU)
```bash
myllm config set default_model_params.gpu_layers 0
myllm config set default_model_params.context_length 2048
myllm config set advanced.threads 16
myllm config set advanced.batch_size 256
```

### For Apple M1/M2 (16GB Unified Memory)
```bash
myllm config set default_model_params.gpu_layers -1
myllm config set default_model_params.context_length 4096
```

## Inference Parameters

### Temperature (Creativity)
```bash
# More deterministic (coding, facts)
myllm config set default_model_params.temperature 0.2

# Balanced (general use)
myllm config set default_model_params.temperature 0.7

# More creative (writing, brainstorming)
myllm config set default_model_params.temperature 0.9
```

### Max Tokens (Response Length)
```bash
# Short responses
myllm config set default_model_params.max_tokens 256

# Medium responses (default)
myllm config set default_model_params.max_tokens 512

# Long responses
myllm config set default_model_params.max_tokens 2048
```

## Benchmarking

### Test Model Speed

```python
import time
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8080/v1", api_key="x")

start = time.time()
response = client.chat.completions.create(
    model="your-model",
    messages=[{"role": "user", "content": "Count to 10"}],
    max_tokens=100
)
elapsed = time.time() - start

tokens = response.usage.total_tokens
print(f"Time: {elapsed:.2f}s")
print(f"Tokens: {tokens}")
print(f"Speed: {tokens/elapsed:.2f} tokens/sec")
```

### Compare Configurations

Test different settings and compare:
- GPU offload levels
- Context lengths
- Batch sizes
- Thread counts

## Troubleshooting Performance

### Slow Inference

1. Check GPU is being used: `nvidia-smi`
2. Verify GPU offload: `myllm ps` (check gpu_layers)
3. Reduce context length
4. Use smaller model or better quantization
5. Close other GPU applications

### Out of Memory

1. Reduce context length: `--context-length 2048`
2. Reduce GPU offload: `--gpu 0.5`
3. Use smaller quantized model
4. Close other applications
5. Try CPU mode: `--gpu 0`

### High Latency

1. Reduce max_tokens for shorter responses
2. Increase batch_size (if you have VRAM)
3. Use smaller model
4. Check network (if using remote server)

## Best Practices

1. **Start Small**: Begin with smaller models and scale up
2. **Monitor Resources**: Watch GPU/CPU/RAM usage
3. **Test Settings**: Benchmark different configurations
4. **Match Hardware**: Choose model size for your hardware
5. **Update Drivers**: Keep GPU drivers current
6. **Use SSD**: Store models on SSD for faster loading

## Hardware Recommendations

### Minimum (CPU Only)
- CPU: 4+ cores
- RAM: 8GB
- Storage: 10GB+ free
- Model: 7B Q4

### Recommended (Entry GPU)
- GPU: 8GB VRAM (RTX 3060, RTX 4060)
- CPU: 6+ cores
- RAM: 16GB
- Storage: 50GB+ SSD
- Model: 13B Q4

### Optimal (High-End)
- GPU: 16GB+ VRAM (RTX 4080, RTX 4090)
- CPU: 8+ cores
- RAM: 32GB+
- Storage: 100GB+ NVMe SSD
- Model: 20B+ Q5

## Advanced Optimization

### Batch Processing

For multiple requests, batch them:

```python
# Instead of multiple single requests
# Use batch processing when possible
```

### Model Caching

Keep models loaded to avoid reload time:

```bash
# Load models you use frequently
myllm load frequent-model --identifier daily
# Keep it loaded instead of unloading
```

### Server Configuration

For API server, optimize:

```bash
# Use uvicorn workers for multiple requests
# Set appropriate timeout values
# Enable keep-alive connections
```

## Questions?

If you're experiencing performance issues:
1. Check this guide for optimization tips
2. Share your hardware specs when asking for help
3. Include output from `myllm ps` and `myllm config show`
