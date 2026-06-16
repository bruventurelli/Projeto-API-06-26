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

# Instalação e Execução

```bash
.\venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
Após iniciar o servidor, a documentação interativa Swagger estará disponível no endereço local:
http://127.0.0.1:8000/docs
