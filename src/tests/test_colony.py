"""
Ce module test la classe colony
"""

import unittest
from src.classes.colony import Colony
from src.classes.settings import Settings
from src.classes.food import Food
from src.classes.queen import Queen


class TestColony(unittest.TestCase):

    def setUp(self):
        """Set up des classes nécessaires pour les tests."""
        self.settings = Settings()
        self.food = Food(self.settings)
        self.colony = Colony(self.settings, self.food)
        self.queen = Queen(self.settings, self.food)

    def test_initial_state(self):
        """Test si la colonie est créée avec les bons attributs."""
        self.assertEqual(self.colony.day, 0)
        self.assertEqual(len(self.colony.ants), self.settings.initial_ant_quantity)
        self.assertEqual(self.colony.queen.age, 0)
        self.assertEqual(self.colony.queen.food.quantity, self.settings.initial_food_quantity)
        self.assertEqual(self.colony.queen.is_alive, True)
        self.assertEqual(len(self.colony.eggs), 0)
        self.assertEqual(self.colony.settings, self.settings)
        self.assertEqual(self.colony.food, self.food)

    def test_ant_count(self):
        self.assertEqual(self.colony.ant_count(), len(self.colony.ants) + int(self.queen.is_alive))

    def test_dead_ant_count(self):
        self.assertEqual(self.colony.dead_ant_count(), 0)

    def test_worker_count(self):
        self.assertAlmostEqual(self.colony.worker_count() / len(self.colony.ants), self.settings.ant_worker_chance, delta=0.1)

    def test_egg_count(self):
        self.assertEqual(len(self.colony.eggs), self.colony.egg_count())

    def test_evolve(self):
        self.colony.evolve()
        # Update day
        self.assertEqual(self.colony.day, 1)
        # Update food
        ants_hunger = self.settings.ant_hunger * self.colony.ant_count()
        queen_hunger = self.settings.queen_hunger * int(self.colony.queen.is_alive)
        start_food = self.settings.initial_food_quantity - ants_hunger - queen_hunger*2
        minimum = start_food + round(self.colony.worker_count() * self.settings.min_food_multiplier)
        maximum = start_food + round(self.colony.worker_count() * self.settings.max_food_multiplier)
        self.assertTrue(minimum <= self.colony.food.quantity <= maximum)
        # Update ants
        self.assertEqual(self.colony.ants[0].age, 1)
        # Update eggs
        minimum_eggs = self.settings.queen_avg_eggs - self.settings.queen_avg_egg_variation
        maximum_eggs = self.settings.queen_avg_eggs + self.settings.queen_avg_egg_variation
        self.assertTrue(minimum_eggs <= len(self.colony.eggs) <= maximum_eggs)


if __name__ == "__main__":
    unittest.main()