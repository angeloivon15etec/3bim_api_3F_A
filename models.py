# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class ProdutoDB(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)

class ProfessoresDB(Base):
    __tablename__ = 'professores'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    materia = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
