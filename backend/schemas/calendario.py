from datetime import date, datetime

from pydantic import BaseModel


class EpocaIn(BaseModel):
    epoca : str


class EpocaOut(EpocaIn):
    id: int

    # Permite converter um objecto Book (SQLAlchemy) para este modelo Pydantic
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


class CampoOut(CampoIn):
    id: int

    # Permite converter um objecto Book (SQLAlchemy) para este modelo Pydantic
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
