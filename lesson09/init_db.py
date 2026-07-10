from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "postgresql://postgres:123@localhost:5432/posgres"


def init_database():
    """Инициализация базы данных"""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    init_database()
