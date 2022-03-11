# python_project_epita
=======

Deux équipes composées de divers personnages s'affrontent.

Les joueurs disposent des propriétés communes suivantes:

-Points de vie (Un joueur disparait définitivement s'il n'a plus de vie)
-Points de force (Propre à chaque classe)
-Points d'expérience (Ceux ci sont incrémentés lorsqu'une attaque est réussie et augmentent la force)

5 classes distinctes héritant de la classe Player ont été implémentées:


- Pyro: 	Possibilité d'infliger des dégats sur plusieurs tours (en brûlant l'ennemi)
		De plus cette classe est insensible aux brûlures
                Compétence spéciale : fire

- Scout: 	Probabilité de coût critique doublant les dégats infligés
		Probabilité d'éviter une attaque adverse
                Compétence spéciale : bonk

- Medic: 	Peut soigner ses alliers en les visants
                Compétence spéciale : heal
- Soldier:	Probabilité de tuer instantanément l'ennemi viser.
		Mais il a une probabilité de lui même s'infliger des dégats. 
                Compétence spéciale : rocket

- Spy: 	        Il peut changer temporairement d'équipe
		Mais il peut subir des attaques de sa propre équipe.
                Compétence spéciale : change_team
Déroulé d'un combat:
Pour commencer, on lance le scénario en lancant le fichier fight.py
On a décidé d'initialiser deux petites équipe de 2 personnages chacun
afin que les scénarios ne s'étendent pas en longueur et qu'ils soient
compréhensibles. 

Dans cet exemple, les deux personnages initialisés dans chaque équipe sont un
soldat ainsi qu'un medic. L'objectif à terme serait de pouvoir sélectionner des
personnages pour les affrontements. 

Le combat se déroule au tour par tour, on choisit quelle compétence on utilise
et sur qui on souhaite l'utiliser. 
