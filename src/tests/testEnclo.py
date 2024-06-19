import unittest
from models.enclos import Enclos
from services.encloService import Enclos


class TestAnimal(unittest.TestCase):

    def test_On_peut_récupérer_un_enclo_du_systeme(self):
        pass

    def test_On_peut_ajouter_un_enclo_du_systeme(self):
        enclo_services = Enclos
        enclo_1 = Enclos(id=1, nom="Enclo 1", taille="petit", especes_acceptes=["lion"])
        Enclos.ajouter_un_enclo(enclo_1)

    def test_On_peut_modifier_un_enclo_du_systeme(self):
        pass

    def test_On_peut_supprimer_un_enclo_vide_du_systeme(self):
        pass

    def test_On_ne_peut_pas_supprimer_un_enclo_non_vide_du_systeme(self):
        pass
