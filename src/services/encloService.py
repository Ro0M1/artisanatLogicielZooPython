from models.enclos import Enclos
from typing import Dict, List


class AnimalServices:
    def __init__(self):
        self.enclos: Dict[int, Enclos] = {}
        self.id = 1
