from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        driver.get("https://"
                   "bonigarcia.dev/selenium-webdriver-java/"
                   "slow-calculator.html")

        # Устанавливаем задержку 45 секунд
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Функция для клика с прокруткой и JavaScript
        def click_with_js(selector):
            element = driver.find_element(By.XPATH, selector)
            driver.execute_script("arguments[0]."
                                  "scrollIntoView({block:"
                                  " 'center'});", element)
            driver.execute_script("arguments[0].click();", element)

        # Нажимаем кнопки
        click_with_js("//span[text()='7']")
        click_with_js("//span[text()='+']")
        click_with_js("//span[text()='8']")
        click_with_js("//span[text()='=']")

        # Ожидаем, что в элементе .screen появится текст "15"
        WebDriverWait(driver,
                      50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )

        # Проверяем результат
        result = driver.find_element(By.CSS_SELECTOR, ".screen")
        assert result.text == "15", f"Expected '15', got '{result.text}'"

        print("✅ Тест пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
