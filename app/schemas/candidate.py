from typing import List,Optional
from pydantic import BaseModel, Field, UUID4

class CandidateInDb(BaseModel):  
    candidate_id: int
    dni:str
    name: str
    lastname: str
    class Config:
        # Para uso de un ORM
	    from_attributes = True

class CandidateInput(BaseModel):
    dni: Optional[str] = Field(min_length=1, max_length=9)
    name: Optional[str] = Field(min_length=1, max_length=40)
    lastname: Optional[str] = Field(min_length=1, max_length=40)

class CandidateOutput(BaseModel):
    candidate_id: int
    dni:str
    name: str
    lastname: str
