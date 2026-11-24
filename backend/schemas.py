# Esquemas Pydantic: definem o formato do JSON da API.
# São diferentes do models.py:
#   - models.py  ->  tabela MySQL (SQLAlchemy)
#   - schemas.py ->  dados que entram e saem na API (Pydantic)

from pydantic import BaseModel
from datetime import date, datetime


# Dados que o cliente envia para criar ou actualizar um livro (JSON de entrada)
class EpocaIn(BaseModel):
    epoca : str


# Dados que a API devolve (os mesmos campos + o id gerado pela base de dados)
class EpocaOut(EpocaIn):
    id: int

    # Permite converter um objecto Book (SQLAlchemy) para este modelo Pydantic
    model_config = {"from_attributes": True}

class CoordenadaMetricasIn(BaseModel):
    registo_metrica_id: int
    posicao_X: float
    posicao_Y: float

class CoordenadaMetricasOut(CoordenadaMetricasIn):
    id: int

    model_config = {"from_attributes": True}

class CompeticaoIn(BaseModel):
    nome: int
    tipo_competicao: int 

class CompeticaoOut(CompeticaoIn):
    id: int

    model_config = {"from_attributes": True}




class CampoIn(BaseModel):
    nome: str
    morada: str | None
    cidade: str | None
    capacidade: int | None


# Dados que a API devolve (os mesmos campos + o id gerado pela base de dados)
class CampoOut(CampoIn):
    id: int

    # Permite converter um objecto Book (SQLAlchemy) para este modelo Pydantic
    model_config = {"from_attributes": True}



class UtilizadorIn(BaseModel):
    primeiro_nome: str
    apelido: str | None
    tipo: int
    password: str
    email: str
    foto_url: str


class UtilizadorOut(UtilizadorIn):
    id: int

    model_config = {"from_attributes": True}



class GestorIn(BaseModel):
    primeiro_nome: str
    apelido: str | None
    equipa_id : int


class GestorOut(GestorIn):
    id: int

    model_config = {"from_attributes": True}



class MetricasIn(BaseModel):
    descricao: str
    unidade: str
    desporto_id: int
    sempre_visivel: str


class MetricasOut(MetricasIn):
    id: int

    model_config = {"from_attributes": True}

class RegistoMetricasIn(BaseModel):
    jogador_id: int
    equipa_id: int
    jogo_id: int
    metrica_id: int
    periodo: int
    tempo_segundos: int
    sucesso: str
    tem_posicao: str
    obs: str

class RegistoMetricasOut(RegistoMetricasIn):
    id: int

    model_config = {"from_attributes": True}

class MetricasJogoIn(BaseModel):
    gestor_id: int
    jogador_id: int
    jogo_id: int
    equipa_id: int
    metrica_id: int
    valor: float 

class MetricasJogoOut(MetricasJogoIn):
    id: int

    model_config = {"from_attributes": True}

class SubMetricaIn(BaseModel):
    metrica_id: int
    descricao: str
    equipa_id: int | None


class SubMetricaOut(SubMetricaIn):
    id: int

    model_config = {"from_attributes": True}

class RegistoSubMetricaIn(BaseModel):
    submetrica_id: int
    registo_metrica_id: int

class RegistoSubMetricaOut(RegistoSubMetricaIn):

    model_config = {"from_attributes": True}


class SubmetricasJogoIn(BaseModel):
    jogo_id: int
    jogador_id: int
    submetrica_id: int
    valor: float

class SubmetricasJogoOut(SubmetricasJogoIn):
    id: int

    model_config = {"from_attributes": True}


class JogadorIn(BaseModel):
    primeiro_nome: str
    apelido: str | None
    nacionalidade: str
    data_nascimento: date
    altura_cm: float
    peso_kg: float
    foto_url: str | None
    numero_camisola: int | None
    equipa_id: int
    desporto_id: int
    posicao_id: int
    utilizador_id: int | None


class JogadorOut(JogadorIn):
    id: int

    model_config = {"from_attributes": True}

class JogoJogadoresIn(BaseModel):
    jogo_id: int
    equipa_id: int
    jogador_id: int
    estatudo: str
    numero_camisola: int

class JogoJogadoresOut(JogoJogadoresIn):
    id: int

    model_config = {"from_attributes": True}




class LesaoIn(BaseModel):
    estado: str
    descricao: str
    jogador_id: int
    epoca_id: int
    zona: int
    data_inicio: date 
    data_prevista_fim: date | None
    data_fim: date | None


class LesaoOut(LesaoIn):
    id: int

    model_config = {"from_attributes": True}

class PosicaoIn(BaseModel):
    desporto_id: int
    nome: str
    sigla: int


class PosicaoOut(PosicaoIn):
    id: int

    model_config = {"from_attributes": True}

class PosicaoSecundariaIn(BaseModel):
    posicao_id: int
    jogador_id: int


class PosicaoSecundariaOut(PosicaoSecundariaIn):
    id: int

    model_config = {"from_attributes": True}

class PosicaoMetricaIn(BaseModel):
    posicao_id: int
    metrica_id: int
    equipa_id: int


class PosicaoMetricaOut(PosicaoMetricaIn):
    id: int

    model_config = {"from_attributes": True}

class JogoIn(BaseModel):
    epoca_id: int
    campo_id: int
    equipa_casa: int
    equipa_fora: int
    pontos_casa: int
    pontos_fora: int
    data_hora: datetime

class JogoOut(JogoIn):
    id: int

    model_config = {"from_attributes": True}

class ZonaLesaoIn(BaseModel):
    descricao: str
    segmento: str 

class ZonaLesaoOut(ZonaLesaoIn):
    id: int

    model_config = {"from_attributes": True}


class DesportoIn(BaseModel):
    nome: str
    icone_url: str | None
    periodos: int
    duracao_periodo_seg: int

class DesportoOut(DesportoIn):
    id: int

    model_config = {"from_attributes": True}



class JogoOut(JogoIn):
    id: int

    model_config = {"from_attributes": True}