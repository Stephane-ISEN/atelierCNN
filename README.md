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
```python

UPLOAD_FOLDER = "satelite_images"   # Path to the folder where the images will be uploaded

LABELS = {0:"nuageux", 1:"désert", 2:"forêt", 3:"mer"}

DB_NAME = "cnn"
DB_USER = "cnn_user"
DB_PASSWORD = "cnn_pwd"
DB_HOST = "localhost"
DB_PORT = "3306"
```

ajout d'un nouveau répertoire bdd.
création d'un classe de connexion dans le fichier connexion.py
```python
import mysql.connector as mysqlpyth

from app.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

class Connexion :

    @classmethod
    def ouvrir_connexion(cls):
        cls.bdd = mysqlpyth.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_NAME)
        cls.cursor = cls.bdd.cursor(dictionary=True)
    
    @classmethod
    def fermer_connexion(cls):
        if hasattr(cls, "cursor") and cls.cursor:
            cls.cursor.close()
        if hasattr(cls, "bdd") and cls.bdd:
            cls.bdd.close()
```
création d'un modèle pour les données de prédictions
```python
from pydantic import BaseModel

class Prediction(BaseModel) :
    id : int = None
    image : str
    label : str
    commentaire : str
    modele : str
```

création d'une classe service, dans le fichier service.py

l'idée : une méthode = une requête
```python
from app.bdd.connexion import Connexion
from app.bdd.prediction import Prediction

class Service_Prediction(Connexion):

    @classmethod
    def sauvegarder_prediction(cls, prediction:Prediction):
        try:
            cls.ouvrir_connexion()
            query = "Select id from labels where label = %s"
            values = [prediction.label]
            cls.cursor.execute(query, values)
            label = cls.cursor.fetchone()["id"]

            query = "INSERT INTO predictions (image, label, commentaire, modele) VALUES (%s, %s, %s, %s)"
            values = [prediction.image, label, prediction.commentaire, prediction.modele]
            
            cls.cursor.execute(query, values)
            cls.bdd.commit()

        except Exception as e:
                print(f"Une erreur inattendue est survenue :{e}")
        
        finally:
            cls.fermer_connexion()
    
    @classmethod
    def lister_predictions(cls):
        predictions=[]

        try:
            cls.ouvrir_connexion()
            query = "SELECT predictions.image as image, labels.label as label, predictions.commentaire as commentaire, predictions.modele as modele FROM predictions JOIN labels ON predictions.label = labels.id"
            cls.cursor.execute(query)
              
            for prediction_lue in cls.cursor :
                prediction = Prediction(image=prediction_lue["image"], label=prediction_lue["label"], commentaire=prediction_lue["commentaire"], modele=prediction_lue["modele"])
                predictions.append(prediction)

        except Exception as e:
            print(f"Une erreur inattendue est survenue :{e}")
        
        finally:
            cls.fermer_connexion()
        
        return predictions
```


### modification de l'API
modifier le endpoint existant pour enregistrer les prédictions en bdd
ajout d'un nouvel edn-point qui retourne toute les prédiction.`
```python
from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os

from app.modele import cnn
from app.config import UPLOAD_FOLDER
from app.bdd.service import Service_Prediction
from app.bdd.prediction import Prediction

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()

@app.get("/")
async def index():
    return "API Prediction!"

@app.post("/predictions/satelite/")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    if not file.filename.endswith(("jpg", "jpeg", "png")):
        raise HTTPException(status_code=400, detail="Format non supporté")

    with open(file_path, "wb") as buffer :
        shutil.copyfileobj(file.file, buffer)
        
    
    label = cnn.predict_image(file_path)
    prediction = Prediction(image=file_path, label=label, commentaire="OK", modele="CNN")
    Service_Prediction.sauvegarder_prediction(prediction)

    #return {'filename':file.filename, "prediction":label}
    return {"prediction": prediction }

@app.get("/predictions/")
async def list_predictions():
    predictions = Service_Prediction.lister_predictions()
    return predictions
```

### modification du client
ajout d'un menu pour passer de la prédiction à la liste de prédiction.
affichage de la liste de prédiction.


