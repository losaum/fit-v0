from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic
from src.domain.IAM.user.entities.user import User
from src.domain.IAM.user.value_objects.email import EmailVO

ProfileT = TypeVar('ProfileT')


class UserRepository(ABC, Generic[ProfileT]):
    @abstractmethod
    def save(self, user: User, profile: Optional[ProfileT] = None) -> User:
        pass

    @abstractmethod
    def find_by_email(self, email: EmailVO) -> Optional[User]:
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
