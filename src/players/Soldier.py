from math import ceil
from random import random
from players.Player import Player


class Soldier(Player):
    def __init__(self, team: bool):
        super().__init__("Soldier", 200, 300, team)

    # Available action for the Soldier class:
    # ROCKET: probability to kill instantly the target but you can hurt yourself
    def rocket(self, enemy: 'Player'):
        # Self dammage
        if (ceil(random() * 100) <= 33):
            self.health -= random() * 10

        # Instant kill ennemy
        if (random() * 100) <= 20:
            dammage = enemy.health
            enemy.health = 0
            return dammage
        else:
            return super().attack(enemy)
