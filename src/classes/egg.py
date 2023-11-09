import random
from .ant import Ant


class Egg:
    """
    Représente un œuf dans la colonie, avec la possibilité d'éclore.
    """

    def __init__(self):
        self._age = 0
        self._is_hatched = False
        self._is_dead = False

    def __str__(self):
        return f"Œuf: {self._is_hatched}\nAge: {self._age}\n"

    @property
    def is_hatched(self) -> bool:
        return self._is_hatched

    @property
    def is_dead(self) -> bool:
        return self._is_dead

    def evolve(self) -> Ant or None:
        """
        Fait vieillir l'œuf et détermine s'il éclot ou meurt.
        """
        self._age += 1
        if self._age >= 3 and random.random() < 0.8:
            self._is_hatched = True
            return Ant()
        elif self._age >= 3:
            self._is_hatched = True
        return None
