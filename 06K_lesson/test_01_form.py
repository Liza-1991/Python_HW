from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_data_types_form():
    driver = webdriver.Edge()
    try:
        driver.get("https://bonigarcia.dev/"
                   "selenium-webdriver-java/data-types.html")
        # Заполнение
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        for name, value in fields.items():
            driver.find_element(By.NAME, name).send_keys(value)

        # Клик по кнопке
        btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        (driver.execute_script
         ("arguments[0].scrollIntoView({block: 'center'});", btn))
        driver.execute_script("arguments[0].click();", btn)

        time.sleep(3)  # даём время на обработку

        print("URL после клика:", driver.current_url)

        # Ищем поля
        for name in fields.keys():
            try:
                el = driver.find_element(By.NAME, name)
                print(f"{name}: class={el.get_attribute('class')}, "
                      f"border-color={el.value_of_css_property
                    ('border-color')}")
            except: print(f"{name} NOT FOUND")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_data_types_form()
