import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.slow_calculator_page import SlowCalculatorPage


class TestSlowCalculator:
    @allure.feature("Калькулятор")
    @allure.story("Вычисление с задержкой")
    @allure.title("Проверка сложения 7+8 с задержкой 45 секунд")
    @allure.description("Тест проверяет, что калькулятор корректно вычисляет 7+8 после заданной задержки")
    @allure.severity(Severity.NORMAL)
    def test_seven_plus_eight_with_delay(self):
        with allure.step("Создание и настройка драйвера"):
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()

        page = SlowCalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора и установить задержку 45 секунд"):
            page.open()
            page.set_delay(45)

        with allure.step("Выполнить вычисление 7+8"):
            page.calculate_seven_plus_eight()

        with allure.step("Получить результат"):
            result = page.get_result()

        with allure.step("Проверить, что результат равен 15"):
            assert result == "15", f"Expected '15', got '{result}'"

        driver.quit()
