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

# CRUD COMPETICOES
@app.get("/competicoes", response_model=list[CompeticaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Competicoes).all()

@app.post("/competicoes", response_model=CompeticaoOut, status_code=201)
def criar(dados: CompeticaoIn, db: Session = Depends(get_db)):
    competicao = Competicoes(**dados.model_dump())
    db.add(competicao)
    db.commit()
    db.refresh(competicao)
    return competicao 

@app.put("/competicoes/{competicao_id}", response_model=CompeticaoOut)
def actualizar(competicao_id: int, dados: CompeticaoIn, db: Session = Depends(get_db)):
    competicao = db.query(Competicoes).filter(Competicoes.id == competicao_id).first()
    if not competicao:
        raise HTTPException(status_code=404, detail="Competição não encontrada.")
    competicao.nome = dados.nome
    competicao.tipo_competicao = dados.tipo_competicao
    db.commit()
    db.refresh(competicao)
    return competicao

@app.delete("/competicoes/{competicao_id}", status_code=204)
def apagar(competicao_id: int, db: Session = Depends(get_db)):
    competicao = db.query(Competicoes).filter(Competicoes.id == competicao_id).first()
    if not competicao:
        raise HTTPException(status_code=404, detail="Competição não encontrada")
    db.delete(competicao)
    db.commit()

# CRUD COORDENADAS_METRICAS
@app.get("/coordenadas_metricas", response_model=list[CoordenadaMetricasOut])
def listar(db: Session = Depends(get_db)):
    return db.query(CoordernadasMetricas).all()

@app.post("/coordenadas_metricas", response_model=CampoOut, status_code=201)
def criar(dados: CoordenadaMetricasIn, db: Session = Depends(get_db)):
    coordenadas_metricas = CoordernadasMetricas(**dados.model_dump())
    db.add(coordenadas_metricas)
    db.commit()
    db.refresh(coordenadas_metricas)
    return coordenadas_metricas 

@app.put("/coordenadas_metricas/{coordenada_metrica_id}", response_model=CoordenadaMetricasOut)
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

@app.delete("/coordenadas_metricas/{coordenada_metrica_id}", status_code=204)
def apagar(coordenada_metrica_id: int, db: Session = Depends(get_db)):
    coordenada_metrica = db.query(CoordernadasMetricas).filter(CoordernadasMetricas.id == coordenada_metrica_id).first()
    if not coordenada_metrica:
        raise HTTPException(status_code=404, detail="Coordenada Métrica não encontrada.")
    db.delete(coordenada_metrica)
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

@app.delete("/utilizadores/{utilizador_id}", status_code=204)
def apagar(utilizador_id: int, db: Session = Depends(get_db)):
    utilizador = db.query(Utilizadores).filter(Utilizadores.id == utilizador_id).first()
    if not utilizador:
        raise HTTPException(status_code=404, detail="Utilizador não encontrado.")
    db.delete(utilizador)
    db.commit()

# CRUD METRICAS 
@app.get("/metricas", response_model=list[MetricasOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Metricas).all()

@app.post("/metricas", response_model=MetricasOut, status_code=201)
def criar(dados: MetricasIn, db: Session = Depends(get_db)):
    metrica = Metricas(**dados.model_dump())
    db.add(metrica)
    db.commit()
    db.refresh(metrica)
    return metrica

@app.put("/metricas/{metrica_id}", response_model=MetricasOut)
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

@app.delete("/metricas/{metrica_id}", status_code=204)
def apagar(metrica_id: int, db: Session = Depends(get_db)):
    metrica = db.query(Metricas).filter(Metricas.id == metrica_id).first()
    if not metrica:
        raise HTTPException(status_code=404, detail="Metrica não encontrada.")
    db.delete(metrica)
    db.commit()

# CRUD REGISTO_METRICAS 
@app.get("/registo_metricas", response_model=list[RegistoMetricasIn])
def listar(db: Session = Depends(get_db)):
    return db.query(RegistoMetricas).all()

@app.post("/registo_metricas", response_model=RegistoMetricasOut, status_code=201)
def criar(dados: RegistoMetricasIn, db: Session = Depends(get_db)):
    reg_metrica = RegistoMetricas(**dados.model_dump())
    db.add(reg_metrica)
    db.commit()
    db.refresh(reg_metrica)
    return reg_metrica 

@app.put("/registo_metricas/{registo_metrica_id}", response_model=RegistoMetricasOut)
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

@app.delete("/registo_metricas/{registo_metrica_id}", status_code=204)
def apagar(registo_metrica_id: int, db: Session = Depends(get_db)):
    reg_metrica = db.query(RegistoMetricas).filter(RegistoMetricas.id == registo_metrica_id).first()
    if not reg_metrica:
        raise HTTPException(status_code=404, detail="RegistoMetrica não encontrada.")
    db.delete(reg_metrica)
    db.commit()

# CRUD METRICAS_JOGO 
@app.get("/metricas_jogo", response_model=list[MetricasJogoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(MetricasJogos).all()

@app.post("/metricas_jogo", response_model=MetricasJogoOut, status_code=201)
def criar(dados: MetricasJogoIn, db: Session = Depends(get_db)):
    metrica_jogo = MetricasJogos(**dados.model_dump())
    db.add(metrica_jogo)
    db.commit()
    db.refresh(metrica_jogo)
    return metrica_jogo 

@app.put("/metricas_jogo/{metricas_jogo_id}", response_model=MetricasJogoOut)
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

@app.delete("/metricas_jogo/{metricas_jogo_id}", status_code=204)
def apagar(metricas_jogo_id: int, db: Session = Depends(get_db)):
    metricas_jogo = db.query(MetricasJogos).filter(MetricasJogos.id == metricas_jogo_id).first()
    if not metricas_jogo:
        raise HTTPException(status_code=404, detail="Metricas Jogo não encontrada.")
    db.delete(metricas_jogo)
    db.commit()

# CRUD SUBMETRICAS 
@app.get("/submetricas", response_model=list[SubMetricaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(SubMetricas).all()

@app.post("/submetricas", response_model=SubMetricaOut, status_code=201)
def criar(dados: SubMetricaIn, db: Session = Depends(get_db)):
    submetrica = SubMetricas(**dados.model_dump())
    db.add(submetrica)
    db.commit()
    db.refresh(submetrica)
    return submetrica

@app.put("/submetricas/{submetrica_id}", response_model=SubMetricaOut)
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

@app.delete("/submetricas/{submetrica_id}", status_code=204)
def apagar(submetrica_id: int, db: Session = Depends(get_db)):
    submetrica = db.query(SubMetricas).filter(SubMetricas.id == submetrica_id).first()
    if not submetrica:
        raise HTTPException(status_code=404, detail="Sub-metrica não encontrada.")
    db.delete(submetrica)
    db.commit()

# CRUD REGISTO_SUBMETRICAS 
@app.get("/registo_submetricas", response_model=list[RegistoSubMetricaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(RegistoSubMetricas).all()

@app.post("/registo_submetricas", response_model=RegistoSubMetricaOut, status_code=201)
def criar(dados: RegistoSubMetricaIn, db: Session = Depends(get_db)):
    reg_submetrica = RegistoSubMetricas(**dados.model_dump())
    db.add(reg_submetrica)
    db.commit()
    db.refresh(reg_submetrica)
    return reg_submetrica

@app.put("/registo_submetricas/{registo_submetrica_id}", response_model=RegistoSubMetricaOut)
def actualizar(registo_submetrica_id: int, dados: RegistoSubMetricaIn, db: Session = Depends(get_db)):
    reg_submetrica = db.query(RegistoSubMetricas).filter(RegistoSubMetricas.id == registo_submetrica_id).first()
    if not reg_submetrica:
        raise HTTPException(status_code=404, detail="Registo Sub-metrica não encontrada.")
    reg_submetrica.submetrica_id= dados.submetrica_id
    reg_submetrica.registo_metrica_id = dados.registo_metrica_id
    db.commit()
    db.refresh(reg_submetrica)
    return reg_submetrica 

@app.delete("/registo_submetricas/{registo_submetrica_id}", status_code=204)
def apagar(registo_submetrica_id: int, db: Session = Depends(get_db)):
    reg_submetrica = db.query(RegistoSubMetricas).filter(RegistoSubMetricas.id == registo_submetrica_id).first()
    if not reg_submetrica:
        raise HTTPException(status_code=404, detail="Registo Sub-metrica não encontrado.")
    db.delete(reg_submetrica)
    db.commit()

# CRUD LESAO 
@app.get("/lesoes", response_model=list[LesaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Lesoes).all()

@app.post("/lesoes", response_model=LesaoOut, status_code=201)
def criar(dados: LesaoIn, db: Session = Depends(get_db)):
    lesao = Lesoes(**dados.model_dump())
    db.add(lesao)
    db.commit()
    db.refresh(lesao)
    return lesao 

@app.put("/lesoes/{lesoes_id}", response_model=LesaoOut)
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

@app.delete("/lesoes/{lesao_id}", status_code=204)
def apagar(lesao_id: int, db: Session = Depends(get_db)):
    lesao = db.query(Lesoes).filter(Lesoes.id == lesao_id).first()
    if not lesao:
        raise HTTPException(status_code=404, detail="Lesão não encontrada.")
    db.delete(lesao)
    db.commit()

# READ POSICOES 
@app.get("/posicoes", response_model=list[PosicaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Posicoes).all()

# CRUD POSICAOSECUNDARIA 
@app.get("/posicoes_secundarias", response_model=list[PosicaoSecundariaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(PosicoesSecundarias).all()

@app.post("/posicoes_secundarias", response_model=PosicaoSecundariaOut, status_code=201)
def criar(dados: PosicaoSecundariaIn, db: Session = Depends(get_db)):
    pos_sec = PosicoesSecundarias(**dados.model_dump())
    db.add(pos_sec)
    db.commit()
    db.refresh(pos_sec)
    return pos_sec 

@app.put("/posicoes_secundarias/{pos_sec_id}", response_model=PosicaoSecundariaOut)
def actualizar(pos_sec_id: int, dados: PosicaoSecundariaIn, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    pos_sec.posicao_id = dados.posicao_id
    pos_sec.jogador_id = dados.jogador_id
    db.commit()
    db.refresh(pos_sec)
    return pos_sec 

@app.delete("/posicoes_secundarias/{pos_sec_id}", status_code=204)
def apagar(pos_sec_id: int, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    db.delete(pos_sec)
    db.commit()

# CRUD POSICAO_METRICAS 
@app.get("/posicoes_metricas", response_model=list[PosicaoMetricaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(PosicaoMetricas).all()

@app.post("/posicoes_metricas", response_model=PosicaoMetricaOut, status_code=201)
def criar(dados: PosicaoMetricaIn, db: Session = Depends(get_db)):
    pos_met = PosicaoMetricas(**dados.model_dump())
    db.add(pos_met)
    db.commit()
    db.refresh(pos_met)
    return pos_met 

@app.put("/posicoes_metricas/{pos_met_id}", response_model=PosicaoMetricaOut)
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

@app.delete("/posicoes_metricas/{pos_met_id}", status_code=204)
def apagar(pos_met_id: int, db: Session = Depends(get_db)):
    pos_met = db.query(PosicaoMetricas).filter(PosicaoMetricas.id == pos_met_id).first()
    if not pos_met:
        raise HTTPException(status_code=404, detail="Posição Métrica não encontrada.")
    db.delete(pos_met)
    db.commit()


# CRUD JOGO 
@app.get("/jogos", response_model=list[JogoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Jogos).all()

@app.post("/jogos", response_model=JogoOut, status_code=201)
def criar(dados: JogoIn, db: Session = Depends(get_db)):
    jogo = Jogos(**dados.model_dump())
    db.add(jogo)
    db.commit()
    db.refresh(jogo)
    return jogo

@app.put("/posicoes_secundarias/{pos_sec_id}", response_model=PosicaoSecundariaOut)
def actualizar(pos_sec_id: int, dados: PosicaoSecundariaIn, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    pos_sec.posicao_id = dados.posicao_id
    pos_sec.jogador_id = dados.jogador_id
    db.commit()
    db.refresh(pos_sec)
    return pos_sec 

@app.delete("/posicoes_secundarias/{pos_sec_id}", status_code=204)
def apagar(pos_sec_id: int, db: Session = Depends(get_db)):
    pos_sec = db.query(PosicoesSecundarias).filter(PosicoesSecundarias.id == pos_sec_id).first()
    if not pos_sec:
        raise HTTPException(status_code=404, detail="Posição secundária não encontrada.")
    db.delete(pos_sec)
    db.commit()

# CRUD JOGO_JOGADORES 
@app.get("/jogo_jogadores", response_model=list[JogoJogadoresOut])
def listar(db: Session = Depends(get_db)):
    return db.query(JogoJogadores).all()

@app.post("/jogo_jogadores", response_model=JogoJogadoresOut, status_code=201)
def criar(dados: JogoJogadoresIn, db: Session = Depends(get_db)):
    jogo_jogador = JogoJogadores(**dados.model_dump())
    db.add(jogo_jogador)
    db.commit()
    db.refresh(jogo_jogador)
    return jogo_jogador

@app.put("/jogo_jogadores/{jogo_jogadores_id}", response_model=JogoJogadoresOut)
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

@app.delete("/jogo_jogadores/{jogo_jogadores_id}", status_code=204)
def apagar(jogo_jogadores_id: int, db: Session = Depends(get_db)):
    jogo_jogador = db.query(JogoJogadores).filter(JogoJogadores.id == jogo_jogadores_id).first()
    if not jogo_jogador:
        raise HTTPException(status_code=404, detail="Jogo / Jogador não encontrado.")
    db.delete(jogo_jogador)
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

# CRUD ZONALESAO 
@app.get("/zona_lesao", response_model=list[ZonaLesaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(ZonaLesao).all()

@app.post("/zona_lesao", response_model=ZonaLesaoOut, status_code=201)
def criar(dados: ZonaLesaoIn, db: Session = Depends(get_db)):
    zona_lesao = ZonaLesao(**dados.model_dump())
    db.add(zona_lesao)
    db.commit()
    db.refresh(zona_lesao)
    return zona_lesao

@app.put("/zona_lesao/{zona_lesao_id}", response_model=ZonaLesaoOut)
def actualizar(zona_lesao_id: int, dados: ZonaLesaoIn, db: Session = Depends(get_db)):
    zona_lesao = db.query(ZonaLesao).filter(ZonaLesao.id == zona_lesao_id).first()
    if not zona_lesao:
        raise HTTPException(status_code=404, detail="Zona-Lesão não encontrada.")
    zona_lesao.descricao = dados.descricao
    zona_lesao.segmento = dados.segmento
    db.commit(zona_lesao)
    db.refresh(zona_lesao)
    return zona_lesao

@app.delete("/zona_lesao/{zona_lesao_id}", status_code=204)
def apagar(zona_lesao_id: int, db: Session = Depends(get_db)):
    zona_lesao = db.query(ZonaLesao).filter(ZonaLesao.id == zona_lesao_id).first()
    if not zona_lesao:
        raise HTTPException(status_code=404, detail="Zona-Lesão não encontrada.")
    db.delete(zona_lesao)
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