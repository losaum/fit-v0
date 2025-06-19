from datetime import timedelta, datetime
from jose import jwt
from passlib.hash import bcrypt
from application.dtos.auth_dto import AuthLoginDTO, AuthTokenDTO
from domain.value_objects.email import EmailVO
from domain.repositories.user_repository import UserRepository
from domain.exceptions import DomainException
from config.settings import settings

class AutenticarUsuarioUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, dto: AuthLoginDTO) -> AuthTokenDTO:
        email_vo = EmailVO(dto.login)
        user = self.repo.exists_by_email(email_vo)
        if not user or not bcrypt.verify(dto.senha, user.senha_hash):
            raise DomainException("Credenciais inválidas.")

        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {"sub": user.id, "exp": expire}
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
        return AuthTokenDTO(access_token=token)