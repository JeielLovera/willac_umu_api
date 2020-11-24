from fastapi import APIRouter
from datetime import datetime
from server.code.Data_Standardization import *
from server.code.Multilayer_Perceptron_Trainer import *
import os
import asyncio
import pyrebase
from datetime import datetime

from server.database import (
    save_weightsbias,
    weigthsbias_helper
)

APP_FOLDER = os.path.dirname(__file__)
FILES_FOLDER = os.path.dirname(APP_FOLDER)
FILES_FOLDER = os.path.join(FILES_FOLDER, 'files')


config = {
    "apiKey": 'AIzaSyBaqiZZrer3auWeVmgNelB2dSB-xUTY_QI',
    "authDomain": 'willacumufiles.firebaseapp.com',
    "databaseURL": 'https://willacumufiles.firebaseio.com',
    "projectId": 'willacumufiles',
    "storageBucket": 'willacumufiles.appspot.com',
    "messagingSenderId": '951512023033',
    "appId": '1:951512023033:web:a379668a52ac4aa6d48728',
    "measurementId": 'G-D6FPT5Y5VZ'
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
router = APIRouter()

#download the file to training data
@router.get("/{filename}")
async def getDataToTraining(filename: str):
    today = datetime.today()
    now = datetime.now()
    current = today.strftime("%d%m%y") + now.strftime("%H%M%S")
    filepath = "\{time}data_training.csv".format(time=current)
    storage.child('files/'+filename).download(FILES_FOLDER+filepath)
    return {"filename": str(current)+"data_training.csv"}

#save the weights and bias to MongoDB, and upload the img of errors after training
@router.post("/{filename}")
async def postWeightsBias(filename: str):
    today = datetime.today()
    now = datetime.now()
    current = today.strftime("%d%m%y") + now.strftime("%H%M%S")
    Standardization(FILES_FOLDER+"/"+filename, current)
    (hw, hb, ow, ob) = Multilayer_Perceptron_Trainer(current)
    jsonStr = {
        "hidden_weights": hw,
        "hidden_bias": hb,
        "output_weights": ow,
        "output_bias": ob
    }
    response = await save_weightsbias(jsonStr)
    imgfile = "/{time}error.png".format(time=current)
    storage.child("files"+imgfile).put(FILES_FOLDER+imgfile)
    return { "id_weightsbias": response["_id"], "img_error": str(current)+"error.png"}


