from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr

class FitnessProfileCreateDTO(BaseModel):
    email: EmailStr
    senha: constr(min_length=8)
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

class FitnessProfileReadDTO(BaseModel):
    id: str
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
    criado_em: datetime