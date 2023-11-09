import time
import argparse
from classes.colony import Colony


def main():
    parser = argparse.ArgumentParser(description="Simuler une colonie de fourmis")

    parser.add_argument("ants", help="Le nombre initial de fourmis", type=int)
    parser.add_argument("food", help="La quantité initiale de nourriture", type=int)
    parser.add_argument(
        "--speed", help="La vitesse de simulation en secondes par jour (par défaut=0.5)", default=0.5, type=float
    )

    args = parser.parse_args()

    colony = Colony(args.ants, args.food)

    while colony.ants or colony.queen.is_alive or colony.eggs:
        colony.update()
        print(colony)
        time.sleep(args.speed)


if __name__ == "__main__":
    main()
