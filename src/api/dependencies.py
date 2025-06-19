from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from src.infrastructure.db.base import SessionLocal
from src.infrastructure.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from src.domain.repositories.user_repository import UserRepository


def get_db() -> Generator[Session, None, None]:
    """
    Dependência para obter uma sessão do banco de dados.
    Garante que a sessão seja fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    """
    Dependência para obter uma instância de repositório de usuário.
    Usa a sessão do DB para criar o SQLAlchemyUsuarioRepository.
    """
    return SQLAlchemyUserRepository(db)
