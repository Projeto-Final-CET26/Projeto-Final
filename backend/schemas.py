# Esquemas Pydantic: definem o formato do JSON da API.
# São diferentes do models.py:
#   - models.py  ->  tabela MySQL (SQLAlchemy)
#   - schemas.py ->  dados que entram e saem na API (Pydantic)

from pydantic import BaseModel


# Dados que o cliente envia para criar ou actualizar um livro (JSON de entrada)
class BookIn(BaseModel):
    title: str
    author: str
    year: int | None = None  # o ano é opcional


# Dados que a API devolve (os mesmos campos + o id gerado pela base de dados)
class BookOut(BookIn):
    id: int

    # Permite converter um objecto Book (SQLAlchemy) para este modelo Pydantic
    model_config = {"from_attributes": True}
