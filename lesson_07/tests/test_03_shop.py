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



#         # Переход в корзину
#         driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#
#         # Ждём загрузки корзины
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
#         )
#
#         # Checkout
#         driver.find_element(By.ID, "checkout").click()
#
#         # Заполнение формы
#         driver.find_element(By.ID, "first-name").send_keys("Иван")
#         driver.find_element(By.ID, "last-name").send_keys("Петров")
#         driver.find_element(By.ID, "postal-code").send_keys("123456")
#
#         driver.find_element(By.ID, "continue").click()
#
#         # Ожидание итоговой суммы
#         total_element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME,
#                                             "summary_total_label"))
#         )
#         total_text = total_element.text
#         total_value = total_text.replace("Total: ", "").strip()
#
#         expected_total = "$58.29"
#         assert total_value == expected_total, \
#             f"Ожидалось {expected_total}, получено {total_value}"
#
#         print(f"✅ Итоговая сумма: {total_value}")
#
#     finally:
#         driver.quit()
#
#
# if __name__ == "__main__":
#     test_shop_total()
