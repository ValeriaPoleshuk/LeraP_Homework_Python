import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    (None, None),
])
def test_capitalize_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == expected

# Тесты для функции trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world  ", "hello world  "),
    ("123  ", "123  "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    (None, None),
])
def test_trim_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected

# Тесты для функции contains
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("12345", "3", True),
])
def test_delete_symbol_negative(input_str, string: str, symbol: str) -> bool:
    if not string.strip():
        return False
    return symbol in string

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "S", False),
    (None, "S", False),
])
def test_contains_negative(input_str, symbol, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.contains(input_str, symbol)
    else:
        assert string_utils.contains(input_str, symbol) == expected

# Тесты для функции delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("12345", "3", "1245"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "k", ""),
    (" ", " ", ""),
    (None, "k", None),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.delete_symbol(input_str, symbol)
    else:
        assert string_utils.delete_symbol(input_str, symbol) == expected
