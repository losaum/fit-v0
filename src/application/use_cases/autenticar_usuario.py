from datetime import timedelta, datetime
from jose import jwt
from src.application.dtos.auth_dto import AuthLoginDTO, AuthTokenDTO
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.user.repositories.user_repository import UserRepository
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException
from src.domain.IAM.shared.services.password_service import PasswordService
from src.config.settings import settings

class AutenticarUsuarioUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.password_service = PasswordService()

    def execute(self, dto: AuthLoginDTO) -> AuthTokenDTO:
        email_vo = EmailVO(dto.login)
        user = self.repo.exists_by_email(email_vo)
        if not user or not self.password_service.verify_password(dto.senha, user.senha_hash):
            raise DomainException("Credenciais inválidas.")

        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {"sub": user.id, "exp": expire}
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
        return AuthTokenDTO(access_token=token)