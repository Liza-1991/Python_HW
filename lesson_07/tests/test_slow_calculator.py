from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from  lesson_07.pages.slow_calculator_page import SlowCalculatorPage

class TestSlowCalculator:
    def test_seven_plus_eight_with_delay(self):
        # 1. Создание и настройка драйвера
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # 2. Создание объекта страницы
        page = SlowCalculatorPage(driver)

        # 3. Действия с калькулятором
        page.open()                     # открыть страницу
        page.set_delay(45)              # установить задержку 45 секунд
        page.calculate_seven_plus_eight()  # нажать 7, +, 8, =

        # 4. Получение результата и проверка
        result = page.get_result()
        assert result == "15", f"Expected '15', got '{result}'"

        # 5. Закрытие драйвера
        driver.quit()
