from enum import Enum
from pydantic import BaseModel


class Taille(Enum):
    PETIT = "petit"
    MOYEN = "moyen"
    GRAND = "grand"


class Enclos(BaseModel):
    id: int
    nom: str
    taille: Taille
    especes_acceptes: list
