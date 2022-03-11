from math import ceil
from random import random
from players.Player import Player


class Pyro(Player):
    def __init__(self, team: str):
        super().__init__("Pyro", 300, 300, team)

    # FIRE: burn the enemy
    def attack(self, enemy: 'Player'):
        super().attack(enemy)
        enemy._be_burned()

    # The Pyro can't be burned
    def _be_burned(self):
        pass
