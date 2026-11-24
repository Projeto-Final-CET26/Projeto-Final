
comando para ativar venv:
    .venv\Scripts\activate

comando para correr api:
    uvicorn main:app --reload --port 8000

Rotas organizadas por tópico em `routers/`:
    calendario.py  -> campos, competições, épocas, jogos e desportos
    plantel.py     -> utilizadores, equipa, posições e lesões
    metricas.py    -> métricas e respetivos registos

Os schemas Pydantic estão organizados pelos mesmos tópicos em `schemas/`.
No Swagger (`/docs`), as operações aparecem agrupadas por estas secções.