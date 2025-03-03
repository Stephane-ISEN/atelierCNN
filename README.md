# 🛰️ Atelier CNN - Classification d'Images Satellites  

## **Introduction à Docker et ses concepts clés**  

Pour l'installation, voir le [site officiel](https://www.docker.com/).

Docker est une **technologie de conteneurisation** qui permet d’exécuter des applications de manière **isolée, portable et reproductible**. Il facilite le déploiement en encapsulant **le code, les dépendances et la configuration** dans des **conteneurs**.

---

### **1. Qu'est-ce qu'un conteneur Docker ?**  
Un **conteneur** est une unité logicielle **légère et isolée** qui contient tout le nécessaire pour exécuter une application (**code, librairies, dépendances, configuration**). Il fonctionne indépendamment du système d’exploitation sous-jacent.  

---

### **2. Qu'est-ce qu'une image Docker ?**  
Une **image Docker** est un **modèle pré-configuré** qui contient le **code de l’application, son environnement et ses dépendances**.  

 Exemple :  
```bash
docker pull python:3.9  # Récupère l'image Python 3.9
docker run python:3.9  # Lance un conteneur basé sur cette image
```

Vous pouvez trouver de nombreuses images utilisables sur le [DockerHub](https://hub.docker.com/).

---

### **3. Qu'est-ce que Docker Compose ?**  
**Docker Compose** est un outil qui permet de gérer **plusieurs conteneurs** avec un seul fichier **`docker-compose.yml`**. Il est utile pour définir des architectures complexes (ex : **API + Base de données**).  

 **Exemple : Lancer une API FastAPI avec MySQL en un seul fichier :**
```yaml
version: '3.9'

services:
  web:
    image: my-fastapi-app
    ports:
      - "8080:80"
  db:
    image: mysql
    environment:
      - MYSQL_ROOT_PASSWORD=example
```
 Une seule commande pour tout démarrer :
```bash
docker-compose up -d
```

---

### **Résumé**
| **Concept** | **Définition** |
|------------|--------------|
| **Docker** | Plateforme permettant de conteneuriser des applications. |
| **Conteneur** | Instance d’une image Docker qui exécute une application de manière isolée. |
| **Image Docker** | Modèle qui contient l’application et ses dépendances. |
| **Docker Compose** | Outil pour orchestrer plusieurs conteneurs avec un fichier `docker-compose.yml`. |

## Conteneurisation de notre API CNN
Commencer par mettre à jour les dépendances avec la commande `pip freeze > requirements.txt`.
L'image utilisée pour le conteneur sera créée à partir d'une image Python, grâce au Dockerfile suivant : 
```dockerfile
FROM python:3.11

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN 
COPY
```
Vérifiez, tout de même, que la version Python de l'image correspond à celle que vous utilisez.
Compléter les deux dernières lignes, pour que le `RUN`lance un pip install à partir du requirements et copier le code du répertoire ``app`` vers ``code\app``.

le `.dokerignore`est vide. Il faut y ajouter les chemins des répertoire à ignorer. Dans notre cas, l'environnement virtuel et les __pycache__.

il reste plus qu'à préparer le docker-compose : 
```yaml
version: "3.9"

services:
  web:
    build:
      context: .  # Chemin vers le répertoire contenant le Dockerfile
      dockerfile: Dockerfile  # Facultatif si le fichier s'appelle Dockerfile
    container_name: api_cnn
    volumes:
      - ./app:/code/app  # Recharge le code source en direct (optionnel)
    environment:
      - PYTHONUNBUFFERED=1  # Assure que les logs apparaissent immédiatement dans la console
    command:
```
Ce fichier **Docker Compose** définit un **service web** qui exécute une **API FastAPI** à l'intérieur d'un **conteneur Docker**. Il configure l’image, les ports, les volumes et les variables d’environnement : 
- `3.9` est une version récente et stable.
- Crée un service nommé `web`, qui correspond à l’API FastAPI.
- Indique comment construire l’image Docker : 
- Configuration de l’image Docker : 
    - `context: .` → La construction se fait à partir du répertoire actuel (`.`).  
    - `dockerfile: Dockerfile` → Spécifie le fichier `Dockerfile` à utiliser (optionnel si nommé `Dockerfile`).  
- Nom du conteneur
- Configuration des ports : à vous de la remplir pour faire correspondre votre port au port 80, en interne.
- Le volume permet d’utiliser les fichiers du système hôte dans le conteneur. Il faut en rajouter 2 : un pour le requirement et l'autre pour le répertoire d'image `satelite_images`.
- Il reste à compléter ``command:`` pour démarer l'API grâce au serveur unicorn. Attention, il vaut mieux écrire la commande en JSON : ['uvicorn',...]

**Comment utiliser ce `docker-compose.yml` ?**
- Construire et démarrer le conteneur : ``docker-compose up -d``
- Vérifier que le conteneur tourne : ``docker ps``
- Tester l’API dans le navigateur, sur l'url `` http://localhost:8081/docs``
- vous pouvez stopper le conteneur : ``docker-compose down``
