import pytest  # noqa: F401
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_total():
    driver = webdriver.Firefox()
    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Ждём загрузки каталога
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        # Добавляем товары
        items = ["Sauce Labs Backpack",
                 "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for item_name in items:
            # Находим все карточки товаров
            items_container = driver.find_elements(By.CLASS_NAME,
                                                   "inventory_item")
            for item in items_container:
                # Ищем название товара внутри карточки
                name_element = (item.find_element
                                (By.CLASS_NAME, "inventory_item_name"))
                if name_element.text == item_name:
                    # Нажимаем кнопку "Add to cart" внутри этой карточки
                    (item.find_element(By.XPATH,
                                      ".//button[text()='Add to cart']")
                     .click())
                    break

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Ждём загрузки корзины
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        # Checkout
        driver.find_element(By.ID, "checkout").click()

        # Заполнение формы
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        # Ожидание итоговой суммы
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            "summary_total_label"))
        )
        total_text = total_element.text
        total_value = total_text.replace("Total: ", "").strip()

        expected_total = "$58.29"
        assert total_value == expected_total, \
            f"Ожидалось {expected_total}, получено {total_value}"

        print(f"✅ Итоговая сумма: {total_value}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop_total()
