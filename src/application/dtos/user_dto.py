from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class UserCreateDTO(BaseModel):
    nome: constr(min_length=3)
    login: EmailStr
    senha: constr(min_length=8)


class UserReadDTO(BaseModel):
    id: str
    nome: str
    email: EmailStr
    criado_em: datetime

    model_config = {
        "from_attributes": True
    }
