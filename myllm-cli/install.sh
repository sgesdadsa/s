#!/bin/bash

# MyLLM CLI Installation Script for Linux/Mac

echo "================================"
echo "MyLLM CLI Installation"
echo "================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
required_version="3.8"

if [ -z "$python_version" ]; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher."
    exit 1
fi

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "Error: Python $python_version is installed, but Python $required_version or higher is required."
    exit 1
fi

echo "✓ Python $python_version found"
echo ""

# Check if pip is installed
echo "Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed."
    echo "Please install pip3 first."
    exit 1
fi

echo "✓ pip3 found"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies."
    exit 1
fi

echo "✓ Dependencies installed"
echo ""

# Install MyLLM CLI
echo "Installing MyLLM CLI..."
pip3 install -e .

if [ $? -ne 0 ]; then
    echo "Error: Failed to install MyLLM CLI."
    exit 1
fi

echo "✓ MyLLM CLI installed"
echo ""

# Test installation
echo "Testing installation..."
if myllm --version &> /dev/null; then
    echo "✓ Installation successful!"
else
    echo "⚠ Installation may be incomplete."
    echo "Try running: myllm --help"
fi

echo ""
echo "================================"
echo "Installation Complete!"
echo "================================"
echo ""
echo "Quick Start:"
echo "  1. Set your models directory:"
echo "     myllm config set models_directory /path/to/models"
echo ""
echo "  2. List available models:"
echo "     myllm ls"
echo ""
echo "  3. Load a model:"
echo "     myllm load <model-name>"
echo ""
echo "  4. Start chatting:"
echo "     myllm chat"
echo ""
echo "For more information, run: myllm --help"
echo ""
