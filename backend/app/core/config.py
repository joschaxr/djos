from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "DJOS API"
    VERSION: str = "0.1.0"

    class Config:
        env_file = ".env"


settings = Settings()
