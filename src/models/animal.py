from models.enclos import Enclos


class Animal:
    def __init__(self, id: int, nom: str, espece: str, age: int, enclo: Enclos) -> None:
        self.id = id
        self.nom = nom
        self.espece = espece
        self.age = age
        self.enclos = enclo
