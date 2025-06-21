from fastapi.testclient import TestClient
import pytest
from datetime import date
from sqlalchemy.orm import Session
from src.main import app
from src.api.dependencies import get_db
from src.infrastructure.db.base import Base

@pytest.fixture
def client(db_session: Session):
    # Garante que as tabelas existam
    Base.metadata.create_all(bind=db_session.get_bind())
    
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

def test_create_fitness(client):
    # Dados para criar um usuário fitness
    fitness_data = {
        "email": "api_test_fitness@exemplo.com",
        "senha": "senha12345",
        "full_name": "Fitness Teste",
        "birth_date": "1990-01-01",
        "height": 170.0,
        "weight": 70.0,
        "fitness_goals": ["Perda de peso", "Ganho de força"],
        "training_preferences": ["Musculação", "Yoga"],
        "health_conditions": ["Nenhuma"],
        "dietary_restrictions": ["Sem glúten"],
        "preferred_training_time": "manhã",
        "training_frequency": 4,
        "experience_level": "intermediário"
    }

    # Faz a requisição POST
    response = client.post("/users/fitness", json=fitness_data)

    # Verifica se a resposta foi bem-sucedida
    assert response.status_code == 201
    
    # Verifica os dados retornados
    data = response.json()
    assert data["email"] == fitness_data["email"]
    assert "id" in data
    assert "criado_em" in data

def test_create_fitness_invalid_data(client):
    # Dados inválidos (sem campos obrigatórios)
    invalid_data = {
        "email": "fitness@exemplo.com",
        "senha": "senha12345",
        "full_name": "Fitness Teste"
    }

    # Faz a requisição POST
    response = client.post("/users/fitness", json=invalid_data)

    # Verifica se a resposta indica erro de validação
    assert response.status_code == 422