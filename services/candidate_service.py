from sqlalchemy.orm import Session

from models import candidate
from schemas.candidate import CandidateBase, Candidate

class candidate_service():

    def create_candidate(self, body: Candidate, db: Session):
        db_candidate = Candidate(dni=body.dni, name=body.name, lastname=body.lastname)
        db.add(db_candidate)
        db.commit()
        db.refresh(db_candidate)
        
        return db_candidate