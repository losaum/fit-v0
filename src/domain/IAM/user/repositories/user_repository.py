from abc import ABC, abstractmethod
from typing import Optional
from src.domain.IAM.user.entities.user import User
from src.domain.IAM.user.value_objects.email import EmailVO


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def exists_by_email(self, email: EmailVO) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[User]:
        """Busca um usuário pelo ID

        Args:
            id (str): ID do usuário

        Returns:
            Optional[User]: Usuário encontrado ou None se não existir
        """
        pass
