from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import event, inspect

# Define a classe base para os modelos
Base = declarative_base()

# Função para criar uma sessão com o engine fornecido
def get_session_maker(engine):
    # Configura o SQLite para suportar JSON
    @event.listens_for(engine, 'connect')
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON')
        cursor.close()

    # Verifica se o engine está conectado e as tabelas existem
    inspector = inspect(engine)
    try:
        # Tenta criar todas as tabelas se não existirem
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
        raise e

    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )