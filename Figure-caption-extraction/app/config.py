from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    api_key: str
    ncbi_api_key: str
    max_file_size: int = 5 * 1024 * 1024  # 5MB

    class Config:
        env_file = ".env"


settings = Settings()