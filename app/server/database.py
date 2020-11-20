import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb+srv://adminzuricata:teamzuricatas@willacumucluster.1tzxq.mongodb.net/willacumuDB?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.willacumuDB

estudiantes_collection = database.get_collection("estudiantes")

#---------------------------------------------helpers---------------------------------------------
def estudiantes_helper(estudiante) -> dict:
    return {
        "_id": str(estudiante["_id"]),
        "est_id": estudiante["est_id"],
        "name": estudiante["name"],
        "score": estudiante["score"],
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





