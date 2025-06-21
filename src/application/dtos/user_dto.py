from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr, field_validator
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.user.entities.user import UserRole, UserStatus


class UserPasswordChangeDTO(BaseModel):
    """DTO para troca de senha do usuário"""
    id: str
    senha_atual: constr(min_length=8)
    nova_senha: constr(min_length=8)


class FitnessProfileDTO(BaseModel):
    full_name: str
    birth_date: date
    height: float
    weight: float
    fitness_goals: List[str]
    training_preferences: List[str]
    health_conditions: Optional[List[str]] = None
    dietary_restrictions: Optional[List[str]] = None
    preferred_training_time: Optional[str] = None
    training_frequency: Optional[int] = None
    experience_level: Optional[str] = None

class TrainerProfileDTO(BaseModel):
    full_name: str
    specialties: List[str]
    certifications: List[str]
    experience_years: str
    availability: Optional[List[str]] = None
    preferred_training_types: Optional[List[str]] = None
    bio: Optional[str] = None

class NutritionistProfileDTO(BaseModel):
    full_name: str
    specialties: List[str]
    certifications: List[str]
    experience_years: str
    availability: Optional[List[str]] = None
    dietary_approach: Optional[List[str]] = None
    bio: Optional[str] = None

class UserCreateDTO(BaseModel):
    email: EmailStr
    senha: constr(min_length=8)
    fitness_profile: Optional[FitnessProfileDTO] = None
    trainer_profile: Optional[TrainerProfileDTO] = None
    nutritionist_profile: Optional[NutritionistProfileDTO] = None


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

    @field_validator('roles', mode='before')
    def parse_roles(cls, v):
        # Se vier lista de UserRole, retorna os valores
        if isinstance(v, list) and all(isinstance(x, UserRole) for x in v):
            return [x.value for x in v]
        return v

    @field_validator('status', mode='before')
    def parse_status(cls, v):
        # Se vier UserStatus, retorna o valor
        if isinstance(v, UserStatus):
            return v.value
        return v

    model_config = {
        "from_attributes": True
    }
