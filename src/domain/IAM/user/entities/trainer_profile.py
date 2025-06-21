from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class TrainerProfile:
    id: UUID
    cref_number: str
    specialties: Optional[list[str]] = None
    certifications: Optional[list[str]] = None
    experience_years: Optional[str] = None
    availability: Optional[list[str]] = None
    preferred_training_types: Optional[list[str]] = None
    bio: Optional[str] = None