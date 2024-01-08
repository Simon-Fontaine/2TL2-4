import unittest


from src.classes.egg import Egg
from src.classes.settings import Settings
from src.classes.food import Food
from src.classes.enums import State

class TestEgg(unittest.TestCase):

    def setUp(self):
        # Create a Settings instance for testing
        self.settings = Settings()

        # Create a Food instance with some quantity for testing
        self.food = Food(self.settings)  # Pass the Settings instance to the Food constructor

    def test_egg_initialization(self):
        # Create an Egg instance
        egg = Egg(self.settings, self.food, is_queen_egg=True)

        # Check if the properties are correctly set
        self.assertEqual(egg.age, 0)
        self.assertTrue(0 <= egg.max_age <= self.settings.queen_avg_egg_age  + self.settings.queen_avg_egg_age_variation)
        self.assertEqual(egg.state, State.ALIVE)
        self.assertTrue(egg.is_queen_egg)
        self.assertEqual(egg.is_alive, True)

    def test_egg_evolve(self):
        # Create an Egg instance
        egg = Egg(self.settings, self.food, is_queen_egg=False)

        # Set age to the maximum to force evolve
        egg.age = egg.max_age

        # Force evolve and check the result
        evolved_ant = egg.evolve()
        self.assertIsNotNone(evolved_ant, "Regular egg should not evolve into an ant")  # Since it's not a queen egg, it should return None

        # Create a Queen Egg instance
        queen_egg = Egg(self.settings, self.food, is_queen_egg=True)

        # Set age to the maximum to force evolve
        queen_egg.age = queen_egg.max_age

        # Force evolve and check the result
        evolved_queen = queen_egg.evolve()
        self.assertIsNotNone(evolved_queen)  # Queen egg should evolve into a Queen instance

if __name__ == '__main__':
    unittest.main()
