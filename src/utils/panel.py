"""
Ce module contient une fonction pour créer un panneau
"""
from rich.panel import Panel


def create_panel(desc: str, border_style: str, title: str) -> Panel:
    """
    Crée un panneau avec les styles donnés
    """
    return Panel(
        desc,
        safe_box=True,
        border_style=border_style,
        title=title,
        title_align="left",
        width=60,
        highlight=True,
    )
