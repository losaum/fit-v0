from dataclasses import dataclass
from uuid import UUID
from typing import List, Optional
from datetime import date

@dataclass
class FitnessProfile:
    id: UUID
    birth_date: date
    height: float  # em centímetros
    weight: float  # em quilogramas
    fitness_goals: List[str]
    training_preferences: List[str]
    health_conditions: Optional[List[str]] = None
    dietary_restrictions: Optional[List[str]] = None
    preferred_training_time: Optional[str] = None  # manhã, tarde, noite
    training_frequency: Optional[int] = None  # dias por semana
    experience_level: Optional[str] = None  # iniciante, intermediário, avançado