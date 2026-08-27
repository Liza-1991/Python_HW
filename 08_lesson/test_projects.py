import pytest
import uuid


# =============================================
# POST /api-v2/projects – позитивные и негативные тесты
# =============================================

class TestCreateProject:
    """Тесты для POST /api-v2/projects"""

    def test_create_project_positive(self, api_client):
        """Позитивный тест: создание проекта с корректными данными."""
        title = f"Мой новый проект {uuid.uuid4()}"  # уникальное название
        response = api_client.create_project(title=title)

        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
        data = response.json()
        assert "id" in data, "В ответе нет id созданного проекта"
        project_id = data["id"]

        # Проверяем, что проект действительно создался – получаем его через GET
        get_response = api_client.get_project(project_id)
        assert get_response.status_code == 200, "Не удалось получить созданный проект"
        project_data = get_response.json()
        assert project_data.get("title") == title, \
            f"Ожидался title '{title}', получен {project_data.get('title')}"

        # Удаление пропускаем, т.к. API не поддерживает DELETE для проектов
        # (если в будущем появится – можно добавить)

    def test_create_project_negative_empty_title(self, api_client):
        """Негативный тест: создание проекта с пустым названием."""
        response = api_client.create_project(title="")

        # Ожидаем ошибку валидации (400 Bad Request)
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        error_data = response.json()
        assert "error" in error_data, "В ответе нет поля error"


# =============================================
# GET /api-v2/projects/{id} – позитивные и негативные тесты
# =============================================

class TestGetProject:
    """Тесты для GET /api-v2/projects/{id}"""

    def test_get_project_positive(self, api_client, created_project_id):
        """Позитивный тест: получение существующего проекта."""
        response = api_client.get_project(created_project_id)

        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        data = response.json()
        assert data.get("id") == created_project_id, "ID проекта не совпадает"
        assert "title" in data, "В ответе нет поля title"

    def test_get_project_negative_not_found(self, api_client):
        """Негативный тест: запрос несуществующего проекта."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.get_project(fake_id)

        # Ожидаем 404 Not Found
        assert response.status_code == 404, f"Ожидался 404, получен {response.status_code}"
        error_data = response.json()
        assert "error" in error_data, "В ответе нет поля error"


# =============================================
# PUT /api-v2/projects/{id} – позитивные и негативные тесты
# =============================================

class TestUpdateProject:
    """Тесты для PUT /api-v2/projects/{id}"""

    def test_update_project_positive(self, api_client, created_project_id):
        """Позитивный тест: обновление названия проекта."""
        new_title = f"Обновлённое название проекта {uuid.uuid4()}"
        response = api_client.update_project(created_project_id, title=new_title)

        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        # Ответ может не содержать title, поэтому проверяем через GET
        get_response = api_client.get_project(created_project_id)
        assert get_response.status_code == 200, "Не удалось получить обновлённый проект"
        project_data = get_response.json()
        assert project_data.get("title") == new_title, \
            f"Ожидался title '{new_title}', получен {project_data.get('title')}"

    def test_update_project_negative_not_found(self, api_client):
        """Негативный тест: обновление несуществующего проекта."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.update_project(fake_id, title="Новое название")

        # Ожидаем 404 Not Found
        assert response.status_code == 404, f"Ожидался 404, получен {response.status_code}"
        error_data = response.json()
        assert "error" in error_data, "В ответе нет поля error"

    def test_update_project_negative_empty_title(self, api_client, created_project_id):
        """Негативный тест: обновление с пустым названием."""
        response = api_client.update_project(created_project_id, title="")

        # Ожидаем ошибку валидации (400 Bad Request)
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        error_data = response.json()
        assert "error" in error_data, "В ответе нет поля error"

