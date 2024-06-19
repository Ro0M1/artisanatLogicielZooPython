from enum import Enum


class Taille(Enum):
    PETIT = "petit"
    MOYEN = "moyen"
    GRAND = "grand"


class Enclos:
    def __init__(
        self, id: int, nom: str, taille: Taille, especes_acceptes: list
    ) -> None:
        self.id = id
        self.nom = nom
        self.taille = taille
        self.especes_acceptes = especes_acceptes
