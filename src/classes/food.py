class Food:
    """
    Représente les réserves de nourriture de la colonie.
    """

    def __init__(self, initial_quantity: int):
        self._quantity = initial_quantity

    def __str__(self):
        return f"Nourriture: {self._quantity}\n"

    @property
    def quantity(self) -> int:
        return self._quantity

    def consume(self, amount: int):
        self._quantity = max(self._quantity - amount, 0)

    def add(self, amount: int):
        self._quantity += amount
