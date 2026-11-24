from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers.calendario import router as calendario_router
from routers.metricas import router as metricas_router
from routers.plantel import router as plantel_router


# Cria as tabelas no MySQL se ainda n?o existirem.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Projeto final",
    openapi_tags=[
        {"name": "Calendário e competições", "description": "Campos, competições, épocas, jogos e desportos."},
        {"name": "Plantel e saúde", "description": "Utilizadores, jogadores, equipa técnica, posições e lesões."},
        {"name": "Métricas", "description": "Métricas, registos e associações a jogos, posições e jogadores."},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calendario_router)
app.include_router(plantel_router)
app.include_router(metricas_router)
