from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org/links/10")
        print(f"Открыта страница: {driver.current_url}")

        # Находим все ссылки на странице (тег <a>)
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Найдено ссылок: {len(links)}")

        # Проверяем, что количество ссылок равно 9
        # Ожидаемое количество: 9 (на странице ссылки с номерами 0..9, всего 10)
        # Но по заданию нужно проверить, что их 9, поэтому используем assert
        expected_count = 9
        assert len(links) == expected_count, f"Ожидалось {expected_count} ссылок, найдено {len(links)}"
        print(f"Количество ссылок совпадает: {len(links)}")

        # Проверяем, что все ссылки отображаются на странице
        for i, link in enumerate(links):
            assert link.is_displayed(), f"Ссылка {i} не отображается"
        print("Все ссылки отображаются")

        # Проверяем, что текст первой ссылки содержит "1"
        first_link_text = links[0].text
        assert "1" in first_link_text, f"Текст первой ссылки '{first_link_text}' не содержит '1'"
        print(f"Текст первой ссылки: '{first_link_text}' - содержит '1'")

        print("Тест пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_multiple_elements()