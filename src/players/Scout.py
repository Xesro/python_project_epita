from math import ceil
from random import random
from players.Player import Player


class Scout(Player):
    def __init__(self, team: bool):
        super().__init__("Scout", 300, 100, team)

    # BONK
    def attack(self, enemy: 'Player'):
        total = super()._attack(enemy)
        if (ceil(random()) == 1):
            total += super()._attack(enemy)
        return total

    def _receive_attack(self, enemy: 'Player'):
        if (ceil(random()) == 1):
            super()._receive_attack(enemy)
