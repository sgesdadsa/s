"""Interactive chat functionality"""

from typing import Optional, List, Dict
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt

from .models import model_manager
from .config import config

console = Console()


class ChatSession:
    """Manages an interactive chat session"""

    def __init__(self, model_identifier: str):
        self.model_identifier = model_identifier
        self.model = model_manager.get_model(model_identifier)

        if self.model is None:
            raise ValueError(f"Model '{model_identifier}' is not loaded")

        self.history: List[Dict[str, str]] = []
        self.system_prompt = "You are a helpful AI assistant."

    def chat(self, user_message: str) -> str:
        """Send a message and get a response"""

        # Build the prompt with history
        prompt = self._build_prompt(user_message)

        # Get model parameters from config
        temperature = config.get("default_model_params.temperature", 0.7)
        top_p = config.get("default_model_params.top_p", 0.9)
        max_tokens = config.get("default_model_params.max_tokens", 512)

        # Generate response
        response = self.model(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            echo=False,
            stop=["User:", "Assistant:", "\n\n\n"]
        )

        assistant_message = response["choices"][0]["text"].strip()

        # Add to history
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    def _build_prompt(self, user_message: str) -> str:
        """Build the full prompt with history"""
        prompt_parts = [f"System: {self.system_prompt}\n"]

        # Add conversation history
        for msg in self.history[-6:]:  # Keep last 3 exchanges
            role = msg["role"].capitalize()
            content = msg["content"]
            prompt_parts.append(f"{role}: {content}\n")

        # Add current user message
        prompt_parts.append(f"User: {user_message}\nAssistant:")

        return "\n".join(prompt_parts)

    def set_system_prompt(self, prompt: str):
        """Set the system prompt"""
        self.system_prompt = prompt

    def clear_history(self):
        """Clear conversation history"""
        self.history = []


def start_interactive_chat(model_identifier: Optional[str] = None):
    """Start an interactive chat session"""

    # If no model specified, check if any model is loaded
    if model_identifier is None:
        loaded_models = model_manager.get_loaded_models()
        if not loaded_models:
            console.print("[red]No models are loaded. Please load a model first with 'myllm load <model>'[/red]")
            return
        model_identifier = loaded_models[0]["identifier"]
        console.print(f"[yellow]Using model: {model_identifier}[/yellow]")

    try:
        session = ChatSession(model_identifier)

        console.print(Panel.fit(
            "[bold green]Chat Session Started[/bold green]\n\n"
            f"Model: {model_identifier}\n"
            "Type your message and press Enter to chat.\n"
            "Commands:\n"
            "  /clear  - Clear conversation history\n"
            "  /system <prompt> - Set system prompt\n"
            "  /exit or /quit - Exit chat",
            title="MyLLM Chat",
            border_style="green"
        ))

        while True:
            try:
                # Get user input
                user_input = Prompt.ask("\n[bold cyan]You[/bold cyan]")

                if not user_input.strip():
                    continue

                # Handle commands
                if user_input.startswith("/"):
                    command = user_input.lower().strip()

                    if command in ["/exit", "/quit"]:
                        console.print("[yellow]Exiting chat...[/yellow]")
                        break

                    elif command == "/clear":
                        session.clear_history()
                        console.print("[green]Conversation history cleared.[/green]")
                        continue

                    elif command.startswith("/system "):
                        new_prompt = user_input[8:].strip()
                        session.set_system_prompt(new_prompt)
                        console.print(f"[green]System prompt updated: {new_prompt}[/green]")
                        continue

                    else:
                        console.print("[red]Unknown command. Available commands: /clear, /system, /exit, /quit[/red]")
                        continue

                # Generate response
                console.print("\n[bold magenta]Assistant[/bold magenta]")
                with console.status("[bold green]Thinking...", spinner="dots"):
                    response = session.chat(user_input)

                # Display response as markdown
                console.print(Markdown(response))

            except KeyboardInterrupt:
                console.print("\n[yellow]Chat interrupted. Type /exit to quit.[/yellow]")
                continue

            except Exception as e:
                console.print(f"[red]Error: {str(e)}[/red]")
                continue

    except Exception as e:
        console.print(f"[red]Failed to start chat: {str(e)}[/red]")
