from pydantic import BaseModel


class CandidateBase(BaseModel):
    dni: str
    name: str
    lastname: str

class Candidate(CandidateBase):  
    id: int  
    class Config:
	    from_attributes = True
