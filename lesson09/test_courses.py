from models import Course


class TestCourseOperations:
    """Тесты для операций с курсами"""

    def test_add_course(self, session, test_course_data, cleanup_course):
        """Тест добавления курса"""
        # Проверяем, что курс с таким именем существует
        existing = session.query(Course).filter(
            Course.name == test_course_data["name"]
        ).first()

        if existing:
            session.delete(existing)
            session.commit()

        # Создаем новый курс
        course = Course(**test_course_data)
        session.add(course)
        session.commit()

        # Проверяем, что курс добавлен
        saved_course = session.query(Course).filter(
            Course.name == test_course_data["name"]
        ).first()

        assert saved_course is not None
        assert saved_course.name == test_course_data["name"]
        assert saved_course.description == test_course_data["description"]
        assert saved_course.id is not None

        # Очистка
        cleanup_course(test_course_data["name"])

    def test_update_course(self, session, test_course_data, cleanup_course):
        """Тест изменения данных курса"""
        # Создаем курс
        course = Course(**test_course_data)
        session.add(course)
        session.commit()

        # Обновляем данные
        new_description = "Advanced Python programming"
        course.description = new_description
        session.commit()

        # Проверяем, что данные изменились
        updated_course = session.query(Course).filter(
            Course.name == test_course_data["name"]
        ).first()

        assert updated_course is not None
        assert updated_course.description == new_description

        # Очистка
        cleanup_course(test_course_data["name"])

    def test_delete_course(self, session, test_course_data, cleanup_course):
        """Тест удаления курса"""
        # Создаем курс
        course = Course(**test_course_data)
        session.add(course)
        session.commit()

        # Проверяем, что курс создан
        created = session.query(Course).filter(
            Course.name == test_course_data["name"]
        ).first()
        assert created is not None

        # Удаляем курс
        session.delete(created)
        session.commit()

        # Проверяем, что курс удален
        deleted = session.query(Course).filter(
            Course.name == test_course_data["name"]
        ).first()

        assert deleted is None

        # Очистка
        cleanup_course(test_course_data["name"])
