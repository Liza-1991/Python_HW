from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org/forms/post")
        print(f"Открыта страница: {driver.current_url}")

        # Поле ввода custname
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "custname"))
        )
        name_field.send_keys("Иван Петров")
        print("Имя введено в поле custname")

        # Пытаемся найти кнопку разными способами
        try:
            # Вариант 1: input с type='submit' или value='Submit', или button с type='submit'
            submit_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//input[@type='submit' or @value='Submit'] | //button[@type='submit']"
                ))
            )
            submit_button.click()
            print("Кнопка найдена и нажата (input/button с type='submit')")
        except:
            try:
                # Вариант 2: любой элемент с value='Submit'
                submit_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@value='Submit']"))
                )
                submit_button.click()
                print("Кнопка найдена по value='Submit' и нажата")
            except:
                try:
                    # Вариант 3: любой элемент с текстом, содержащим 'Submit'
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Submit')]"))
                    )
                    submit_button.click()
                    print("Кнопка найдена по тексту, содержащему 'Submit', и нажата")
                except:
                    # Если ничего не сработало — отправляем форму через submit()
                    print("Кнопка не найдена, отправляем форму через submit()")
                    name_field.submit()
                    print("Форма отправлена через submit()")

        # Проверяем, что URL изменился
        WebDriverWait(driver, 5).until(
            EC.url_changes("https://httpbin.org/forms/post")
        )
        print(f"URL изменился: {driver.current_url}")

        print("Тест пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form_submission()