# API REST de livros (CRUD).
# CRUD = Create, Read, Update, Delete (criar, ler, actualizar, apagar).
# Sem autenticação / sem API key: qualquer cliente pode chamar os endpoints.

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Epocas, Campos 
from schemas import EpocaIn, EpocaOut, CampoIn, CampoOut


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


# CRUD EPOCAS
@app.get("/epocas", response_model=list[EpocaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Epocas).all()




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