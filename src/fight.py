
from math import ceil
from random import random
from players.Medic import Medic
from players.Pyro import Pyro
from players.Scout import Scout
from players.Solider import Soldier
from players.Spy import Spy

redTeamCanPlay = True


red_team = [Medic(True), Pyro(True), Scout(True), Soldier(True), Spy(True)]
blue_team = [Medic(False), Pyro(False), Scout(
    False), Soldier(False), Spy(False)]

while(True):
    redTeamCanPlay = not redTeamCanPlay

    playingTeam = red_team if redTeamCanPlay else blue_team
    otherTeam = blue_team if not redTeamCanPlay else red_team
    playerIndex = ceil(
        random() * (len(playingTeam)-1))
    player = playingTeam[playerIndex]

    # PRINT current player
    print("C'est au tour de " + player.name + " de la team " +
          ("RED" if player.team else "BLUE") + " de jouer.")

    # Update status
    player.updateStatus()

    # If is dead
    if player.isDead():
        red_team.pop(
            playerIndex) if redTeamCanPlay else blue_team.pop(playerIndex)
        print(player.name + "de la team " +
              "RED" if player.team else "BLUE" + " est mort.")
    else:
        while 1:
            action = input("Quelle action voulez vous faire ?\n")
            print("Voici vos alliés")
            for a in playingTeam:
                print(a.name + " a encore " +
                      str(a.health) + " points de vie")
            print("Voici vos ennemis")
            for a in otherTeam:
                print(a.name + " a encore " +
                      str(a.health) + " points de vie")

            if hasattr(player, action):  # Si l'action existe dans la classe
                # get target
                while 1:
                    target = input("Qui souhaitez vous attaquer ?\n")
                    if(target in otherTeam):
                        break
                    else:
                        print("Le joueur n'existe pas dans l'equipe adverse")
                result = getattr(playingTeam[target], action)(player)
                if otherTeam[target].isDead():
                    otherTeam.pop(target)
                    print(target + " est mort")
                break

            else:
                print("Cette action n'est pas disponible")
