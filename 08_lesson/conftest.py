import pytest
from api_client import YougileAPIClient
from config import YOUGILE_TOKEN


@pytest.fixture(scope="session")
def api_client():
    """Фикстура, предоставляющая клиент API."""
    return YougileAPIClient(YOUGILE_TOKEN)


@pytest.fixture
def created_project_id(api_client):
    """
    Фикстура создаёт проект перед тестом и удаляет его после.
    Используется для тестов, которым нужен существующий проект.
    """
    # Создаём проект
    response = api_client.create_project(
        title="Тестовый проект для автотестов",
        users={}  # пустой словарь означает, что пользователи не назначаются
    )
    assert response.status_code == 201, "Не удалось создать проект для фикстуры"
    project_id = response.json()["id"]

    yield project_id

    # Удаляем проект после теста (очистка)
    delete_resp = api_client.delete_project(project_id)
    # Не проверяем статус, чтобы не упасть, если проект уже удалён

