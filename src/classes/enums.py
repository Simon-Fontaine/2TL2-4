"""
Ce module contient les enums du projet
"""

import enum


class State(enum.Enum):
    """
    Etat d'une fourmi
    """

    ALIVE = 1
    DEAD = 0


class Job(enum.Enum):
    """
    Metier d'une fourmi
    """

    WORKER = 1
    NOT_WORKER = 0
