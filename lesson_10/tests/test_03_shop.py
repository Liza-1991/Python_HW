import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop_page import ShopPage
import time


@allure.feature("Корзина")
@allure.story("Оформление заказа")
@allure.title("Проверка итоговой стоимости корзины")
@allure.description("Тест проверяет, что итоговая стоимость заказа трёх товаров равна $58.29")
@allure.severity(Severity.CRITICAL)
def test_shop_total():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.maximize_window()
    main = ShopPage(browser)

    with allure.step("Открыть сайт"):
        main.open()
        time.sleep(2)  # ждём загрузки страницы

    with allure.step("Авторизоваться как standard_user"):
        main.login()

    with allure.step("Дождаться загрузки каталога"):
        main.catalog()

    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    with allure.step(f"Добавить товары в корзину: {', '.join(items)}"):
        main.cart(items)

    with allure.step("Перейти в корзину"):
        main.go_to_cart()

    with allure.step("Нажать Checkout"):
        main.checkout()

    with allure.step("Заполнить форму (Liza, Maeva, 12345)"):
        main.fill_checkout_form("Liza", "Maeva", "12345")

    with allure.step("Получить итоговую стоимость"):
        total = main.get_total()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total == "$58.29", f"Ожидалось $58.29, получено {total}"

    browser.quit()


