from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr

class TrainerProfileCreateDTO(BaseModel):
    email: EmailStr
    senha: constr(min_length=8)
    full_name: str
    cref_number: str
    specialties: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
    experience_years: Optional[str] = None
    availability: Optional[List[str]] = None
    preferred_training_types: Optional[List[str]] = None
    bio: Optional[str] = None

class TrainerProfileReadDTO(BaseModel):
    id: str
    full_name: str
    cref_number: str
    specialties: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
    experience_years: Optional[str] = None
    availability: Optional[List[str]] = None
    preferred_training_types: Optional[List[str]] = None
    bio: Optional[str] = None
    criado_em: datetime