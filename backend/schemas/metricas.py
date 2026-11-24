from datetime import date, datetime

from pydantic import BaseModel


class CoordenadaMetricasIn(BaseModel):
    registo_metrica_id: int
    posicao_X: float
    posicao_Y: float


class CoordenadaMetricasOut(CoordenadaMetricasIn):
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


class PosicaoMetricaIn(BaseModel):
    posicao_id: int
    metrica_id: int
    equipa_id: int


class PosicaoMetricaOut(PosicaoMetricaIn):
    id: int

    model_config = {"from_attributes": True}
