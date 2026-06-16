from sqlalchemy import Column, Integer, String
from app.database import Base

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome_cliente = Column(String, nullable=False)
    data = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    servico = Column(String, nullable=False)