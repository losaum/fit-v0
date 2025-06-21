import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.db.base import Base
from src.config.test_settings import test_settings
from src.main import app

# Importa todos os modelos para garantir que eles sejam registrados com o Base.metadata
from src.infrastructure.db.models.user_model import UserModel
from src.infrastructure.db.models.fitness_profile_model import FitnessProfileModel
from src.infrastructure.db.models.trainer_profile_model import TrainerProfileModel
from src.infrastructure.db.models.nutritionist_profile_model import NutritionistProfileModel

# Define o ambiente como teste
os.environ['TESTING'] = 'True'

@pytest.fixture(scope="function")
def engine():
    # Usando configuração de teste com SQLite em memória
    engine = create_engine(
        test_settings.DATABASE_URL,
        connect_args={"check_same_thread": False},
        json_serializer=lambda obj: str(obj),
        json_deserializer=lambda obj: str(obj)
    )
    
    # Configura o SQLite para suportar chaves estrangeiras
    from sqlalchemy import event
    @event.listens_for(engine, 'connect')
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON')
        cursor.close()
    
    # Garante que todas as tabelas sejam criadas
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
        raise
    
    return engine

@pytest.fixture(scope="function")
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    # Sobrescreve a dependência get_db durante os testes
    def override_get_db():
        try:
            yield session
        finally:
            pass

    from src.api.dependencies import get_db
    app.dependency_overrides[get_db] = override_get_db
    
    yield session
    
    app.dependency_overrides.clear()
    session.close()
    transaction.rollback()
    connection.close()

# Remoção do cleanup_database pois agora o banco é recriado para cada teste