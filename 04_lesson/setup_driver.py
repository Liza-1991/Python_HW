from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ya.ru")          # откроем Яндекс
print(driver.title)                  # выведем заголовок страницы
input("Нажмите Enter, чтобы закрыть...")  # пауза, чтобы вы успели увидеть
driver.quit()

