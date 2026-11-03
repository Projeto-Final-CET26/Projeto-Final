# Modelo da tabela "books".
# Aqui descrevemos as colunas. O SQLAlchemy usa isto para criar a tabela
# e para traduzir cada linha da base de dados num objecto Python.

from sqlalchemy import Table
from database import Base, engine


class Campos(Base):
    __table__ = Table("campo", Base.metadata, autoload_with=engine)



class Epocas(Base):
    __table__ = Table("epoca", Base.metadata, autoload_with=engine)

