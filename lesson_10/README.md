# Домашнее задание №10: Allure + PageObject

## Описание проекта
Этот проект содержит автотесты для интернет-магазина SauceDemo и медленного калькулятора, написанные с использованием **Page Object** и **Allure** для генерации отчётов.

## Структура проекта
- `pages/` – классы Page Object:
  - `shop_page.py` – страница магазина
  - `slow_calculator_page.py` – страница калькулятора
- `tests/` – тестовые файлы:
  - `test_03_shop.py` – тест корзины
  - `test_slow_calculator.py` – тест калькулятора

## Требования
- Python 3.10+
- Установленные пакеты: `pytest`, `selenium`, `webdriver-manager`, `allure-pytest`
- Установленный Allure (команда `allure` должна быть доступна в PATH)
- Браузер Chrome (или Firefox с соответствующим драйвером)

## Как запустить тесты и сформировать Allure-отчёт
1. Активируйте виртуальное окружение (если используете):
   ```bash
   .venv\Scripts\activate
## Запустите тесты с сохранением Allure-результатов в папку allure-results:
   pytest lesson_10/ --alluredir=allure-results
## После успешного запуска тестов запустите команду
allure serve allure-results

