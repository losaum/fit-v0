from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr

class NutritionistProfileCreateDTO(BaseModel):
    email: EmailStr
    senha: constr(min_length=8)
    full_name: str
    crn_number: str
    specialties: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
    experience_years: Optional[str] = None
    availability: Optional[List[str]] = None
    dietary_approach: Optional[List[str]] = None
    bio: Optional[str] = None

class NutritionistProfileReadDTO(BaseModel):
    id: str
    crn_number: str
    specialties: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
    experience_years: Optional[str] = None
    availability: Optional[List[str]] = None
    dietary_approach: Optional[List[str]] = None
    bio: Optional[str] = None
    criado_em: datetime