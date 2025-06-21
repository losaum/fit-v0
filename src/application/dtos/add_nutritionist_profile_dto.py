from typing import List, Optional
from pydantic import BaseModel

class AddNutritionistProfileDTO(BaseModel):
    full_name: str
    crn_number: str
    specialties: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
    experience_years: Optional[str] = None
    availability: Optional[List[str]] = None
    dietary_approach: Optional[List[str]] = None
    bio: Optional[str] = None