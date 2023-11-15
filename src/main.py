import time

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.prompt import Confirm, IntPrompt, FloatPrompt

from classes.colony import Colony
from classes.settings import (
    MAX_ANT_AGE,
    MAX_QUEEN_AGE,
    QUEEN_EGG_LAYING_RATE,
    EGG_GROWING_TIME,
    EGG_HATCHING_RATE,
)

console = Console()


def create_table(title, header_style="bold cyan", column_styles=("bold blue", "yellow")):
    """
    Créer une table avec un titre et des styles de colonnes et d'en-tête par défaut.
    """
    table = Table(title=title, show_header=True, header_style=header_style, title_style="bold magenta", min_width=50)
    table.add_column("Métrique", style=column_styles[0])
    table.add_column("Valeur", style=column_styles[1])
    return table


def print_parameters(ants: int, food: int, speed: int) -> Table:
    """
    Affiche les paramètres de la simulation.
    """
    table = create_table("Paramètres de la Simulation")
    table.add_row("Vitesse (secondes/jour)", str(speed))
    table.add_row("Fourmis Initiales", str(ants))
    table.add_row("Nourriture Initiale", str(food))
    return table


def print_simulation_details() -> Table:
    """
    Affiche les détails de la simulation.
    """
    table = create_table("Détails de la Simulation")
    table.add_row("Âge Max des Fourmis (jours)", str(MAX_ANT_AGE))
    table.add_row("Âge Max de la Reine (jours)", str(MAX_QUEEN_AGE))
    table.add_row("Taux de Ponte de la Reine (œufs/jour)", str(QUEEN_EGG_LAYING_RATE))
    table.add_row("Temps de Croissance des Œufs (jours)", str(EGG_GROWING_TIME))
    table.add_row("Taux d'Éclosion des Œufs (%)", f"{EGG_HATCHING_RATE * 100}")
    return table


def print_simulation_results(colony) -> Table:
    """
    Affiche les résultats de la simulation.
    """
    table = create_table("Résultats de la Simulation")
    table.add_row("Temps Total", str(colony.days_to_years_months_days))
    table.add_row("Jours", str(colony.day))
    table.add_row("Œufs", str(len(colony.eggs)))
    table.add_row("Fourmis", str(colony.ant_count))
    table.add_row("Nourriture", str(colony.food.quantity))
    table.add_row("Reine", "Vivante" if colony.queen.is_alive else "Décédée")
    table.add_row("Fourmis Mortes", str(colony.dead_ant_count))
    return table


def main():
    """
    Fonction principale du programme.
    """
    console.print("Bienvenue dans le simulateur de colonie de fourmis!", style="bold green")

    ants = IntPrompt.ask("Entrez le nombre initial de fourmis", default=100)
    food = IntPrompt.ask("Entrez la quantité initiale de nourriture", default=10000)
    speed = FloatPrompt.ask("Entrez la vitesse de la simulation en secondes par jour", default=0.2)

    console.print("Récapitulatif des Paramètres de Simulation:")
    console.print(print_parameters(ants, food, speed))
    console.print("Détails de la Simulation:")
    console.print(print_simulation_details())

    if Confirm.ask("Voulez-vous lancer la simulation maintenant ?"):
        colony = Colony(ants, food)

        with Live(auto_refresh=False) as live:
            while colony.ants or colony.queen.is_alive or colony.eggs:
                colony.update()
                live.update(print_simulation_results(colony))
                live.refresh()
                time.sleep(speed)

        console.print("[bold green]Simulation terminée. Voici les résultats finaux :[/]")
        console.print(print_simulation_results(colony))
    else:
        console.print("[bold red]Simulation annulée.[/]")

    if Confirm.ask("Voulez-vous quitter le programme ?"):
        console.print("[bold green]Au revoir ![/]")
    else:
        console.print("[bold red]Retour au menu principal...[/]")
        main()


if __name__ == "__main__":
    main()
