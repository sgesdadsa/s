"""Model management functionality"""

import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from llama_cpp import Llama

from .config import config


class ModelManager:
    """Manages local LLM models"""

    def __init__(self):
        self.loaded_models: Dict[str, Llama] = {}

    def list_models(self) -> List[Dict[str, Any]]:
        """List all available models in the models directory"""
        models_dir = Path(config.get("models_directory"))

        if not models_dir.exists():
            return []

        models = []
        # Search for GGUF files recursively
        for model_file in models_dir.rglob("*.gguf"):
            # Also check for .bin files (older format)
            stat = model_file.stat()
            models.append({
                "name": model_file.stem,
                "path": str(model_file),
                "size": self._format_size(stat.st_size),
                "size_bytes": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "directory": str(model_file.parent.relative_to(models_dir))
            })

        # Also check for .bin files
        for model_file in models_dir.rglob("*.bin"):
            if "ggml" in model_file.name.lower() or "gguf" in model_file.name.lower():
                stat = model_file.stat()
                models.append({
                    "name": model_file.stem,
                    "path": str(model_file),
                    "size": self._format_size(stat.st_size),
                    "size_bytes": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                    "directory": str(model_file.parent.relative_to(models_dir))
                })

        return sorted(models, key=lambda x: x["modified"], reverse=True)

    def _format_size(self, size_bytes: int) -> str:
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"

    def load_model(
        self,
        model_path: str,
        identifier: Optional[str] = None,
        gpu_layers: Optional[int] = None,
        context_length: Optional[int] = None
    ) -> Dict[str, Any]:
        """Load a model into memory"""

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")

        # Use filename as identifier if not provided
        if identifier is None:
            identifier = Path(model_path).stem

        # Check if model is already loaded
        if identifier in self.loaded_models:
            raise ValueError(f"Model '{identifier}' is already loaded")

        # Get default parameters from config
        if gpu_layers is None:
            gpu_layers = config.get("default_model_params.gpu_layers", -1)
        if context_length is None:
            context_length = config.get("default_model_params.context_length", 2048)

        try:
            # Load the model
            llm = Llama(
                model_path=model_path,
                n_ctx=context_length,
                n_gpu_layers=gpu_layers,
                verbose=False
            )

            self.loaded_models[identifier] = llm

            # Save to config
            model_info = {
                "identifier": identifier,
                "path": model_path,
                "gpu_layers": gpu_layers,
                "context_length": context_length,
                "loaded_at": datetime.now().isoformat()
            }
            config.add_loaded_model(model_info)

            return model_info

        except Exception as e:
            raise Exception(f"Failed to load model: {str(e)}")

    def unload_model(self, identifier: str):
        """Unload a model from memory"""
        if identifier not in self.loaded_models:
            raise ValueError(f"Model '{identifier}' is not loaded")

        # Remove from memory
        del self.loaded_models[identifier]

        # Remove from config
        config.remove_loaded_model(identifier)

    def unload_all(self):
        """Unload all models"""
        self.loaded_models.clear()
        config.clear_loaded_models()

    def get_loaded_models(self) -> List[Dict[str, Any]]:
        """Get list of currently loaded models"""
        return config.get_loaded_models()

    def get_model(self, identifier: str) -> Optional[Llama]:
        """Get a loaded model by identifier"""
        return self.loaded_models.get(identifier)

    def find_model_path(self, model_name: str) -> Optional[str]:
        """Find a model path by name"""
        models = self.list_models()
        for model in models:
            if model["name"] == model_name or model_name in model["path"]:
                return model["path"]
        return None


# Global model manager instance
model_manager = ModelManager()
