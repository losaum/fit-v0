from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, constr, field_validator
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.user.entities.user import UserRole, UserStatus


class UserPasswordChangeDTO(BaseModel):
    """DTO para troca de senha do usuário"""
    id: str
    senha_atual: constr(min_length=8)
    nova_senha: constr(min_length=8)


class UserCreateDTO(BaseModel):
    login: EmailStr
    senha: constr(min_length=8)


class UserReadDTO(BaseModel):
    id: str
    email: EmailStr
    roles: List[UserRole]
    status: UserStatus
    criado_em: datetime

    @field_validator('email', mode='before')
    def parse_emailvo(cls, v):
        # Se vier EmailVO, converte para string
        if isinstance(v, EmailVO):
            return v.value
        return v

    model_config = {
        "from_attributes": True
    }
