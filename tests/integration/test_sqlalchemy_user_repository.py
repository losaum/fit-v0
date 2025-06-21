import pytest
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.value_objects.email import EmailVO
from src.infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository

@pytest.fixture
def user_repository(db_session):
    return SQLAlchemyUserRepository(db_session)

@pytest.fixture
def sample_user():
    return User(
        email=EmailVO("test@example.com"),
        senha_hash="hashed_password123",
        roles=[UserRole.STUDENT],
        status=UserStatus.PENDING
    )

def test_save_new_user(user_repository, sample_user):
    # Act
    saved_user = user_repository.save(sample_user)

    # Assert
    assert saved_user.id is not None
    assert str(saved_user.email) == str(sample_user.email)
    assert saved_user.senha_hash == sample_user.senha_hash
    assert saved_user.roles == sample_user.roles
    assert saved_user.status == sample_user.status

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
    assert str(found_user.email) == str(saved_user.email)
    assert found_user.roles == saved_user.roles
    assert found_user.status == saved_user.status

def test_get_by_id_when_not_exists(user_repository):
    # Act
    non_existing_user = user_repository.get_by_id("nonexistent_id")

    # Assert
    assert non_existing_user is None