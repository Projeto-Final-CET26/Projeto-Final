from datetime import date, datetime

from pydantic import BaseModel


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


class ZonaLesaoIn(BaseModel):
    descricao: str
    segmento: str 


class ZonaLesaoOut(ZonaLesaoIn):
    id: int

    model_config = {"from_attributes": True}
