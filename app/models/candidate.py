from core.db import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String

class candidate(Base):
    #Table
    __tablename__ = "candidates"
    
    id = Column(Integer, primary_key=True)
    dni = Column(String)
    name = Column(String)
    lastname = Column(String)