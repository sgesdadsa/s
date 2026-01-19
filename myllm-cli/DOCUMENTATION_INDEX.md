# MyLLM CLI - Documentation Index

Complete documentation index for MyLLM CLI.

## 📚 Getting Started

### Essential Guides
1. **[README.md](README.md)** - Main documentation
   - Features overview
   - Installation instructions
   - Command reference
   - API documentation
   - Examples

2. **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide
   - 5-minute setup
   - First time configuration
   - Common tasks
   - Tips and tricks

3. **[WINDOWS_GUIDE.md](WINDOWS_GUIDE.md)** - Windows-specific guide
   - Windows installation
   - CUDA setup
   - Troubleshooting
   - Batch scripts
   - Portuguese version

## 🛠 Installation

### Installation Scripts
- **`install.sh`** - Linux/Mac installation
- **`install.bat`** - Windows installation
- **`quickstart.bat`** - Windows quick setup
- **`test_installation.py`** - Test your installation

### Requirements
- **`requirements.txt`** - Python dependencies
- **`setup.py`** - Package configuration

## 📖 User Guides

### Core Documentation
1. **[QUICKSTART.md](QUICKSTART.md)**
   - Quick setup (5 min)
   - Basic usage
   - Common tasks
   - Configuration tips

2. **[WINDOWS_GUIDE.md](WINDOWS_GUIDE.md)**
   - Windows-specific setup
   - GPU configuration
   - Troubleshooting
   - Batch scripts

3. **[OPTIMIZATION.md](OPTIMIZATION.md)**
   - Performance tuning
   - GPU optimization
   - Memory management
   - Hardware recommendations
   - Benchmarking

## 💻 Code Examples

### Example Scripts (`examples/`)

1. **`usage_example.py`**
   - Using the API with requests
   - Chat completions
   - Text completions
   - Multi-turn conversations

2. **`openai_example.py`**
   - Using OpenAI SDK
   - Chat examples
   - Streaming (if supported)
   - Function calling patterns

3. **`advanced_config.py`**
   - Programmatic configuration
   - Configuration presets
   - Hardware-specific setups
   - Custom parameters

4. **`daily_usage.bat`** (Windows)
   - Interactive menu
   - Common tasks
   - Model management
   - Server control

## 🔧 Development

### Contributing
- **[CONTRIBUTING.md](CONTRIBUTING.md)**
  - Development setup
  - Code style guide
  - Testing guidelines
  - Pull request process
  - Areas for contribution

### Project Structure
```
myllm-cli/
├── myllm/              # Main package
│   ├── cli.py          # CLI interface
│   ├── config.py       # Configuration
│   ├── models.py       # Model management
│   ├── chat.py         # Chat functionality
│   └── server.py       # API server
├── examples/           # Usage examples
└── [documentation]     # All guides
```

## 📋 Command Reference

### Model Commands
```bash
myllm ls                    # List models
myllm load <model>          # Load model
myllm unload <identifier>   # Unload model
myllm ps                    # List loaded models
```

### Chat Commands
```bash
myllm chat [model]          # Start chat
# In chat:
#   /clear  - Clear history
#   /system - Set system prompt
#   /exit   - Exit chat
```

### Server Commands
```bash
myllm server start          # Start API server
myllm server stop           # Stop server
myllm server status         # Check status
```

### Configuration Commands
```bash
myllm config show           # Show config
myllm config set <key> <value>  # Set value
myllm config get <key>      # Get value
```

## 🌐 API Reference

### Endpoints

**Models**
- `GET /v1/models` - List loaded models

**Chat**
- `POST /v1/chat/completions` - Chat completions (OpenAI-compatible)

**Completions**
- `POST /v1/completions` - Text completions (OpenAI-compatible)

### API Examples

**Using curl:**
```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "my-model", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Using Python (requests):**
See `examples/usage_example.py`

**Using Python (OpenAI SDK):**
See `examples/openai_example.py`

## ⚙️ Configuration

### Configuration File
Location: `~/.myllm/config.json`

### Key Settings
- `models_directory` - Where .gguf files are stored
- `server.host` - API server host
- `server.port` - API server port
- `default_model_params.gpu_layers` - GPU offload
- `default_model_params.context_length` - Context window
- `default_model_params.temperature` - Response randomness

### Configuration Presets
See `examples/advanced_config.py` for:
- Creative writing preset
- Precise/factual preset
- Balanced preset
- Coding preset
- Hardware-specific configs

## 🐛 Troubleshooting

### Common Issues

**Installation Issues**
- See: [QUICKSTART.md](QUICKSTART.md#common-issues)
- See: [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md#-solução-de-problemas)

**Performance Issues**
- See: [OPTIMIZATION.md](OPTIMIZATION.md#troubleshooting-performance)

**Model Loading Issues**
- Check: [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md#failed-to-load-model)

**GPU Issues**
- See: [OPTIMIZATION.md](OPTIMIZATION.md#gpu-optimization)

## 📊 Performance

### Optimization Topics
1. GPU acceleration (CUDA, ROCm, Metal)
2. Memory optimization
3. CPU threading
4. Model selection
5. Parameter tuning
6. Benchmarking

Full details: [OPTIMIZATION.md](OPTIMIZATION.md)

## 🎯 Use Cases

### By Task
- **Coding**: Use coding preset, temperature 0.2
- **Writing**: Use creative preset, temperature 0.9
- **Q&A**: Use balanced preset, temperature 0.7
- **Analysis**: Use precise preset, temperature 0.3

### By Hardware
- **High-end GPU (24GB+)**: 20B+ models, 8K context
- **Mid-range GPU (12GB)**: 13B models, 4K context
- **Entry GPU (8GB)**: 7B models, 2K context
- **CPU only**: 7B quantized, 2K context

See: [OPTIMIZATION.md](OPTIMIZATION.md#hardware-recommendations)

## 🔗 Quick Links

### Essential Files
- [README.md](README.md) - Complete documentation
- [QUICKSTART.md](QUICKSTART.md) - Get started in 5 min
- [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md) - Windows users
- [OPTIMIZATION.md](OPTIMIZATION.md) - Performance tips

### Installation
- `install.sh` - Linux/Mac installer
- `install.bat` - Windows installer
- `quickstart.bat` - Windows quick setup

### Examples
- `examples/usage_example.py` - Basic API usage
- `examples/openai_example.py` - OpenAI SDK usage
- `examples/advanced_config.py` - Advanced config
- `examples/daily_usage.bat` - Windows menu

### Contributing
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [LICENSE](LICENSE) - MIT License

## 🆘 Getting Help

### In-App Help
```bash
myllm --help              # General help
myllm <command> --help    # Command-specific help
```

### Documentation
1. Start with [QUICKSTART.md](QUICKSTART.md)
2. Check [README.md](README.md) for detailed info
3. See [OPTIMIZATION.md](OPTIMIZATION.md) for performance
4. Windows users: [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md)

### Testing
```bash
python test_installation.py  # Test your installation
```

## 📝 Changelog

### Version 0.1.0 (Initial Release)
- ✅ Model management (load, unload, list)
- ✅ Interactive chat with markdown support
- ✅ OpenAI-compatible API server
- ✅ Configuration management
- ✅ GPU acceleration support
- ✅ Rich CLI interface
- ✅ Comprehensive documentation

### Planned Features
- [ ] Model search and download
- [ ] Streaming responses
- [ ] Web UI
- [ ] Plugin system
- [ ] Conversation export/import
- [ ] Multiple model backends

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution opportunities.

## 🌟 Feature Highlights

### ✨ Easy to Use
- Simple commands
- Interactive chat
- Helpful error messages
- Beautiful CLI output

### ⚡ Powerful
- GPU acceleration
- Multiple models
- API server
- OpenAI-compatible

### 🛠 Flexible
- Extensive configuration
- Multiple presets
- Programmatic access
- Cross-platform

### 📚 Well Documented
- Complete guides
- Code examples
- Troubleshooting
- Performance tips

## 🚀 Next Steps

1. **New Users**: Start with [QUICKSTART.md](QUICKSTART.md)
2. **Windows Users**: Read [WINDOWS_GUIDE.md](WINDOWS_GUIDE.md)
3. **Developers**: Check [examples/](examples/) folder
4. **Performance**: Read [OPTIMIZATION.md](OPTIMIZATION.md)
5. **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📞 Support

- 📖 Documentation: Read this index
- 🐛 Issues: Create GitHub issue
- 💡 Ideas: Discussion board
- 🤝 Contribute: Pull requests welcome

---

**Last Updated**: 2024
**Version**: 0.1.0
**Status**: Initial Release
