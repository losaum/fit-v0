from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.user import User
from domain.value_objects.email import EmailVO


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def exists_by_email(self, email: EmailVO) -> Optional[User]:
        pass
