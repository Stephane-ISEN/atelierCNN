from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os

from app.modele import cnn
from app.config import UPLOAD_FOLDER

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
    
    return {'filename':file.filename, "prediction": label}
