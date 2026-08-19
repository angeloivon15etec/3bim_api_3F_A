# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB, ProfessoresDB
from schemas import ProdutoCreate, ProdutoResponse, ProfessoresResponse, ProfessoresCreate
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)  # cria as tabelas, se ainda não existirem


app = FastAPI()
app.add_middleware(
 CORSMiddleware,
    allow_origins=['*'],
    # em produção, restringir para o domínio real do front-end
    allow_methods=['*'],
    allow_headers=['*'],
)



@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()

# main.py (trecho adicionado)from fastapi import HTTPException
# GET /produtos/{id} -> consulta um produto pelo id no banco
@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id ==produto_id).first()
    if produto is None:    
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto

# DELETE /produtos/{id} -> remove um produto do banco
@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit()
    return produto


@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

# PUT /produtos/{id} -> atualiza um produto existente no banco
@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db:Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')

    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade
    db.commit()
    db.refresh(produto)
    return produto


@app.get('/professores', response_model=list[ProfessoresResponse])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(ProfessoresDB).all()

@app.get('/professores/{professores_id}', response_model=ProfessoresResponse)
def obter_professores(professores_id: int, db: Session = Depends(get_db)):
    professores = db.query(ProfessoresDB).filter(ProfessoresDB.id ==professores_id).first()
    if professores is None:    
        raise HTTPException(status_code=404, detail='professor não encontrado')
    return professores


@app.delete('/professores/{professores_id}', status_code=204)
def remover_professores(professores_id: int, db: Session = Depends(get_db)):
    professores = db.query(ProfessoresDB).filter(ProfessoresDB.id == professores_id).first()
    if professores is None:
        raise HTTPException(status_code=404, detail='professor não encontrado')
    db.delete(professores)
    db.commit()
    return professores


@app.post('/professores', response_model=ProfessoresResponse, status_code=201)
def criar_professores(Professores: ProfessoresCreate, db: Session = Depends(get_db)):
    novo_Professores = ProfessoresDB(**Professores.dict())
    db.add(novo_Professores)
    db.commit()
    db.refresh(novo_Professores)
    return novo_Professores

@app.put('/professores/{professores_id}', response_model=ProfessoresResponse)
def atualizar_professores(professores_id: int, dados: ProfessoresCreate, db:Session = Depends(get_db)):
    professores = db.query(ProfessoresDB).filter(ProfessoresDB.id == professores_id).first()
    if professores is None:
        raise HTTPException(status_code=404, detail='Professor não encontrado')

    professores.nome = dados.nome
    professores.email = dados.email
    professores.materia = dados.materia
    professores.idade = dados.idade
    db.commit()
    db.refresh(professores)
    return professores