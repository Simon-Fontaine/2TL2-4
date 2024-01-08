import unittest
from src.classes.food import Food
from src.classes.settings import Settings

class TestFood(unittest.TestCase):

    def setUp(self):
        # Create a Settings instance for testing
        self.settings = Settings()

    def test_food_initialization(self):
        # Create a Food instance
        food = Food(self.settings)

        # Check if the initial quantity is set correctly
        self.assertEqual(food.quantity, self.settings.initial_food_quantity)

    def test_food_addition(self):
        # Create a Food instance
        food = Food(self.settings)

        # Add some quantity of food
        food.add(10)

        # Check if the quantity is updated correctly
        self.assertEqual(food.quantity, self.settings.initial_food_quantity + 10)

    def test_food_removal(self):
        # Create a Food instance with initial quantity
        food = Food(self.settings)
        initial_quantity = food.quantity

        # Remove some quantity of food
        food.remove(5)

        # Check if the quantity is updated correctly
        self.assertEqual(food.quantity, max(initial_quantity - 5, 0))

    def test_food_quantity_validation(self):
        # Create a Food instance
        food = Food(self.settings)

        # Try setting a negative quantity, should raise a ValueError
        with self.assertRaises(ValueError):
            food.quantity = -5


        self.assertGreaterEqual(food.quantity, 0)

if __name__ == '__main__':
    unittest.main()
