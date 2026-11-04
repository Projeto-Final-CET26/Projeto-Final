# API REST de livros (CRUD).
# CRUD = Create, Read, Update, Delete (criar, ler, actualizar, apagar).
# Sem autenticação / sem API key: qualquer cliente pode chamar os endpoints.

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import * 
from schemas import *


# Cria a tabela "books" no MySQL se ainda não existir.
# Não apaga dados: só cria a estrutura em falta.
Base.metadata.create_all(bind=engine)

# Aplicação FastAPI. A documentação automática fica em /docs
app = FastAPI(title="API Projeto final")

# CORS: permite que uma página web noutro endereço (ex.: localhost:5500)
# faça pedidos a esta API. Sem isto, o browser bloqueia a comunicação.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # aceita pedidos de qualquer origem (útil em aula)
    allow_credentials=False,    # sem cookies / credenciais (combina com origins="*")
    allow_methods=["*"],        # GET, POST, PUT, DELETE, OPTIONS, ...
    allow_headers=["*"],        # aceita quaisquer cabeçalhos HTTP
)


# CRUD CAMPOS
@app.get("/campos", response_model=list[CampoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Campos).all()

@app.post("/campos", response_model=CampoOut, status_code=201)
def criar(dados: CampoIn, db: Session = Depends(get_db)):
    campo = Campos(**dados.model_dump())
    db.add(campo)
    db.commit()
    db.refresh(campo)
    return campo 

@app.put("/campos/{campo_id}", response_model=CampoOut)
def actualizar(campo_id: int, dados: CampoIn, db: Session = Depends(get_db)):
    campo = db.query(Campos).filter(Campos.id == campo_id).first()
    if not campo:
        raise HTTPException(status_code=404, detail="Campo não encontrado.")
    campo.nome = dados.nome
    campo.morada = dados.morada
    campo.cidade = dados.cidade
    campo.capacidade = dados.capacidade
    db.commit()
    db.refresh(campo)
    return campo

@app.delete("/campos/{campo_id}", status_code=204)
def apagar(campo_id: int, db: Session = Depends(get_db)):
    campo = db.query(Campos).filter(Campos.id == campo_id).first()
    if not campo:
        raise HTTPException(status_code=404, detail="Campo não encontrado")
    db.delete(campo)
    db.commit()


# CRUD EPOCAS
@app.get("/epocas", response_model=list[EpocaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Epocas).all()

@app.post("/epocas", response_model=EpocaOut, status_code=201)
def criar(dados: EpocaIn, db: Session = Depends(get_db)):
    epoca = Campos(**dados.model_dump())
    db.add(epoca)
    db.commit()
    db.refresh(epoca)
    return epoca 

@app.put("/epocas/{epoca_id}", response_model=EpocaOut)
def actualizar(epoca_id: int, dados: EpocaIn, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Epoca não encontrada.")
    epoca.epoca = dados.epoca
    db.commit()
    db.refresh(epoca)
    return epoca 

@app.delete("/epocas/{epoca_id}", status_code=204)
def apagar(epoca_id: int, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Epoca não encontrada.")
    db.delete(epoca)
    db.commit()

# CRUD UTILIZADORES 
@app.get("/utilizadores", response_model=list[UtilizadorOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Utilizadores).all()

@app.post("/utilizadores", response_model=UtilizadorOut, status_code=201)
def criar(dados: UtilizadorIn, db: Session = Depends(get_db)):
    utilizador = Utilizadores(**dados.model_dump())
    db.add(utilizador)
    db.commit()
    db.refresh(utilizador)
    return utilizador 

@app.put("/utilizadores/{utilizador_id}", response_model=EpocaOut)
def actualizar(epoca_id: int, dados: EpocaIn, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Epoca não encontrada.")
    epoca.epoca = dados.epoca
    db.commit()
    db.refresh(epoca)
    return epoca 

@app.delete("/epocas/{epoca_id}", status_code=204)
def apagar(epoca_id: int, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Epoca não encontrada.")
    db.delete(epoca)
    db.commit()


# CRUD GESTORES
@app.get("/gestores", response_model=list[GestorOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Gestores).all()

@app.put("/gestores/{gestor_id}", response_model=GestorOut)
def actualizar(gestor_id: int, dados: GestorIn, db: Session = Depends(get_db)):
    gestor = db.query(Gestores).filter(Gestores.id == gestor_id).first()
    if not gestor:
        raise HTTPException(status_code=404, detail="Gestor não encontrado.")
    gestor.primeiro_nome = dados.primeiro_nome
    gestor.apelido = dados.apelido
    gestor.equipa_id = dados.equipa_id
    db.commit()
    db.refresh(gestor)
    return gestor

@app.delete("/gestores/{gestor_id}", status_code=204)
def apagar(gestor_id: int, db: Session = Depends(get_db)):
    gestor = db.query(Gestores).filter(Gestores.id == gestor_id).first()
    if not gestor:
        raise HTTPException(status_code=404, detail="Gestor não encontrado.")
    db.delete(gestor)
    db.commit()


# CRUD JOGADORES
@app.get("/jogadores", response_model=list[JogadorOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Jogadores).all()

@app.post("/jogadores", response_model=JogadorOut, status_code=201)
def criar(dados: JogadorIn, db: Session = Depends(get_db)):
    jogador = Jogadores(**dados.model_dump())
    db.add(jogador)
    db.commit()
    db.refresh(jogador)
    return jogador

@app.put("/jogadores/{jogador_id}", response_model=JogadorOut)
def actualizar(jogador_id: int, dados: JogadorIn, db: Session = Depends(get_db)):
    jogador = db.query(Jogadores).filter(Jogadores.id == jogador_id).first()
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado.")
    jogador.primeiro_nome = dados.primeiro_nome
    jogador.apelido = dados.apelido
    jogador.nacionalidade = dados.nacionalidade
    jogador.data_nascimento = dados.data_nascimento
    jogador.altura_cm = dados.altura_cm
    jogador.peso_kg = dados.peso_kg
    jogador.foto_url = dados.foto_url
    jogador.numero_camisola = dados.numero_camisola
    jogador.equipa_id = dados.equipa_id
    jogador.desporto_id = dados.desporto_id
    jogador.posicao_id = dados.posicao_id
    jogador.utilizador_id = dados.utilizador_id
    db.commit()
    db.refresh(jogador)
    return jogador

@app.delete("/jogadores/{jogador_id}", status_code=204)
def apagar(jogador_id: int, db: Session = Depends(get_db)):
    jogador = db.query(Jogadores).filter(Jogadores.id == jogador_id).first()
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado.")
    db.delete(jogador)
    db.commit()




'''
# GET /books/3  ->  devolve o livro com id 3, ou 404 se não existir
@app.get("/books/{book_id}", response_model=BookOut)
def obter(book_id: int, db: Session = Depends(get_db)):
    livro = db.query(Book).filter(Book.id == book_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro


# POST /books  ->  cria um livro novo e devolve-o com o id (código 201)
@app.post("/books", response_model=BookOut, status_code=201)
def criar(dados: BookIn, db: Session = Depends(get_db)):
    livro = Book(**dados.model_dump())  # passa o JSON para um objecto Book
    db.add(livro)                       # prepara a inserção
    db.commit()                         # grava na base de dados
    db.refresh(livro)                   # lê o id gerado pelo MySQL
    return livro


# PUT /books/3  ->  substitui os dados do livro 3
@app.put("/books/{book_id}", response_model=BookOut)
def actualizar(book_id: int, dados: BookIn, db: Session = Depends(get_db)):
    livro = db.query(Book).filter(Book.id == book_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    livro.title = dados.title
    livro.author = dados.author
    livro.year = dados.year
    db.commit()
    db.refresh(livro)
    return livro


# DELETE /books/3  ->  apaga o livro 3 (código 204 = sucesso sem conteúdo)
@app.delete("/books/{book_id}", status_code=204)
def apagar(book_id: int, db: Session = Depends(get_db)):
    livro = db.query(Book).filter(Book.id == book_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    db.delete(livro)
    db.commit()

'''