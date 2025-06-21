import pytest
from uuid import UUID
from datetime import datetime
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.trainer_profile import TrainerProfile
from src.domain.IAM.user.value_objects.email import EmailVO

@pytest.fixture
def sample_user():
    return User(
        email=EmailVO("unit_test_trainer@example.com"),
        senha_hash="hashed_password",
        full_name="João Silva",
        roles=[UserRole.TRAINER],
        status=UserStatus.ACTIVE,
        id="123e4567-e89b-12d3-a456-426614174000",
        criado_em=datetime(2024, 1, 1, 0, 0, 0)
    )

@pytest.fixture
def sample_trainer_profile(sample_user):
    return TrainerProfile(
        id=UUID(sample_user.id),
        cref_number="123456-G/SP"
    )

def test_create_trainer_profile(sample_trainer_profile):
    assert isinstance(sample_trainer_profile.id, UUID)
    assert sample_trainer_profile.cref_number == "123456-G/SP"

def test_user_trainer_role_integration(sample_user):
    # Verifica se o usuário tem o papel de TRAINER
    assert UserRole.TRAINER in sample_user.roles
    
    # Testa adição e remoção do papel de TRAINER
    sample_user.remove_role(UserRole.TRAINER)
    assert UserRole.TRAINER not in sample_user.roles
    
    sample_user.add_role(UserRole.TRAINER)
    assert UserRole.TRAINER in sample_user.roles
    assert sample_user.has_role(UserRole.TRAINER)