"""
Ce module contient une fonction pour convertir le nombre de jours en une chaîne de caractères
"""

from src.classes.settings import YEAR, MONTH, WEEK


def days_to_string(days: int) -> str:
    """
    Convertit le nombre de jours en une chaîne de caractères
    """
    years = days // YEAR
    remaining_days = days % YEAR
    months = remaining_days // MONTH
    remaining_days = remaining_days % MONTH
    weeks = remaining_days // WEEK
    remaining_days = remaining_days % WEEK

    return f"~ {years} years, {months} months, {weeks} weeks, {remaining_days} days"
