from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from src.infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from src.domain.IAM.user.repositories.user_repository import UserRepository
from src.domain.IAM.shared.services.password_service import PasswordService
from src.infrastructure.db.database import SessionLocal
from src.infrastructure.db.base import Base

# Importa todos os modelos para garantir que eles sejam registrados com o Base.metadata
from src.infrastructure.db.models import (
    UserModel,
    FitnessProfileModel,
    TrainerProfileModel,
    NutritionistProfileModel
)


def get_db() -> Generator[Session, None, None]:
    """
    Dependência para obter uma sessão do banco de dados.
    Garante que a sessão seja fechada após o uso.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    """
    Dependência para obter uma instância de repositório de usuário.
    Usa a sessão do DB para criar o SQLAlchemyUsuarioRepository.
    """
    return SQLAlchemyUserRepository(db)


def get_password_service() -> PasswordService:
    """
    Dependência para obter uma instância do serviço de senha.
    """
    return PasswordService()
