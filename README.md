# Sistema de Agendamentos API

API RESTful para gerenciamento de agendamentos locais, desenvolvida com o framework FastAPI e persistência de dados em SQLite utilizando SQLAlchemy.

## Tecnologias Utilizadas

* Python 3
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* Pydantic

## Estrutura do Projeto

* `app/main.py`: Ponto de entrada da aplicação e inicialização do banco de dados.
* `app/database.py`: Configuração da conexão com o banco de dados SQLite.
* `app/models.py`: Definição das tabelas e modelos do banco de dados.
* `app/schemas.py`: Schemas de validação de dados com Pydantic.
* `app/routers/`: Módulos de rotas isoladas da aplicação.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. pip install -r requirements.txt
3. python -m uvicorn app.main:app --reload
4. Ative o ambiente virtual:
```bash
   .\venv\Scripts\activate
