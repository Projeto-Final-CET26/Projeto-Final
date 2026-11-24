from sqlalchemy import Table
from database import Base, engine


class Campos(Base):
    __table__ = Table("campo", Base.metadata, autoload_with=engine)

class Competicoes(Base):
    __table__ = Table("competicao", Base.metadata, autoload_with=engine)

class CoordernadasMetricas(Base):
    __table__ = Table("coordenadas_metrica", Base.metadata, autoload_with=engine)

class Epocas(Base):
    __table__ = Table("epoca", Base.metadata, autoload_with=engine)

class Utilizadores(Base):
    __table__ = Table("utilizadores", Base.metadata, autoload_with=engine)

class Metricas(Base):
    __table__ = Table("metricas", Base.metadata, autoload_with=engine)

class RegistoMetricas(Base):
    __table__ = Table("registo_metrica", Base.metadata, autoload_with=engine)

class MetricasJogos(Base):
    __table__ = Table("metricas_jogo", Base.metadata, autoload_with=engine)

class SubMetricas(Base):
    __table__ = Table("submetricas", Base.metadata, autoload_with=engine)

class SubMetricasJogo(Base):
    __table__ = Table("submetricas_jogo", Base.metadata, autoload_with=engine)

class RegistoSubMetricas(Base):
    __table__ = Table("registo_submetricas", Base.metadata, autoload_with=engine)

class Lesoes(Base):
    __table__ = Table("lesao", Base.metadata, autoload_with=engine)

class Posicoes(Base):
    __table__ = Table("posicoes", Base.metadata, autoload_with=engine)

class PosicoesSecundarias(Base):
    __table__ = Table("posicoes_secundarias", Base.metadata, autoload_with=engine)

class Jogos(Base):
    __table__ = Table("jogo", Base.metadata, autoload_with=engine)

class JogoJogadores(Base):
    __table__ = Table("jogo_jogadores", Base.metadata, autoload_with=engine)

class Gestores(Base):
    __table__ = Table("gestor", Base.metadata, autoload_with=engine)

class Jogadores(Base):
    __table__ = Table("jogador", Base.metadata, autoload_with=engine)

class Desportos(Base):
    __table__ = Table("desportos", Base.metadata, autoload_with=engine)






