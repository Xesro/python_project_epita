from math import ceil
from random import random


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

    def _attack(self, enemy: 'Player'):
        if (enemy.team != self.team):
            enemy.health -= max(0, self.force - enemy.armor)
            rand = int(random() * 100)

            if (rand <= 25 or enemy.armor == 1):
                enemy.armor = 0
            else:
                enemy.armor -= 1
            self._farm_xp()
            return rand
        return 0

    def receive_attack(self, enemy: 'Player'):
        enemy._attack(self)
        return self.isDead()

    def isDead(self):
        if self.health <= 0:
            return True
        else:
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
        return f'{self.name} has {self.health} health, {self.force} force, and {self.armor} armor.'
