from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db_depend import get_db
from schemas.candidate import CandidateInput,CandidateOutput
from services.candidate_service import candidate_service

router = APIRouter()

class candidate_controller:
    def __init__(self, session: Session):
        """ Inicializa el servicio """
        self.service = candidate_service(session = Depends(get_db))

    # CRUD
    @router.post("/candidate", tags=["candidate"], status_code=200, response_model=CandidateOutput)
    def create_candidate(self, data: CandidateInput , db: Session = Depends(get_db)):
        return self.service.create(data, db)
    
    