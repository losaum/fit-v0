from dataclasses import dataclass
from uuid import UUID

@dataclass
class TrainerProfile:
    id: UUID
    full_name: str
    cref_number: str