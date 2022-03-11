from random import random
from players.Player import Player


class Medic(Player):
    def __init__(self, team: bool):
        super().__init__("Medic", 400, 100, team)

    # FEED: heal the target if he is in the same team else attack him
    def attack(self, enemy: 'Player'):
        if self.team == enemy.team:
            enemy.health += 10
            return -10
        else:
            return super()._attack(enemy)
