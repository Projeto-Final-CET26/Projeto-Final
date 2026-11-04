# Modelo da tabela "books".
# Aqui descrevemos as colunas. O SQLAlchemy usa isto para criar a tabela
# e para traduzir cada linha da base de dados num objecto Python.

from sqlalchemy import Table
from database import Base, engine


class Campos(Base):
    __table__ = Table("campo", Base.metadata, autoload_with=engine)

class Epocas(Base):
    __table__ = Table("epoca", Base.metadata, autoload_with=engine)

class Utilizadores(Base):
    __table__ = Table("utilizadores", Base.metadata, autoload_with=engine)

class Metricas(Base):
    __table__ = Table("metricas", Base.metadata, autoload_with=engine)

class SubMetricas(Base):
    __table__ = Table("submetricas", Base.metadata, autoload_with=engine)

class Lesoes(Base):
    __table__ = Table("lesao", Base.metadata, autoload_with=engine)


