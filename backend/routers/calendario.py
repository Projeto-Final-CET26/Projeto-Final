from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import *
from schemas import *


router = APIRouter(tags=["Calendário e competições"])


@router.get("/campos", response_model=list[CampoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Campos).all()


@router.get("/campos/{campo_id}", response_model=CampoOut)
def obter(campo_id: int, db: Session = Depends(get_db)):
    campo = db.query(Campos).filter(Campos.id == campo_id).first()
    if not campo:
            raise HTTPException(status_code=404, detail="Campo não encontrado.")
    
    return campo


@router.post("/campos", response_model=CampoOut, status_code=201)
def criar(dados: CampoIn, db: Session = Depends(get_db)):
    campo = Campos(**dados.model_dump())
    db.add(campo)
    db.commit()
    db.refresh(campo)
    return campo 


@router.put("/campos/{campo_id}", response_model=CampoOut)
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


@router.delete("/campos/{campo_id}", status_code=204)
def apagar(campo_id: int, db: Session = Depends(get_db)):
    campo = db.query(Campos).filter(Campos.id == campo_id).first()
    if not campo:
        raise HTTPException(status_code=404, detail="Campo não encontrado")
    db.delete(campo)
    db.commit()


@router.get("/competicoes", response_model=list[CompeticaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Competicoes).all()


@router.get("/competicoes/{competicao_id}", response_model=CompeticaoOut)
def obter(competicao_id: int, db: Session = Depends(get_db)):
    competicao = db.query(Competicoes).filter(Competicoes.id == competicao_id).first()
    if not competicao:
        raise HTTPException(status_code=404, detail="Competição não encontrada.")
    return competicao


@router.post("/competicoes", response_model=CompeticaoOut, status_code=201)
def criar(dados: CompeticaoIn, db: Session = Depends(get_db)):
    competicao = Competicoes(**dados.model_dump())
    db.add(competicao)
    db.commit()
    db.refresh(competicao)
    return competicao 


@router.put("/competicoes/{competicao_id}", response_model=CompeticaoOut)
def actualizar(competicao_id: int, dados: CompeticaoIn, db: Session = Depends(get_db)):
    competicao = db.query(Competicoes).filter(Competicoes.id == competicao_id).first()
    if not competicao:
        raise HTTPException(status_code=404, detail="Competição não encontrada.")
    competicao.nome = dados.nome
    competicao.tipo_competicao = dados.tipo_competicao
    db.commit()
    db.refresh(competicao)
    return competicao


@router.delete("/competicoes/{competicao_id}", status_code=204)
def apagar(competicao_id: int, db: Session = Depends(get_db)):
    competicao = db.query(Competicoes).filter(Competicoes.id == competicao_id).first()
    if not competicao:
        raise HTTPException(status_code=404, detail="Competição não encontrada")
    db.delete(competicao)
    db.commit()


@router.get("/epocas", response_model=list[EpocaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Epocas).all()


@router.get("/epocas/{epoca_id}", response_model=EpocaOut)
def obter(epoca_id: int, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Época não encontrada.")
    return epoca


@router.post("/epocas", response_model=EpocaOut, status_code=201)
def criar(dados: EpocaIn, db: Session = Depends(get_db)):
    epoca = Campos(**dados.model_dump())
    db.add(epoca)
    db.commit()
    db.refresh(epoca)
    return epoca 


@router.put("/epocas/{epoca_id}", response_model=EpocaOut)
def actualizar(epoca_id: int, dados: EpocaIn, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Epoca não encontrada.")
    epoca.epoca = dados.epoca
    db.commit()
    db.refresh(epoca)
    return epoca 


@router.delete("/epocas/{epoca_id}", status_code=204)
def apagar(epoca_id: int, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Epoca não encontrada.")
    db.delete(epoca)
    db.commit()


@router.get("/jogos", response_model=list[JogoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Jogos).all()


@router.get("/jogos/{jogo_id}", response_model=JogoOut)
def obter(jogo_id: int, db: Session = Depends(get_db)):
    jogo = db.query(Jogos).filter(Jogos.id == jogo_id).first()
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado.")
    return jogo


@router.post("/jogos", response_model=JogoOut, status_code=201)
def criar(dados: JogoIn, db: Session = Depends(get_db)):
    jogo = Jogos(**dados.model_dump())
    db.add(jogo)
    db.commit()
    db.refresh(jogo)
    return jogo


@router.get("/desportos/{desporto_id}", response_model=DesportoOut)
def obter(desporto_id: int, db: Session = Depends(get_db)):
    desporto = db.query(Desportos).filter(Desportos.id == desporto.id).first()
    if not desporto:
        raise HTTPException(status_code=404, detail="Desporto não encontrado.")
    return desporto
