"""
Fichier permettant de démarrer une simulation
"""
import time
import random

from rich.live import Live
from rich.console import Console
from rich.prompt import Confirm

from src.classes.food import Food
from src.classes.colony import Colony
from src.classes.settings import Settings

from src.utils.table import create_table
from src.utils.panel import create_panel
from src.utils.day_to_string import days_to_string
from src.utils.files import create_save_file


def run_simulation(console: Console, settings: Settings) -> bool:
    """
    Démarre la simulation
    """
    console.clear()

    rows = []
    for key, value in settings.to_dict().items():
        rows.append([key.replace("_", " ").title(), str(value)])

    console.print(
        create_table(
            rows=rows,
        )
    )

    if not Confirm.ask("Start simulation?"):
        return True

    random.seed(settings.simulation_seed)

    sim_food = Food(settings)
    sim_colony = Colony(settings, sim_food)

    with Live(auto_refresh=False) as live:
        while sim_colony.ants or sim_colony.queen.is_alive or sim_colony.eggs:
            sim_colony.evolve()
            live.update(
                create_table(
                    rows=[
                        ("Total Time", days_to_string(sim_colony.day)),
                        ("Days", str(sim_colony.day)),
                        ("Eggs", str(sim_colony.egg_count())),
                        ("Ants", str(sim_colony.ant_count())),
                        ("Workers", str(sim_colony.worker_count())),
                        ("Food", str(round(sim_colony.food.quantity, 2))),
                        (
                            "Queen",
                            "Alive" if sim_colony.queen.is_alive else "Deceased",
                        ),
                        ("Dead Ants", str(sim_colony.dead_ant_count())),
                    ],
                )
            )
            live.refresh()
            time.sleep(settings.simulation_speed)

    console.print(
        create_panel(
            "Simulation completed. The results are displayed above.",
            "green",
            "Ended",
        )
    )

    unique_id = create_save_file(sim_colony)

    console.print(
        create_panel(
            f"Simulation saved at: saves/sim_{unique_id}.json",
            "green",
            "Saved",
        )
    )

    return Confirm.ask("Do you want to start a new simulation?")
