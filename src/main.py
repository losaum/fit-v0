import logging
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.api.routes.users import router as users_router
from src.api.routes.auth import router as auth_router
from src.api.routes.profiles import router as profiles_router
# from api.routes.treino import router as treino_router
from src.infrastructure.db.database import engine, config

# Configuração do logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_details = []
    for error in exc.errors():
        error_details.append({
            'loc': error['loc'],
            'msg': error['msg'],
            'type': error['type']
        })
    logging.error(f"Validation error: {error_details}")
    return JSONResponse(
        status_code=422,
        content={
            "detail": error_details
        }
    )

# Inclui roteadores das diferentes áreas
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(profiles_router)
#app.include_router(treino_router)

@app.get("/health", tags=["Health"])
async def health_check():
    """Verifica se o serviço está ativo e retorna métricas básicas"""
    from sqlalchemy import text
    from datetime import datetime, UTC
    
    try:
        # Verifica conexão com banco de dados
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return {
        "status": "healthy",
        "timestamp": datetime.now(UTC).isoformat(),
        "database": {
            "url": config.DATABASE_URL,
            "status": db_status
        },
        "version": config.PROJECT_VERSION
    }


# Configurações do projeto
print(f"Iniciando {config.PROJECT_NAME} v{config.PROJECT_VERSION}")