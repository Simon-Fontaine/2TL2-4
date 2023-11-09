from typing import List
from .ant import Ant
from .egg import Egg
from .settings import MAX_QUEEN_AGE, QUEEN_EGG_LAYING_RATE


class Queen(Ant):
    """
    Représente la reine de la colonie.
    """

    def __init__(self):
        super().__init__()
        self.max_age = MAX_QUEEN_AGE
        self._egg_laying_rate = QUEEN_EGG_LAYING_RATE

    def __str__(self):
        return f"Rein: {self.is_alive}\nAge: {self.age}\nŒufs: {self._egg_laying_rate}\n"

    @property
    def egg_laying_rate(self) -> int:
        return self._egg_laying_rate

    def lay_eggs(self) -> List[Egg]:
        """
        La reine pond des œufs si elle est en vie.
        """
        return [Egg() for _ in range(self._egg_laying_rate)]
