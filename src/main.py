from fastapi import FastAPI
from config.settings import settings
from api.routes.user import router as user_router
from api.routes.auth import router as auth_router
# #from api.routes.treino import router as treino_router
from infrastructure.db.base import engine
from infrastructure.db.models import Base

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
    """Verifica se o serviço está ativo"""
    return {"status": "healthy", "database": settings.DATABASE_URL}


print(settings)