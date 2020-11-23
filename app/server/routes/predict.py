from fastapi import APIRouter
from datetime import datetime
from server.code.Multilayer_Perceptron_Trainer import *
import os
import asyncio

from server.models.weights_bias import (
    WeightsBias,
    ErrorResponseModel,
)

from server.database import (
    get_weightsbias
)

router = APIRouter()

@router.get("/{id}")
async def getDataPredict(id: str):
    wb = await get_weightsbias(id)
    #AQUI IRA LA FUNCIÓN PARA PREDECIR CON LOS PESOS ENTRENADOS
    