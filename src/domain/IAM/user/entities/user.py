from uuid import uuid4
from datetime import datetime, UTC
from enum import Enum
from typing import List
from src.domain.IAM.user.value_objects.email import EmailVO

class UserRole(Enum):
    FITNESS = "FITNESS"
    TRAINER = "TRAINER"
    NUTRITIONIST = "NUTRITIONIST"

class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"

class User:
    def __init__(
        self,
        email: EmailVO,
        senha_hash: str,
        roles: List[UserRole] = None,
        status: UserStatus = UserStatus.PENDING,
        id: str = None,
        criado_em: datetime = None
    ):
        self.id = id or str(uuid4())
        self.email = email
        self.senha_hash = senha_hash
        self.roles = roles or [UserRole.FITNESS]
        self.status = status
        self.criado_em = criado_em or datetime.now(UTC)

    def add_role(self, role: UserRole) -> None:
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role: UserRole) -> None:
        if role in self.roles:
            self.roles.remove(role)

    def has_role(self, role: UserRole) -> bool:
        return role in self.roles

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": str(self.email),
            "roles": [role.value for role in self.roles],
            "status": self.status.value,
            "criado_em": self.criado_em
        }