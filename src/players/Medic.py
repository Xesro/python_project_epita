from random import random
from players.Player import Player


class Medic(Player):
    def __init__(self, team: bool):
        super().__init__("Medic", 180, 100, team)

    # Available action for the Medic class: 
    # Heal: give back 10 health
    def heal(self, player: 'Player'):
        player.health += 10
