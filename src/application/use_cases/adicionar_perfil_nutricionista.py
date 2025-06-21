from uuid import UUID
from src.domain.IAM.user.entities.user import User, UserRole
from src.domain.IAM.user.entities.nutritionist_profile import NutritionistProfile
from src.domain.IAM.user.repositories.user_repository import UserRepository
from src.application.dtos.add_nutritionist_profile_dto import AddNutritionistProfileDTO
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException

class AdicionarPerfilNutricionistaUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: UUID, dto: AddNutritionistProfileDTO) -> User:
        # Busca o usuário pelo ID
        user = self.user_repository.get_by_id(str(user_id))
        if not user:
            raise DomainException("Usuário não encontrado")

        # Verifica se o usuário já tem o papel de nutricionista
        if user.has_role(UserRole.NUTRITIONIST):
            raise DomainException("Usuário já possui perfil de nutricionista")

        # Cria o perfil de nutricionista
        nutritionist_profile = NutritionistProfile(
            id=user.id,
            full_name=dto.full_name,
            crn_number=dto.crn_number,
            specialties=dto.specialties,
            certifications=dto.certifications,
            experience_years=dto.experience_years,
            availability=dto.availability,
            dietary_approach=dto.dietary_approach,
            bio=dto.bio
        )

        # Adiciona o papel de nutricionista ao usuário
        user.add_role(UserRole.NUTRITIONIST)

        # Salva as alterações
        self.user_repository.save(user, nutritionist_profile)

        return user