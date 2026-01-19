# Contributing to MyLLM CLI

Thank you for your interest in contributing to MyLLM CLI! This document provides guidelines and instructions for contributing.

## Getting Started

### Development Setup

1. Clone the repository
```bash
git clone <repository-url>
cd myllm-cli
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode
```bash
pip install -e .
```

4. Install development dependencies
```bash
pip install pytest black flake8 mypy
```

## Project Structure

```
myllm-cli/
├── myllm/              # Main package
│   ├── __init__.py
│   ├── cli.py          # CLI interface
│   ├── config.py       # Configuration management
│   ├── models.py       # Model management
│   ├── chat.py         # Chat functionality
│   └── server.py       # API server
├── examples/           # Usage examples
├── tests/              # Test files (to be added)
├── requirements.txt    # Dependencies
├── setup.py           # Package setup
└── README.md          # Documentation
```

## Making Changes

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small

Format your code with Black:
```bash
black myllm/
```

Check style with flake8:
```bash
flake8 myllm/
```

### Type Hints

Use type hints for function parameters and return values:

```python
def load_model(
    model_path: str,
    identifier: Optional[str] = None,
    gpu_layers: Optional[int] = None
) -> Dict[str, Any]:
    ...
```

### Testing

Write tests for new features:

```python
# tests/test_models.py
def test_list_models():
    models = model_manager.list_models()
    assert isinstance(models, list)
```

Run tests:
```bash
pytest tests/
```

## Submitting Changes

### Pull Request Process

1. Create a new branch
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit
```bash
git add .
git commit -m "Add: brief description of changes"
```

3. Push to your fork
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request with:
   - Clear description of changes
   - Any related issue numbers
   - Screenshots (if applicable)

### Commit Message Format

Use clear, descriptive commit messages:

- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for changes to existing features
- `Refactor:` for code improvements
- `Docs:` for documentation changes

Examples:
```
Add: streaming support for chat responses
Fix: server not stopping properly on Windows
Update: improve error messages for model loading
Docs: add examples for API usage
```

## Areas for Contribution

### High Priority

- [ ] Add comprehensive test suite
- [ ] Improve error handling and messages
- [ ] Add streaming support for responses
- [ ] Better GPU memory management
- [ ] Model quantization support

### Features

- [ ] Model search and download from Hugging Face
- [ ] Conversation history export/import
- [ ] Multiple model backends (besides llama-cpp)
- [ ] Web UI for easier interaction
- [ ] Plugin system for extensions

### Documentation

- [ ] Video tutorials
- [ ] More usage examples
- [ ] API documentation
- [ ] Troubleshooting guide
- [ ] Performance optimization guide

### Platform Support

- [ ] macOS M1/M2 optimization
- [ ] ARM Linux support
- [ ] Docker container
- [ ] Windows installer

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn

## Questions?

- Open an issue for questions
- Check existing issues and PRs first
- Be specific about your environment and issue

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You!

Every contribution helps make MyLLM CLI better for everyone. Thank you for taking the time to contribute!
