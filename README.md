# ChenapandasProject



# Welcome to PS visualization

Ce projet a été effectué par Hugo Santos (Chenapanda) et Philémon Duval (Philouduv).

	Il prend en entré des documents:
		- un json nommé "sherpas.json" contenant la liste des sherpas
		- un csv nommé "Liste_leads.csv" contenant la liste des lead/binome de chaque projet
		- un excel nommé "EFFECTIFS_CAMPUS.xlsx" contenant pour chaque campus les étudiants par groupe travaillant sur les projets avec les sherpas associés


Ce programme permet  en sortie d'avoir une visualisation sur neo4j de l'ensemble des acteurs de chaque projet (Lead, Binôme, Sherpa, equipe d'étudiants)

# Fonctionnement

Pour utiliser ce programme, il faudra pull le projet
	
	git clone {adresse du repository}
	git pull

Dans un second temps il faudra avoir d'installer dans un environnement local ou bien sur la machine concerné:
		
	- python3
	- neomodel
	- neo4j
	- csv
	- json
	- openpyxl	

une fois ces librairies installées, il faut avoir installé neo4j

https://neo4j.com/download/

L'installer et lancer une base de donnée.

Une fois ces pré-requis finit, il suffira de lancer le main du programme avec les fichiers d'entrée dans le même dossier (par défaut présent sur le git).
		

# Choix des librairies

Pour ce qui est de neo4j nous avons utilisé 2 librairies.

- La première étant neomodel, nous offrait la possibilité de créer des classes représentant les nœuds et leurs attributs ce qui nous facilita énormément la tâche pour concevoir notre représentation

- La seconde, Graphdatabase, nous a offert la possibilité d'envoyer directement des commande cypher et nous a donc permis plus facilement de moduler nos relations entre les différentes classes de nœuds. De plus nous pouvions aisément à chaque nouveau test, supprimer tous les nœuds existants et ainsi éviter de nous embrouiller.

Concernant la lecture des fichiers et la récolte des données nécessaires.
- Nous avons utilisé csv et json pour lire dans les fichier correspondant.
- Par contre, pour le dernier excel, nous avons dû utiliser la librairie openpyxl pour pouvoir lire les différentes feuilles de l'excel et créer une lecture générique a toutes ces dernières.


# Choix de développement

Nous avons complètement changer la manière de créer les nœuds projets ainsi que Sherpa en cours de route. En effet nous avions commencé par gérer les fichiers "Leads.csv" ainsi que "sherpa.json". Cependant il y avait beaucoup d'informations manquantes et au final ne nous aidait pas à reconnecter l'excel de la fin. C'est pourquoi , notre approche a été de parser dans un premier temps l'énorme excel avec chaque feuille, de vérifier que les nœuds projets/sherpas n'était pas déjà présent en se servant des fichiers json comme vérificateur. une fois ce file parsé, il ne nous restait plus qu'a créer tous les nœuds correspondant sur chaque projet. A la suite de quoi, nous avons utiliser le fichier lead pour associer à chaque projet un binôme d'étudiants d'EPITA.

# Pour le futur

Nous aurions aimé avec plus de temps pouvoir développer un petit programme qui permet de détecter les changement d'orthographe d'un fichier à un autre ce qui nous aurait économiser un temps précieux sur le test de chaque fichier, car si deux projets s'écrivent de deux manière différentes car l'auteur s'est trompé, alors sur neo4j nous avons deux projets distincts créés. Nous avons cependant pallier au problème sur le cours terme en alignant dans chaque fichier utilisé l'orthographe.
