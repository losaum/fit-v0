from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Fitness Backend"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./db.sqlite3"
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }

settings = Settings()