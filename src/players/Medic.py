from random import random
from players.Player import Player


class Medic(Player):
    def __init__(self, team: bool):
        super().__init__("Medic", 400, 100, team)

    def heal(self, player: 'Player'):
        player.health += 10
