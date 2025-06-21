# from fastapi.testclient import TestClient
# import pytest
# from uuid import uuid4
# from src.main import app
# from src.domain.IAM.user.entities.user import UserRole
# from src.infrastructure.db.database import Base
# from src.api.dependencies import get_db

# @pytest.fixture(scope="function")
# def client(db_session):
#     # Sobrescreve a dependência do banco de dados para usar a sessão de teste
#     def override_get_db():
#         try:
#             yield db_session
#             db_session.commit()
#         except Exception:
#             db_session.rollback()
#             raise
    
#     app.dependency_overrides[get_db] = override_get_db
#     client = TestClient(app)
#     yield client
#     # Limpa as sobreposições de dependência após o teste
#     app.dependency_overrides.clear()

# def test_add_nutritionist_profile(client):
#     # Primeiro, cria um usuário trainer
#     trainer_data = {
#         "email": "trainer_with_nutri@exemplo.com",
#         "senha": "senha12345",
#         "full_name": "Trainer Teste",
#         "cref_number": "123456-G/SP"
#     }
    
#     response = client.post("/users/trainer", json=trainer_data)
#     assert response.status_code == 201
#     user_id = response.json()["id"]

#     # Dados para adicionar perfil de nutricionista
#     nutritionist_data = {
#         "full_name": "Trainer Nutricionista",
#         "crn_number": "12345",
#         "specialties": ["Nutrição Esportiva", "Nutrição Clínica"],
#         "certifications": ["CRN", "Especialização em Nutrição Esportiva"],
#         "experience_years": "5",
#         "availability": ["manhã", "tarde"],
#         "dietary_approach": ["Vegetariana", "Low Carb"],
#         "bio": "Nutricionista especializado em nutrição esportiva"
#     }

#     # Faz a requisição POST para adicionar o perfil de nutricionista
#     response = client.post(f"/profiles/users/{user_id}/nutritionist", json=nutritionist_data)

#     # Verifica se a resposta foi bem-sucedida
#     assert response.status_code == 200
    
#     # Verifica os dados retornados
#     data = response.json()
#     assert UserRole.NUTRITIONIST.value in data["roles"]
#     assert UserRole.TRAINER.value in data["roles"]

# def test_add_nutritionist_profile_invalid_user(client):
#     # Tenta adicionar perfil para um usuário que não existe
#     invalid_user_id = str(uuid4())
#     nutritionist_data = {
#         "full_name": "Nutricionista Teste",
#         "crn_number": "12345"
#     }

#     response = client.post(f"/profiles/users/{invalid_user_id}/nutritionist", json=nutritionist_data)
#     assert response.status_code == 400
#     assert "Usuário não encontrado" in response.json()["detail"]

# def test_add_duplicate_nutritionist_profile(client):
#     # Primeiro, cria um usuário nutricionista
#     nutritionist_data = {
#         "email": "nutri_duplicate_test@exemplo.com",
#         "senha": "senha12345",
#         "full_name": "Nutricionista Teste",
#         "crn_number": "54321"
#     }
    
#     response = client.post("/users/nutritionist", json=nutritionist_data)
#     assert response.status_code == 201
#     user_id = response.json()["id"]

#     # Tenta adicionar outro perfil de nutricionista ao mesmo usuário
#     duplicate_data = {
#         "full_name": "Nutricionista Teste 2",
#         "crn_number": "98765"
#     }

#     response = client.post(f"/profiles/users/{user_id}/nutritionist", json=duplicate_data)
#     assert response.status_code == 400
#     assert "Usuário já possui perfil de nutricionista" in response.json()["detail"]