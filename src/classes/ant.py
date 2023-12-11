"""
Ce module contient la classe Ant
"""

import random

from src.classes.food import Food
from src.classes.settings import Settings
from src.classes.enums import State, Job


class Ant:
    """
    Classe représentant une fourmi
    """

    def __init__(self, settings: Settings, food: Food):
        self.__age = 0
        self.__max_age = random.randint(
            settings.ant_avg_age - settings.ant_avg_age_variation,
            settings.ant_avg_age + settings.ant_avg_age_variation,
        )
        self.__state = State.ALIVE
        self.__profession = (
            Job.WORKER
            if random.random() < settings.ant_worker_chance
            else Job.NOT_WORKER
        )

        self.__settings = settings
        self.__food = food

    def __validate_value(
        self,
        value,
        value_type,
        error_message="Invalid value",
        min_value=None,
        max_value=None,
    ):
        """
        Valide une valeur. Vérifie le type et la plage de la valeur si c'est numérique.
        """
        if not isinstance(value, value_type):
            raise TypeError(
                f"{error_message}: Expected type {value_type}, got {type(value)} instead."
            )

        if isinstance(value, (int, float)):
            if min_value is not None and value < min_value:
                raise ValueError(
                    f"{error_message}: Value {value} is less than minimum allowed {min_value}."
                )
            if max_value is not None and value > max_value:
                raise ValueError(
                    f"{error_message}: Value {value} is greater than maximum allowed {max_value}."
                )

    @property
    def age(self) -> int:
        """
        Age de la fourmi
        """
        return self.__age

    @age.setter
    def age(self, value: int):
        """
        Modifie l'age de la fourmi
        """
        self.__validate_value(
            value, int, min_value=0, error_message="L'age doit être un entier"
        )
        self.__age = value

    @property
    def max_age(self) -> int:
        """
        Age maximal de la fourmi
        """
        return self.__max_age

    @max_age.setter
    def max_age(self, value: int):
        """
        Modifie l'age maximal de la fourmi
        """
        self.__validate_value(
            value, int, min_value=0, error_message="L'age maximal doit être un entier"
        )
        self.__max_age = value

    @property
    def state(self) -> State:
        """
        Etat de la fourmi
        """
        return self.__state

    @state.setter
    def state(self, value: State):
        """
        Modifie l'état de la fourmi
        """
        self.__validate_value(value, State, "L'état doit être un State")
        self.__state = value

    @property
    def settings(self) -> Settings:
        """
        Paramètres de la simulation
        """
        return self.__settings

    @property
    def food(self) -> Food:
        """
        Nourriture de la fourmi
        """
        return self.__food

    @property
    def is_alive(self) -> bool:
        """
        Si la fourmi est vivante ou non
        """
        return self.__state == State.ALIVE

    @property
    def profession(self) -> bool:
        """
        Si la fourmi est une ouvrière ou non
        """
        return self.__profession

    @profession.setter
    def profession(self, value: Job):
        """
        Modifie le job de la fourmi
        """
        self.__validate_value(value, Job, "Le job doit être un Job")
        self.__profession = value

    def evolve(self):
        """
        Fait évoluer la fourmi
        """
        if self.is_alive and self.__food.quantity >= self.__settings.ant_hunger:
            self.__age += 1
            self.__food.remove(self.__settings.ant_hunger)
            if (
                self.__age > self.__max_age
                or random.random() < self.__settings.ant_random_death_chance
            ):
                self.__state = State.DEAD
        else:
            self.__state = State.DEAD

    def to_dict(self):
        """
        Convertit la fourmi en dictionnaire
        """
        return {
            "age": self.age,
            "max_age": self.max_age,
            "state": self.state.value,
            "profession": "worker" if self.profession else "not_worker",
        }
