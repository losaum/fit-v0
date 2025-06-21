from fastapi.testclient import TestClient
import pytest
from sqlalchemy.orm import Session
from src.main import app
from src.api.dependencies import get_db

@pytest.fixture
def client(db_session):
    # Sobrescreve a dependência do banco de dados para usar a sessão de teste
    def override_get_db():
        try:
            yield db_session
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise
    
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    # Limpa as sobreposições de dependência após o teste
    app.dependency_overrides.clear()

def test_create_nutritionist(client):
    # Dados para criar um nutricionista
    nutritionist_data = {
        "email": "nutricionista_teste_2@exemplo.com",
        "senha": "senha12345",
        "full_name": "Nutricionista Teste",
        "crn_number": "12345"
    }

    # Faz a requisição POST
    response = client.post("/users/nutritionist", json=nutritionist_data)

    # Verifica se a resposta foi bem-sucedida
    assert response.status_code == 201
    
    # Verifica os dados retornados
    data = response.json()
    assert data["email"] == nutritionist_data["email"]
    assert "NUTRITIONIST" in data["roles"]
    assert data["status"] == "PENDING"

def test_create_nutritionist_invalid_data(client):
    # Dados inválidos (sem crn_number)
    invalid_data = {
        "email": "nutricionista_invalid@exemplo.com",
        "senha": "senha12345",
        "full_name": "Nutricionista Teste"
    }

    # Faz a requisição POST
    response = client.post("/users/nutritionist", json=invalid_data)

    # Verifica se retornou erro de validação
    assert response.status_code == 422