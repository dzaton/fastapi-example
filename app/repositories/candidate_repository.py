from sqlalchemy.orm import Session

from models.candidate import candidate
from schemas.candidate import CandidateInput, CandidateInDb

class candidate_repository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, data: CandidateInput) -> CandidateInDb:
        print(self)
        print(data)
        candidate_db = candidate(**data.model_dump(exclude_none=True))
        print(candidate_db)
        self.session.add(candidate_db)  
        self.session.commit()
        self.session.refresh(candidate_db)
        return CandidateInDb(**candidate_db.__dict__)

    def candidate_exists_by_dni(self, dni: str) -> bool:
        candidate_db = self.session.query(candidate).filter_by(dni=dni).first()
        return bool(candidate_db)