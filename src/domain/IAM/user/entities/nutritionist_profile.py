from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass
class NutritionistProfile:
    id: UUID
    full_name: str
    crn_number: str
    specializations: List[str]