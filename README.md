# python_project_epita
=======

Deux équipes composées de 10 joueurs s'affrontent.

Les joueurs disposent des propriétés communes suivantes:

-Points de vie (Un joueur disparait définitivement s'il n'a plus de vie)
-Points de force (Propre à chaque classe)
-Points d'expérience (Ceux ci sont incrémentés lorsqu'une attaque est réussie et augmentent la force)

5 classes distinctes héritant de la classe Player ont été implémentées:


- Pyro: 	Possibilité d'infliger des dégats sur plusieurs tours (en brûlant l'ennemi)
		De plus cette classe est insensible aux brûlures

- Scout: 	Probabilité de coût critique doublant les dégats infligés
		Probabilité d'éviter une attaque adverse

- Medic: 	Peut soigner ses alliers en les visants

- Soldier:	Probabilité de tuer instantanément l'ennemi viser.
			Mais il a une probabilité de lui même s'infliger des dégats. 

- Spy: 	Il peut changer temporairement d'équipe
		Mais il peut subir des attaques de sa propre équipe.

Déroulé d'un combat:
