Fonctionnalité: showing off behave

En tant qu'Administrateur
Je veux créer des dépôts
Afin de mettre en gestion de configuration des projets

  Scénario: Créer un dépôt
    Étant donné la page de creation de depot
	Et le champ nom du depot est ASVN
	Quand je clique sur le bouton Creer
	Alors le depot SVN du projet ASVN est creer
	
  Scénario: Echec de création de dépôt
	Étant donné la page de creation de depot
	Et le champ nom du depot est vide
	Quand je clique sur le bouton Creer
	Alors j'ai l'erreur le nom du depot ne doit pas etre vide
	
  Scénario: Création d'un dépôt déjà présent	
	Étant donné la page de creation de depot
	Et le depot ASVN existe
	Et le champ nom du depot est ASVN
	Quand je clique sur le bouton Creer
	Alors j'ai l'erreur le depot ASVN est deja present