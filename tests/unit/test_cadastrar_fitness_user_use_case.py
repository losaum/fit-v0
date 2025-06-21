import pytest
from datetime import date, datetime
from unittest.mock import Mock
from src.domain.IAM.user.entities.user import UserRole, UserStatus
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.user.services.password_service import PasswordService
from src.domain.IAM.user.use_cases.cadastrar_fitness_user import CadastrarFitnessUserUseCase, CadastrarFitnessUserDTO

@pytest.fixture
def valid_dto():
    return CadastrarFitnessUserDTO(
        email="usecase_test_maria@example.com",
        senha="senha123",
        full_name="Maria Silva",
        birth_date=date(1990, 5, 15),
        height=165.0,
        weight=60.0,
        fitness_goals=["Perda de peso", "Ganho de força"],
        training_preferences=["Musculação", "Yoga"],
        health_conditions=["Nenhuma"],
        dietary_restrictions=["Sem glúten"],
        preferred_training_time="manhã",
        training_frequency=4,
        experience_level="intermediário"
    )

@pytest.fixture
def user_repository_mock():
    return Mock()

@pytest.fixture
def password_service():
    return PasswordService()

@pytest.fixture
def use_case(user_repository_mock, password_service):
    return CadastrarFitnessUserUseCase(user_repository_mock, password_service)

def test_cadastrar_fitness_user_com_sucesso(use_case, valid_dto, user_repository_mock):
    # Configura o mock para indicar que o email não existe
    user_repository_mock.find_by_email.return_value = None

    # Executa o caso de uso
    user_id = use_case.execute(valid_dto)

    # Verifica se um ID foi retornado
    assert user_id is not None

    # Verifica se o usuário foi salvo
    user_repository_mock.save.assert_called_once()
    saved_user, saved_profile = user_repository_mock.save.call_args[0]

    # Verifica o usuário criado
    assert str(saved_user.email) == valid_dto.email
    assert saved_user.id == user_id
    assert saved_user.full_name == valid_dto.full_name
    assert saved_user.roles == [UserRole.FITNESS]
    assert saved_user.status == UserStatus.PENDING

    # Verifica o perfil fitness criado
    assert saved_profile.birth_date == valid_dto.birth_date
    assert saved_profile.height == valid_dto.height
    assert saved_profile.weight == valid_dto.weight
    assert saved_profile.fitness_goals == valid_dto.fitness_goals
    assert saved_profile.training_preferences == valid_dto.training_preferences
    assert saved_profile.health_conditions == valid_dto.health_conditions
    assert saved_profile.dietary_restrictions == valid_dto.dietary_restrictions
    assert saved_profile.preferred_training_time == valid_dto.preferred_training_time
    assert saved_profile.training_frequency == valid_dto.training_frequency
    assert saved_profile.experience_level == valid_dto.experience_level

def test_cadastrar_fitness_user_email_ja_existe(use_case, valid_dto, user_repository_mock):
    # Configura o mock para indicar que o email já existe
    user_repository_mock.find_by_email.return_value = True

    # Verifica se a exceção é lançada
    with pytest.raises(ValueError, match="Email já cadastrado"):
        use_case.execute(valid_dto)

    # Verifica que o save não foi chamado
    user_repository_mock.save.assert_not_called()