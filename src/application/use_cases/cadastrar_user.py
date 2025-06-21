from src.application.dtos.user_dto import UserCreateDTO, UserReadDTO
from src.domain.IAM.entities.user import User
from src.domain.IAM.value_objects.email import EmailVO
from src.domain.IAM.repositories.user_repository import UserRepository
from src.domain.IAM.exceptions import DomainException
from src.domain.IAM.services.password_service import PasswordService


class CadastrarUsuarioUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.password_service = PasswordService()

    def execute(self, dto: UserCreateDTO) -> UserReadDTO:
        email_vo = EmailVO(dto.login)
        if self.repo.exists_by_email(email_vo):
            raise DomainException("E-mail já cadastrado.")
        senha_hash = self.password_service.get_password_hash(dto.senha)
        user = User(nome=dto.nome, email=email_vo, senha_hash=senha_hash)
        self.repo.save(user)
        return UserReadDTO.model_validate(user)