# Ligação à base de dados MySQL.
# Este ficheiro só trata de comunicar com o MySQL:
# criar a base se faltar, abrir sessões e fechá-las no fim.

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Endereço de ligação:
# utilizador "root", sem palavra-passe, servidor local, porta 3306, base "library".
# Se o MySQL tiver palavra-passe, use: mysql+pymysql://root:PASSWORD@localhost:3306/library
DATABASE_URL = "mysql+pymysql://root@localhost:3306/library"

# Primeiro ligamos sem escolher uma base, só para criar a "library" se ainda não existir.
with create_engine("mysql+pymysql://root@localhost:3306").connect() as ligacao:
    ligacao.execute(text("CREATE DATABASE IF NOT EXISTS library"))
    ligacao.commit()

# Motor de ligação já apontado para a base "library".
engine = create_engine(DATABASE_URL)

# Fábrica de sessões: cada pedido à API usa uma sessão para ler/escrever na tabela.
SessionLocal = sessionmaker(bind=engine)


# Classe-mãe dos modelos (tabelas). O models.py herda desta classe.
class Base(DeclarativeBase):
    pass


# Função usada pelo FastAPI (Depends) em cada pedido.
# Abre uma sessão, entrega-a ao endpoint e fecha-a no fim, mesmo se der erro.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
