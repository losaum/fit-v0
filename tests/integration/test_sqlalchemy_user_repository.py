import pytest
from datetime import date
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.fitness_profile import FitnessProfile
from src.domain.IAM.user.entities.trainer_profile import TrainerProfile
from src.domain.IAM.user.value_objects.email import EmailVO
from src.infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from src.infrastructure.db.models.user_model import UserModel
from src.infrastructure.db.models.trainer_profile_model import TrainerProfileModel

@pytest.fixture
def user_repository(db_session):
    return SQLAlchemyUserRepository(db_session)

@pytest.fixture
def sample_user():
    return User(
        email=EmailVO("test@example.com"),
        senha_hash="hashed_password123",
        roles=[UserRole.FITNESS],
        status=UserStatus.PENDING
    )

def test_save_new_user_with_fitness_profile(db_session):
    # Arrange
    repository = SQLAlchemyUserRepository(db_session)
    user = User(
        email=EmailVO("test@example.com"),
        senha_hash="hashed_password123",
        roles=[UserRole.FITNESS],
        status=UserStatus.PENDING
    )

    fitness_profile = FitnessProfile(
        id=user.id,
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

    # Act
    saved_user = repository.save(user, fitness_profile)

    # Assert
    assert saved_user.id == user.id
    assert str(saved_user.email) == str(user.email)
    assert saved_user.senha_hash == user.senha_hash
    
    # Busca o usuário do banco para verificar o perfil fitness
    db_user = db_session.query(UserModel).filter_by(id=user.id).first()
    assert db_user.fitness_profile is not None
    assert db_user.fitness_profile.full_name == fitness_profile.full_name
    assert db_user.fitness_profile.height == fitness_profile.height
    assert db_user.fitness_profile.weight == fitness_profile.weight

def test_save_existing_user(user_repository, sample_user):
    # Arrange
    saved_user = user_repository.save(sample_user)
    saved_user.status = UserStatus.ACTIVE
    saved_user.add_role(UserRole.TRAINER)

    # Act
    updated_user = user_repository.save(saved_user)

    # Assert
    assert updated_user.id == saved_user.id
    assert str(updated_user.email) == str(sample_user.email)
    assert UserRole.TRAINER in updated_user.roles
    assert updated_user.status == UserStatus.ACTIVE

def test_find_by_email_when_exists(user_repository, sample_user):
    # Arrange
    user_repository.save(sample_user)

    # Act
    existing_user = user_repository.find_by_email(sample_user.email)

    # Assert
    assert existing_user is not None
    assert str(existing_user.email) == str(sample_user.email)

def test_find_by_email_when_not_exists(user_repository):
    # Act
    non_existing_user = user_repository.find_by_email(EmailVO("nonexistent@example.com"))

    # Assert
    assert non_existing_user is None

def test_get_by_id_when_exists(user_repository, sample_user):
    # Arrange
    saved_user = user_repository.save(sample_user)

    # Act
    found_user = user_repository.get_by_id(saved_user.id)

    # Assert
    assert found_user is not None
    assert found_user.id == saved_user.id

def test_save_new_user_with_trainer_profile(db_session):
    # Arrange
    repository = SQLAlchemyUserRepository(db_session)
    user = User(
        email=EmailVO("trainer@example.com"),
        senha_hash="hashed_password123",
        roles=[UserRole.TRAINER],
        status=UserStatus.PENDING
    )

    trainer_profile = TrainerProfile(
        id=user.id,
        full_name="João Silva",
        cref_number="123456-G/SP",
        specialties=["Musculação", "Crossfit"],
        certifications=["CREF", "Crossfit L1"],
        experience_years="5",
        availability=["manhã", "tarde"],
        preferred_training_types=["HIIT", "Funcional"],
        bio="Treinador experiente"
    )

    # Act
    saved_user = repository.save(user, trainer_profile)

    # Assert
    assert saved_user.id == user.id
    assert str(saved_user.email) == str(user.email)
    assert saved_user.senha_hash == user.senha_hash
    
    # Busca o usuário do banco para verificar o perfil trainer
    db_user = db_session.query(UserModel).filter_by(id=user.id).first()
    assert db_user.trainer_profile is not None
    assert db_user.trainer_profile.full_name == trainer_profile.full_name
    assert db_user.trainer_profile.cref_number == trainer_profile.cref_number
def test_get_by_id_when_not_exists(user_repository):
    # Act
    non_existing_user = user_repository.get_by_id("nonexistent_id")

    # Assert
    assert non_existing_user is None