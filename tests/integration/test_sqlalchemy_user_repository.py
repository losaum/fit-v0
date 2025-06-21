import pytest
from src.domain.IAM.entities.user import User
from src.domain.IAM.value_objects.email import EmailVO
from src.infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository

@pytest.fixture
def user_repository(db_session):
    return SQLAlchemyUserRepository(db_session)

@pytest.fixture
def sample_user():
    return User(
        nome="Test User",
        email=EmailVO("test@example.com"),
        senha_hash="hashed_password123"
    )

def test_save_new_user(user_repository, sample_user):
    # Act
    saved_user = user_repository.save(sample_user)

    # Assert
    assert saved_user.id is not None
    assert saved_user.nome == sample_user.nome
    assert str(saved_user.email) == str(sample_user.email)
    assert saved_user.senha_hash == sample_user.senha_hash

def test_save_existing_user(user_repository, sample_user):
    # Arrange
    saved_user = user_repository.save(sample_user)
    saved_user.nome = "Updated Name"

    # Act
    updated_user = user_repository.save(saved_user)

    # Assert
    assert updated_user.id == saved_user.id
    assert updated_user.nome == "Updated Name"
    assert str(updated_user.email) == str(sample_user.email)

def test_exists_by_email_when_exists(user_repository, sample_user):
    # Arrange
    user_repository.save(sample_user)

    # Act
    existing_user = user_repository.exists_by_email(sample_user.email)

    # Assert
    assert existing_user is not None
    assert str(existing_user.email) == str(sample_user.email)

def test_exists_by_email_when_not_exists(user_repository):
    # Act
    non_existing_user = user_repository.exists_by_email(EmailVO("nonexistent@example.com"))

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
    assert found_user.nome == saved_user.nome
    assert str(found_user.email) == str(saved_user.email)

def test_get_by_id_when_not_exists(user_repository):
    # Act
    non_existing_user = user_repository.get_by_id("nonexistent_id")

    # Assert
    assert non_existing_user is None