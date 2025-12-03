import pytest
from selenium import webdriver
from calc import Calculator

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(browser):
    calc = Calculator(browser)
    calc.set_delay("45")
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")
    assert calc.get_result("15") == "15"

   