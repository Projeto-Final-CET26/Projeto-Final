from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import *
from schemas import *


router = APIRouter(tags=["Métricas"])


@router.get("/coordenadas_metricas", response_model=list[CoordenadaMetricasOut])
def listar(db: Session = Depends(get_db)):
    return db.query(CoordernadasMetricas).all()


@router.get("/coordenadas_metricas/{coordenada_metrica_id}", response_model=CoordenadaMetricasOut)
def obter(coordenada_metrica_id: int, db: Session = Depends(get_db)):
    coordenada_metrica = db.query(CoordernadasMetricas).filter(
        CoordernadasMetricas.id == coordenada_metrica_id
    ).first()
    if not coordenada_metrica:
        raise HTTPException(status_code=404, detail="Coordenada Métrica não encontrada.")
    return coordenada_metrica


@router.post("/coordenadas_metricas", response_model=CampoOut, status_code=201)
def criar(dados: CoordenadaMetricasIn, db: Session = Depends(get_db)):
    coordenadas_metricas = CoordernadasMetricas(**dados.model_dump())
    db.add(coordenadas_metricas)
    db.commit()
    db.refresh(coordenadas_metricas)
    return coordenadas_metricas 


@router.put("/coordenadas_metricas/{coordenada_metrica_id}", response_model=CoordenadaMetricasOut)
def actualizar(coordenada_metrica_id: int, dados: CoordenadaMetricasIn, db: Session = Depends(get_db)):
    coordenada_metrica = db.query(CoordernadasMetricas).filter(CoordernadasMetricas.id == coordenada_metrica_id).first()
    if not coordenada_metrica:
        raise HTTPException(status_code=404, detail="Coordenada Métrica não encontrada.")
    coordenada_metrica.registo_metrica_id = dados.registo_metrica_id
    coordenada_metrica.posicao_X = dados.posicao_X
    coordenada_metrica.posicao_Y = dados.posicao_Y
    db.commit()
    db.refresh(coordenada_metrica)
    return coordenada_metrica


@router.delete("/coordenadas_metricas/{coordenada_metrica_id}", status_code=204)
def apagar(coordenada_metrica_id: int, db: Session = Depends(get_db)):
    coordenada_metrica = db.query(CoordernadasMetricas).filter(CoordernadasMetricas.id == coordenada_metrica_id).first()
    if not coordenada_metrica:
        raise HTTPException(status_code=404, detail="Coordenada Métrica não encontrada.")
    db.delete(coordenada_metrica)
    db.commit()


@router.get("/metricas", response_model=list[MetricasOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Metricas).all()


@router.get("/metricas/{metrica_id}", response_model=MetricasOut)
def obter(metrica_id: int, db: Session = Depends(get_db)):
    metrica = db.query(Metricas).filter(Metricas.id == metrica_id).first()
    if not metrica:
        raise HTTPException(status_code=404, detail="Métrica não encontrada.")
    return metrica


@router.post("/metricas", response_model=MetricasOut, status_code=201)
def criar(dados: MetricasIn, db: Session = Depends(get_db)):
    metrica = Metricas(**dados.model_dump())
    db.add(metrica)
    db.commit()
    db.refresh(metrica)
    return metrica


@router.put("/metricas/{metrica_id}", response_model=MetricasOut)
def actualizar(metrica_id: int, dados: MetricasIn, db: Session = Depends(get_db)):
    metrica = db.query(Metricas).filter(Metricas.id == metrica_id).first()
    if not metrica:
        raise HTTPException(status_code=404, detail="Metrica não encontrada.")
    metrica.descricao = dados.descricao
    metrica.unidade = dados.unidade
    metrica.desporto_id = dados.desporto_id
    metrica.sempre_visivel = dados.sempre_visivel
    db.commit()
    db.refresh(metrica)
    return metrica 


@router.delete("/metricas/{metrica_id}", status_code=204)
def apagar(metrica_id: int, db: Session = Depends(get_db)):
    metrica = db.query(Metricas).filter(Metricas.id == metrica_id).first()
    if not metrica:
        raise HTTPException(status_code=404, detail="Metrica não encontrada.")
    db.delete(metrica)
    db.commit()


@router.get("/registo_metricas", response_model=list[RegistoMetricasIn])
def listar(db: Session = Depends(get_db)):
    return db.query(RegistoMetricas).all()


@router.get("/registo_metricas/{registo_metrica_id}", response_model=RegistoMetricasOut)
def obter(registo_metrica_id: int, db: Session = Depends(get_db)):
    registo_metrica = db.query(RegistoMetricas).filter(
        RegistoMetricas.id == registo_metrica_id
    ).first()
    if not registo_metrica:
        raise HTTPException(status_code=404, detail="Registo de métrica não encontrado.")
    return registo_metrica


@router.post("/registo_metricas", response_model=RegistoMetricasOut, status_code=201)
def criar(dados: RegistoMetricasIn, db: Session = Depends(get_db)):
    reg_metrica = RegistoMetricas(**dados.model_dump())
    db.add(reg_metrica)
    db.commit()
    db.refresh(reg_metrica)
    return reg_metrica 


@router.put("/registo_metricas/{registo_metrica_id}", response_model=RegistoMetricasOut)
def actualizar(registo_metrica_id: int, dados: RegistoMetricasIn, db: Session = Depends(get_db)):
    reg_metrica = db.query(RegistoMetricas).filter(RegistoMetricas.id == registo_metrica_id).first()
    if not reg_metrica:
        raise HTTPException(status_code=404, detail="Metrica não encontrada.")
    reg_metrica.jogador_id = dados.jogador_id
    reg_metrica.equipa_id = dados.equipa_id
    reg_metrica.jogo_id = dados.jogo_id
    reg_metrica.metrica_id = dados.metrica_id
    reg_metrica.periodo = dados.periodo
    reg_metrica.tempo_segundos = dados.tempo_segundos
    reg_metrica.sucesso = dados.sucesso
    reg_metrica.tem_posicao = dados.tem_posicao
    reg_metrica.obs = dados.obs
    db.commit()
    db.refresh(reg_metrica)
    return reg_metrica 


@router.delete("/registo_metricas/{registo_metrica_id}", status_code=204)
def apagar(registo_metrica_id: int, db: Session = Depends(get_db)):
    reg_metrica = db.query(RegistoMetricas).filter(RegistoMetricas.id == registo_metrica_id).first()
    if not reg_metrica:
        raise HTTPException(status_code=404, detail="RegistoMetrica não encontrada.")
    db.delete(reg_metrica)
    db.commit()


@router.get("/metricas_jogo", response_model=list[MetricasJogoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(MetricasJogos).all()


@router.get("/metricas_jogo/{metricas_jogo_id}", response_model=MetricasJogoOut)
def obter(metricas_jogo_id: int, db: Session = Depends(get_db)):
    metrica_jogo = db.query(MetricasJogos).filter(
        MetricasJogos.id == metricas_jogo_id
    ).first()
    if not metrica_jogo:
        raise HTTPException(status_code=404, detail="Métrica de jogo não encontrada.")
    return metrica_jogo


@router.post("/metricas_jogo", response_model=MetricasJogoOut, status_code=201)
def criar(dados: MetricasJogoIn, db: Session = Depends(get_db)):
    metrica_jogo = MetricasJogos(**dados.model_dump())
    db.add(metrica_jogo)
    db.commit()
    db.refresh(metrica_jogo)
    return metrica_jogo 


@router.put("/metricas_jogo/{metricas_jogo_id}", response_model=MetricasJogoOut)
def actualizar(metricas_jogo_id: int, dados: MetricasJogoIn, db: Session = Depends(get_db)):
    metricas_jogo = db.query(MetricasJogos).filter(MetricasJogos.id == metricas_jogo_id).first()
    if not metricas_jogo:
        raise HTTPException(status_code=404, detail="Metricas Jogo não encontrada.")
    metricas_jogo.gestor_id = dados.gestor_id
    metricas_jogo.jogador_id = dados.jogador_id
    metricas_jogo.jogo_id = dados.jogo_id
    metricas_jogo.equipa_id = dados.equipa_id
    metricas_jogo.metrica_id = dados.metrica_id
    metricas_jogo.valor = dados.valor
    db.commit()
    db.refresh(metricas_jogo)
    return metricas_jogo 


@router.delete("/metricas_jogo/{metricas_jogo_id}", status_code=204)
def apagar(metricas_jogo_id: int, db: Session = Depends(get_db)):
    metricas_jogo = db.query(MetricasJogos).filter(MetricasJogos.id == metricas_jogo_id).first()
    if not metricas_jogo:
        raise HTTPException(status_code=404, detail="Metricas Jogo não encontrada.")
    db.delete(metricas_jogo)
    db.commit()


@router.get("/submetricas", response_model=list[SubMetricaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(SubMetricas).all()


@router.get("/submetricas/{submetrica_id}", response_model=SubMetricaOut)
def obter(submetrica_id: int, db: Session = Depends(get_db)):
    submetrica = db.query(SubMetricas).filter(SubMetricas.id == submetrica_id).first()
    if not submetrica:
        raise HTTPException(status_code=404, detail="Sub-métrica não encontrada.")
    return submetrica


@router.post("/submetricas", response_model=SubMetricaOut, status_code=201)
def criar(dados: SubMetricaIn, db: Session = Depends(get_db)):
    submetrica = SubMetricas(**dados.model_dump())
    db.add(submetrica)
    db.commit()
    db.refresh(submetrica)
    return submetrica


@router.put("/submetricas/{submetrica_id}", response_model=SubMetricaOut)
def actualizar(submetrica_id: int, dados: SubMetricaIn, db: Session = Depends(get_db)):
    submetrica = db.query(SubMetricas).filter(SubMetricas.id == submetrica_id).first()
    if not submetrica:
        raise HTTPException(status_code=404, detail="Sub-metrica não encontrada.")
    submetrica.metrica_id= dados.metrica_id
    submetrica.descricao = dados.descricao
    submetrica.equipa_id = dados.equipa_id
    db.commit()
    db.refresh(submetrica)
    return submetrica 


@router.delete("/submetricas/{submetrica_id}", status_code=204)
def apagar(submetrica_id: int, db: Session = Depends(get_db)):
    submetrica = db.query(SubMetricas).filter(SubMetricas.id == submetrica_id).first()
    if not submetrica:
        raise HTTPException(status_code=404, detail="Sub-metrica não encontrada.")
    db.delete(submetrica)
    db.commit()


@router.get("/submetricas_jogo", response_model=list[SubmetricasJogoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(SubMetricasJogo).all()


@router.get("/submetricas_jogo/{submetricas_jogo_id}", response_model=SubmetricasJogoOut)
def obter(submetricas_jogo_id: int, db: Session = Depends(get_db)):
    submetrica_jogo = db.query(SubMetricasJogo).filter(
        SubMetricasJogo.id == submetricas_jogo_id
    ).first()
    if not submetrica_jogo:
        raise HTTPException(status_code=404, detail="Sub-métrica de jogo não encontrada.")
    return submetrica_jogo


@router.post("/submetricas_jogo", response_model=SubmetricasJogoOut, status_code=201)
def criar(dados: SubmetricasJogoIn, db: Session = Depends(get_db)):
    submetrica_jogo = SubMetricasJogo(**dados.model_dump())
    db.add(submetrica_jogo)
    db.commit()
    db.refresh(submetrica_jogo)
    return submetrica_jogo


@router.put("/submetricas_jogo/{submetricas_jogo_id}", response_model=SubmetricasJogoOut)
def actualizar(submetricas_jogo_id: int, dados: SubmetricasJogoIn, db: Session = Depends(get_db)):
    submetrica_jogo = db.query(SubMetricasJogo).filter(SubMetricasJogo.id == submetricas_jogo_id).first()
    if not submetrica_jogo:
        raise HTTPException(status_code=404, detail="Sub-metrica jogo não encontrada.")
    submetrica_jogo.jogo_id= dados.jogo_id
    submetrica_jogo.jogador_id = dados.jogador_id
    submetrica_jogo.submetrica_id = dados.submetrica_id
    submetrica_jogo.valor = dados.valor
    db.commit()
    db.refresh(submetrica_jogo)
    return submetrica_jogo


@router.delete("/submetricas_jogo/{submetricas_jogo_id}", status_code=204)
def apagar(submetricas_jogo_id: int, db: Session = Depends(get_db)):
    submetrica_jogo = db.query(SubMetricasJogo).filter(SubMetricasJogo.id == submetricas_jogo_id).first()
    if not submetrica_jogo:
        raise HTTPException(status_code=404, detail="Sub-metrica jogo não encontrada.")
    db.delete(submetrica_jogo)
    db.commit()


@router.get("/registo_submetricas", response_model=list[RegistoSubMetricaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(RegistoSubMetricas).all()


@router.get(
    "/registo_submetricas/{registo_metrica_id}/{submetrica_id}",
    response_model=RegistoSubMetricaOut,
)
def obter(registo_metrica_id: int, submetrica_id: int, db: Session = Depends(get_db)):
    registo_submetrica = db.query(RegistoSubMetricas).filter(
        RegistoSubMetricas.registo_metrica_id == registo_metrica_id,
        RegistoSubMetricas.submetrica_id == submetrica_id,
    ).first()
    if not registo_submetrica:
        raise HTTPException(status_code=404, detail="Registo de sub-métrica não encontrado.")
    return registo_submetrica


@router.post("/registo_submetricas", response_model=RegistoSubMetricaOut, status_code=201)
def criar(dados: RegistoSubMetricaIn, db: Session = Depends(get_db)):
    reg_submetrica = RegistoSubMetricas(**dados.model_dump())
    db.add(reg_submetrica)
    db.commit()
    db.refresh(reg_submetrica)
    return reg_submetrica


@router.put("/registo_submetricas/{registo_submetrica_id}", response_model=RegistoSubMetricaOut)
def actualizar(registo_submetrica_id: int, dados: RegistoSubMetricaIn, db: Session = Depends(get_db)):
    reg_submetrica = db.query(RegistoSubMetricas).filter(RegistoSubMetricas.id == registo_submetrica_id).first()
    if not reg_submetrica:
        raise HTTPException(status_code=404, detail="Registo Sub-metrica não encontrada.")
    reg_submetrica.submetrica_id= dados.submetrica_id
    reg_submetrica.registo_metrica_id = dados.registo_metrica_id
    db.commit()
    db.refresh(reg_submetrica)
    return reg_submetrica 


@router.delete("/registo_submetricas/{registo_submetrica_id}", status_code=204)
def apagar(registo_submetrica_id: int, db: Session = Depends(get_db)):
    reg_submetrica = db.query(RegistoSubMetricas).filter(RegistoSubMetricas.id == registo_submetrica_id).first()
    if not reg_submetrica:
        raise HTTPException(status_code=404, detail="Registo Sub-metrica não encontrado.")
    db.delete(reg_submetrica)
    db.commit()


@router.get("/posicoes_metricas", response_model=list[PosicaoMetricaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(PosicaoMetricas).all()


@router.post("/posicoes_metricas", response_model=PosicaoMetricaOut, status_code=201)
def criar(dados: PosicaoMetricaIn, db: Session = Depends(get_db)):
    pos_met = PosicaoMetricas(**dados.model_dump())
    db.add(pos_met)
    db.commit()
    db.refresh(pos_met)
    return pos_met 


@router.put("/posicoes_metricas/{pos_met_id}", response_model=PosicaoMetricaOut)
def actualizar(pos_met_id: int, dados: PosicaoMetricaIn, db: Session = Depends(get_db)):
    pos_met = db.query(PosicaoMetricas).filter(PosicaoMetricas.id == pos_met_id).first()
    if not pos_met:
        raise HTTPException(status_code=404, detail="Posição Métrica não encontrada.")
    pos_met.posicao_id = dados.posicao_id
    pos_met.metrica_id = dados.metrica_id
    pos_met.equipa_id = dados.equipa_id
    db.commit()
    db.refresh(pos_met)
    return pos_met


@router.delete("/posicoes_metricas/{pos_met_id}", status_code=204)
def apagar(pos_met_id: int, db: Session = Depends(get_db)):
    pos_met = db.query(PosicaoMetricas).filter(PosicaoMetricas.id == pos_met_id).first()
    if not pos_met:
        raise HTTPException(status_code=404, detail="Posição Métrica não encontrada.")
    db.delete(pos_met)
    db.commit()
