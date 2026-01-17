from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.live import Live
from rich.rule import Rule
import time

console = Console()


def print_status(message, style="white"):
    """print status messages with style"""
    console.print(f"[{style}][[DeepSeek]][/{style}] {message}", justify="left")


def print_response_start():
    """show when response starts"""
    console.print()
    console.print(Rule("[bold cyan]Response[/bold cyan]", style="cyan", align="left"))
    console.print()


def stream_live(content_generator, thinking_enabled=False):
    """stream content live as it comes in with markdown rendering, separating thinking from response"""
    thinking_content = ""
    response_content = ""
    from rich.console import Group

    # create panels that update live
    with Live(console=console, refresh_per_second=10) as live:
        for item in content_generator:
            if item:
                # Handle tuple format (type, content)
                if isinstance(item, tuple):
                    fragment_type, chunk = item
                else:
                    # Fallback for old format
                    fragment_type, chunk = "RESPONSE", item

                if fragment_type == "THINK":
                    thinking_content += chunk
                else:
                    response_content += chunk

                # Build the display
                panels = []

                # Show thinking panel if we have thinking content and thinking is enabled
                if thinking_content and thinking_enabled:
                    think_md = Markdown(
                        thinking_content, code_theme="monokai", justify="left"
                    )
                    think_panel = Panel(
                        think_md,
                        border_style="yellow",
                        padding=(1, 2),
                        title="[bold yellow]💭 Thinking[/bold yellow]",
                        title_align="left",
                        subtitle="[dim]razonamiento interno[/dim]",
                        subtitle_align="right",
                    )
                    panels.append(think_panel)

                # Always show response panel (even if empty during thinking to maintain layout)
                resp_md = Markdown(
                    response_content if response_content else "...",
                    code_theme="monokai",
                    justify="left",
                )
                resp_panel = Panel(
                    resp_md,
                    border_style="bright_cyan",
                    padding=(1, 2),
                    title="[bold white]✨ DeepSeek[/bold white]",
                    title_align="left",
                )
                # Only add response panel if we have content or if thinking just finished
                if response_content or not thinking_content:
                    panels.append(resp_panel)

                if panels:
                    live.update(Group(*panels))

    return response_content


def get_user_input(prompt_text="You"):
    """get input from user with nice prompt"""
    return Prompt.ask(f"\n[bold green]{prompt_text}[/bold green]")


def print_goodbye():
    """say goodbye when exiting"""
    console.print("\n[yellow]Goodbye![/yellow]\n", justify="left")
