from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


class CandidateBase(BaseModel):
    dni: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None

class Candidate(CandidateBase):  
    id: Optional[int] = None 
    class Config:
	    from_attributes = True
