from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class TrainerProfileModel(Base):
    __tablename__ = 'trainer_profiles'

    id = Column(String, ForeignKey('users.id'), primary_key=True)
    cref_number = Column(String(20), nullable=False, unique=True)
    specialties = Column(Text, nullable=True)
    certifications = Column(Text, nullable=True)
    experience_years = Column(String, nullable=True)
    availability = Column(Text, nullable=True)
    preferred_training_types = Column(Text, nullable=True)
    bio = Column(String, nullable=True)

    # Relacionamento
    user = relationship('UserModel', back_populates='trainer_profile')