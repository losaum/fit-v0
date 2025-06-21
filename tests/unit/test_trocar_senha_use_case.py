import pytest
from unittest.mock import Mock
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException
from src.domain.IAM.shared.services.password_service import PasswordService
from src.application.dtos.user_dto import UserPasswordChangeDTO
from src.application.use_cases.trocar_senha import TrocarSenhaUseCase

@pytest.fixture
def user_repository_mock():
    return Mock()

@pytest.fixture
def valid_user():
    return User(
        email=EmailVO("usecase_test_password@example.com"),
        senha_hash=PasswordService().get_password_hash("senha_atual"),
        full_name="Test Password User",
        roles=[UserRole.FITNESS],
        status=UserStatus.ACTIVE
    )

@pytest.fixture
def valid_dto():
    return UserPasswordChangeDTO(
        id="user123",
        senha_atual="senha_atual",
        nova_senha="nova_senha123"
    )

def test_trocar_senha_com_sucesso(user_repository_mock, valid_user, valid_dto):
    # Arrange
    user_repository_mock.get_by_id.return_value = valid_user
    use_case = TrocarSenhaUseCase(user_repository_mock)

    # Act
    use_case.execute(valid_dto)

    # Assert
    user_repository_mock.get_by_id.assert_called_once_with(valid_dto.id)
    user_repository_mock.save.assert_called_once()
    assert valid_user.senha_hash != "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY.FHBQw.6Zj.4K"

def test_trocar_senha_usuario_nao_encontrado(user_repository_mock, valid_dto):
    # Arrange
    user_repository_mock.get_by_id.return_value = None
    use_case = TrocarSenhaUseCase(user_repository_mock)

    # Act & Assert
    with pytest.raises(DomainException) as exc_info:
        use_case.execute(valid_dto)
    
    assert str(exc_info.value) == "Usuário não encontrado"
    user_repository_mock.get_by_id.assert_called_once_with(valid_dto.id)
    user_repository_mock.save.assert_not_called()

def test_trocar_senha_senha_atual_incorreta(user_repository_mock, valid_user, valid_dto):
    # Arrange
    valid_dto.senha_atual = "senha_errada"
    user_repository_mock.get_by_id.return_value = valid_user
    use_case = TrocarSenhaUseCase(user_repository_mock)

    # Act & Assert
    with pytest.raises(DomainException) as exc_info:
        use_case.execute(valid_dto)
    
    assert str(exc_info.value) == "Senha atual incorreta"
    user_repository_mock.get_by_id.assert_called_once_with(valid_dto.id)
    user_repository_mock.save.assert_not_called()