"""
Ce module contient la classe Settings.
"""
YEAR = 365
MONTH = YEAR // 12
WEEK = MONTH // 4
SAVE_DIRECTORY = "saves"


class Settings:
    """
    Classe représentant les paramètres de la simulation.
    """

    def __init__(
        self,
        simulation_seed: int = 1234,
        simulation_speed: float = 1.0,
        initial_food_quantity: float = 30000.0,
        initial_ant_quantity: int = 100,
        ant_avg_age: int = 90,
        ant_avg_age_variation: int = 20,
        ant_worker_chance: float = 0.95,
        min_food_multiplier: float = 0.5,
        max_food_multiplier: float = 1.5,
        ant_hunger: float = 0.3,
        ant_random_death_chance: float = 0.01,
        queen_avg_age: int = 5 * YEAR,
        queen_avg_age_variation: int = 1 * YEAR,
        queen_hunger: float = 10.0,
        queen_laying_rate: int = 5,
        queen_avg_eggs: int = 500,
        queen_avg_egg_variation: int = 150,
        egg_avg_age: int = 2 * WEEK,
        egg_avg_age_variation: int = 1 * WEEK,
        egg_hunger: float = 0.1,
        egg_evolve_chance: float = 0.9,
        queen_avg_egg_age: int = 2 * MONTH,
        queen_avg_egg_age_variation: int = 2 * WEEK,
        queen_egg_hunger: float = 1.0,
        queen_egg_evolve_chance: float = 0.5,
    ):
        self.simulation_seed = simulation_seed
        self.simulation_speed = simulation_speed
        self.initial_food_quantity = initial_food_quantity
        self.initial_ant_quantity = initial_ant_quantity
        self.ant_avg_age = ant_avg_age
        self.ant_avg_age_variation = ant_avg_age_variation
        self.ant_worker_chance = ant_worker_chance
        self.min_food_multiplier = min_food_multiplier
        self.max_food_multiplier = max_food_multiplier
        self.ant_hunger = ant_hunger
        self.ant_random_death_chance = ant_random_death_chance
        self.queen_avg_age = queen_avg_age
        self.queen_avg_age_variation = queen_avg_age_variation
        self.queen_hunger = queen_hunger
        self.queen_laying_rate = queen_laying_rate
        self.queen_avg_eggs = queen_avg_eggs
        self.queen_avg_egg_variation = queen_avg_egg_variation
        self.egg_avg_age = egg_avg_age
        self.egg_avg_age_variation = egg_avg_age_variation
        self.egg_hunger = egg_hunger
        self.egg_evolve_chance = egg_evolve_chance
        self.queen_avg_egg_age = queen_avg_egg_age
        self.queen_avg_egg_age_variation = queen_avg_egg_age_variation
        self.queen_egg_hunger = queen_egg_hunger
        self.queen_egg_evolve_chance = queen_egg_evolve_chance

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
    def simulation_seed(self) -> int:
        """
        Graine de la simulation.
        """
        return self.__simulation_seed

    @simulation_seed.setter
    def simulation_seed(self, value: int):
        """
        Modifie la graine de la simulation.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Simulation seed must be a positive integer",
        )
        self.__simulation_seed = value

    @property
    def simulation_speed(self) -> float:
        """
        Vitesse de la simulation.
        """
        return self.__simulation_speed

    @simulation_speed.setter
    def simulation_speed(self, value: float):
        """
        Modifie la vitesse de la simulation.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Simulation speed must be a positive float",
        )
        self.__simulation_speed = value

    @property
    def initial_food_quantity(self) -> float:
        """
        Quantité de nourriture initiale.
        """
        return self.__initial_food_quantity

    @initial_food_quantity.setter
    def initial_food_quantity(self, value: float):
        """
        Modifie la quantité de nourriture initiale.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Initial food quantity must be a positive float",
        )
        self.__initial_food_quantity = value

    @property
    def initial_ant_quantity(self) -> int:
        """
        Quantité de fourmis initiale.
        """
        return self.__initial_ant_quantity

    @initial_ant_quantity.setter
    def initial_ant_quantity(self, value: int):
        """
        Modifie la quantité de fourmis initiale.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Initial ant quantity must be a positive integer",
        )
        self.__initial_ant_quantity = value

    @property
    def ant_avg_age(self) -> int:
        """
        Age moyen des fourmis.
        """
        return self.__ant_avg_age

    @ant_avg_age.setter
    def ant_avg_age(self, value: int):
        """
        Modifie l'age moyen des fourmis.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Ant average age must be a positive integer",
        )
        self.__ant_avg_age = value

    @property
    def ant_avg_age_variation(self) -> int:
        """
        Variation de l'age moyen des fourmis.
        """
        return self.__ant_avg_age_variation

    @ant_avg_age_variation.setter
    def ant_avg_age_variation(self, value: int):
        """
        Modifie la variation de l'age moyen des fourmis.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Ant average age variation must be a positive integer",
        )
        self.__ant_avg_age_variation = value

    @property
    def ant_worker_chance(self) -> float:
        """
        Chance qu'une fourmi soit une ouvrière.
        """
        return self.__ant_worker_chance

    @ant_worker_chance.setter
    def ant_worker_chance(self, value: float):
        """
        Modifie la chance qu'une fourmi soit une ouvrière.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            max_value=1.0,
            error_message="Ant worker chance must be a float between 0 and 1",
        )
        self.__ant_worker_chance = value

    @property
    def min_food_multiplier(self) -> float:
        """
        Multiplicateur de la quantité de nourriture minimum.
        """
        return self.__min_food_multiplier

    @min_food_multiplier.setter
    def min_food_multiplier(self, value: float):
        """
        Modifie le multiplicateur de la quantité de nourriture minimum.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Minimum food multiplier must be a positive float",
        )
        self.__min_food_multiplier = value

    @property
    def max_food_multiplier(self) -> float:
        """
        Multiplicateur de la quantité de nourriture maximum.
        """
        return self.__max_food_multiplier

    @max_food_multiplier.setter
    def max_food_multiplier(self, value: float):
        """
        Modifie le multiplicateur de la quantité de nourriture maximum.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Maximum food multiplier must be a positive float",
        )
        self.__max_food_multiplier = value

    @property
    def ant_hunger(self) -> float:
        """
        Faim des fourmis.
        """
        return self.__ant_hunger

    @ant_hunger.setter
    def ant_hunger(self, value: float):
        """
        Modifie la faim des fourmis.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Ant hunger must be a positive float",
        )
        self.__ant_hunger = value

    @property
    def ant_random_death_chance(self) -> float:
        """
        Chance qu'une fourmi meurt aléatoirement.
        """
        return self.__ant_random_death_chance

    @ant_random_death_chance.setter
    def ant_random_death_chance(self, value: float):
        """
        Modifie la chance qu'une fourmi meurt aléatoirement.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            max_value=1.0,
            error_message="Ant random death chance must be a float between 0 and 1",
        )
        self.__ant_random_death_chance = value

    @property
    def queen_avg_age(self) -> int:
        """
        Age moyen de la reine.
        """
        return self.__queen_avg_age

    @queen_avg_age.setter
    def queen_avg_age(self, value: int):
        """
        Modifie l'age moyen de la reine.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Queen average age must be a positive integer",
        )
        self.__queen_avg_age = value

    @property
    def queen_avg_age_variation(self) -> int:
        """
        Variation de l'age moyen de la reine.
        """
        return self.__queen_avg_age_variation

    @queen_avg_age_variation.setter
    def queen_avg_age_variation(self, value: int):
        """
        Modifie la variation de l'age moyen de la reine.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Queen average age variation must be a positive integer",
        )
        self.__queen_avg_age_variation = value

    @property
    def queen_hunger(self) -> float:
        """
        Faim de la reine.
        """
        return self.__queen_hunger

    @queen_hunger.setter
    def queen_hunger(self, value: float):
        """
        Modifie la faim de la reine.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Queen hunger must be a positive float",
        )
        self.__queen_hunger = value

    @property
    def queen_laying_rate(self) -> int:
        """
        Tout les combien de jours la reine pond des oeufs.
        """
        return self.__queen_laying_rate

    @queen_laying_rate.setter
    def queen_laying_rate(self, value: int):
        """
        Modifie le nombre de jours entre chaque ponte de la reine.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Queen laying rate must be a positive integer",
        )
        self.__queen_laying_rate = value

    @property
    def queen_avg_eggs(self) -> int:
        """
        Nombre moyen d'oeufs pondus par la reine.
        """
        return self.__queen_avg_eggs

    @queen_avg_eggs.setter
    def queen_avg_eggs(self, value: int):
        """
        Modifie le nombre moyen d'oeufs pondus par la reine.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Queen average eggs must be a positive integer",
        )
        self.__queen_avg_eggs = value

    @property
    def queen_avg_egg_variation(self) -> int:
        """
        Variation du nombre moyen d'oeufs pondus par la reine.
        """
        return self.__queen_avg_egg_variation

    @queen_avg_egg_variation.setter
    def queen_avg_egg_variation(self, value: int):
        """
        Modifie la variation du nombre moyen d'oeufs pondus par la reine.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Queen average egg variation must be a positive integer",
        )
        self.__queen_avg_egg_variation = value

    @property
    def egg_avg_age(self) -> int:
        """
        Age moyen des oeufs.
        """
        return self.__egg_avg_age

    @egg_avg_age.setter
    def egg_avg_age(self, value: int):
        """
        Modifie l'age moyen des oeufs.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Egg average age must be a positive integer",
        )
        self.__egg_avg_age = value

    @property
    def egg_avg_age_variation(self) -> int:
        """
        Variation de l'age moyen des oeufs.
        """
        return self.__egg_avg_age_variation

    @egg_avg_age_variation.setter
    def egg_avg_age_variation(self, value: int):
        """
        Modifie la variation de l'age moyen des oeufs.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Egg average age variation must be a positive integer",
        )
        self.__egg_avg_age_variation = value

    @property
    def egg_hunger(self) -> float:
        """
        Faim des oeufs.
        """
        return self.__egg_hunger

    @egg_hunger.setter
    def egg_hunger(self, value: float):
        """
        Modifie la faim des oeufs.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Egg hunger must be a positive float",
        )
        self.__egg_hunger = value

    @property
    def egg_evolve_chance(self) -> float:
        """
        Chance qu'un oeuf évolue.
        """
        return self.__egg_evolve_chance

    @egg_evolve_chance.setter
    def egg_evolve_chance(self, value: float):
        """
        Modifie la chance qu'un oeuf évolue.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            max_value=1.0,
            error_message="Egg evolve chance must be a float between 0 and 1",
        )
        self.__egg_evolve_chance = value

    @property
    def queen_avg_egg_age(self) -> int:
        """
        Age moyen des oeufs de  reine.
        """
        return self.__queen_avg_egg_age

    @queen_avg_egg_age.setter
    def queen_avg_egg_age(self, value: int):
        """
        Modifie l'age moyen des oeufs de reine.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Queen average egg age must be a positive integer",
        )
        self.__queen_avg_egg_age = value

    @property
    def queen_avg_egg_age_variation(self) -> int:
        """
        Variation de l'age moyen des oeufs de reine.
        """
        return self.__queen_avg_egg_age_variation

    @queen_avg_egg_age_variation.setter
    def queen_avg_egg_age_variation(self, value: int):
        """
        Modifie la variation de l'age moyen des oeufs de reine.
        """
        self.__validate_value(
            value,
            int,
            min_value=0,
            error_message="Queen average egg age variation must be a positive integer",
        )
        self.__queen_avg_egg_age_variation = value

    @property
    def queen_egg_hunger(self) -> float:
        """
        Faim des oeufs de reine.
        """
        return self.__queen_egg_hunger

    @queen_egg_hunger.setter
    def queen_egg_hunger(self, value: float):
        """
        Modifie la faim des oeufs de reine.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            error_message="Queen egg hunger must be a positive float",
        )
        self.__queen_egg_hunger = value

    @property
    def queen_egg_evolve_chance(self) -> float:
        """
        Chance qu'un oeuf de reine évolue.
        """
        return self.__queen_egg_evolve_chance

    @queen_egg_evolve_chance.setter
    def queen_egg_evolve_chance(self, value: float):
        """
        Modifie la chance qu'un oeuf de reine évolue.
        """
        self.__validate_value(
            value,
            float,
            min_value=0.0,
            max_value=1.0,
            error_message="Queen egg evolve chance must be a float between 0 and 1",
        )
        self.__queen_egg_evolve_chance = value

    def to_dict(self):
        """
        Convertit les paramètres en dictionnaire
        """
        return {
            "simulation_seed": self.simulation_seed,
            "simulation_speed": self.simulation_speed,
            "initial_food_quantity": self.initial_food_quantity,
            "initial_ant_quantity": self.initial_ant_quantity,
            "ant_avg_age": self.ant_avg_age,
            "ant_avg_age_variation": self.ant_avg_age_variation,
            "ant_worker_chance": self.ant_worker_chance,
            "min_food_multiplier": self.min_food_multiplier,
            "max_food_multiplier": self.max_food_multiplier,
            "ant_hunger": self.ant_hunger,
            "ant_random_death_chance": self.ant_random_death_chance,
            "queen_avg_age": self.queen_avg_age,
            "queen_avg_age_variation": self.queen_avg_age_variation,
            "queen_hunger": self.queen_hunger,
            "queen_laying_rate": self.queen_laying_rate,
            "queen_avg_eggs": self.queen_avg_eggs,
            "queen_avg_egg_variation": self.queen_avg_egg_variation,
            "egg_avg_age": self.egg_avg_age,
            "egg_avg_age_variation": self.egg_avg_age_variation,
            "egg_hunger": self.egg_hunger,
            "egg_evolve_chance": self.egg_evolve_chance,
            "queen_avg_egg_age": self.queen_avg_egg_age,
            "queen_avg_egg_age_variation": self.queen_avg_egg_age_variation,
            "queen_egg_hunger": self.queen_egg_hunger,
            "queen_egg_evolve_chance": self.queen_egg_evolve_chance,
        }
