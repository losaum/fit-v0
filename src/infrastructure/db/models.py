from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Enum as SQLAlchemyEnum, Float, Date, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
import json

from src.infrastructure.db.base import Base
from src.domain.IAM.user.entities.user import UserRole, UserStatus

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    roles = Column(Text, nullable=False, default=lambda: json.dumps([UserRole.FITNESS.value]))
    status = Column(SQLAlchemyEnum(UserStatus), nullable=False, default=UserStatus.PENDING)
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relacionamentos
    trainer_profile = relationship("TrainerProfileModel", uselist=False, back_populates="user")
    nutritionist_profile = relationship("NutritionistProfileModel", uselist=False, back_populates="user")
    fitness_profile = relationship("FitnessProfileModel", uselist=False, back_populates="user")

class TrainerProfileModel(Base):
    __tablename__ = "trainer_profiles"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    cref_number = Column(String(20), nullable=False, unique=True)
    specialties = Column(Text, nullable=True)
    certifications = Column(Text, nullable=True)
    experience_years = Column(String, nullable=True)
    availability = Column(Text, nullable=True)
    preferred_training_types = Column(Text, nullable=True)
    bio = Column(String, nullable=True)

    # Relacionamento com User
    user = relationship("UserModel", back_populates="trainer_profile")

class NutritionistProfileModel(Base):
    __tablename__ = "nutritionist_profiles"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    crn_number = Column(String(20), nullable=False, unique=True)
    specialties = Column(Text, nullable=True)
    certifications = Column(Text, nullable=True)
    experience_years = Column(String, nullable=True)
    availability = Column(Text, nullable=True)
    dietary_approach = Column(Text, nullable=True)
    bio = Column(String, nullable=True)

    # Relacionamento com User
    user = relationship("UserModel", back_populates="nutritionist_profile")


class FitnessProfileModel(Base):
    __tablename__ = "fitness_profiles"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    height = Column(Float, nullable=False)  # em centímetros
    weight = Column(Float, nullable=False)  # em quilogramas
    fitness_goals = Column(Text, nullable=False, default=lambda: json.dumps([]))
    training_preferences = Column(Text, nullable=False, default=lambda: json.dumps([]))
    health_conditions = Column(Text, nullable=True)
    dietary_restrictions = Column(Text, nullable=True)
    preferred_training_time = Column(String(20), nullable=True)
    training_frequency = Column(Integer, nullable=True)
    experience_level = Column(String(20), nullable=True)

    # Relacionamento com User
    user = relationship("UserModel", back_populates="fitness_profile")


