from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()


@router.post("/", response_model=schemas.AgendamentoResponse, status_code=status.HTTP_201_CREATED)
def agendar_horario(agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    novo_agendamento = models.Agendamento(
        nome_cliente=agendamento.nome_cliente,
        data=agendamento.data,
        horario=agendamento.horario,
        servico=agendamento.servico
    )
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    return novo_agendamento

@router.get("/", response_model=list[schemas.AgendamentoResponse])
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(models.Agendamento).all()