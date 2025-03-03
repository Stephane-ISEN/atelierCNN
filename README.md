# 🛰️ Atelier CNN - Classification d'Images Satellites  

## Web API
Déployer un modèle d'intelligence artificielle via une **API** permet de le rendre **accessible, scalable et facilement intégrable** dans divers systèmes sans avoir besoin de redéployer le modèle à chaque utilisation.

### 🔹 **Principaux avantages :**  
- **Accessibilité** → Toute application (web, mobile, backend) peut envoyer des requêtes et obtenir des prédictions en temps réel.
- **Scalabilité** → L’API permet d’héberger le modèle sur un serveur centralisé et de gérer plusieurs requêtes simultanément.
- **Mise à jour simplifiée** → On peut améliorer ou remplacer le modèle sans impacter les utilisateurs finaux.
- **Interopérabilité** → Le modèle peut être utilisé par des applications écrites dans différents langages (Python, JavaScript, Java…).
- **Sécurité** → L'API contrôle qui peut accéder au modèle et protège les données sensibles.  

Un modèle de **classification d’images satellites** peut être déployé sous forme d'API REST. Une application web peut alors envoyer une image via une requête **HTTP POST**, et l’API renvoie un label (`forêt`, `mer`, `désert`, `nuageux`) en réponse.

### FastAPI
**FastAPI** est un framework Python rapide et performant pour créer des **API RESTful**. Il est idéal pour exposer un modèle d'IA, car il permet de gérer facilement les requêtes HTTP, d'assurer une exécution asynchrone optimisée et d'intégrer automatiquement la documentation interactive.

### **Endpoint dans FastAPI**  
Un **endpoint** est une route définie dans FastAPI qui répond à une requête HTTP (ex: `GET`, `POST`). Il permet d’exécuter une fonction spécifique, comme recevoir une image et retourner une prédiction d’un modèle d’IA. Il structure l’API et facilite l’accès aux services.

### **Uvicorn**  
**Uvicorn** est un serveur ASGI (Asynchronous Server Gateway Interface) qui exécute les applications **FastAPI** de manière ultra-rapide et asynchrone. Il est essentiel pour servir l’API en production et gérer efficacement les requêtes entrantes.

## Développement de la Web API
Tout le code se trouve dans le répertoire ``cnn_app\api``.
- Sur votre machine créez un environnement virtuel dans ce répertoire.
- Puis installez les dépedances suivantes :
  ```bash
  pip install --upgrade -r /code/requirements.txt
  ```
- recopier le fichier ``.pth`` dans le répertoire ``cnn_app\api\app\modele``.

Le fichier ``.pth`` contient un dictionnaire d'états du modèle. Un dictionnaire d'état de modèle est un dictionnaire Python qui associe chaque couche du modèle à ses paramètres (poids et biais). Ce dictionnaire ne contient que les paramètres du modèle, pas l'architecture elle-même.

- Ouvrir le fichier ``cnn.py``.

dans le ``try`` recopier le code suivant :
```python
        # Recréer l'architecture du modèle
        model = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.DEFAULT)  # False car on charge nos propres poids
        #    Modifier la dernière couche du classificateur pour correspondre aux poids entraînés
        num_classes =  # Mettre le bon nombre de classes
        model.classifier[3] = torch.nn.Linear(in_features=1024, out_features=num_classes)
```
Ce code indique le modèle à utiliser avec le fichier ``.pth``. Ce modèle propose 1000 sortie, il faut rajouter une couche pour passer au nombre de classes utiles à notre modèle. 
**Penseez à remplir la ligne suivante ``num_classes = ``.**

Il faut ensuite charger notre dictionnaire d'état et démarer l'évaluation prédictive. Ajout``tez ce code à la suite du précédent, toujours dans le ``try``.
```python
        model_path = # Mettre le bon chemin pour le fichier pth
        model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")), strict=False)  # Charger les poids
        model.eval()  # Mode évaluation pour la prédiction
```
**Pensez à remplir la varaible ``model_path`` en indiquant le chemin de votre ``.pth``.**

Après le ``try : except : `` le code prépare l'image pour sa prédiction :
```python
# retrouver la transformation utilisée pour entraîner le modèle
    transform = 

    image = Image.open(file_path).convert("RGB")
    image = transform(image).unsqueeze(0)
```
**Pensez à retrouver la transformation de l'entrainement pour le recopier ici.**

Enfin, le code fait l'interprétation et récupère les résultats.
```python
    output = model(image)
    _, predicted = torch.max(output, 1)

    return 
```
**La variable ``predicted.item()`` contient le code de la classe ayant la meilleur prédition. Nous souhaitons que le retour de la fonction predict_image() soit une chaine de caractères grâce aux dictionnaire LABEL, qui fait conrrespondre les classes à leurs labels.**
