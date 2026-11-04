# Esquemas Pydantic: definem o formato do JSON da API.
# São diferentes do models.py:
#   - models.py  ->  tabela MySQL (SQLAlchemy)
#   - schemas.py ->  dados que entram e saem na API (Pydantic)

from pydantic import BaseModel
from datetime import date


# Dados que o cliente envia para criar ou actualizar um livro (JSON de entrada)
class EpocaIn(BaseModel):
    epoca : str


# Dados que a API devolve (os mesmos campos + o id gerado pela base de dados)
class EpocaOut(EpocaIn):
    id: int

    # Permite converter um objecto Book (SQLAlchemy) para este modelo Pydantic
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
class MetricasIn(BaseModel):
    descricao: str
    unidade: str
    desporto_id: int
    sempre_visivel: str


class MetricasOut(MetricasIn):
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
class LesaoIn(BaseModel):
    estado: str
    descricao: str
    jogador_id: int
    epoca_id: int
    zona: int
    data_inicio: date
    data_prevista_fim: date
    data_fim: date


class LesaoOut(LesaoIn):
    id: int

    model_config = {"from_attributes": True}
