import unittest
import sys
import os

# Ajouter le répertoire parent au sys.path pour les importations correctes
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from models.enclos import Enclos
from models.animal import Animal
from services.animalServices import AnimalServices

ENCLO = Enclos(id=1, nom="Enclo 1", taille="moyen", especes_acceptes=["lion", "tigre"])


class TestAnimal(unittest.TestCase):

    def test_On_peut_récupérer_un_animal_du_systeme(self):
        service = AnimalServices()
        # Lorsque je donne un id d'animal
        animal_recherche = service.recuperer_un_animal(1)
        self.assertEqual(animal_recherche, None)

    def test_On_peut_rajouter_un_animal_au_sytème(self):
        service = AnimalServices()
        # Lorsque je donne un animal avec un enclo existant
        animal_a_ajouter = Animal(1, "lion", "félin", 10, ENCLO)
        service.ajouter_un_animal(animal_a_ajouter)
        self.assertEqual(service.recuperer_un_animal(1), animal_a_ajouter)

    def test_On_peut_modifier_un_animal(self):
        service = AnimalServices()
        animal = service.ajouter_un_animal(1, "lion", "félin", 10, ENCLO)
        animal_modifié = service.modifier_un_animal(1, age=12)
        # Je récupére un animal modifié
        self.assertEqual(animal_modifié.id, animal.id)
        self.assertEqual(animal_modifié.age, animal.age)

    def test_On_peut_supprimer_un_animal_du_système(self):
        service = AnimalServices()
        animal = service.ajouter_un_animal(1, "lion", "félin", 10, ENCLO)
        animal_a_supprimer = service.supprimer_animal_par_id(1)
        self.assertEqual(service.recuperer_un_animal(1), None)


if __name__ == "__main__":
    unittest.main()
