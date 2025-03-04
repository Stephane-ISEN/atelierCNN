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