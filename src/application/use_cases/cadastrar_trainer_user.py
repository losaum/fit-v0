from uuid import uuid4
from datetime import datetime
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.trainer_profile import TrainerProfile
from src.domain.IAM.user.value_objects.email import EmailVO
from src.application.dtos.trainer_profile_dto import TrainerProfileCreateDTO
from src.domain.IAM.shared.services.password_service import PasswordService
from src.domain.IAM.user.repositories.user_repository import UserRepository
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException

class CadastrarTrainerUserUseCase:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService):
        self.user_repository = user_repository
        self.password_service = password_service

    def execute(self, dto: TrainerProfileCreateDTO) -> tuple[User, TrainerProfile]:
        # Verifica se já existe usuário com o email
        email_vo = EmailVO(dto.email)
        if self.user_repository.find_by_email(email_vo):
            raise DomainException("Email já cadastrado")

        # Cria o hash da senha
        senha_hash = self.password_service.get_password_hash(dto.senha)

        # Gera um ID único para o usuário e perfil
        user_id = str(uuid4())

        # Cria o usuário
        user = User(
            id=user_id,
            email=email_vo,
            senha_hash=senha_hash,
            full_name=dto.full_name,
            roles=[UserRole.TRAINER],
            status=UserStatus.PENDING
        )

        # Cria o perfil trainer com o mesmo ID do usuário
        trainer_profile = TrainerProfile(
            id=user_id,
            cref_number=dto.cref_number,
            specialties=dto.specialties,
            certifications=dto.certifications,
            experience_years=dto.experience_years,
            availability=dto.availability,
            preferred_training_types=dto.preferred_training_types,
            bio=dto.bio
        )

        # Salva o usuário e o perfil
        self.user_repository.save(user, trainer_profile)

        return user.to_dict()