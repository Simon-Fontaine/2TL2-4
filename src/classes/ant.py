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
        """ Ceci construit les paramètres de la fourmis

        PRE : Settings: instance de la classe Settings
              food: int
        POST : __age: age de la fourmis == 0
               __max_age: age de mort de la fourmis définis aléatoirement en fonction des paramètres
               choisis
               __state: état ALIVE
               __profession: en fonction des settings, chance random d'être WORKER sinon, NOT_WORKER
               settings: des paramètres
               food: nombre de nouriture
        RAISE : Tous les cas sont gèrés par les setters grâce à la méthode __validate_value
        """
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
        """Valide une valeur. Lance un erreur si le type et/ou la plage de la valeur n'est pas voulue

        PRE: value doit être de type int si min_value ou max_value est utilitsé
             value type doit être un type existant
        POST: Message d'erreur contenant la valeur qui pose probleme et la valeur attendue
        RAISE: TypeError si value n'est pas de type value_type
               ValueError si value n'est pas entre min_value et max_value

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
        """Modifie l'age de la fourmi

        PRE: Pas de précondition spécifique
        POST: self.__age = value
        RAISE: voir __validate_value()
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
        """Fait évoluer la fourmi

        PRE: Pas de précondition spécifique
        POST: - si fourmis est vivante et que sa nourriture >= __settings.ant_hunger, son âge
              s'incrémente de 1 et sa nourriture diminue de __settings.ant_hunger
              - si sont âge dépasse __max_age ou une chance aléatoire définie par
              __settings.ant_random_death_chance, elle meurt

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

        PRE: Pas de précondition
        POST: Retourne age, max_age, state. Retourne "worker" si profession == True sinon retourne "not_worker"
        """
        return {
            "age": self.age,
            "max_age": self.max_age,
            "state": self.state.value,
            "profession": "worker" if self.profession else "not_worker",
        }
