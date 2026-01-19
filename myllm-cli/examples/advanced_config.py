"""
Advanced Configuration Example for MyLLM

This shows how to programmatically configure and manage MyLLM
"""

import json
from pathlib import Path

# Configuration file location
CONFIG_DIR = Path.home() / ".myllm"
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config():
    """Load current configuration"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_config(config):
    """Save configuration"""
    CONFIG_DIR.mkdir(exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


def setup_advanced_config():
    """Set up advanced configuration"""

    config = {
        # Models directory (where .gguf files are stored)
        "models_directory": str(Path.home() / "models"),

        # Server configuration
        "server": {
            "host": "0.0.0.0",  # Listen on all interfaces
            "port": 8080
        },

        # Default model parameters
        "default_model_params": {
            "gpu_layers": -1,  # -1 = offload all layers to GPU
            "context_length": 4096,  # Larger context window
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40,
            "max_tokens": 1024,
            "repeat_penalty": 1.1
        },

        # Chat settings
        "chat": {
            "system_prompt": "You are a helpful, creative, and intelligent AI assistant.",
            "max_history": 10,  # Number of message pairs to keep in history
            "streaming": True,  # Enable streaming responses
        },

        # Model presets (quick configurations for different use cases)
        "presets": {
            "creative": {
                "temperature": 0.9,
                "top_p": 0.95,
                "repeat_penalty": 1.05
            },
            "precise": {
                "temperature": 0.3,
                "top_p": 0.85,
                "repeat_penalty": 1.15
            },
            "balanced": {
                "temperature": 0.7,
                "top_p": 0.9,
                "repeat_penalty": 1.1
            },
            "coding": {
                "temperature": 0.2,
                "top_p": 0.95,
                "repeat_penalty": 1.0
            }
        },

        # Advanced settings
        "advanced": {
            "verbose": False,
            "threads": 8,  # Number of CPU threads
            "batch_size": 512,
            "rope_freq_base": 10000.0,
            "rope_freq_scale": 1.0
        }
    }

    return config


def apply_preset(preset_name):
    """Apply a configuration preset"""
    config = load_config()

    if "presets" not in config or preset_name not in config["presets"]:
        print(f"Preset '{preset_name}' not found")
        return False

    preset = config["presets"][preset_name]

    # Update default parameters with preset
    for key, value in preset.items():
        config["default_model_params"][key] = value

    save_config(config)
    print(f"Applied preset: {preset_name}")
    return True


def show_config():
    """Display current configuration"""
    config = load_config()
    print("Current Configuration:")
    print(json.dumps(config, indent=2))


def example_custom_setup():
    """Example: Custom setup for specific hardware"""

    config = load_config()

    # Example 1: Low VRAM GPU (6GB)
    low_vram_config = {
        "gpu_layers": 20,  # Only offload 20 layers
        "context_length": 2048,  # Smaller context
        "batch_size": 256  # Smaller batch size
    }

    # Example 2: High-end GPU (24GB+)
    high_vram_config = {
        "gpu_layers": -1,  # All layers
        "context_length": 8192,  # Large context
        "batch_size": 512  # Larger batch
    }

    # Example 3: CPU only (no GPU)
    cpu_only_config = {
        "gpu_layers": 0,  # No GPU offload
        "context_length": 2048,
        "threads": 16  # Use more CPU threads
    }

    print("Custom configuration examples created")
    print("Choose one based on your hardware:")
    print("  - Low VRAM GPU: gpu_layers=20, context=2048")
    print("  - High VRAM GPU: gpu_layers=-1, context=8192")
    print("  - CPU Only: gpu_layers=0, threads=16")


def main():
    """Main function"""
    print("=" * 50)
    print("MyLLM Advanced Configuration")
    print("=" * 50)
    print()

    # Set up advanced configuration
    print("Setting up advanced configuration...")
    config = setup_advanced_config()
    save_config(config)
    print("Configuration saved to:", CONFIG_FILE)
    print()

    # Show configuration
    print("Current configuration:")
    print(json.dumps(config, indent=2))
    print()

    # Show custom examples
    print("=" * 50)
    print("Hardware-Specific Examples")
    print("=" * 50)
    example_custom_setup()
    print()

    # Show how to use presets
    print("=" * 50)
    print("Available Presets")
    print("=" * 50)
    print("You can apply presets using:")
    print("  apply_preset('creative')  - For creative writing")
    print("  apply_preset('precise')   - For factual answers")
    print("  apply_preset('balanced')  - For general use")
    print("  apply_preset('coding')    - For code generation")
    print()

    # Tips
    print("=" * 50)
    print("Configuration Tips")
    print("=" * 50)
    print("1. GPU Layers:")
    print("   - -1: Offload all layers (fastest)")
    print("   - 0: CPU only")
    print("   - 1-N: Offload N layers")
    print()
    print("2. Context Length:")
    print("   - 2048: Standard (less memory)")
    print("   - 4096: Large (more memory)")
    print("   - 8192+: Very large (lots of memory needed)")
    print()
    print("3. Temperature:")
    print("   - 0.1-0.3: Focused, deterministic")
    print("   - 0.5-0.7: Balanced")
    print("   - 0.8-1.0: Creative, diverse")
    print()


if __name__ == "__main__":
    main()
