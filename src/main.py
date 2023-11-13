import time
import argparse
from termcolor import colored, cprint
from classes.colony import Colony
from classes.settings import (
    MAX_ANT_AGE,
    MAX_QUEEN_AGE,
    QUEEN_EGG_LAYING_RATE,
    EGG_GROWING_TIME,
    EGG_HATCHING_RATE,
)


def print_header(text):
    """
    Affiche un texte en vert et en gras.
    """
    print(colored(text, "green", attrs=["bold"]))


def print_separator():
    """
    Affiche un séparateur jaune.
    """
    print(colored("=" * 40, "yellow"))


def main():
    """
    Fonction principale du programme.
    """
    parser = argparse.ArgumentParser(description="Simuler une colonie de fourmis")

    parser.add_argument("ants", help="Le nombre initial de fourmis", type=int)
    parser.add_argument("food", help="La quantité initiale de nourriture", type=int)
    parser.add_argument(
        "--speed",
        help="La vitesse de simulation en secondes par jour (défaut = 1 secondes/jour)",
        default=1,
        type=float,
    )

    args = parser.parse_args()

    print_header("Paramètres de la simulation :")
    print_separator()
    cprint(f"Vitesse : {args.speed} secondes/jour", "blue")
    cprint(f"Fourmis initiales : {args.ants}", "blue")
    cprint(f"Nourriture initiale : {args.food}", "blue")
    print_separator()
    cprint(f"Âge maximal des fourmis : {MAX_ANT_AGE} jours", "cyan")
    cprint(f"Âge maximal de la reine : {MAX_QUEEN_AGE} jours", "cyan")
    cprint(f"Production d'œufs de la reine : {QUEEN_EGG_LAYING_RATE} œufs/jour", "cyan")
    cprint(f"Temps d'incubation des œufs : {EGG_GROWING_TIME} jours", "cyan")
    cprint(f"Taux d'éclosion des œufs : {EGG_HATCHING_RATE * 100}%", "cyan")
    print_separator()

    input(colored("Appuyez sur Entrée pour commencer la simulation...", "red", attrs=["bold"]))

    colony = Colony(args.ants, args.food)

    while colony.ants or colony.queen.is_alive or colony.eggs:
        colony.update()
        print_separator()
        cprint(colony.days_to_years_months_days, "magenta", attrs=["bold"])
        cprint(f"Total: {colony.day} jours\n", "blue", attrs=["bold"])
        cprint(f"Oeufs: {len(colony.eggs)}", "cyan")
        cprint(f"Fourmis: {colony.ant_count}", "cyan")
        cprint(f"Nourriture: {colony.food.quantity}", "cyan")
        cprint(
            f"Reine vivante: {'Oui' if colony.queen.is_alive else 'Non'}",
            "green" if colony.queen.is_alive else "red",
        )
        cprint(f"Fourmis mortes: {colony.dead_ant_count}", "cyan")
        print_separator()
        time.sleep(args.speed)

    cprint("La simulation est terminée.", "magenta", attrs=["bold"])


if __name__ == "__main__":
    main()
