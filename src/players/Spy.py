from math import ceil
from random import random
from players.Player import Player


class Spy(Player):
    def __init__(self, team: bool):
        super().__init__("Spy", 200, 200, team)

    # Can be attacked by enemies from his own team
    def receive_attack(self, enemy: 'Player'):
        self.team = not self.team
        super().receive_attack(enemy)

    # Can switch team
    def change_team(self):
        self.team = not self.team
