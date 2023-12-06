"""
Ce module contient la classe Colony
"""

import random


from src.classes.food import Food
from src.classes.settings import Settings
from src.classes.enums import Job

from src.classes.ant import Ant
from src.classes.egg import Egg
from src.classes.queen import Queen


class Colony:
    """
    Classe représentant une colonie
    """

    def __init__(self, settings: Settings, food: Food):
        self.__day = 0
        self.__ants = [
            Ant(settings, food) for _ in range(settings.initial_ant_quantity)
        ]
        self.__born_ants = settings.initial_ant_quantity + 1
        self.__queen = Queen(settings, food)
        self.__eggs = []
        self.__settings = settings
        self.__food = food

    @property
    def day(self) -> int:
        """
        Jour de la colonie
        """
        return self.__day

    @property
    def queen(self) -> Queen:
        """
        Reine de la colonie
        """
        return self.__queen

    @property
    def food(self) -> Food:
        """
        Nourriture de la colonie
        """
        return self.__food

    @property
    def ants(self) -> [Ant]:
        """
        Fourmis de la colonie
        """
        return self.__ants

    @property
    def eggs(self) -> [Egg]:
        """
        Oeufs de la colonie
        """
        return self.__eggs

    @property
    def settings(self) -> Settings:
        """
        Paramètres de la colonie
        """
        return self.__settings

    def ant_count(self) -> int:
        """
        Nombre de fourmis
        """
        return len(self.__ants) + int(self.__queen.is_alive)

    def dead_ant_count(self) -> int:
        """
        Nombre de fourmis mortes
        """
        return self.__born_ants - self.ant_count()

    def worker_count(self) -> int:
        """
        Nombre d'ouvrières
        """
        return len(
            [worker for worker in self.__ants if worker.profession == Job.WORKER]
        )

    def egg_count(self) -> int:
        """
        Nombre d'oeufs
        """
        return len(self.__eggs)

    def __update_food(self):
        self.__food.add(
            random.randint(
                round(self.worker_count() * self.__settings.min_food_multiplier),
                round(self.worker_count() * self.__settings.max_food_multiplier),
            )
        )

    def __update_ants(self):
        self.__queen.evolve()
        if self.__queen.is_alive and self.__queen.age >= self.__queen.max_age - 1:
            self.__lay_successor_egg()

        for ant in self.__ants:
            ant.evolve()
        self.__ants = [ant for ant in self.__ants if ant.is_alive]

    def __lay_successor_egg(self):
        if self.__queen.is_alive and self.food.quantity >= self.settings.queen_hunger:
            self.food.remove(self.settings.queen_hunger)
            self.__eggs.append(Egg(self.settings, self.food, is_queen_egg=True))

    def __lay_eggs(self):
        if self.__day % self.__settings.queen_laying_rate == 0:
            if self.queen.is_alive and self.food.quantity >= self.settings.queen_hunger:
                self.food.remove(self.settings.queen_hunger)
                for _ in range(
                    random.randint(
                        self.settings.queen_avg_eggs
                        - self.settings.queen_avg_egg_variation,
                        self.settings.queen_avg_eggs
                        + self.settings.queen_avg_egg_variation,
                    )
                ):
                    self.__eggs.append(Egg(self.settings, self.food))

    def __update_eggs(self):
        new_queen = None
        for egg in self.__eggs:
            new_ant = egg.evolve()
            if new_ant:
                if isinstance(new_ant, Queen):
                    new_queen = new_ant
                else:
                    self.__ants.append(new_ant)
                    self.__born_ants += 1
        self.__eggs = [egg for egg in self.__eggs if egg.is_alive]

        if new_queen and not self.__queen.is_alive:
            self.__queen = new_queen

    def evolve(self):
        """
        Fait évoluer la colonie d'un jour
        """
        self.__update_food()
        self.__update_ants()
        self.__update_eggs()
        self.__lay_eggs()
        self.__day += 1

    def to_dict(self):
        """
        Convertit la colonie en dictionnaire
        """
        return {
            "day": self.day,
            "queen": self.queen.to_dict(),
            "food": self.food.to_dict(),
            "ants": [ant.to_dict() for ant in self.ants],
            "eggs": [egg.to_dict() for egg in self.eggs],
        }
