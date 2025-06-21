from pydantic_settings import BaseSettings

class TestSettings(BaseSettings):
    PROJECT_NAME: str = "Fitness Backend Test"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///:memory:"
    JWT_SECRET: str = "test_secret"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = {
        "env_file": ".env.test",
        "env_file_encoding": "utf-8"
    }

test_settings = TestSettings()