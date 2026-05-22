from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://admin:adminpassword@db:5432/fastapi_db"

settings = Settings()