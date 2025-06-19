from fastapi import FastAPI
from src.config.settings import settings
from src.api.routes.user import router as user_router
from src.api.routes.auth import router as auth_router
# #from api.routes.treino import router as treino_router
from src.infrastructure.db.base import engine
from src.infrastructure.db.models import Base

# Cria tabelas no banco se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Inclui roteadores das diferentes áreas
app.include_router(user_router)
app.include_router(auth_router)
#app.include_router(treino_router)

@app.get("/health", tags=["Health"])
async def health_check():
    """Verifica se o serviço está ativo e retorna métricas básicas"""
    from sqlalchemy import text
    from datetime import datetime
    
    try:
        # Verifica conexão com banco de dados
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "database": {
            "url": settings.DATABASE_URL,
            "status": db_status
        },
        "version": settings.PROJECT_VERSION
    }


# Configurações do projeto
print(f"Iniciando {settings.PROJECT_NAME} v{settings.PROJECT_VERSION}")