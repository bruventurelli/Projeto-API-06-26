from fastapi import FastAPI
from app.database import engine, Base
from app.routers import agenda_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Agendamentos API")

app.include_router(agenda_router.router, prefix="/agenda")

@app.get("/")
def index():
    return {"status": "ok"}