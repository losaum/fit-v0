from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from src.infrastructure.db.base import Base
from src.domain.IAM.user.entities.user import UserRole, UserStatus

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    roles = Column(JSON, nullable=False, default=lambda: [UserRole.STUDENT.value])
    status = Column(SQLAlchemyEnum(UserStatus), nullable=False, default=UserStatus.PENDING)
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relacionamentos
    trainer_profile = relationship("TrainerProfileModel", uselist=False, back_populates="user")
    nutritionist_profile = relationship("NutritionistProfileModel", uselist=False, back_populates="user")

class TrainerProfileModel(Base):
    __tablename__ = "trainer_profiles"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    cref_number = Column(String(20), nullable=False, unique=True)

    # Relacionamento com User
    user = relationship("UserModel", back_populates="trainer_profile")

class NutritionistProfileModel(Base):
    __tablename__ = "nutritionist_profiles"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    crn_number = Column(String(20), nullable=False, unique=True)
    specializations = Column(JSON, nullable=False, default=list)

    # Relacionamento com User
    user = relationship("UserModel", back_populates="nutritionist_profile")


