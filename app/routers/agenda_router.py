from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def agendar_horario(db: Session = Depends(get_db)):
    return {"mensagem": "Rota funcionando"}