from dataclasses import dataclass
from datetime import date
from typing import List
from uuid import UUID, uuid4

from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.fitness_profile import FitnessProfile
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.user.repositories.user_repository import UserRepository
from src.domain.IAM.user.services.password_service import PasswordService

@dataclass
class CadastrarFitnessUserDTO:
    email: str
    senha: str
    full_name: str
    birth_date: date
    height: float
    weight: float
    fitness_goals: List[str]
    training_preferences: List[str]
    health_conditions: List[str]
    dietary_restrictions: List[str]
    preferred_training_time: str
    training_frequency: int
    experience_level: str

class CadastrarFitnessUserUseCase:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService):
        self.user_repository = user_repository
        self.password_service = password_service

    def execute(self, dto: CadastrarFitnessUserDTO) -> UUID:
        # Verifica se já existe um usuário com o mesmo email
        if self.user_repository.find_by_email(EmailVO(dto.email)):
            raise ValueError("Email já cadastrado")

        # Cria o hash da senha
        senha_hash = self.password_service.hash_password(dto.senha)

        # Cria o ID que será compartilhado entre User e FitnessProfile
        user_id = uuid4()

        # Cria o usuário
        user = User(
            id=user_id,
            email=EmailVO(dto.email),
            senha_hash=senha_hash,
            roles=[UserRole.FITNESS],
            status=UserStatus.PENDING
        )

        # Cria o perfil fitness
        fitness_profile = FitnessProfile(
            id=user_id,
            full_name=dto.full_name,
            birth_date=dto.birth_date,
            height=dto.height,
            weight=dto.weight,
            fitness_goals=dto.fitness_goals,
            training_preferences=dto.training_preferences,
            health_conditions=dto.health_conditions,
            dietary_restrictions=dto.dietary_restrictions,
            preferred_training_time=dto.preferred_training_time,
            training_frequency=dto.training_frequency,
            experience_level=dto.experience_level
        )

        # Salva o usuário e o perfil fitness
        self.user_repository.save(user, fitness_profile)

        return user_id