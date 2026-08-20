from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # максимальное время ожидания – 60 секунд

        # Локаторы элементов
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: int):
        """Устанавливает значение задержки в поле ввода."""
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))

    def _click_button(self, text: str):
        """
        Внутренний метод для клика по кнопке калькулятора с заданным текстом.
        Использует JavaScript для прокрутки и клика, чтобы избежать перекрытия.
        """
        locator = (By.XPATH, f"//span[text()='{text}']")
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def calculate_seven_plus_eight(self):
        """Выполняет последовательное нажатие кнопок: 7, +, 8, =."""
        self._click_button("7")
        self._click_button("+")
        self._click_button("8")
        self._click_button("=")

    def get_result(self) -> str:
        """
        Ожидает, пока в поле результата появится осмысленное число (не пусто и не "NaN"),
        затем возвращает текст результата.
        """

        self.wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return self.driver.find_element(*self.result_screen).text
