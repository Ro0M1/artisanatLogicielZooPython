from models.animal import Animal
from typing import Dict, List


class AnimalServices:
    def __init__(self):
        self.animals: Dict[int, Animal] = {}
        self.next_id = 1

    def recuperer_un_animal(self, id: int):
        return self.animal[id]

    def ajouter_un_animal():
        pass

    def modifier_un_animal():
        pass

    def supprimer_un_animal_par_id():
        pass
