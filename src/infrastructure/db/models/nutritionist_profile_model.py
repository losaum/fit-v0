from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class NutritionistProfileModel(Base):
    __tablename__ = 'nutritionist_profiles'

    id = Column(String, ForeignKey('users.id'), primary_key=True)
    full_name = Column(String, nullable=False)
    crn_number = Column(String, nullable=False)
    specialties = Column(Text, nullable=True)
    certifications = Column(Text, nullable=True)
    experience_years = Column(String, nullable=True)
    availability = Column(Text, nullable=True)
    dietary_approach = Column(Text, nullable=True)
    bio = Column(String, nullable=True)

    # Relacionamento
    user = relationship('UserModel', back_populates='nutritionist_profile')