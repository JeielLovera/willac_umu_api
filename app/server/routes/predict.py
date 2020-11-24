from fastapi import APIRouter
from datetime import datetime
from server.code.Willaq_Umu_Prediction import *
from server.code.Data_Standardization import *
import os
import asyncio
import pyrebase
from datetime import datetime

from server.models.weights_bias import (
    WeightsBias,
    ErrorResponseModel,
)

from server.database import (
    get_weightsbias
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

@router.get("/{filename}")
async def getDataToPredict(filename: str):
    today = datetime.today()
    now = datetime.now()
    current = today.strftime("%d%m%y") + now.strftime("%H%M%S")
    filepath = "\{time}data_predict.csv".format(time=current)
    storage.child('files/'+filename).download(FILES_FOLDER+filepath)
    return { "filename": str(current)+"data_predict.csv"}

@router.post("/{id}/{filename}")
async def postDataPredicted(id: str, filename: str):
    today = datetime.today()
    now = datetime.now()
    current = today.strftime("%d%m%y") + now.strftime("%H%M%S")
    wb = await get_weightsbias(id)
    Standardization(FILES_FOLDER+"/"+filename, current)
    Predict_Inputs(current, wb["hidden_weights"], wb["hidden_bias"], wb["output_weights"], wb["output_bias"])
    predictedfile = "/{time}predicted_file.csv".format(time=current)
    storage.child("files"+predictedfile).put(FILES_FOLDER+predictedfile)
    return {"filename": str(current)+"predicted_file.csv"}