from math import ceil
from random import random
from players.Medic import Medic
from players.Pyro import Pyro
from players.Scout import Scout
from players.Soldier import Soldier
from players.Spy import Spy
from random import randrange
redTeamCanPlay = True


#red_team = [Medic(True), Pyro(True), Scout(True), Soldier(True), Spy(True)]
#blue_team = [Medic(False), Pyro(False), Scout(
#    False), Soldier(False), Spy(False)]
red_team = [Soldier(True), Medic(True)]
blue_team = [Soldier(False), Medic(False)]
while(True):
    redTeamCanPlay = not redTeamCanPlay


    playingTeam = red_team if redTeamCanPlay else blue_team
    otherTeam = red_team if not redTeamCanPlay else blue_team
    playerIndex = ceil(
        random() * (len(playingTeam)-1))
    player = playingTeam[playerIndex]

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
            print("\nVotre équipe est composée de")
            for a in playingTeam:
                print(a)
            print("\nLes membres restant de l'équipe adverse sont :")
            for a in otherTeam:
                print(a)
                # PRINT current player
            print("\nC'est au tour de " + player.name + " de la team " +
                  ("RED" if player.team else "BLUE") + " de jouer.")
            action = input("Quelle action voulez vous faire ? " + "(Entrez: \'attack\' ou une capacité de la classe)" + "\n")
            if hasattr(player, action):  # Si l'action existe dans la classe
                # Get target
                while 1:
                    target = input("Quelle est votre cible?\n")
                    otherIndex = -1
                    for i in range(len(otherTeam)):
                        if otherTeam[i].name == target:
                            otherIndex = i
                            break
                    if otherIndex == -1:
                        print("Le joueur n'existe pas dans l'equipe adverse")
                    else:
                        break
                getattr(player, action)(otherTeam[otherIndex])
                if otherTeam[otherIndex].isDead():
                    otherTeam.pop(otherIndex)
                break

            else:
                print("Cette action n'est pas disponible")
    if len(red_team) == 0:
        print()
        print("Victoire de l'équipe bleue")
        break
    if len(blue_team) == 0:
        print()
        print("Victoire de l'équipe rouge")
        break
