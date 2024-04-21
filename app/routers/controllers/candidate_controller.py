from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db_depend import get_db
from schemas.candidate import CandidateInput, CandidateOutput
from services.candidate_service import candidate_service

router = APIRouter()

class candidate_controller:
    
    @router.post("/candidate", tags=["candidate"], status_code=200, response_model=CandidateOutput)
    async def create_candidate(data: CandidateInput, session: Session = Depends(get_db)):
        
        _service = candidate_service(session)
        return _service.create(data)
    
    