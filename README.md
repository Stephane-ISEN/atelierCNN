# atelierCNN


Maintenant que nous savons comment sont constitués les CNN, pourquoi ils sont si puissants sur les images, nous savons en plus créer et entrainer un de ces modèles "from scratch". 

Nous avons obtenu des performances tout à faire intéressantes, mais peut-on faire mieux ?

Depuis quelques années, la mise à disposition de modèles de taille gigantesques ayant été entrainé sur de grands datasets permet une nouvelle approche, le fine-tuning. L'idée est de partir de ces modèles, qui n'ont pas été entrainés à reconnaitre ce qui nous intéresse, et de modifier leurs poids pour correspondre à nos besoins tout en profitant de tout son "savoir" sur des caractéristiques de bas et de haut niveau.

Cette approche est réputée souvent meilleure que l'entrainement from scratch, celà va-t-il se confirmer pour notre cas d'usage ?
