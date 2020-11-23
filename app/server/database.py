
import motor.motor_asyncio
from bson.objectid import ObjectId



MONGO_DETAILS = "mongodb+srv://adminzuricata:teamzuricatas@willacumucluster.1tzxq.mongodb.net/willacumuDB?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.willacumuDB

estudiantes_collection = database.get_collection("estudiantes")
weigthsbias_collection = database.get_collection("weigthsbias")

#---------------------------------------------helpers---------------------------------------------
def estudiantes_helper(estudiante) -> dict:
    return {
        "_id": str(estudiante["_id"]),
        "est_id": estudiante["est_id"],
        "name": estudiante["name"],
        "score": estudiante["score"]
    }

def weigthsbias_helper(weightsbias) -> dict:
    return {
        "_id": str(weightsbias["_id"]),
        "hidden_weights": weightsbias["hidden_weights"],
        "hidden_bias": weightsbias["hidden_bias"],
        "output_weights": weightsbias["output_weights"],
        "output_bias": weightsbias["output_bias"]
    }

#---------------------------------------------crud operations---------------------------------------------
async def get_estudiantes():
    estudiantes = []
    async for estudiante in estudiantes_collection.find():
        estudiantes.append(estudiantes_helper(estudiante))
    return estudiantes

async def save_estudiante(estudiante: dict) -> dict:
    nuevo_estudiante = await estudiantes_collection.insert_one(estudiante)
    response = await estudiantes_collection.find_one({"_id": nuevo_estudiante.inserted_id})
    return estudiantes_helper(response)

async def get_estudiante(id: str) -> dict:
    estudiante = await estudiantes_collection.find_one({"_id": ObjectId(id)})
    if estudiante:
        return estudiantes_helper(estudiante)

async def update_estudiante(id: str, data: dict):
    if len(data) < 1:
        return False
    estudiante = await estudiantes_collection.find_one({"_id": ObjectId(id)})
    if estudiante:
        updated_estudiante = await estudiantes_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if updated_estudiante:
            return True
        return False

async def delete_estudiante(id: str):
    estudiante = await estudiantes_collection.find_one({"_id": ObjectId(id)})
    if estudiante:
        await estudiantes_collection.delete_one({"_id": ObjectId(id)})
        return True

async def get_weightsbias(id: str) -> dict:
    wb = await weigthsbias_collection.find_one({"_id": ObjectId(id)})
    if wb:
        return weigthsbias_helper(wb)

async def save_weightsbias(weightsbias: dict) -> dict:
    nuevo_wb = await weigthsbias_collection.insert_one(weightsbias)
    response = await weigthsbias_collection.find_one({"_id": nuevo_wb.inserted_id})
    return weigthsbias_helper(response)



