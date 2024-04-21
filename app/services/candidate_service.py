from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException

from schemas.candidate import CandidateInput, CandidateInDb, CandidateOutput
from repositories.candidate_repository import candidate_repository

class candidate_service:
    def __init__(self, session: Session):
        self.repository = candidate_repository(session)
    
    def create(self, data: CandidateInput) -> CandidateInDb:
        """ Crea un candidato si no existe
        
        Args:
            data: CandidateInput
        """
        if self.repository.candidate_exists_by_dni(data.dni):
            raise HTTPException(status_code=400, detail="El candidato ya existe")
        
        return self.repository.create(data)
    
    def get_all(self) -> List[CandidateOutput]:
        """ Retorna la lista con todos los candidatos
        
        Returns:
            list[CandidateOutput]
        """
        
        return self.repository.get_all()
    
    