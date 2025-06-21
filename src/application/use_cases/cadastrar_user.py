from src.application.dtos.user_dto import UserCreateDTO, UserReadDTO
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.user.repositories.user_repository import UserRepository
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException
from src.domain.IAM.shared.services.password_service import PasswordService


class CadastrarUsuarioUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.password_service = PasswordService()

    def execute(self, dto: UserCreateDTO) -> UserReadDTO:
        email_vo = EmailVO(dto.login)
        if self.repo.exists_by_email(email_vo):
            raise DomainException("E-mail já cadastrado.")
        senha_hash = self.password_service.get_password_hash(dto.senha)
        user = User(
            email=email_vo,
            senha_hash=senha_hash,
            roles=[UserRole.STUDENT],
            status=UserStatus.PENDING
        )
        self.repo.save(user)
        return UserReadDTO.model_validate(user)