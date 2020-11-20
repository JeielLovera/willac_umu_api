from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import(
    get_estudiantes,
    save_estudiante,
    get_estudiante,
    update_estudiante,
    delete_estudiante,
)

from server.models.estudiantes import(
    ErrorResponseModel,
    ResponseModel,
    EstudianteSchema,
    UpdateEstudianteModel,
)

router = APIRouter()

@router.post("/", response_description="Estudiante data added into database")
async def postEstudiante(estudiante: EstudianteSchema = Body(...)):
    estudiante = jsonable_encoder(estudiante)
    new_estudiante = await save_estudiante(estudiante)
    return ResponseModel(new_estudiante, "Estudiante added successfully")

@router.get("/", response_description="Estudiantes retrieved")
async def getEstudiantes():
    estudiantes = await get_estudiantes()
    if estudiantes:
        return ResponseModel(estudiantes, "Estudiantes data retrieved successfully")
    return ResponseModel(estudiantes, "Empty list returned")

@router.get("/{id}", response_description="Estudiante data retrieved")
async def getEstudiante(id):
    estudiante = await get_estudiante(id)
    if estudiante:
        return ResponseModel(estudiante, "Estudiante data retrieved successfully")
    return ErrorResponseModel(
        "An error ocurred",
        404,
        "Estudiante doesn't exist"
    )

@router.put("/{id}")
async def putEstudiante(id: str, req: UpdateEstudianteModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    modify_estudiante = await update_estudiante(id, req)
    if modify_estudiante:
        return ResponseModel(
            "Estudiante with ID: {} fields update is successfull".format(id),
            "Estudiante fields updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data."
    )

@router.delete("/{id}", response_description="Estudiante data deleted from the database")
async def deleteEstudiante(id: str):
    estudiante_delete = await delete_estudiante(id)
    if estudiante_delete:
        return ResponseModel(
            "Estudiante with ID: {} removed".format(id),
            "Estudiante deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "Estudiante with id {0} doesn't exist".format(id)
    )