"""
Ce module contient la classe Food
"""

from src.classes.settings import Settings


class Food:
    """
    Classe représentant la nourritures
    """

    def __init__(self, settings: Settings):
        self.__quantity = settings.initial_food_quantity

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
    def quantity(self):
        """
        Quantité de nourriture
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        """
        Modifie la quantité de nourriture
        """
        self.__validate_value(
            value,
            (int, float),
            min_value=0,
            error_message="Invalid quantity: Value must be a positive number",
        )
        self.__quantity = value

    def remove(self, amount: (int, float) = 1):
        """
        Retire de la nourriture
        """
        self.__quantity = max(self.__quantity - amount, 0)

    def add(self, amount: (int, float) = 1):
        """
        Ajoute de la nourriture
        """
        self.__quantity += amount

    def to_dict(self):
        """
        Convertit la nourriture en dictionnaire
        """
        return {"quantity": self.quantity}
