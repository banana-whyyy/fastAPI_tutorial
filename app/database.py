# Подключение к базе данных и создание сессий

# Импорт моделей нужен чтобы модели были зарегистрированы в metadata до create_all
from .models import Book, Author
from .config import settings
from sqlmodel import Session, create_engine, SQLModel


DATABASE_URL = (
    f"postgresql+psycopg2://{settings.db_user}:"
    f"{settings.db_password}@{settings.db_host}:"
    f"{settings.db_port}/{settings.db_name}"
)

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
