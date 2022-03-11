from math import ceil
from random import random
from players.Player import Player


class Soldier(Player):
    def __init__(self, team: bool):
        super().__init__("Solider", "400", "300", team)

    # HUGE ROCKET: probability to kill instantly the target but you can hurt yourself
    def attack(self, enemy: 'Player'):
        # Self dammage
        if (ceil(random() * 100) <= 33):
            self.health -= random() * 10

        # Instant kill ennemy
        if (random() * 100) <= 20:
            dammage = enemy.health
            enemy.health = 0
            return dammage
        else:
            return super()._attack(enemy) * 2 * ceil(random())
