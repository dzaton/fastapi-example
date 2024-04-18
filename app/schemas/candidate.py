from typing import List,Optional
from pydantic import BaseModel, Field

class Candidate(BaseModel):  
    id: Optional[int] = None
    dni: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    class Config:
        # Para uso de un ORM
	    from_attributes = True
