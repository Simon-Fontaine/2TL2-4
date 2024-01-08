"""
Ce module test la classe colony
"""

import unittest
import random

from src.classes.colony import Colony
from src.classes.settings import Settings
from src.classes.food import Food
from src.classes.queen import Queen


class TestColony(unittest.TestCase):

    def setUp(self):
        """Set up des classes nécessaires pour les tests."""
        random.seed(42)

        self.settings = Settings()
        self.food = Food(self.settings)
        self.colony = Colony(self.settings, self.food)
        self.queen = Queen(self.settings, self.food)

    def tearDown(self):
        """Réinitialise la graine après chaque test."""
        random.seed()

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
        self.assertTrue(0 <= self.colony.worker_count() <= len(self.colony.ants))

    def test_egg_count(self):
        self.assertEqual(len(self.colony.eggs), self.colony.egg_count())

    def test_evolve(self):
        self.colony.evolve()
        # check day
        self.assertEqual(self.colony.day, 1)
        # check food
        self.assertEqual(round(self.colony.food.quantity), round(30052))
        # check ants
        self.assertEqual(self.colony.ant_count(), 99)
        self.assertEqual(self.colony.worker_count(), 92)
        self.assertEqual(self.colony.dead_ant_count(), 2)
        # check queen
        self.assertEqual(self.colony.queen.is_alive, True)
        # check eggs
        self.assertEqual(self.colony.egg_count(), 429)

    def test_evolve_x4(self):
        # evolve 4x
        for i in range(1, 5):
            self.colony.evolve()

        # check day
        self.assertEqual(self.colony.day, 4)
        # check food
        self.assertEqual(round(self.colony.food.quantity), round(30073))
        # check ants
        self.assertEqual(self.colony.ant_count(), 98)
        self.assertEqual(self.colony.worker_count(), 91)
        self.assertEqual(self.colony.dead_ant_count(), 3)
        # check queen
        self.assertEqual(self.colony.queen.is_alive, True)
        # check eggs
        self.assertEqual(self.colony.egg_count(), 429)

    def test_evolve_x20(self):
        for i in range(1, 21):
            self.colony.evolve()

        # check day
        self.assertEqual(self.colony.day, 20)
        # check food
        self.assertEqual(round(self.colony.food.quantity), round(30779))
        # check ants
        self.assertEqual(self.colony.ant_count(), 608)
        self.assertEqual(self.colony.worker_count(), 573)
        self.assertEqual(self.colony.dead_ant_count(), 35)
        # chek queen
        self.assertEqual(self.colony.queen.is_alive, True)
        # check eggs
        self.assertEqual(self.colony.egg_count(), 1216)


if __name__ == "__main__":
    unittest.main()