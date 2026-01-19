"""Local API server for serving models"""

import os
import signal
import subprocess
import sys
from pathlib import Path
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from .models import model_manager
from .config import config


# API Models
class ChatRequest(BaseModel):
    model: str
    messages: List[dict]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 512
    top_p: Optional[float] = 0.9


class ChatResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[dict]
    usage: dict


class CompletionRequest(BaseModel):
    model: str
    prompt: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 512
    top_p: Optional[float] = 0.9


class ModelInfo(BaseModel):
    id: str
    object: str
    owned_by: str


# Create FastAPI app
app = FastAPI(title="MyLLM API", version="0.1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "MyLLM API Server",
        "version": "0.1.0",
        "endpoints": {
            "models": "/v1/models",
            "chat": "/v1/chat/completions",
            "completions": "/v1/completions"
        }
    }


@app.get("/v1/models")
async def list_models():
    """List available models (OpenAI-compatible)"""
    loaded_models = model_manager.get_loaded_models()

    models = [
        {
            "id": model["identifier"],
            "object": "model",
            "owned_by": "user",
            "permission": []
        }
        for model in loaded_models
    ]

    return {"object": "list", "data": models}


@app.post("/v1/chat/completions")
async def chat_completions(request: ChatRequest):
    """Chat completions endpoint (OpenAI-compatible)"""
    import time

    # Get the model
    model = model_manager.get_model(request.model)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Model '{request.model}' not found or not loaded")

    # Build prompt from messages
    prompt_parts = []
    for msg in request.messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        prompt_parts.append(f"{role.capitalize()}: {content}")

    prompt = "\n".join(prompt_parts) + "\nAssistant:"

    # Generate response
    try:
        response = model(
            prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            echo=False
        )

        # Format response in OpenAI format
        return {
            "id": f"chatcmpl-{int(time.time())}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": request.model,
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": response["choices"][0]["text"].strip()
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": response["usage"]["prompt_tokens"],
                "completion_tokens": response["usage"]["completion_tokens"],
                "total_tokens": response["usage"]["total_tokens"]
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/v1/completions")
async def completions(request: CompletionRequest):
    """Text completions endpoint (OpenAI-compatible)"""
    import time

    # Get the model
    model = model_manager.get_model(request.model)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Model '{request.model}' not found or not loaded")

    # Generate response
    try:
        response = model(
            request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            echo=False
        )

        # Format response in OpenAI format
        return {
            "id": f"cmpl-{int(time.time())}",
            "object": "text_completion",
            "created": int(time.time()),
            "model": request.model,
            "choices": [
                {
                    "text": response["choices"][0]["text"],
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": response["usage"]["prompt_tokens"],
                "completion_tokens": response["usage"]["completion_tokens"],
                "total_tokens": response["usage"]["total_tokens"]
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def start_server_process():
    """Start the server in a background process"""
    host = config.get("server.host", "127.0.0.1")
    port = config.get("server.port", 8080)

    # Check if server is already running
    if config.is_server_running():
        return False, "Server is already running"

    # Start server in background
    python_path = sys.executable
    script_path = Path(__file__).resolve()

    # Create a subprocess to run the server
    process = subprocess.Popen(
        [python_path, "-c", f"from myllm.server import run_server; run_server('{host}', {port})"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

    # Update config
    config.set_server_running(True, process.pid, port)

    return True, f"Server started on {host}:{port} (PID: {process.pid})"


def stop_server_process():
    """Stop the server process"""
    if not config.is_server_running():
        return False, "Server is not running"

    pid = config.server_state.get("pid")
    if pid:
        try:
            os.kill(pid, signal.SIGTERM)
            config.set_server_running(False)
            return True, "Server stopped successfully"
        except ProcessLookupError:
            config.set_server_running(False)
            return False, "Server process not found (may have already stopped)"
        except Exception as e:
            return False, f"Error stopping server: {str(e)}"

    return False, "Server PID not found"


def run_server(host: str = "127.0.0.1", port: int = 8080):
    """Run the server (called by subprocess)"""
    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    # Run server directly
    host = config.get("server.host", "127.0.0.1")
    port = config.get("server.port", 8080)
    run_server(host, port)
