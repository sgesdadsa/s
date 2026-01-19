"""
MyLLM Studio CLI Commands
Commands for launching and managing the visual studio
"""

import click
import subprocess
import sys
import os
from pathlib import Path


@click.group()
def studio():
    """Launch MyLLM Studio - Visual Interface"""
    pass


@studio.command()
@click.option('--port', '-p', default=8090, help='Port to run on')
@click.option('--host', '-h', default='0.0.0.0', help='Host to bind to')
@click.option('--browser/--no-browser', default=True, help='Open browser automatically')
def start(port, host, browser):
    """Start MyLLM Studio web interface"""
    import uvicorn
    from rich.console import Console

    console = Console()

    console.print(f"\n[bold green]🚀 Starting MyLLM Studio...[/bold green]\n")
    console.print(f"  Host: [cyan]{host}[/cyan]")
    console.print(f"  Port: [cyan]{port}[/cyan]")
    console.print(f"  URL:  [cyan]http://{'localhost' if host == '0.0.0.0' else host}:{port}[/cyan]\n")

    if browser:
        import webbrowser
        import threading

        def open_browser():
            import time
            time.sleep(1.5)  # Wait for server to start
            webbrowser.open(f"http://localhost:{port}")

        threading.Thread(target=open_browser, daemon=True).start()

    # Start server
    from .studio_server import app
    uvicorn.run(app, host=host, port=port, log_level="info")


@studio.command()
def build():
    """Build MyLLM Studio as standalone executable"""
    from rich.console import Console
    from rich.progress import Progress

    console = Console()

    console.print("\n[bold cyan]🔨 Building MyLLM Studio Executable...[/bold cyan]\n")

    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        console.print("[red]❌ PyInstaller not installed![/red]")
        console.print("\nInstall with: [cyan]pip install pyinstaller[/cyan]\n")
        return

    # Build command
    script_path = Path(__file__).parent / "studio_server.py"
    build_cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "MyLLM-Studio",
        "--icon", "NONE",
        "--add-data", f"{Path(__file__).parent}:myllm",
        str(script_path)
    ]

    console.print(f"[yellow]Building...[/yellow]")

    try:
        result = subprocess.run(build_cmd, capture_output=True, text=True)

        if result.returncode == 0:
            console.print("\n[bold green]✓ Build successful![/bold green]")
            console.print(f"\nExecutable location:")
            console.print(f"  [cyan]dist/MyLLM-Studio[.exe][/cyan]\n")
        else:
            console.print("\n[bold red]✗ Build failed![/bold red]")
            console.print(f"\n{result.stderr}\n")

    except Exception as e:
        console.print(f"\n[bold red]✗ Error: {e}[/bold red]\n")


@studio.command()
def desktop():
    """Create desktop shortcut for MyLLM Studio"""
    from rich.console import Console
    import platform

    console = Console()
    system = platform.system()

    console.print("\n[bold cyan]🖥️ Creating Desktop Shortcut...[/bold cyan]\n")

    if system == "Windows":
        create_windows_shortcut(console)
    elif system == "Darwin":
        create_mac_app(console)
    elif system == "Linux":
        create_linux_desktop(console)
    else:
        console.print(f"[red]❌ Unsupported platform: {system}[/red]\n")


def create_windows_shortcut(console):
    """Create Windows shortcut"""
    try:
        from pathlib import Path
        import os

        # Create batch file
        desktop = Path.home() / "Desktop"
        batch_file = desktop / "MyLLM Studio.bat"

        python_exe = sys.executable
        script_content = f'''@echo off
title MyLLM Studio
echo Starting MyLLM Studio...
"{python_exe}" -m myllm.studio_cli start
pause
'''

        with open(batch_file, 'w') as f:
            f.write(script_content)

        console.print(f"[green]✓ Shortcut created![/green]")
        console.print(f"  Location: [cyan]{batch_file}[/cyan]\n")

    except Exception as e:
        console.print(f"[red]✗ Error: {e}[/red]\n")


def create_mac_app(console):
    """Create macOS app"""
    console.print("[yellow]macOS app creation coming soon![/yellow]\n")
    console.print("For now, run: [cyan]python -m myllm.studio_cli start[/cyan]\n")


def create_linux_desktop(console):
    """Create Linux desktop entry"""
    try:
        from pathlib import Path

        desktop_file = Path.home() / ".local" / "share" / "applications" / "myllm-studio.desktop"
        desktop_file.parent.mkdir(parents=True, exist_ok=True)

        python_exe = sys.executable
        content = f'''[Desktop Entry]
Type=Application
Name=MyLLM Studio
Comment=Visual interface for MyLLM
Exec={python_exe} -m myllm.studio_cli start
Terminal=false
Categories=Development;
'''

        with open(desktop_file, 'w') as f:
            f.write(content)

        console.print(f"[green]✓ Desktop entry created![/green]")
        console.print(f"  Location: [cyan]{desktop_file}[/cyan]\n")

    except Exception as e:
        console.print(f"[red]✗ Error: {e}[/red]\n")


if __name__ == "__main__":
    studio()
