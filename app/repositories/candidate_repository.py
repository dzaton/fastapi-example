from sqlalchemy.orm import Session
from models.candidate import candidate
from schemas.candidate import CandidateInput, CandidateOutput


class candidate_repository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, data: CandidateInput) -> CandidateOutput:
        candidate_db = candidate(**data.model_dump(exclude_none=True))
        self.session.add(candidate_db)  
        self.session.commit()
        self.session.refresh(candidate_db)
        return CandidateOutput(id=candidate_db.id, dni=candidate_db.dni, name=candidate_db.name, lastname=candidate_db.lastname)

    def candidate_exists_by_dni(self, dni: str) -> bool:
        candidate_db = self.session.query(candidate).filter_by(dni=dni).first()
        return bool(candidate_db)