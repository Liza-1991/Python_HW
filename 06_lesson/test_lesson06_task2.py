from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    try:

        # Куки пользователя 1 (Session_id + SESSION)
        cookies_user1 = {
                "name": "SESSION",
                "value": "Y2Y4OWFlZGUtNGQ4My00NmI0LWFkYTctNmVkYzk1YmJkNTAy"
            }
        # Куки пользователя 2 (Session_id + SESSION)
        cookies_user2 = {
                "name": "SESSION",
                "value": "MWU5MTVkZTgtZGJkMC00YzJjLWIzMGEtYWY2YzNjMjYwNmI0"
            }
        driver.get("https://gitflic.ru/")
        driver.add_cookie(cookies_user1)
        driver.refresh()
        driver.get("https://gitflic.ru/user/id711178064")

        url_user1 = driver.current_url

        # Выход
        driver.delete_all_cookies()
        driver.refresh()

        # Устанавливаем куки пользователя 2
        driver.get("https://gitflic.ru/")
        driver.add_cookie(cookies_user2)
        driver.refresh()
        driver.get("https://gitflic.ru/user/esgeras")

        url_user2 = driver.current_url

        assert url_user1 != url_user2, f"URL одинаковые: {url_user1}"
        print("✅ Тест пройден! URL'ы различаются.")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()
