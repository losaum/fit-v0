from typing import TypeVar, Union, Optional
from sqlalchemy.orm import Session
import json
from src.domain.IAM.user.entities.user import User, UserRole, UserStatus
from src.domain.IAM.user.entities.fitness_profile import FitnessProfile
from src.domain.IAM.user.entities.trainer_profile import TrainerProfile
from src.domain.IAM.user.entities.nutritionist_profile import NutritionistProfile
from src.domain.IAM.user.value_objects.email import EmailVO
from src.domain.IAM.user.repositories.user_repository import UserRepository
from src.infrastructure.db.models import UserModel, FitnessProfileModel, TrainerProfileModel, NutritionistProfileModel

ProfileT = TypeVar('ProfileT', FitnessProfile, TrainerProfile, NutritionistProfile)
ProfileModelT = TypeVar('ProfileModelT', FitnessProfileModel, TrainerProfileModel, NutritionistProfileModel)


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def find_by_email(self, email: EmailVO) -> User | None:
        row = (
            self.session.query(UserModel)
            .filter(UserModel.email == email.value)
            .first()
        )
        if not row:
            return None

        return User(
            id=row.id,
            email=EmailVO(row.email),
            senha_hash=row.senha_hash,
            roles=[UserRole(role) for role in json.loads(row.roles)],
            status=row.status,
            criado_em=row.criado_em,
        )

    def save(self, user: User, profile: Optional[ProfileT] = None) -> User:
        model = UserModel(
            id=user.id,
            email=user.email.value,
            senha_hash=user.senha_hash,
            roles=json.dumps([role.value for role in user.roles]),
            status=user.status,
            criado_em=user.criado_em,
        )
        self.session.merge(model)

        if profile:
            if isinstance(profile, FitnessProfile):
                db_profile = FitnessProfileModel(
                    id=str(profile.id),
                    full_name=profile.full_name,
                    birth_date=profile.birth_date,
                    height=profile.height,
                    weight=profile.weight,
                    fitness_goals=json.dumps(profile.fitness_goals if profile.fitness_goals is not None else []),
                    training_preferences=json.dumps(profile.training_preferences if profile.training_preferences is not None else []),
                    health_conditions=json.dumps(profile.health_conditions if profile.health_conditions is not None else []),
                    dietary_restrictions=json.dumps(profile.dietary_restrictions if profile.dietary_restrictions is not None else []),
                    preferred_training_time=profile.preferred_training_time,
                    training_frequency=profile.training_frequency,
                    experience_level=profile.experience_level
                )
                self.session.add(db_profile)
            elif isinstance(profile, TrainerProfile):
                # Verifica se já existe um perfil de treinador para este usuário
                existing_profile = self.session.query(TrainerProfileModel).filter_by(id=str(profile.id)).first()
                if not existing_profile:
                    db_profile = TrainerProfileModel(
                        id=str(profile.id),
                        full_name=profile.full_name,
                        cref_number=profile.cref_number,
                        specialties=json.dumps(profile.specialties if profile.specialties is not None else []),
                        certifications=json.dumps(profile.certifications if profile.certifications is not None else []),
                        experience_years=profile.experience_years if profile.experience_years is not None else "0",
                        availability=json.dumps(profile.availability if profile.availability is not None else []),
                        preferred_training_types=json.dumps(profile.preferred_training_types if profile.preferred_training_types is not None else []),
                        bio=profile.bio
                    )
                    self.session.add(db_profile)
            elif isinstance(profile, NutritionistProfile):
                # Verifica se já existe um perfil de nutricionista para este usuário
                existing_profile = self.session.query(NutritionistProfileModel).filter_by(id=str(profile.id)).first()
                if not existing_profile:
                    db_profile = NutritionistProfileModel(
                        id=str(profile.id),
                        full_name=profile.full_name,
                        crn_number=profile.crn_number,
                        specialties=json.dumps(profile.specialties if profile.specialties is not None else []),
                        certifications=json.dumps(profile.certifications if profile.certifications is not None else []),
                        experience_years=profile.experience_years if profile.experience_years is not None else "0",
                        availability=json.dumps(profile.availability if profile.availability is not None else []),
                        dietary_approach=json.dumps(profile.dietary_approach if profile.dietary_approach is not None else []),
                        bio=profile.bio
                    )
                    self.session.add(db_profile)

        self.session.commit()
        return user

    def get_by_id(self, id: str) -> User | None:
        """Busca um usuário pelo ID

        Args:
            id (str): ID do usuário

        Returns:
            User | None: Usuário encontrado ou None se não existir
        """
        row = (
            self.session.query(UserModel)
            .filter(UserModel.id == id)
            .first()
        )
        if not row:
            return None

        return User(
            id=row.id,
            email=EmailVO(row.email),
            senha_hash=row.senha_hash,
            roles=[UserRole(role) for role in json.loads(row.roles)],
            status=row.status,
            criado_em=row.criado_em,
        )
