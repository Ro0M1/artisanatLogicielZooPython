import unittest
from models.enclos import Enclos
from services.encloService import EnclosService

class TestEnclos(unittest.TestCase):

    def setUp(self):
        # Créer un service pour gérer les enclos, qui pourrait être un singleton ou une instance partagée
        self.enclos_service = EnclosService()
        self.enclos_1 = Enclos(id=1, nom="Enclos 1", taille="petit", especes_acceptes=["lion"])
        self.enclos_2 = Enclos(id=2, nom="Enclos 2", taille="moyen", especes_acceptes=["ours"])

    def test_on_peut_récupérer_un_enclos_du_systeme(self):
        # Ajouter un enclos pour test
        self.enclos_service.ajouter_un_enclos(self.enclos_1)
        result = self.enclos_service.get_enclos(1)
        self.assertEqual(result, self.enclos_1)

    def test_on_peut_ajouter_un_enclos_du_systeme(self):
        self.enclos_service.ajouter_un_enclos(self.enclos_1)
        result = self.enclos_service.get_enclos(1)
        self.assertEqual(result, self.enclos_1)

    def test_on_peut_modifier_un_enclos_du_systeme(self):
        self.enclos_service.ajouter_un_enclos(self.enclos_1)
        # Modifier les propriétés de l'enclos
        self.enclos_1.nom = "Enclos 1 Modifié"
        self.enclos_service.modifier_un_enclos(self.enclos_1)
        result = self.enclos_service.get_enclos(1)
        self.assertEqual(result.nom, "Enclos 1 Modifié")

    def test_on_peut_supprimer_un_enclos_vide_du_systeme(self):
        self.enclos_service.ajouter_un_enclos(self.enclos_1)
        self.enclos_service.supprimer_un_enclos(1)
        result = self.enclos_service.get_enclos(1)
        self.assertIsNone(result)

    def test_on_ne_peut_pas_supprimer_un_enclos_non_vide_du_systeme(self):
        self.enclos_service.ajouter_un_enclos(self.enclos_2)
        with self.assertRaises(ValueError):
            self.enclos_service.supprimer_un_enclos(2)

if __name__ == '__main__':
    unittest.main()
