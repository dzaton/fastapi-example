from core.db import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String

class candidate(Base):
    #Table
    __tablename__ = "candidates"
    
    id = Column(Integer, primary_key=True)
    dni = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    lastname = Column(String, index=True)