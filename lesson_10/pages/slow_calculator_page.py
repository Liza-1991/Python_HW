from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """
    Класс Page Object для страницы медленного калькулятора.
    Позволяет задавать задержку, выполнять вычисления и получать результат.
    """

    def __init__(self, driver) -> None:
        """
        Инициализирует страницу калькулятора.

        Args:
            driver: WebDriver-экземпляр Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # максимальное время ожидания – 60 секунд

        # Локаторы элементов
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает значение задержки в поле ввода.

        Args:
            seconds (int): Количество секунд задержки перед вычислением.
        """
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))

    def _click_button(self, text: str) -> None:
        """
        Внутренний метод для клика по кнопке калькулятора с заданным текстом.
        Использует JavaScript для прокрутки и клика, чтобы избежать перекрытия.

        Args:
            text (str): Текст, отображаемый на кнопке (например, '7', '+', '=').
        """
        locator = (By.XPATH, f"//span[text()='{text}']")
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def calculate_seven_plus_eight(self) -> None:
        """Выполняет последовательное нажатие кнопок для вычисления выражения 7 + 8."""
        self._click_button("7")
        self._click_button("+")
        self._click_button("8")
        self._click_button("=")

    def get_result(self) -> str:
        """
        Ожидает, пока в поле результата появится число 15, затем возвращает его.

        Returns:
            str: Текст, отображаемый в поле результата (ожидается '15').
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return self.driver.find_element(*self.result_screen).text

