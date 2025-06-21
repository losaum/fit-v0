from uuid import uuid4
from datetime import datetime
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.nutritionist_profile import NutritionistProfile
from src.domain.IAM.user.value_objects.email import EmailVO
from src.application.dtos.nutritionist_profile_dto import NutritionistProfileCreateDTO
from src.domain.IAM.shared.services.password_service import PasswordService
from src.domain.IAM.user.repositories.user_repository import UserRepository

class CadastrarNutritionistUserUseCase:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService):
        self.user_repository = user_repository
        self.password_service = password_service

    def execute(self, dto: NutritionistProfileCreateDTO) -> tuple[User, NutritionistProfile]:
        # Verifica se já existe usuário com o email
        email_vo = EmailVO(dto.email)
        if self.user_repository.find_by_email(email_vo):
            raise ValueError("Email já cadastrado")

        # Cria o hash da senha
        senha_hash = self.password_service.get_password_hash(dto.senha)

        # Cria o usuário com ID
        user_id = str(uuid4())
        user = User(
            id=user_id,
            email=email_vo,
            senha_hash=senha_hash,
            full_name=dto.full_name,
            roles=[UserRole.NUTRITIONIST],
            status=UserStatus.PENDING
        )

        # Cria o perfil nutritionist
        nutritionist_profile = NutritionistProfile(
            id=user_id,
            crn_number=dto.crn_number,
            specialties=dto.specialties,
            certifications=dto.certifications,
            experience_years=dto.experience_years,
            availability=dto.availability,
            dietary_approach=dto.dietary_approach,
            bio=dto.bio
        )

        # Salva o usuário e o perfil
        self.user_repository.save(user, nutritionist_profile)

        return user.to_dict()