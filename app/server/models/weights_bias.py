from typing import Optional
from pydantic import BaseModel, Field

class WeightsBias(BaseModel):
    hidden_weights: list = Field(...)
    hidden_bias: list = Field(...)
    output_weights: list = Field(...)
    output_bias: list = Field(...)

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code}