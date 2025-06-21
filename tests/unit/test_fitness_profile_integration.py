import pytest
from uuid import UUID
from datetime import datetime, date
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.fitness_profile import FitnessProfile
from src.domain.IAM.user.value_objects.email import EmailVO

@pytest.fixture
def sample_user():
    return User(
        email=EmailVO("unit_test_student@example.com"),
        senha_hash="hashed_password",
        full_name="Maria Silva",
        roles=[UserRole.FITNESS],
        status=UserStatus.ACTIVE,
        id="123e4567-e89b-12d3-a456-426614174000",
        criado_em=datetime(2024, 1, 1, 0, 0, 0)
    )

@pytest.fixture
def sample_fitness_profile(sample_user):
    return FitnessProfile(
        id=UUID(sample_user.id),
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

def test_create_fitness_profile(sample_fitness_profile):
    assert isinstance(sample_fitness_profile.id, UUID)
    assert sample_fitness_profile.birth_date == date(1990, 5, 15)
    assert sample_fitness_profile.height == 165.0
    assert sample_fitness_profile.weight == 60.0
    assert "Perda de peso" in sample_fitness_profile.fitness_goals
    assert "Musculação" in sample_fitness_profile.training_preferences
    assert sample_fitness_profile.health_conditions == ["Nenhuma"]
    assert sample_fitness_profile.dietary_restrictions == ["Sem glúten"]
    assert sample_fitness_profile.preferred_training_time == "manhã"
    assert sample_fitness_profile.training_frequency == 4
    assert sample_fitness_profile.experience_level == "intermediário"

def test_user_fitness_role_integration(sample_user):
    # Verifica se o usuário tem o papel de FITNESS
    assert UserRole.FITNESS in sample_user.roles
    assert sample_user.has_role(UserRole.FITNESS)
    
    # Verifica que o usuário não tem outros papéis
    assert not sample_user.has_role(UserRole.TRAINER)
    assert not sample_user.has_role(UserRole.NUTRITIONIST)