# 🛰️ Atelier CNN - Classification d'Images Satellites  

## Docker
Pour l'installation, voir le [site officiel](https://www.docker.com/).

### 🐳 **Introduction à Docker et ses concepts clés**  

Docker est une **technologie de conteneurisation** qui permet d’exécuter des applications de manière **isolée, portable et reproductible**. Il facilite le déploiement en encapsulant **le code, les dépendances et la configuration** dans des **conteneurs**.

---

### 🔹 **1. Qu'est-ce qu'un conteneur Docker ?**  
Un **conteneur** est une unité logicielle **légère et isolée** qui contient tout le nécessaire pour exécuter une application (**code, librairies, dépendances, configuration**). Il fonctionne indépendamment du système d’exploitation sous-jacent.  

📌 **Comparaison avec une machine virtuelle :**  
✅ **Plus léger** qu’une VM (partage le noyau du système hôte).  
✅ **Démarrage rapide** (~secondes).  
✅ **Facilement portable** entre différents environnements.

---

### 🔹 **2. Qu'est-ce qu'une image Docker ?**  
Une **image Docker** est un **modèle pré-configuré** qui contient le **code de l’application, son environnement et ses dépendances**.  

📌 **Une image est un blueprint (modèle), tandis qu’un conteneur est une instance active de cette image.**  

➡️ Exemple :  
```bash
docker pull python:3.9  # Récupère l'image Python 3.9
docker run python:3.9  # Lance un conteneur basé sur cette image
```

---

### 🔹 **3. Qu'est-ce que Docker Compose ?**  
**Docker Compose** est un outil qui permet de gérer **plusieurs conteneurs** avec un seul fichier **`docker-compose.yml`**. Il est utile pour définir des architectures complexes (ex : **API + Base de données**).  

📌 **Exemple : Lancer une API FastAPI avec MySQL en un seul fichier :**
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
➡️ Une seule commande pour tout démarrer :
```bash
docker-compose up -d
```

---

### ✅ **Résumé**
| **Concept** | **Définition** |
|------------|--------------|
| **Docker** | Plateforme permettant de conteneuriser des applications. |
| **Conteneur** | Instance d’une image Docker qui exécute une application de manière isolée. |
| **Image Docker** | Modèle qui contient l’application et ses dépendances. |
| **Docker Compose** | Outil pour orchestrer plusieurs conteneurs avec un fichier `docker-compose.yml`. |

🚀 **Docker simplifie le déploiement et garantit que l’application fonctionne de la même manière sur tous les environnements !** 🔥


