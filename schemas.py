# schemas.py
from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass
    
class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
      from_attributes = True


class ProfessoresBase(BaseModel):
    nome: str
    email: str
    materia: str
    idade: int

class ProfessoresCreate(ProfessoresBase):
    pass
    
class ProfessoresResponse(ProfessoresBase):
    id: int

    class Config:
      from_attributes = True