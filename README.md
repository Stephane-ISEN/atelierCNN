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



