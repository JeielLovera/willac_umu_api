from typing import Optional
from pydantic import BaseModel, EmailStr, Field

#score: float = Field(..., gt=0.0, le=20.0)

class EstudianteSchema(BaseModel):
    est_id: str = Field(...)
    name: str = Field(...)
    score: list = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "est_id":"idmedioraro",
                "name": "Teodoro",
                "score": {
                    "nota1": 10.0,
                    "nota2": 11.5
                }
            }
        }

class UpdateEstudianteModel(BaseModel):
    name: Optional[str]
    score: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "est_id":"idmedioraro",
                "name": "TeodoroUpdate",
                "score": {
                    "nota1": 10.0,
                    "nota2": 11.5
                }
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code}