import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        """Авторизация стандартным пользователем."""
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def catalog(self):
        """Ожидание загрузки каталога товаров."""
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def cart(self, items):
        """
        Добавляет перечисленные товары в корзину по их названиям.
        :param items: список названий товаров (например, ["Sauce Labs Backpack", ...])
        """
        self.catalog()
        for item_name in items:
            items_container = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            for item in items_container:
                name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
                if name_element.text == item_name:
                    item.find_element(By.XPATH, ".//button[text()='Add to cart']").click()
                    break

    def go_to_cart(self):
        """Переход в корзину."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        """Нажатие кнопки Checkout на странице корзины."""
        self.driver.find_element(By.ID, "checkout").click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполняет форму оформления заказа и нажимает Continue."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """Возвращает итоговую стоимость в виде строки (например, '$58.29')."""
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text.replace("Total: ", "").strip()


# ---------- Фикстура для управления браузером ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# ---------- Сам тест ----------
def test_total_price(driver):
    shop = ShopPage(driver)

    shop.open()                     # 1. Открыть сайт
    shop.login()                    # 2. Авторизоваться
    shop.cart([                     # 3. Добавить товары
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ])
    shop.go_to_cart()               # 4. Перейти в корзину
    shop.checkout()                 # 5. Нажать Checkout
    shop.fill_checkout_form("Liza", "Maeva", "12345")  # 6. Ваши данные
    total = shop.get_total()        # 7. Прочитать итоговую стоимость
    assert total == "$58.29", f"Ожидалось $58.29, получено {total}"  # 8. Проверка

