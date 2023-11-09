from .ant import Ant
from .food import Food
from .queen import Queen


class Colony:
    """
    Représente une colonie de fourmis avec des fourmis, des œufs, une reine et des réserves de nourriture.
    """

    def __init__(self, initial_ant_count: int, initial_food_quantity: int):
        self.ants = [Ant() for _ in range(initial_ant_count)]
        self.eggs = []
        self.queen = Queen()
        self.food = Food(initial_food_quantity)
        self.day = 0
        self.born_ants = initial_ant_count + 1

    def __str__(self):
        return (
            f"Jour: {self.day}\n"
            f"Œufs: {len(self.eggs)}\n"
            f"Fourmis: {self.ant_count}\n"
            f"Nourriture: {self.food.quantity}\n"
            f"Reine vivante: {self.queen.is_alive}\n"
            f"Fourmis mortes: {self.dead_ant_count}\n"
        )

    @property
    def ant_count(self) -> int:
        return len(self.ants) + int(self.queen.is_alive)

    @property
    def dead_ant_count(self) -> int:
        return self.born_ants - self.ant_count

    def _update_ants(self):
        """
        Met à jour les fourmis, en les faisant vieillir et manger.
        """
        self.queen.grow_older()
        self.queen.eat(self.food, hunger=self.queen.egg_laying_rate)

        for ant in self.ants:
            ant.grow_older()
            ant.eat(self.food)

        self.ants = [ant for ant in self.ants if ant.is_alive]

    def _update_eggs(self):
        """
        Met à jour tous les œufs, les fait éclore si possible, et ajoute une nouvelle fourmi à la colonie.
        """
        for egg in self.eggs:
            ant = egg.evolve()
            if isinstance(ant, Ant):
                self.ants.append(ant)
                self.born_ants += 1

        # filtre les œufs qui ont éclos ou qui sont morts
        self.eggs = [egg for egg in self.eggs if not egg.is_hatched and not egg.is_dead]

    def _lay_eggs(self):
        """
        La reine pond de nouveaux œufs si elle est en vie.
        """
        if self.queen.is_alive:
            self.eggs.extend(self.queen.lay_eggs())

    def update(self):
        """
        Met à jour la colonie : vieillit les fourmis et les œufs et fait pondre de nouveaux œufs à la reine.
        """
        self._update_ants()
        self._update_eggs()
        self._lay_eggs()
        self.day += 1
