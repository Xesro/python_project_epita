from math import ceil
from random import random
from players.Player import Player


class Pyro(Player):
    def __init__(self, team: str):
        super().__init__("Pyro", 300, 300, team)

    # Specificity of the class:
    # The Pyro can't be burned
    def _be_burned(self):
        pass

    # Available action for the Pyro class: 
    # Burns the enemy
    def fire(self, enemy: 'Player'):
        super().attack(enemy)
        enemy._be_burned()
