"""
Ce module contient une fonction pour créer un tableau
"""

from rich.table import Table


def create_table(
    show_header: bool = True,
    title: str = None,
    title_style: str = "bold magenta",
    header_style: str = "bold cyan",
    column_styles=("bold blue", "yellow"),
    rows=None,
    min_width: int = 60,
) -> Table:
    """
    Crée un tableau avec les styles donnés
    """
    table = Table(
        show_header=show_header,
        title=title,
        header_style=header_style,
        title_style=title_style,
        min_width=min_width,
    )
    table.add_column("Metric", style=column_styles[0], max_width=20)
    table.add_column("Value", style=column_styles[1], max_width=40)
    if rows:
        for row in rows:
            table.add_row(row[0], row[1])
    return table
