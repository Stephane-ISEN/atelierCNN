import torch
from torchvision import models, transforms
from PIL import Image

from app.config import LABELS

def predict_image(file_path):
    # Charger le modèle PyTorch
    try:
        # Recréer l'architecture du modèle VGG16
        model = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.DEFAULT)  # False car on charge nos propres poids
        #    Modifier la dernière couche du classificateur pour correspondre aux poids entraînés
        num_classes = 4  # Mettre le bon nombre de classes
        model.classifier[3] = torch.nn.Linear(in_features=1024, out_features=num_classes)


        model.load_state_dict(torch.load("./app/modele/vgg16_finetuned.pth", map_location=torch.device("cpu")), strict=False)  # Charger les poids
        model.eval()  # Mode évaluation pour la prédiction

        #model = torch.load('vgg16_finetuned.pth', map_location=torch.device("cpu"))  # Charger sur CPU
        #model.eval()  # Mettre le modèle en mode évaluation
    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement du modèle : {e}")

    transform = transforms.Compose([
        transforms.Resize((128, 128)),  # Resize images
        transforms.ToTensor(),          # Convert images to tensors
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalize to [-1, 1]
    ])

    image = Image.open(file_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    output = model(image)
    _, predicted = torch.max(output, 1)

    return LABELS[predicted.item()]