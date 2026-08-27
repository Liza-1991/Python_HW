import pytest
from database import SessionLocal, Student

@pytest.fixture(scope="function")
def db_session():
    """Фикстура: создаёт сессию БД и закрывает её после теста."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture(scope="function")
def test_student(db_session):
    """
    Фикстура: создаёт тестового студента перед тестом,
    а после теста удаляет его (очистка данных).
    """
    student = Student(
        name="Тестовый Студент",
        email="test_student@example.com"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    yield student  # передаём объект в тест

    # ---- Удаляем после теста ----
    db_session.delete(student)
    db_session.commit()

