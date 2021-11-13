Dans le cadre du module "deploiement" de la formation Fulstack Jedha, il s'agit de mettre en production un modèle de prédiction de la qualité du vin sur la base d'éléments physico-chimiques.
Ces indicateurs sont les suivants : 
* "acidité fixe"
* "acidité volatile"
* "acide citrique"
* "sucre résiduel"
* "chlorures"
* "anhydride sulfureux libre"
* "anhydride sulfureux total"
* "densité"
* "pH"
* "sulfates"
* "alcool"

Cette application est en ligne à l'adresse https://wine-quality-prediction-21.herokuapp.com/

Les points suivant peuvent créer des difficultés  et voici leur solution : 
* Bien penser à créer un Procfile pour Heroku ici : gunicorn app:app. le serveur Gunicorn est largement compatible avec de nombreux framework web, il est simple à mettre en œuvre, peu gourmand en ressources serveur et assez rapide.
* pip install gunicorn avant de générer correctement le fichier requirements.txt grace à la commande pip freeze requirements.txt
* En cas de mauvaise initialisation de git : sur windows la solution passe par la commande wsl rm -rf .git 
* commandes magiques sur github : git pull    /  git add .    /     git commit -m "add xxxx"         / git push
