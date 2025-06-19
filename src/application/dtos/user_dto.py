from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, field_validator
from src.domain.value_objects.email import EmailVO


class UserPasswordChangeDTO(BaseModel):
    """DTO para troca de senha do usuário"""
    id: str
    senha_atual: constr(min_length=8)
    nova_senha: constr(min_length=8)


class UserCreateDTO(BaseModel):
    nome: constr(min_length=3)
    login: EmailStr
    senha: constr(min_length=8)


class UserReadDTO(BaseModel):
    id: str
    nome: str
    email: EmailStr
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
