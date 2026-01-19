"""Configuration management for MyLLM CLI"""

import os
import json
from pathlib import Path
from typing import Optional, Dict, Any

class Config:
    """Manages configuration for MyLLM CLI"""

    def __init__(self):
        self.config_dir = Path.home() / ".myllm"
        self.config_file = self.config_dir / "config.json"
        self.models_file = self.config_dir / "models.json"
        self.server_file = self.config_dir / "server.json"

        # Create config directory if it doesn't exist
        self.config_dir.mkdir(exist_ok=True)

        # Load or create default config
        self.config = self._load_config()
        self.models_state = self._load_models_state()
        self.server_state = self._load_server_state()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        else:
            # Default configuration
            default_config = {
                "models_directory": str(Path.home() / "models"),
                "server": {
                    "host": "127.0.0.1",
                    "port": 8080
                },
                "default_model_params": {
                    "gpu_layers": -1,  # -1 means offload all layers to GPU
                    "context_length": 2048,
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "max_tokens": 512
                }
            }
            self._save_config(default_config)
            return default_config

    def _save_config(self, config: Dict[str, Any]):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)

    def _load_models_state(self) -> Dict[str, Any]:
        """Load models state (loaded models)"""
        if self.models_file.exists():
            with open(self.models_file, 'r') as f:
                return json.load(f)
        return {"loaded_models": []}

    def _save_models_state(self):
        """Save models state to file"""
        with open(self.models_file, 'w') as f:
            json.dump(self.models_state, f, indent=2)

    def _load_server_state(self) -> Dict[str, Any]:
        """Load server state"""
        if self.server_file.exists():
            with open(self.server_file, 'r') as f:
                return json.load(f)
        return {"running": False, "pid": None, "port": None}

    def _save_server_state(self):
        """Save server state to file"""
        with open(self.server_file, 'w') as f:
            json.dump(self.server_state, f, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    def set(self, key: str, value: Any):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self._save_config(self.config)

    def add_loaded_model(self, model_info: Dict[str, Any]):
        """Add a loaded model to the state"""
        self.models_state["loaded_models"].append(model_info)
        self._save_models_state()

    def remove_loaded_model(self, identifier: str):
        """Remove a loaded model from the state"""
        self.models_state["loaded_models"] = [
            m for m in self.models_state["loaded_models"]
            if m.get("identifier") != identifier
        ]
        self._save_models_state()

    def get_loaded_models(self):
        """Get list of loaded models"""
        return self.models_state.get("loaded_models", [])

    def clear_loaded_models(self):
        """Clear all loaded models"""
        self.models_state["loaded_models"] = []
        self._save_models_state()

    def set_server_running(self, running: bool, pid: Optional[int] = None, port: Optional[int] = None):
        """Update server state"""
        self.server_state["running"] = running
        self.server_state["pid"] = pid
        self.server_state["port"] = port
        self._save_server_state()

    def is_server_running(self) -> bool:
        """Check if server is running"""
        return self.server_state.get("running", False)


# Global config instance
config = Config()
