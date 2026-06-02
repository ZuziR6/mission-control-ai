"""
Interface CLI Mission Control AI
"""

from rich.console import Console
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from datetime import datetime
import pyfiglet

console = Console()

session = PromptSession(
    style=Style.from_dict(
        {
            "prompt": "#06B6D4 bold"
        }
    )
)


def show_banner():

    banner = pyfiglet.figlet_format(
        "Mission Control",
        font="slant"
    )

    console.print(
        f"[bold cyan]{banner}[/bold cyan]"
    )

    console.print(
        Panel.fit(
            "EnviroSat - Monitoramento Ambiental\n"
            "Use /help para ajuda\n"
            "Use /exit para sair",
            title="MISSION CONTROL AI"
        )
    )


def show_response(text):

    horario = datetime.now().strftime("%H:%M:%S")

    console.print(
        Panel(
            text,
            title="Mission Control",
            subtitle=horario
        )
    )


def run_cli(engine):

    show_banner()

    if engine.is_ready():
        console.print(
            "[green]✓ Engine carregada[/green]"
        )
    else:
        console.print(
            "[yellow]⚠ Engine não pronta[/yellow]"
        )

    while True:

        try:

            comando = session.prompt(
                "❯ ",
                style=None
            ).strip()

        except (KeyboardInterrupt, EOFError):
            break

        if not comando:
            continue

        if comando == "/exit":
            break

        elif comando == "/help":

            console.print(
                Panel(
                    "/help\n"
                    "/status\n"
                    "/clear\n"
                    "/about\n"
                    "/exit",
                    title="Comandos"
                )
            )

        elif comando == "/status":

            show_response(
                engine.status_snapshot()
            )

        elif comando == "/about":

            show_response(
                "Mission Control AI - EnviroSat\n"
                "Global Solution 2026.1"
            )

        elif comando == "/clear":

            console.clear()
            show_banner()

        else:

            resposta = engine.analyze(comando)

            show_response(resposta)
