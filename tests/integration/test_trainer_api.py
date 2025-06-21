from fastapi.testclient import TestClient
import pytest
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_trainer(client):
    # Dados para criar um trainer
    trainer_data = {
        "email": "trainer_only@exemplo.com",
        "senha": "senha12345",
        "full_name": "Trainer Teste",
        "cref_number": "123456-G/SP",
        "specialties": ["Musculação", "Crossfit"],
        "certifications": ["CREF", "Primeiros Socorros"],
        "experience_years": "5",
        "availability": ["manhã", "tarde"],
        "preferred_training_types": ["Personal", "Grupo"],
        "bio": "Personal trainer especializado em treinos funcionais"
    }

    # Faz a requisição POST
    response = client.post("/users/trainer", json=trainer_data)

    # Verifica se a resposta foi bem-sucedida
    assert response.status_code == 201
    
    # Verifica os dados retornados
    data = response.json()
    assert data["email"] == trainer_data["email"]
    assert "id" in data
    assert "criado_em" in data

def test_create_trainer_invalid_data(client):
    # Dados inválidos (sem cref_number)
    invalid_data = {
        "email": "trainer_invalid@exemplo.com",
        "senha": "senha12345",
        "full_name": "Trainer Teste"
    }

    # Faz a requisição POST
    response = client.post("/users/trainer", json=invalid_data)

    # Verifica se a resposta indica erro de validação
    assert response.status_code == 422