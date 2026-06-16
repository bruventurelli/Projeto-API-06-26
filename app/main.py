from fastapi import FastAPI
from app.database import engine, Base
from app.routers import agenda_router
from app import models  # IMPORTANTE: Deixa essa linha aqui para criar as tabelas!

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Agendamentos API")

app.include_router(agenda_router.router, prefix="/agenda")

@app.get("/")
def index():
    return {"status": "ok"}