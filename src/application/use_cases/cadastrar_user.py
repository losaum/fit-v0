from application.dtos.user_dto import UserCreateDTO, UserReadDTO
from domain.entities.user import User
from domain.value_objects.email import EmailVO
from domain.repositories.user_repository import UserRepository
from domain.exceptions import DomainException
from passlib.hash import bcrypt

class CadastrarUsuarioUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, dto: UserCreateDTO) -> UserReadDTO:
        email_vo = EmailVO(dto.login)
        if self.repo.exists_by_email(email_vo.value):
            raise DomainException("E-mail já cadastrado.")
        senha_hash = bcrypt.hash(dto.senha)
        user = User(nome=dto.nome, email=email_vo, senha_hash=senha_hash)
        self.repo.save(user)
        return UserReadDTO.from_orm(user)