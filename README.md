# 🛰️ Atelier CNN - Classification d'Images Satellites  

## interrêt de structurer les données pour l'IA en passant par une bdd ?

## créer la base de données
Nous allons passer par docker pour créer une base SQL

le docker-compose
```yaml
```

le sql pour l'init de la base
```sql
```
lancer les conteneur avec la commande docker-compose

Il est possible d'utiliser adminer pour vérifier l'existance de la base.

## modifier l'API pour passer par une bdd

### gestion de la base
modification du config.py pour ajouter les paramètres de la bdd.

ajout d'un nouveau répertoire bdd.
création d'un classe de connexion dans le fichier connexion.py

création d'une classe service, dans le fichier service.py
l'idée : une méthode = une requête

création d'un modèle pour les données de prédictions
### modification de l'API
modifier le endpoint existant pour enregistrer les prédictions en bdd
ajout d'un nouvel edn-point qui retourne toute les prédiction.

### modification du client
ajout d'un menu pour passer de la prédiction à la liste de prédiction.
affichage de la liste de prédiction.


