# Настройки приложения, чтобы хранить все в переменных окружения
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_name: str = Field(alias="DB_NAME")
    db_user: str = Field(alias="DB_USER")
    db_password: str = Field(alias="DB_PASSWORD")
    db_port: int = Field(default=5432, alias="DB_PORT")
    db_host: str = Field(default="localhost", alias="DB_HOST")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()