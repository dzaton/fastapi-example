from typing import List, Optional, Type
from sqlalchemy.orm import Session

from models.candidate import candidate
from schemas.candidate import CandidateInput, CandidateOutput, CandidateInDb

class candidate_repository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, data: CandidateInput) -> CandidateInDb:
        """ Graba un candidato en la BBDD 
        
        Args:
            data: CandidateInput   
        Returns
            CandidateInDb
        """
        
        candidate_db = candidate(**data.model_dump(exclude_none=True))
        self.session.add(candidate_db)  
        self.session.commit()
        self.session.refresh(candidate_db)
        return CandidateInDb(**candidate_db.__dict__)

    def candidate_exists_by_dni(self, dni: str) -> bool:
        """ Comprueba si el DNI de un candidato existe ya en la BBDD 
        
        Args:
            dni: str   
        Returns
            bool
        """
        
        exist = self.session.query(candidate).filter_by(dni=dni).first()
        return bool(exist)
    
    def get_all(self) -> List[Optional[CandidateOutput]]:
        """ Obtiene todos los candidatos almacenados en la BBDD 
         
        Returns
            CandidateOutput[]
        """
        candidates = self.session.query(candidate).all()
        return [CandidateOutput(**candidate.__dict__) for candidate in candidates]

