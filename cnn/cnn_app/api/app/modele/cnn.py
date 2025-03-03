import torch
from torchvision import models, transforms
from PIL import Image

LABELS = {0:"nuageux", 1:"désert", 2:"forêt", 3:"mer"}

def predict_image(file_path):
    """
    Classe une image satellite en l'une des quatre catégories : Forêts, Mer, Désert, Nuageux.

    Étapes :
    1. Charge le modèle. 
    2. Charge l'image et applique les transformations nécessaires.
    3. Effectue une prédiction à l'aide du modèle CNN.
    4. Renvoie la classe prédite avec son score de confiance.

    Paramètres :
    - file_path (str) : Chemin de l'image à classer.

    Retourne :
    - dict : Un dictionnaire contenant la classe prédite et le score de confiance.
    """
    
    try:
        # copier ici le code indiquant le modèle pytorch à utiliser

        # copier ici le code chargeant le .pth


    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement du modèle : {e}")

    # retrouver la transformation utilisée pour entraîner le modèle
    transform = 

    image = Image.open(file_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    output = model(image)
    _, predicted = torch.max(output, 1)

    return