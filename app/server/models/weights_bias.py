from typing import Optional
from pydantic import BaseModel, Field

"""class WeightsBias:
    def __init__(self, hw, hb, ow, ob):
        self.hidden_weights = hw
        self.hidden_bias = hb
        self.output_weights = ow
        self.output_bias = ob"""

class WeightsBias(BaseModel):
    hidden_weights: list = Field(...)
    hidden_bias: list = Field(...)
    output_weights: list = Field(...)
    output_bias: list = Field(...)

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code}