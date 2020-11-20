from fastapi import APIRouter, Body, UploadFile, File
from fastapi.responses import StreamingResponse
from server.code.Data_Standardization import *
import io
import asyncio

router = APIRouter()

@router.post("/", response_description="Training dataset")
async def postTrainingDataset(csv_file: UploadFile = File(...)):
    
    file = Standardization(csv_file.file)
    stream = io.StringIO()
    file.to_csv(stream, index = False, header = True)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=standarfile.csv"
    return response


