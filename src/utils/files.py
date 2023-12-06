"""
Ce module contient des fonctions pour gérer les fichiers
"""

import os
import json
import datetime
from typing import List

from src.classes.settings import SAVE_DIRECTORY
from src.classes.colony import Colony


def __ensure_save_directory_exists():
    """
    Vérifie que le dossier de sauvegarde existe
    """
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)


def list_save_files() -> List[str]:
    """
    Liste les fichiers de sauvegarde disponibles
    """
    __ensure_save_directory_exists()

    files = os.listdir(SAVE_DIRECTORY)
    sim_files = [
        file for file in files if file.endswith(".json") and file.startswith("sim_")
    ]
    sim_map = {}

    for index, file in enumerate(sim_files, start=1):
        unique_id = file.replace("sim_", "").replace(".json", "")
        sim_map[str(index)] = unique_id

    return sim_map


def load_save_file(unique_id: str) -> dict:
    """
    Charge un fichier de sauvegarde
    """
    file_path = f"{SAVE_DIRECTORY}/sim_{unique_id}.json"
    if not os.path.exists(file_path):
        raise FileNotFoundError("The file you are trying to load does not exist")

    with open(file_path, "r", encoding="utf8") as file:
        return json.load(file)["settings"]


def create_save_file(colony: Colony) -> str:
    """
    Crée un fichier de sauvegarde
    """
    __ensure_save_directory_exists()

    unique_id = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"{SAVE_DIRECTORY}/sim_{unique_id}.json"
    with open(file_path, "w", encoding="utf8") as file:
        json.dump(
            {
                "settings": colony.settings.to_dict(),
                "colony": colony.to_dict(),
            },
            file,
            indent=2,
        )

    return unique_id
