import unittest
from models.animal import Animal
from models.enclos import Enclos
from services.animalServices import AnimalServices

ENCLO = Enclos(1, "Enclo 1", "moyen", ["lion", "tigre"])


class TestAnimal(unittest.TestCase):

    def On_peut_récupérer_un_animal_du_systeme(self):
        service = AnimalServices()
        # Lorsque je donne un id d'animal
        animal_recherche = service.recuperer_un_animal()
        self.assertNotEqual(animal_recherche, None)

    def On_peut_rajouter_un_animal_au_sytème(self):
        service = AnimalServices()
        # Lorsque je donne un animal avec un enclo existant
        animal = service.ajouter_un_animal(1, "lion", "félin", 10, ENCLO)
        # Un animaml est rajouté au système avec les infos saisies
        self.assertEqual(animal.id, 1)
        self.assertEqual(animal.nom, "Lion")
        self.assertEqual(animal.espece, "félin")
        self.assertEqual(animal.age, 5)
        self.assertEqual(animal.enclos, ENCLO)

    def On_peut_modifier_un_animal(self):
        service = AnimalServices()
        animal = service.ajouter_un_animal(1, "lion", "félin", 10, ENCLO)
        animal_modifié = service.modifier_un_animal(1, age=12)
        # Je récupére un animal modifié
        self.assertEqual(animal_modifié.id, animal.id)
        self.assertEqual(animal_modifié.age, animal.age)

    def On_peut_supprimer_un_animal_du_système(self):
        service = AnimalServices()
        animal = service.ajouter_un_animal(1, "lion", "félin", 10, ENCLO)
        animal_a_supprimer = service.supprimer_animal_par_id(1)
        self.assertEqual(service.recuperer_un_animal(1), None)


if __name__ == "__main__":
    unittest.main()
