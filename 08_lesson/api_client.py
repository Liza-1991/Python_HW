import requests


class YougileAPIClient:
    """Клиент для работы с API Yougile (Page Object для API)."""

    BASE_URL = "https://yougile.com/api-v2"

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def create_project(self, title: str, users: dict = None) -> dict:
        """
        POST /api-v2/projects
        Создаёт новый проект.
        """
        payload = {"title": title}
        if users:
            payload["users"] = users

        response = requests.post(
            f"{self.BASE_URL}/projects",
            headers=self.headers,
            json=payload
        )
        return response

    def get_project(self, project_id: str) -> dict:
        """
        GET /api-v2/projects/{id}
        Возвращает информацию о проекте.
        """
        response = requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )
        return response

    def update_project(self, project_id: str, title: str = None, users: dict = None) -> dict:
        """
        PUT /api-v2/projects/{id}
        Обновляет проект.
        """
        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users

        response = requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
            json=payload
        )
        return response

    def delete_project(self, project_id: str) -> dict:
        """
        DELETE /api-v2/projects/{id} – используется для очистки после тестов.
        (В документации этот метод может отсутствовать, но в реальном API он есть.)
        """
        response = requests.delete(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )
        return response

