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