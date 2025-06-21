from datetime import datetime, UTC
from sqlalchemy import Column, String, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from src.domain.IAM.user.entities.user import UserRole, UserStatus
from src.infrastructure.db.base import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    roles = Column(Text, nullable=False)
    status = Column(Enum(UserStatus), nullable=False)
    criado_em = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))

    # Relacionamentos
    fitness_profile = relationship('FitnessProfileModel', uselist=False, back_populates='user')
    trainer_profile = relationship('TrainerProfileModel', uselist=False, back_populates='user')
    nutritionist_profile = relationship('NutritionistProfileModel', uselist=False, back_populates='user')