import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    """Фикстура для создания экземпляра StringUtils."""
    return StringUtils()


# ---------- Тесты для capitalize ----------
class TestCapitalize:
    """Позитивные и негативные тесты для метода capitalize."""

    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),          # обычный случай
        ("hello world", "Hello world"),  # с пробелом внутри
        ("123abc", "123abc"),          # начинается с цифры
        # → первая буква не меняется
        ("", ""),                      # пустая строка
        ("a", "A"),                    # один символ
        ("ALREADY", "Already"),        # все заглавные → .capitalize()
        # приводит остальные к нижнему
    ])
    def test_capitalize_positive(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("input_str", [
        None,                          # передача None (не строка)
        123,                           # передача числа
    ])
    def test_capitalize_negative_non_string(self, utils, input_str):
        with pytest.raises(AttributeError):
            utils.capitalize(input_str)


# ---------- Тесты для trim ----------
class TestTrim:
    """Тесты для метода trim."""

    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),  # пробелы
        # в начале
        ("skypro", "skypro"),          # без пробелов
        ("   sky   pro   ", "sky   pro   "),  # пробелы внутри
        # и в конце не трогаем
        ("", ""),                      # пустая строка
        (" \t\nskypro", " \t\nskypro"),  # табуляция и перевод строки
        # – НЕ удаляются (дефект?)
    ])
    def test_trim_positive(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

    @pytest.mark.parametrize("input_str", [
        None,
        123,
    ])
    def test_trim_negative_non_string(self, utils, input_str):
        with pytest.raises(AttributeError):
            utils.trim(input_str)


# ---------- Тесты для contains ----------
class TestContains:
    """Тесты для метода contains."""

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        # символ есть
        ("SkyPro", "U", False),
        # символа нет
        ("SkyPro", "Pro", True),
        # подстрока есть
        ("", "", True),                # пустая строка и пустой символ →
        # True (особенность)
        ("abc", "", True),             # пустой символ всегда
        # считается найденным
        # (index("")=0)
    ])
    def test_contains_positive(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol", [
        (None, "a"),                   # string не строка
        ("abc", None),                 # symbol не строка
    ])
    def test_contains_negative_non_string(self, utils, string, symbol):
        with pytest.raises(TypeError):
            utils.contains(string, symbol)


# ---------- Тесты для delete_symbol ----------
class TestDeleteSymbol:
    """Тесты для метода delete_symbol."""

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),      # удаление символа
        ("SkyPro", "Pro", "Sky"),      # удаление подстроки
        ("SkyPro", "z", "SkyPro"),     # символ не найден –
        # возвращает исходную строку
        ("", "", ""),                  # пустая строка, пустой символ
        ("aaa", "a", ""),              # удаление всех вхождений
        ("aabbaa", "aa", "bb"),        # удаление подстроки
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol", [
        (None, "a"),
        ("abc", None),
    ])
    def test_delete_symbol_negative_non_string(self, utils, string, symbol):
        with pytest.raises(TypeError):
            utils.delete_symbol(string, symbol)
