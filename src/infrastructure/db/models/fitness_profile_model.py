from datetime import date
from sqlalchemy import Column, String, Float, Integer, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class FitnessProfileModel(Base):
    __tablename__ = 'fitness_profiles'

    id = Column(String, ForeignKey('users.id'), primary_key=True)
    birth_date = Column(Date, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    fitness_goals = Column(Text, nullable=False)
    training_preferences = Column(Text, nullable=False)
    health_conditions = Column(Text, nullable=True)
    dietary_restrictions = Column(Text, nullable=True)
    preferred_training_time = Column(String, nullable=True)
    training_frequency = Column(Integer, nullable=True)
    experience_level = Column(String, nullable=True)

    # Relacionamento
    user = relationship('UserModel', back_populates='fitness_profile')