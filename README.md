# 🛰️ Atelier CNN - Classification d'Images Satellites  

## interrêt de structurer les données pour l'IA en passant par une bdd ?

## créer la base de données
Nous allons passer par docker pour créer une base SQL

le docker-compose
```yaml
version: "3.9"

services:
  db:
    image: mysql
    container_name: db_cnn
    environment:
      - MYSQL_ROOT_PASSWORD=example
      - MYSQL_DATABASE=cnn 
      - MYSQL_USER=cnn_user
      - MYSQL_PASSWORD=cnn_pwd
    ports:
      - 3306:3306
    volumes:
      - ./db/databases:/var/lib/mysql
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
    restart: always
  adminer:
    image: adminer
    container_name: adminer_cnn
    restart: always
    ports:
      - 8080:8080
```

le sql pour l'init de la base
```sql
-- Adminer 4.8.1 MySQL 8.2.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

USE `cnn`;

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `predictions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `label` int NOT NULL,
  `commentaire` varchar(100) NOT NULL,
  `modele` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `label` (`label`),
  CONSTRAINT `images_ibfk_1` FOREIGN KEY (`label`) REFERENCES `labels` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `labels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `labels` (`label`) VALUES
('forêt'),
('mer'),
('désert'),
('nuageux');

-- 2025-02-27 09:47:52
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


