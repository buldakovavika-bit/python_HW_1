import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course

# Строка подключения к БД
DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"


@pytest.fixture(scope="session")
def engine():
    """Создание движка SQLAlchemy"""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # Создаем таблицы, если их нет
    yield engine
    # Очистка после всех тестов (опционально)
    # Base.metadata.drop_all(engine)


@pytest.fixture
def session(engine):
    """Создание сессии для работы с БД"""
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()  # Откат транзакции после каждого теста
    session.close()


@pytest.fixture
def test_course_data():
    """Тестовые данные для курса"""
    return {
        "name": "Python Basics",
        "description": "Learn Python programming from scratch"
    }


@pytest.fixture
def cleanup_course(session):
    """Фикстура для очистки тестовых курсов после тестов"""
    def _cleanup(name):
        session.query(Course).filter(Course.name == name).delete()
        session.commit()
    return _cleanup
