
from math import ceil
from random import random
from players.Medic import Medic
from players.Pyro import Pyro
from players.Scout import Scout
from players.Solider import Soldier
from players.Spy import Spy

redTeamCanPlay = True

if(__name__ == 'main'):
    red_team = [Medic(True), Pyro(True), Scout(True), Soldier(True), Spy(True)]
    blue_team = [Medic(False), Pyro(False), Scout(
        False), Soldier(False), Spy(False)]

    while(True):
        redTeamCanPlay = not redTeamCanPlay

        playingTeam = red_team if redTeamCanPlay else blue_team
        otherTeam = blue_team if not redTeamCanPlay else red_team
        playerIndex = ceil(
            random() * ceil(playingTeam))
        player = playingTeam[playerIndex]

        # PRINT current player
        print("C'est au tour de " + player.name + " de la team " +
              "RED" if player.team else "BLUE" + " de jouer.")

        # Update status
        player.updateStatus()
        if player.isDead():
            red_team.pop(
                playerIndex) if redTeamCanPlay else blue_team.pop(playerIndex)
            print(player.name + "de la team " +
                  "RED" if player.team else "BLUE" + " est mort.")
            continue

        # Get action to perform
        while 1:
            action = input("Quelle action voulez vous faire ?\n")
            if (action == "stats"):
                for a in playingTeam:
                    print(a.name + " a encore " + a.health + " points de vie")
            elif hasattr(player, action):
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
