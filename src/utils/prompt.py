"""
Ce module contient les fonctions permettant de prompt l'utilisateur
"""

import time

from rich.console import Console
from rich.prompt import IntPrompt, FloatPrompt, Prompt

from src.classes.settings import Settings

from src.utils.panel import create_panel


def prompt_initial_settings(console: Console) -> Settings:
    """
    Demande les paramètres initiaux
    """
    console.clear()
    default_settings = Settings()

    simulation_seed = IntPrompt.ask(
        "Simulation seed (0 for random)", default=default_settings.simulation_seed
    )
    simulation_speed = FloatPrompt.ask(
        "Initial simulation speed (in seconds)",
        default=default_settings.simulation_speed,
    )
    initial_ant_quantity = IntPrompt.ask(
        "Initial ant quantity", default=default_settings.initial_ant_quantity
    )
    initial_food_quantity = FloatPrompt.ask(
        "Initial food quantity", default=default_settings.initial_food_quantity
    )
    ant_avg_age = IntPrompt.ask("Average ant age", default=default_settings.ant_avg_age)
    ant_avg_age_variation = IntPrompt.ask(
        "Average ant age variation", default=default_settings.ant_avg_age_variation
    )
    ant_worker_chance = FloatPrompt.ask(
        "Ant worker chance", default=default_settings.ant_worker_chance
    )
    min_food_multiplier = FloatPrompt.ask(
        "Minimum food multiplier", default=default_settings.min_food_multiplier
    )
    max_food_multiplier = FloatPrompt.ask(
        "Maximum food multiplier", default=default_settings.max_food_multiplier
    )
    ant_hunger = FloatPrompt.ask("Ant hunger", default=default_settings.ant_hunger)
    ant_random_death_chance = FloatPrompt.ask(
        "Ant random death chance", default=default_settings.ant_random_death_chance
    )
    queen_avg_age = IntPrompt.ask(
        "Average queen age", default=default_settings.queen_avg_age
    )
    queen_avg_age_variation = IntPrompt.ask(
        "Average queen age variation",
        default=default_settings.queen_avg_age_variation,
    )
    queen_hunger = FloatPrompt.ask(
        "Queen hunger", default=default_settings.queen_hunger
    )
    queen_laying_rate = IntPrompt.ask(
        "Queen laying rate", default=default_settings.queen_laying_rate
    )
    queen_avg_eggs = IntPrompt.ask(
        "Average queen eggs", default=default_settings.queen_avg_eggs
    )
    queen_avg_egg_variation = IntPrompt.ask(
        "Average queen egg variation",
        default=default_settings.queen_avg_egg_variation,
    )
    egg_avg_age = IntPrompt.ask("Average egg age", default=default_settings.egg_avg_age)
    egg_avg_age_variation = IntPrompt.ask(
        "Average egg age variation", default=default_settings.egg_avg_age_variation
    )
    egg_hunger = FloatPrompt.ask("Egg hunger", default=default_settings.egg_hunger)
    egg_evolve_chance = FloatPrompt.ask(
        "Egg evolve chance", default=default_settings.egg_evolve_chance
    )
    queen_avg_egg_age = IntPrompt.ask(
        "Average queen egg age", default=default_settings.queen_avg_egg_age
    )
    queen_avg_egg_age_variation = IntPrompt.ask(
        "Average queen egg age variation",
        default=default_settings.queen_avg_egg_age_variation,
    )
    queen_egg_hunger = FloatPrompt.ask(
        "Queen egg hunger", default=default_settings.queen_egg_hunger
    )
    queen_egg_evolve_chance = FloatPrompt.ask(
        "Queen egg evolve chance", default=default_settings.queen_egg_evolve_chance
    )

    return Settings(
        simulation_seed=simulation_seed if simulation_seed != 0 else int(time.time()),
        simulation_speed=simulation_speed,
        initial_ant_quantity=initial_ant_quantity,
        initial_food_quantity=initial_food_quantity,
        ant_avg_age=ant_avg_age,
        ant_avg_age_variation=ant_avg_age_variation,
        ant_worker_chance=ant_worker_chance,
        min_food_multiplier=min_food_multiplier,
        max_food_multiplier=max_food_multiplier,
        ant_hunger=ant_hunger,
        ant_random_death_chance=ant_random_death_chance,
        queen_avg_age=queen_avg_age,
        queen_avg_age_variation=queen_avg_age_variation,
        queen_hunger=queen_hunger,
        queen_laying_rate=queen_laying_rate,
        queen_avg_eggs=queen_avg_eggs,
        queen_avg_egg_variation=queen_avg_egg_variation,
        egg_avg_age=egg_avg_age,
        egg_avg_age_variation=egg_avg_age_variation,
        egg_hunger=egg_hunger,
        egg_evolve_chance=egg_evolve_chance,
        queen_avg_egg_age=queen_avg_egg_age,
        queen_avg_egg_age_variation=queen_avg_egg_age_variation,
        queen_egg_hunger=queen_egg_hunger,
        queen_egg_evolve_chance=queen_egg_evolve_chance,
    )


def prompt_options(
    console: Console, no_saves: bool = False, error_message: str = None
) -> str:
    """
    Demande les options
    """
    console.clear()

    console.print(
        create_panel(
            "[1] Start New Simulation\n[2] Load Existing Simulation\n[3] Exit",
            "cyan",
            "Options",
        )
    )

    if error_message:
        console.print(
            create_panel(
                error_message,
                "red",
                "Error",
            )
        )

    if no_saves:
        console.print(
            create_panel(
                "No saves were found.",
                "red",
                "Error",
            )
        )

    return Prompt.ask("Please choose an option :", choices=["1", "2", "3"], default="1")


def prompt_files_to_load(console: Console, files: dict) -> str:
    """
    Affiche et demande le fichier à charger
    """
    console = Console()
    console.clear()

    console.print(
        create_panel(
            "Please choose a save file.",
            "cyan",
            "Options",
        )
    )

    console.print("[0] Go back")
    for index, file in files.items():
        console.print(f"[{index}] {file}")

    unique_id = Prompt.ask(
        "Please choose an option :",
        choices=[str(i) for i in range(len(files) + 1)],
        default="1",
    )

    return files[unique_id] if unique_id != "0" else "back"
