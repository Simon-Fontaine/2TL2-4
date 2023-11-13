"""
Ce fichier contient la classe Colony.
"""
from .ant import Ant
from .food import Food
from .queen import Queen


class Colony:
    """
    Représente une colonie de fourmis est ses caractéristiques.
    """

    def __init__(self, initial_ant_count: int, initial_food_quantity: int):
        self._ants = [Ant() for _ in range(initial_ant_count)]
        self._eggs = []
        self._queen = Queen()
        self._food = Food(initial_food_quantity)
        self._day = 0
        self._born_ants = initial_ant_count + 1

    def __str__(self):
        separator = "=" * 40
        return (
            f"{separator}\n"
            f"{self.days_to_years_months_days}\n"
            f"Œufs: {len(self._eggs)}\n"
            f"Fourmis: {self.ant_count}\n"
            f"Nourriture: {self.food.quantity}\n"
            f"Reine vivante: {'Oui' if self._queen.is_alive else 'Non'}\n"
            f"Fourmis mortes: {self.dead_ant_count}\n"
            f"{separator}\n"
        )

    @property
    def days_to_years_months_days(self):
        """
        Convertit le nombre de jours en années, mois et jours.
        """
        days_in_year = 365.25
        days_in_month = days_in_year / 12

        years = int(self._day // days_in_year)
        remaining_days = self._day % days_in_year
        months = int(remaining_days // days_in_month)
        days = int(remaining_days % days_in_month)

        return f"~ {years} ans, {months} mois et {days} jours"

    @property
    def food(self):
        """
        Retourne la nourriture.
        """
        return self._food

    @property
    def ants(self):
        """
        Retourne la liste des fourmis.
        """
        return self._ants

    @property
    def eggs(self):
        """
        Retourne la liste des œufs.
        """
        return self._eggs

    @property
    def queen(self):
        """
        Retourne la reine.
        """
        return self._queen

    @property
    def ant_count(self) -> int:
        """
        Retourne le nombre de fourmis vivantes.
        """
        return len(self._ants) + int(self._queen.is_alive)

    @property
    def dead_ant_count(self) -> int:
        """
        Retourne le nombre de fourmis mortes.
        """
        return self._born_ants - self.ant_count

    @property
    def day(self) -> int:
        """
        Retourne le jour actuel.
        """
        return self._day

    def _update_ants(self):
        """
        Met à jour les fourmis, en les faisant vieillir et manger.
        """
        self._queen.grow_older()
        self._queen.eat(self._food, hunger=self._queen.egg_laying_rate)

        for ant in self._ants:
            ant.grow_older()
            ant.eat(self._food)

        self._ants = [ant for ant in self._ants if ant.is_alive]

    def _update_eggs(self):
        """
        Met à jour tous les œufs, éclos si possible, ajoute une nouvelle fourmi à la colonie.
        """
        for egg in self._eggs:
            ant = egg.evolve()
            if isinstance(ant, Ant):
                self._ants.append(ant)
                self._born_ants += 1

        # filtre les œufs qui ont éclos ou qui sont morts
        self._eggs = [egg for egg in self._eggs if not egg.is_hatched and not egg.is_dead]

    def _lay_eggs(self):
        """
        La reine pond de nouveaux œufs si elle est en vie.
        """
        if self._queen.is_alive:
            self._eggs.extend(self._queen.lay_eggs())

    def update(self):
        """
        Update la colonie : vieillit les fourmis et les œufs et fait pondre de nouveaux œufs.
        """
        self._update_ants()
        self._update_eggs()
        self._lay_eggs()
        self._day += 1
