import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("hello world") == "Hello world"
    assert string_utils.capitalize("a") == "A"


def test_capitalize_empty_string(string_utils):
    assert string_utils.capitalize("") == ""


def test_capitalize_already_capitalized(string_utils):
    assert string_utils.capitalize("Skypro") == "Skypro"


def test_trim_positive(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("  hello world") == "hello world"
    assert string_utils.trim(" skypro  ") == "skypro  "


def test_trim_no_leading_spaces(string_utils):
    assert string_utils.trim("skypro") == "skypro"


def test_trim_empty_string(string_utils):
    assert string_utils.trim("") == ""


def test_trim_only_spaces(string_utils):
    assert string_utils.trim("   ") == ""


def test_contains_positive(string_utils):
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "P") is True
    assert string_utils.contains("SkyPro", "o") is True
    assert string_utils.contains("SkyPro", "y") is True


def test_contains_negative(string_utils):
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("SkyPro", "z") is False
    assert string_utils.contains("SkyPro", " ") is False


def test_contains_empty_string(string_utils):
    assert string_utils.contains("", "A") is False


def test_contains_empty_symbol(string_utils):
    with pytest.raises(ValueError):
        string_utils.contains("SkyPro", "")


def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "P") == "Skyro"
    assert string_utils.delete_symbol("SkyPro", "S") == "kyPro"
    assert string_utils.delete_symbol("banana", "a") == "bnn"


def test_delete_symbol_symbol_not_present(string_utils):
    assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"


def test_delete_symbol_empty_string(string_utils):
    assert string_utils.delete_symbol("", "a") == ""


def test_delete_symbol_empty_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"


def test_delete_symbol_delete_all(string_utils):
    assert string_utils.delete_symbol("aaaa", "a") == ""