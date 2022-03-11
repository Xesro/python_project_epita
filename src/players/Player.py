from math import ceil
from random import random

RED = True
BLUE = False


class Player:
    def __init__(self, name: str, health: int, force: int, team: bool):
        self.name = name
        self.health = health
        self.force = force
        self.team = team
        self.armor = 0
        self.burned = 0

    def _farm_xp(self):
        self.force += ceil(random() * 10)

    def attack(self, enemy: 'Player'):
        enemy._receive_attack(self)

    def _receive_attack(self, enemy: 'Player'):
        if (enemy.team != self.team):
            rand = int(random() * 100)

            damage = self.armor - enemy.force

            self.armor = max(damage, 0)
            if (damage < 0):
                self.health += damage
            print(f'{self.name} has received {enemy.force} damage.')
            enemy._farm_xp()
            return rand
        return 0

    def isDead(self):
        if self.health <= 0:
            print(
                f'{self.name}, of the team {"RED" if self.team == RED else "BLUE"} is dead.')
            return True
        else:
            print(
                f'{self.name}, of the team {"RED" if self.team == RED else "BLUE"} is still alive.')
            return False

    def updateStatus(self):
        if self.burned > 0:
            self.burned -= 1
            if self.armor > 0:
                self.armor -= 3
            else:
                self.health -= 3

    def _be_burned(self):
        self.burned += 3
        self.burned = max(self.burned, 5)

    def __str__(self):
        return f'{self.name} of the {"RED" if self.team == RED else "BLUE"} has {self.health} health, {self.force} force, and {self.armor} armor.'
