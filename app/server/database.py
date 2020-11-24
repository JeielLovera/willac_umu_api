
import motor.motor_asyncio
from bson.objectid import ObjectId



MONGO_DETAILS = "mongodb+srv://adminzuricata:teamzuricatas@willacumucluster.1tzxq.mongodb.net/willacumuDB?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.willacumuDB

weigthsbias_collection = database.get_collection("weigthsbias")

#---------------------------------------------helpers---------------------------------------------
def weigthsbias_helper(weightsbias) -> dict:
    return {
        "_id": str(weightsbias["_id"]),
        "hidden_weights": weightsbias["hidden_weights"],
        "hidden_bias": weightsbias["hidden_bias"],
        "output_weights": weightsbias["output_weights"],
        "output_bias": weightsbias["output_bias"]
    }

#---------------------------------------------crud operations---------------------------------------------
async def get_weightsbias(id: str) -> dict:
    wb = await weigthsbias_collection.find_one({"_id": ObjectId(id)})
    if wb:
        return weigthsbias_helper(wb)

async def save_weightsbias(weightsbias: dict) -> dict:
    nuevo_wb = await weigthsbias_collection.insert_one(weightsbias)
    response = await weigthsbias_collection.find_one({"_id": nuevo_wb.inserted_id})
    return weigthsbias_helper(response)



