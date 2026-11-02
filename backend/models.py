# Modelo da tabela "books".
# Aqui descrevemos as colunas. O SQLAlchemy usa isto para criar a tabela
# e para traduzir cada linha da base de dados num objecto Python.

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Book(Base):
    # Nome real da tabela no MySQL
    __tablename__ = "books"

    # Chave primária: número inteiro gerado automaticamente (1, 2, 3, ...)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Título e autor são obrigatórios (não podem ficar vazios na base de dados)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)

    # Ano de publicação: opcional (pode ser nulo)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
