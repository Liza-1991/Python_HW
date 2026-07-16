from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org/")
        print(f"Открыта главная страница: {driver.current_url}")

        # Находим ссылку по атрибуту href, ведущему на /forms/post
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/forms/post')]"))
        )
        link.click()
        print("Клик по ссылке 'HTML Form' выполнен")

        expected_url = "https://httpbin.org/forms/post"
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        assert driver.current_url == expected_url, f"Ожидался URL {expected_url}, а получили {driver.current_url}"
        print(f"URL успешно изменился: {driver.current_url}")

        driver.back()
        print("Нажата кнопка 'Назад'")

        main_url = "https://httpbin.org/"
        WebDriverWait(driver, 5).until(EC.url_to_be(main_url))
        assert driver.current_url == main_url, f"Ожидался URL {main_url}, а получили {driver.current_url}"
        print(f"Успешно вернулись на главную: {driver.current_url}")

        print("Тест пройден!")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_navigation()
