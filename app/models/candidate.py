from sqlalchemy import Column
from sqlalchemy import Integer, String

from core.db import Base

class candidate(Base):
    #Table
    __tablename__ = "candidates"
    
    id = Column(Integer, primary_key=True)
    dni = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)