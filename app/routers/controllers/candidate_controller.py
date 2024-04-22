from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db_depend import get_db
from schemas.candidate import CandidateInput, CandidateOutput
from services.candidate_service import candidate_service

router = APIRouter()

class candidate_controller:
    
    # Crea un candidato
    @router.post("/create", status_code=200, response_model=CandidateOutput)
    def create_candidate(data: CandidateInput, session: Session = Depends(get_db)):
        """ Ruta para crear un candidato 
        
        Args:
            data: CandidateInput
            session: Session
        """
        
        _service = candidate_service(session)
        return _service.create(data)
    
    # Lista todos los candidatos
    @router.get("/list", status_code=200, response_model=List[CandidateOutput])
    def get_cities(session: Session = Depends(get_db)):
        """ Ruta que obtiene todos los candidatos 
        
        Args:
            session: Session   
        """
        
        _service = candidate_service(session)
        return _service.get_all()
    
    