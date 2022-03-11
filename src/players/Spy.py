from math import ceil
from random import random
from players.Player import Player


class Spy(Player):
    def __init__(self, team: bool):
        super().__init__("Spy", 200, 200, team)

    # Specificity of the class:
    # The Spy can be attacked by enemies from his own team
    def _receive_attack(self, enemy: 'Player'):
        self.team = not self.team
        super()._receive_attack(enemy)
        self.team = not self.team
        super()._receive_attack(enemy)

    # Available action for the Soldier class:
    # Can switch team
    def change_team(self, enemy: 'Player'):
        self.team = not self.team