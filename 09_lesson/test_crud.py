import pytest
from database import Student

class TestStudentCRUD:
    """Набор тестов для CRUD-операций над сущностью Student."""

    # ------------------------------------------------------------
    # 1. Тест на ДОБАВЛЕНИЕ (CREATE)
    # ------------------------------------------------------------
    def test_create_student(self, db_session):
        """
        Позитивный тест: создание нового студента.
        Проверяем, что запись появляется в БД.
        """
        # 1. Создаём студента
        new_student = Student(
            name="Иван Петров",
            email="ivan.petrov@example.com"
        )
        db_session.add(new_student)
        db_session.commit()

        # 2. Ищем его в БД по email
        saved_student = db_session.query(Student).filter_by(
            email="ivan.petrov@example.com"
        ).first()

        # 3. Проверяем, что он есть и данные корректны
        assert saved_student is not None, "Студент не найден в БД"
        assert saved_student.name == "Иван Петров", "Имя не совпадает"

        # 4. Очистка: удаляем созданного студента
        db_session.delete(saved_student)
        db_session.commit()

    # ------------------------------------------------------------
    # 2. Тест на ИЗМЕНЕНИЕ (UPDATE)
    # ------------------------------------------------------------
    def test_update_student(self, db_session, test_student):
        """
        Позитивный тест: обновление имени студента.
        Использует фикстуру test_student, которая создаёт запись
        и удаляет её после теста.
        """
        # 1. Меняем имя
        test_student.name = "Анна Сидорова"
        db_session.commit()

        # 2. Проверяем, что имя обновилось в БД
        updated_student = db_session.query(Student).filter_by(
            id=test_student.id
        ).first()
        assert updated_student is not None, "Студент пропал после обновления"
        assert updated_student.name == "Анна Сидорова", "Имя не обновилось"

        # 3. Очистка происходит автоматически в фикстуре test_student

    # ------------------------------------------------------------
    # 3. Тест на УДАЛЕНИЕ (DELETE)
    # ------------------------------------------------------------
    def test_delete_student(self, db_session):
        """
        Позитивный тест: удаление студента.
        Создаём студента → удаляем → проверяем отсутствие в БД.
        """
        # 1. Создаём студента специально для этого теста
        student = Student(
            name="Временный Студент",
            email="temp_student@example.com"
        )
        db_session.add(student)
        db_session.commit()
        student_id = student.id

        # 2. Удаляем его
        db_session.delete(student)
        db_session.commit()

        # 3. Проверяем, что он исчез из БД
        deleted_student = db_session.query(Student).filter_by(
            id=student_id
        ).first()
        assert deleted_student is None, "Студент не был удалён"
