from models.animal import Animal
from models.animal import Enclos
from typing import Dict, List


class AnimalServices:
    def __init__(self):
        self.animaux: Dict[int, Animal] = {}
        self.id = 1

    def recuperer_un_animal(self, id: int):
        if id in self.animaux:
            return self.animaux[id]
        else:
            return None

    def récuperer_tous_les_animaux(self):
        return self

    def ajouter_un_animal(self, nouvel_animal: Animal):
        if nouvel_animal.id not in self.animaux:
            self.animaux[nouvel_animal] = nouvel_animal
        else:
            return

    def modifier_un_animal():
        pass

    def supprimer_un_animal_par_id():
        pass
