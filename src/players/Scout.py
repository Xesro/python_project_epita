from math import ceil
from random import random
from players.Player import Player


class Scout(Player):
    def __init__(self, team: bool):
        super().__init__("Scout", "300", "100", team)

    # BONK
    def attack(self, enemy: 'Player'):
        return super()._attack(enemy) * 2 * ceil(random())

    def receive_attack(self, enemy: 'Player'):
        if (ceil(random()) == 1):
            super().receive_attack(enemy)
