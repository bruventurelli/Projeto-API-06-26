from pydantic import BaseModel

class AgendamentoCreate(BaseModel):
    nome_cliente: str
    data: str
    horario: str
    servico: str

class AgendamentoResponse(AgendamentoCreate):
    id: int

    class Config:
        from_attributes = True