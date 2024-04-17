from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db_depend import get_db
from schemas.candidate import Candidate
from services.candidate_service import candidate_service

router = APIRouter()

class candidate_controller:
    def __init__(self):
        """ Inicializa el servicio """
        self.service = candidate_service()

    # CRUD
    @router.post("/candidate", response_model=Candidate, tags=["candidates"], status_code=200)
    def create_candidate(self, body:Candidate , db: Session = Depends(get_db)):
        return self.service.create_candidate(body, db)
    
    