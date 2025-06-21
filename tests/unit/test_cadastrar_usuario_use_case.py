import pytest
from unittest.mock import Mock
from datetime import datetime
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException
from src.application.dtos.user_dto import UserCreateDTO
from src.application.use_cases.cadastrar_user import CadastrarUsuarioUseCase

@pytest.fixture
def user_repository_mock():
    return Mock()

@pytest.fixture
def valid_dto():
    return UserCreateDTO(
        email="usecase_test_john@example.com",
        senha="senha123",
        full_name="John Doe"
    )

def test_cadastrar_usuario_com_sucesso(user_repository_mock, valid_dto):
    # Arrange
    user_repository_mock.exists_by_email.return_value = None
    use_case = CadastrarUsuarioUseCase(user_repository_mock)

    # Act
    result = use_case.execute(valid_dto)

    # Assert
    assert str(result.email) == valid_dto.email
    assert result.id is not None
    assert result.full_name == valid_dto.full_name
    assert result.roles == [UserRole.FITNESS]
    assert result.status == UserStatus.PENDING
    assert isinstance(result.criado_em, datetime)
    user_repository_mock.exists_by_email.assert_called_once()
    user_repository_mock.save.assert_called_once()

def test_cadastrar_usuario_email_ja_existe(user_repository_mock, valid_dto):
    # Arrange
    existing_user = User(
        email=EmailVO(valid_dto.email),
        senha_hash="hash123",
        full_name="John Doe",
        roles=[UserRole.FITNESS],
        status=UserStatus.ACTIVE
    )
    user_repository_mock.exists_by_email.return_value = existing_user
    use_case = CadastrarUsuarioUseCase(user_repository_mock)

    # Act & Assert
    with pytest.raises(DomainException) as exc_info:
        use_case.execute(valid_dto)
    
    assert str(exc_info.value) == "E-mail já cadastrado."
    user_repository_mock.exists_by_email.assert_called_once()
    user_repository_mock.save.assert_not_called()