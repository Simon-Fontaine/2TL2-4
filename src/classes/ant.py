from .settings import MAX_ANT_AGE


class Ant:
    """
    Représent une fourmi dans la colonie.
    """

    def __init__(self):
        self._age = 0
        self._is_alive = True
        self.max_age = MAX_ANT_AGE

    def __str__(self):
        return f"Fourmi: {self._is_alive}\nAge: {self._age}\n"

    @property
    def age(self) -> int:
        return self._age

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    def grow_older(self):
        if self._is_alive:
            self._age += 1
            if self._age >= self.max_age:
                self.die()

    def eat(self, food, hunger=1):
        if self._is_alive and food.quantity >= hunger:
            food.consume(hunger)
        else:
            self.die()

    def die(self):
        self._is_alive = False
