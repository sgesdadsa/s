"""Main CLI interface for MyLLM"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from tabulate import tabulate

from .config import config
from .models import model_manager
from .chat import start_interactive_chat
from .server import start_server_process, stop_server_process
from .studio_cli import studio

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """
    MyLLM CLI - Command-line tool for managing and interacting with local LLM models

    \b
    Local Models:
      ls        List available models
      load      Load a model into memory
      unload    Unload a model from memory
      ps        List currently loaded models
      chat      Start an interactive chat session

    \b
    Server:
      server    Manage the local API server

    \b
    Visual Studio:
      studio    Launch MyLLM Studio (Visual Interface)

    \b
    Configuration:
      config    Manage configuration settings
    """
    pass


# Add studio command group
cli.add_command(studio)


# ==================== MODEL COMMANDS ====================

@cli.command()
def ls():
    """List all available models in the models directory"""
    models = model_manager.list_models()

    if not models:
        console.print("[yellow]No models found in the models directory.[/yellow]")
        console.print(f"Models directory: {config.get('models_directory')}")
        console.print("\nAdd .gguf model files to this directory.")
        return

    # Create table
    table = Table(title="Available Models", show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan", no_wrap=False)
    table.add_column("Size", style="green")
    table.add_column("Modified", style="yellow")
    table.add_column("Directory", style="blue")

    for model in models:
        table.add_row(
            model["name"],
            model["size"],
            model["modified"],
            model["directory"]
        )

    console.print(table)
    console.print(f"\n[dim]Total: {len(models)} model(s)[/dim]")
    console.print(f"[dim]Models directory: {config.get('models_directory')}[/dim]")


@cli.command()
@click.argument("model_path")
@click.option("--identifier", "-i", help="Custom identifier for the model")
@click.option("--gpu", "-g", type=float, help="GPU offload percentage (0.0-1.0) or 'max' for full offload")
@click.option("--context-length", "-c", type=int, help="Context window size")
def load(model_path, identifier, gpu, context_length):
    """Load a model into memory

    MODEL_PATH can be:
    - Full path to a .gguf file
    - Model name from 'myllm ls'
    - Relative path from models directory
    """

    # Try to find the model if not a full path
    if not model_path.endswith(".gguf") and not model_path.endswith(".bin"):
        found_path = model_manager.find_model_path(model_path)
        if found_path:
            model_path = found_path
        else:
            console.print(f"[red]Model not found: {model_path}[/red]")
            console.print("\nAvailable models:")
            models = model_manager.list_models()
            for model in models[:5]:
                console.print(f"  - {model['name']}")
            return

    # Convert GPU percentage to layers
    gpu_layers = None
    if gpu is not None:
        if gpu == 1.0 or str(gpu).lower() == "max":
            gpu_layers = -1  # All layers
        else:
            gpu_layers = int(gpu * 100)  # Approximate

    try:
        with console.status("[bold green]Loading model...", spinner="dots"):
            model_info = model_manager.load_model(
                model_path=model_path,
                identifier=identifier,
                gpu_layers=gpu_layers,
                context_length=context_length
            )

        console.print(Panel.fit(
            f"[bold green]✓ Model loaded successfully[/bold green]\n\n"
            f"Identifier: {model_info['identifier']}\n"
            f"Path: {model_info['path']}\n"
            f"GPU Layers: {model_info['gpu_layers']}\n"
            f"Context Length: {model_info['context_length']}",
            title="Model Loaded",
            border_style="green"
        ))

    except Exception as e:
        console.print(f"[red]✗ Failed to load model: {str(e)}[/red]")


@cli.command()
@click.argument("identifier", required=False)
@click.option("--all", "-a", is_flag=True, help="Unload all models")
def unload(identifier, all):
    """Unload a model from memory"""

    if all:
        loaded = model_manager.get_loaded_models()
        if not loaded:
            console.print("[yellow]No models are loaded.[/yellow]")
            return

        model_manager.unload_all()
        console.print(f"[green]✓ Unloaded {len(loaded)} model(s)[/green]")
        return

    if not identifier:
        console.print("[red]Please specify a model identifier or use --all[/red]")
        return

    try:
        model_manager.unload_model(identifier)
        console.print(f"[green]✓ Model '{identifier}' unloaded successfully[/green]")
    except Exception as e:
        console.print(f"[red]✗ Failed to unload model: {str(e)}[/red]")


@cli.command()
def ps():
    """List currently loaded models"""
    loaded_models = model_manager.get_loaded_models()

    if not loaded_models:
        console.print("[yellow]No models are currently loaded.[/yellow]")
        console.print("\nLoad a model with: [cyan]myllm load <model>[/cyan]")
        return

    # Create table
    table = Table(title="Loaded Models", show_header=True, header_style="bold magenta")
    table.add_column("Identifier", style="cyan")
    table.add_column("GPU Layers", style="green")
    table.add_column("Context", style="yellow")
    table.add_column("Loaded At", style="blue")

    for model in loaded_models:
        table.add_row(
            model["identifier"],
            str(model["gpu_layers"]),
            str(model["context_length"]),
            model["loaded_at"]
        )

    console.print(table)
    console.print(f"\n[dim]Total: {len(loaded_models)} model(s) loaded[/dim]")


@cli.command()
@click.argument("model", required=False)
def chat(model):
    """Start an interactive chat session

    MODEL is optional. If not specified, uses the first loaded model.
    """
    try:
        start_interactive_chat(model)
    except KeyboardInterrupt:
        console.print("\n[yellow]Chat session ended.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


# ==================== SERVER COMMANDS ====================

@cli.group()
def server():
    """Manage the local API server"""
    pass


@server.command()
@click.option("--host", "-h", default=None, help="Host address")
@click.option("--port", "-p", type=int, default=None, help="Port number")
def start(host, port):
    """Start the API server"""

    # Update config if provided
    if host:
        config.set("server.host", host)
    if port:
        config.set("server.port", port)

    success, message = start_server_process()

    if success:
        console.print(f"[green]✓ {message}[/green]")
        console.print(f"\nAPI Endpoints:")
        console.print(f"  - Chat: http://{config.get('server.host')}:{config.get('server.port')}/v1/chat/completions")
        console.print(f"  - Completions: http://{config.get('server.host')}:{config.get('server.port')}/v1/completions")
        console.print(f"  - Models: http://{config.get('server.host')}:{config.get('server.port')}/v1/models")
    else:
        console.print(f"[red]✗ {message}[/red]")


@server.command()
def stop():
    """Stop the API server"""
    success, message = stop_server_process()

    if success:
        console.print(f"[green]✓ {message}[/green]")
    else:
        console.print(f"[yellow]{message}[/yellow]")


@server.command()
def status():
    """Check server status"""
    if config.is_server_running():
        console.print("[green]● Server is running[/green]")
        console.print(f"  PID: {config.server_state.get('pid')}")
        console.print(f"  Port: {config.server_state.get('port')}")
        console.print(f"  URL: http://{config.get('server.host')}:{config.get('server.port')}")
    else:
        console.print("[red]● Server is not running[/red]")


# ==================== CONFIG COMMANDS ====================

@cli.group()
def config_group():
    """Manage configuration settings"""
    pass


# Register as 'config' command
cli.add_command(config_group, name="config")


@config_group.command(name="show")
def config_show():
    """Show current configuration"""
    console.print(Panel.fit(
        f"Models Directory: {config.get('models_directory')}\n"
        f"Server Host: {config.get('server.host')}\n"
        f"Server Port: {config.get('server.port')}\n"
        f"Default GPU Layers: {config.get('default_model_params.gpu_layers')}\n"
        f"Default Context Length: {config.get('default_model_params.context_length')}\n"
        f"Default Temperature: {config.get('default_model_params.temperature')}\n"
        f"Default Max Tokens: {config.get('default_model_params.max_tokens')}",
        title="Configuration",
        border_style="blue"
    ))
    console.print(f"\n[dim]Config file: {config.config_file}[/dim]")


@config_group.command(name="set")
@click.argument("key")
@click.argument("value")
def config_set(key, value):
    """Set a configuration value

    Examples:
      myllm config set models_directory /path/to/models
      myllm config set server.port 8080
    """
    try:
        # Try to convert to int or float if possible
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass  # Keep as string

        config.set(key, value)
        console.print(f"[green]✓ Configuration updated: {key} = {value}[/green]")
    except Exception as e:
        console.print(f"[red]✗ Failed to update configuration: {str(e)}[/red]")


@config_group.command(name="get")
@click.argument("key")
def config_get(key):
    """Get a configuration value"""
    value = config.get(key)
    if value is not None:
        console.print(f"{key} = {value}")
    else:
        console.print(f"[yellow]Configuration key not found: {key}[/yellow]")


if __name__ == "__main__":
    cli()
