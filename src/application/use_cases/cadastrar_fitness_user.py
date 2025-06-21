from uuid import uuid4
from datetime import datetime
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.fitness_profile import FitnessProfile
from src.domain.IAM.user.value_objects.email import EmailVO
from src.application.dtos.fitness_profile_dto import FitnessProfileCreateDTO
from src.domain.IAM.shared.services.password_service import PasswordService
from src.domain.IAM.user.repositories.user_repository import UserRepository

class CadastrarFitnessUserUseCase:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService):
        self.user_repository = user_repository
        self.password_service = password_service

    def execute(self, dto: FitnessProfileCreateDTO) -> tuple[User, FitnessProfile]:
        # Verifica se já existe usuário com o email
        email_vo = EmailVO(dto.email)
        if self.user_repository.find_by_email(email_vo):
            raise ValueError("Email já cadastrado")

        # Cria o hash da senha
        senha_hash = self.password_service.get_password_hash(dto.senha)

        # Cria o usuário com um ID
        user = User(
            id=str(uuid4()),
            email=email_vo,
            senha_hash=senha_hash,
            roles=[UserRole.FITNESS],
            status=UserStatus.PENDING
        )

        # Cria o perfil fitness com o mesmo ID do usuário
        fitness_profile = FitnessProfile(
            id=user.id,
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

        # Salva o usuário e o perfil
        self.user_repository.save(user, fitness_profile)

        return user.to_dict()