# 🛰️ Atelier CNN - Classification d'Images Satellites
Après avoir vu comment préparer les données pour l'apprentissage d'un CNN, il est l'heure de se pencher sérieusement sur ce qu'est un CNN.

## La convolution
Nous commencerons par aborder les briques élémentaires qui font sa spécificité. La convolution en est une, et nous l'illustrerons en manipulant cet outil sur Excel, afin de comprendre comment cet opérateur mathématique peut extraire textures et caractéristiques dans une image.
téléchargez les fichiers suivants : 

-[supports/CNN sur MNIST.xlsm](https://github.com/Stephane-ISEN/atelierCNN/blob/ch3_cnn_zero/supports/CNN%20sur%20MNIST.xlsm) 
-[supports/Visualisation d'une convolution - fonction d'activation.xlsm](https://github.com/Stephane-ISEN/atelierCNN/blob/ch3_cnn_zero/supports/Visualisation%20d'une%20convolution%20-%20fonction%20d'activation.xlsm) 
-[supports/Visualisation d'une convolution.xlsm](https://github.com/Stephane-ISEN/atelierCNN/blob/ch3_cnn_zero/supports/Visualisation%20d'une%20convolution.xlsm)

## Présentation détaillée du CNN
[Appronfondissement du CNN](https://github.com/Stephane-ISEN/atelierCNN/blob/ch3_cnn_zero/supports/cnn_prez.pdf) avant d'aborder la pratique.

## Un CNN à partir de zéro
Dans cette deuxième partie, nous allons développer un modèle CNN "from scratch", afin de classifier correctement des images satellitaires de 4 types : désert, foret, océan et nuageux.

Participez à l'atelier en téléchargeant le notebook : (cnn/notebooks/notebook2_SatelliteImages_Classification_avec_trous.ipynb)[https://github.com/Stephane-ISEN/atelierCNN/blob/ch3_cnn_zero/cnn/notebooks/notebook2_SatelliteImages_Classification_avec_trous.ipynb], suivez les étapes pas à pas et créez un CNN complet.

Les étapes à suivre sont :
- **Importer les librairies utiles pour l'atelier**
- **Vérifier la présence de capacité de calcul GPU sur l'ordinateur**
- **Charger le Dataset et transformation des données pour qu'elles soient utilisables par un modèle CNN**
- **Construir l'architecture du CNN**
- **Entrainement**
- **Evaluer du modèle sur les données de Test, données extérieures à l'apprentissage**

## Navigation
- [Chapitre 2 : préparation des données](https://github.com/Stephane-ISEN/atelierCNN/tree/ch2_prepa_data)
- [Chapitre 4 : Finetuning d'un CNN](https://github.com/Stephane-ISEN/atelierCNN/tree/ch4_cnn_finetuning)
