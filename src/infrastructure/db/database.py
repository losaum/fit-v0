import os
from sqlalchemy import create_engine
from src.config.settings import settings
from src.config.test_settings import test_settings
from src.infrastructure.db.base import get_session_maker, Base

# Importa todos os modelos para garantir que eles sejam registrados com o Base.metadata
from src.infrastructure.db.models import (
    UserModel,
    FitnessProfileModel,
    TrainerProfileModel,
    NutritionistProfileModel
)

# Seleciona as configurações baseado no ambiente
config = test_settings if os.getenv('TESTING') else settings

# Cria engine com as configurações apropriadas
engine = create_engine(
    config.DATABASE_URL,
    connect_args={"check_same_thread": False},
    json_serializer=lambda obj: str(obj),
    json_deserializer=lambda obj: str(obj)
)

# Cria o SessionLocal usando o engine configurado
SessionLocal = get_session_maker(engine)

# As tabelas são criadas automaticamente ao criar o SessionLocal em base.py