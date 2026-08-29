from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List


class ShopPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self) -> None:
        self.driver.get("https://www.saucedemo.com/")
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    def login(self) -> None:
        username = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username.send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        try:
            popup = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='password-change-modal']"))
            )
            cancel_btn = popup.find_element(By.XPATH, ".//button[contains(text(), 'Not now') or contains(text(), 'Cancel')]")
            cancel_btn.click()
        except Exception:
            pass

    def catalog(self) -> None:
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    def cart(self, items: List[str]) -> None:
        self.catalog()
        for item_name in items:
            items_container = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            for item in items_container:
                name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
                if name_element.text == item_name:
                    item.find_element(By.XPATH, ".//button[text()='Add to cart']").click()
                    break

    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(EC.presence_of_element_located((By.ID, "checkout")))

    def checkout(self) -> None:
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text.replace("Total: ", "").strip()

