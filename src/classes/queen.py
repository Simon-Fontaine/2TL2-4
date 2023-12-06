"""
Ce module contient la classe Queen
"""

import random

from src.classes.food import Food
from src.classes.settings import Settings
from src.classes.enums import State, Job

from src.classes.ant import Ant


class Queen(Ant):
    """
    Classe représentant une reine
    """

    def __init__(self, settings: Settings, food: Food):
        super().__init__(settings, food)
        self.max_age = random.randint(
            settings.queen_avg_age - settings.queen_avg_age_variation,
            settings.queen_avg_age + settings.queen_avg_age_variation,
        )
        self.is_worker = Job.NOT_WORKER

    def evolve(self):
        """
        Fait évoluer la reine
        """
        if self.is_alive and self.food.quantity >= self.settings.queen_hunger:
            self.age += 1
            self.food.remove(self.settings.queen_hunger)
            if self.age >= self.max_age:
                self.state = State.DEAD
        else:
            self.state = State.DEAD
