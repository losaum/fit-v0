from pydantic import BaseModel, EmailStr, constr

class AuthLoginDTO(BaseModel):
    login: EmailStr
    senha: constr(min_length=8)

class AuthTokenDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"