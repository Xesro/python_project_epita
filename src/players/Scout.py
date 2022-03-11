from math import ceil
from random import random
from players.Player import Player


class Scout(Player):
    def __init__(self, team: bool):
        super().__init__("Scout", 150, 100, team)

    # Specificity of the class:
    # The received attacks have a chance to be dodged
    def _receive_attack(self, enemy: 'Player'):
        if (ceil(random()) == 1):
            super()._receive_attack(enemy)
    
    # Available action for the Scout class:
    # bonk: this attack's damages can be doubled
    def bonk(self, enemy: 'Player'):
        total = super()._attack(enemy)
        if (ceil(random()) == 1):
            total += super()._attack(enemy)
        return total
