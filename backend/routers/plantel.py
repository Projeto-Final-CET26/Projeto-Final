from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import *
from schemas import *


router = APIRouter(tags=["Plantel e saúde"])


@router.get("/utilizadores", response_model=list[UtilizadorOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Utilizadores).all()


@router.get("/utilizadores/{utilizador_id}", response_model=UtilizadorOut)
def obter(utilizador_id: int, db: Session = Depends(get_db)):
    utilizador = db.query(Utilizadores).filter(Utilizadores.id == utilizador_id).first()
    if not utilizador:
        raise HTTPException(status_code=404, detail="Utilizador não encontrado.")
    return utilizador


@router.post("/utilizadores", response_model=UtilizadorOut, status_code=201)
def criar(dados: UtilizadorIn, db: Session = Depends(get_db)):
    utilizador = Utilizadores(**dados.model_dump())
    db.add(utilizador)
    db.commit()
    db.refresh(utilizador)
    return utilizador 


@router.put("/utilizadores/{utilizador_id}", response_model=EpocaOut)
def actualizar(epoca_id: int, dados: EpocaIn, db: Session = Depends(get_db)):
    epoca = db.query(Epocas).filter(Epocas.id == epoca_id).first()
    if not epoca:
        raise HTTPException(status_code=404, detail="Epoca não encontrada.")
    epoca.epoca = dados.epoca
    db.commit()
    db.refresh(epoca)
    return epoca 


@router.delete("/utilizadores/{utilizador_id}", status_code=204)
def apagar(utilizador_id: int, db: Session = Depends(get_db)):
    utilizador = db.query(Utilizadores).filter(Utilizadores.id == utilizador_id).first()
    if not utilizador:
        raise HTTPException(status_code=404, detail="Utilizador não encontrado.")
    db.delete(utilizador)
    db.commit()


@router.get("/lesoes", response_model=list[LesaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Lesoes).all()


@router.get("/lesoes/{lesao_id}", response_model=LesaoOut)
def obter(lesao_id: int, db: Session = Depends(get_db)):
    lesao = db.query(Lesoes).filter(Lesoes.id == lesao_id).first()
    if not lesao:
        raise HTTPException(status_code=404, detail="Lesão não encontrada.")
    return lesao


@router.post("/lesoes", response_model=LesaoOut, status_code=201)
def criar(dados: LesaoIn, db: Session = Depends(get_db)):
    lesao = Lesoes(**dados.model_dump())
    db.add(lesao)
    db.commit()
    db.refresh(lesao)
    return lesao 


@router.put("/lesoes/{lesoes_id}", response_model=LesaoOut)
def actualizar(lesoes_id: int, dados: LesaoIn, db: Session = Depends(get_db)):
    lesao = db.query(Lesoes).filter(Lesoes.id == lesoes_id).first()
    if not lesao:
        raise HTTPException(status_code=404, detail="Lesão não encontrada.")
    lesao.estado = dados.estado
    lesao.descricao = dados.descricao
    lesao.jogador_id = dados.jogador_id
    lesao.epoca_id = dados.epoca_id
    lesao.zona = dados.zona
    lesao.data_inicio = dados.data_inicio
    lesao.data_prevista_fim = dados.data_prevista_fim
    lesao.data_fim = dados.data_fim
    db.commit()
    db.refresh(lesao)
    return lesao 


@router.delete("/lesoes/{lesao_id}", status_code=204)
def apagar(lesao_id: int, db: Session = Depends(get_db)):
    lesao = db.query(Lesoes).filter(Lesoes.id == lesao_id).first()
    if not lesao:
        raise HTTPException(status_code=404, detail="Lesão não encontrada.")
    db.delete(lesao)
    db.commit()


@router.get("/posicoes", response_model=list[PosicaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Posicoes).all()


@router.get("/posicoes/{posicao_id}", response_model=PosicaoOut)
def obter(posicao_id: int, db: Session = Depends(get_db)):
    posicao = db.query(Posicoes).filter(Posicoes.id == posicao_id).first()
    if not posicao:
        raise HTTPException(status_code=404, detail="Posição não encontrada.")
    return posicao


@router.get("/posicoes_secundarias", response_model=list[PosicaoSecundariaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(PosicoesSecundarias).all()


@router.get("/posicoes_secundarias/{pos_sec_id}", response_model=PosicaoSecundariaOut)
def obter(pos_sec_id: int, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(
        PosicoesSecundarias.id == pos_sec_id
    ).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    return pos_sec


@router.post("/posicoes_secundarias", response_model=PosicaoSecundariaOut, status_code=201)
def criar(dados: PosicaoSecundariaIn, db: Session = Depends(get_db)):
    pos_sec = PosicoesSecundarias(**dados.model_dump())
    db.add(pos_sec)
    db.commit()
    db.refresh(pos_sec)
    return pos_sec 


@router.put("/posicoes_secundarias/{pos_sec_id}", response_model=PosicaoSecundariaOut)
def actualizar(pos_sec_id: int, dados: PosicaoSecundariaIn, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    pos_sec.posicao_id = dados.posicao_id
    pos_sec.jogador_id = dados.jogador_id
    db.commit()
    db.refresh(pos_sec)
    return pos_sec 


@router.delete("/posicoes_secundarias/{pos_sec_id}", status_code=204)
def apagar(pos_sec_id: int, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    db.delete(pos_sec)
    db.commit()


@router.put("/posicoes_secundarias/{pos_sec_id}", response_model=PosicaoSecundariaOut)
def actualizar(pos_sec_id: int, dados: PosicaoSecundariaIn, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    pos_sec.posicao_id = dados.posicao_id
    pos_sec.jogador_id = dados.jogador_id
    db.commit()
    db.refresh(pos_sec)
    return pos_sec 


@router.delete("/posicoes_secundarias/{pos_sec_id}", status_code=204)
def apagar(pos_sec_id: int, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    db.delete(pos_sec)
    db.commit()


@router.get("/jogo_jogadores", response_model=list[JogoJogadoresOut])
def listar(db: Session = Depends(get_db)):
    return db.query(JogoJogadores).all()


@router.get("/jogo_jogadores/{jogo_jogadores_id}", response_model=JogoJogadoresOut)
def obter(jogo_jogadores_id: int, db: Session = Depends(get_db)):
    jogo_jogador = db.query(JogoJogadores).filter(
        JogoJogadores.id == jogo_jogadores_id
    ).first()
    if not jogo_jogador:
        raise HTTPException(status_code=404, detail="Jogo / Jogador não encontrado.")
    return jogo_jogador


@router.post("/jogo_jogadores", response_model=JogoJogadoresOut, status_code=201)
def criar(dados: JogoJogadoresIn, db: Session = Depends(get_db)):
    jogo_jogador = JogoJogadores(**dados.model_dump())
    db.add(jogo_jogador)
    db.commit()
    db.refresh(jogo_jogador)
    return jogo_jogador


@router.put("/jogo_jogadores/{jogo_jogadores_id}", response_model=JogoJogadoresOut)
def actualizar(jogo_jogadores_id: int, dados: JogoJogadoresIn, db: Session = Depends(get_db)):
    jogo_jogador = db.query(JogoJogadores).filter(JogoJogadores.id == jogo_jogadores_id).first()
    if not jogo_jogador:
        raise HTTPException(status_code=404, detail="Jogo / Jogador não encontrado.")
    jogo_jogador.jogo_id = dados.jogo_id
    jogo_jogador.equipa_id = dados.equipa_id
    jogo_jogador.jogador_id = dados.jogador_id
    jogo_jogador.estatuto = dados.estatudo
    jogo_jogador.numero_camisola = dados.numero_camisola
    db.commit()
    db.refresh(jogo_jogador)
    return jogo_jogador 


@router.delete("/jogo_jogadores/{jogo_jogadores_id}", status_code=204)
def apagar(jogo_jogadores_id: int, db: Session = Depends(get_db)):
    jogo_jogador = db.query(JogoJogadores).filter(JogoJogadores.id == jogo_jogadores_id).first()
    if not jogo_jogador:
        raise HTTPException(status_code=404, detail="Jogo / Jogador não encontrado.")
    db.delete(jogo_jogador)
    db.commit()


@router.get("/gestores", response_model=list[GestorOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Gestores).all()


@router.get("/gestores/{gestor_id}", response_model=GestorOut)
def obter(gestor_id: int, db: Session = Depends(get_db)):
    gestor = db.query(Gestores).filter(Gestores.id == gestor_id).first()
    if not gestor:
        raise HTTPException(status_code=404, detail="Gestor não encontrado.")
    return gestor


@router.put("/gestores/{gestor_id}", response_model=GestorOut)
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


@router.delete("/gestores/{gestor_id}", status_code=204)
def apagar(gestor_id: int, db: Session = Depends(get_db)):
    gestor = db.query(Gestores).filter(Gestores.id == gestor_id).first()
    if not gestor:
        raise HTTPException(status_code=404, detail="Gestor não encontrado.")
    db.delete(gestor)
    db.commit()


@router.get("/jogadores", response_model=list[JogadorOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Jogadores).all()


@router.get("/jogadores/{jogador_id}", response_model=JogadorOut)
def obter(jogador_id: int, db: Session = Depends(get_db)):
    jogador = db.query(Jogadores).filter(Jogadores.id == jogador_id).first()
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado.")
    return jogador


@router.post("/jogadores", response_model=JogadorOut, status_code=201)
def criar(dados: JogadorIn, db: Session = Depends(get_db)):
    jogador = Jogadores(**dados.model_dump())
    db.add(jogador)
    db.commit()
    db.refresh(jogador)
    return jogador


@router.put("/jogadores/{jogador_id}", response_model=JogadorOut)
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


@router.delete("/jogadores/{jogador_id}", status_code=204)
def apagar(jogador_id: int, db: Session = Depends(get_db)):
    jogador = db.query(Jogadores).filter(Jogadores.id == jogador_id).first()
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado.")
    db.delete(jogador)
    db.commit()


@router.get("/zona_lesao", response_model=list[ZonaLesaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(ZonaLesao).all()


@router.post("/zona_lesao", response_model=ZonaLesaoOut, status_code=201)
def criar(dados: ZonaLesaoIn, db: Session = Depends(get_db)):
    zona_lesao = ZonaLesao(**dados.model_dump())
    db.add(zona_lesao)
    db.commit()
    db.refresh(zona_lesao)
    return zona_lesao


@router.put("/zona_lesao/{zona_lesao_id}", response_model=ZonaLesaoOut)
def actualizar(zona_lesao_id: int, dados: ZonaLesaoIn, db: Session = Depends(get_db)):
    zona_lesao = db.query(ZonaLesao).filter(ZonaLesao.id == zona_lesao_id).first()
    if not zona_lesao:
        raise HTTPException(status_code=404, detail="Zona-Lesão não encontrada.")
    zona_lesao.descricao = dados.descricao
    zona_lesao.segmento = dados.segmento
    db.commit(zona_lesao)
    db.refresh(zona_lesao)
    return zona_lesao


@router.delete("/zona_lesao/{zona_lesao_id}", status_code=204)
def apagar(zona_lesao_id: int, db: Session = Depends(get_db)):
    zona_lesao = db.query(ZonaLesao).filter(ZonaLesao.id == zona_lesao_id).first()
    if not zona_lesao:
        raise HTTPException(status_code=404, detail="Zona-Lesão não encontrada.")
    db.delete(zona_lesao)
    db.commit()
