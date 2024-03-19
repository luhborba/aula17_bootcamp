from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo=True)


print("Conexão com SQLite criada com sucesso!")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    idade = Column(Integer)

Base.metadata.create_all(engine)