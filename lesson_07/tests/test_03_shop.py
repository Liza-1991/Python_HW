import pytest  # noqa: F401
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_07.pages.shop_page import ShopPage


def test_shop_total():
    driver = webdriver.Firefox()
    main = ShopPage(driver)

    # Открыть
    main.open()

    # Авторизация
    main.login()

    # Ждём загрузки каталога
    main.catalog()

    # Добавляем товары
    items = ["Sauce Labs Backpack",
                 "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    main.cart(items)

