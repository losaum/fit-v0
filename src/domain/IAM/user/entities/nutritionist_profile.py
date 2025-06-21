from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass
class NutritionistProfile:
    id: UUID
    crn_number: str
    specialties: List[str] | None = None
    certifications: List[str] | None = None
    experience_years: str | None = None
    availability: List[str] | None = None
    dietary_approach: List[str] | None = None
    bio: str | None = None