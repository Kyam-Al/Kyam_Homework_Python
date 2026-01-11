import pytest
import allure
from selenium import webdriver
from calc import Calculator

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тест для калькулятора")
@allure.feature("Калькулятор")
@allure.description("Тест проверяет складывания суммы и выдержку 45 сек")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(browser):
    calc = Calculator(browser)

    with allure.step("Установить задержку 45 сек"):
        calc.set_delay("45")

    with allure.step("Нажатие на кнопку 7"):
        calc.click_button("7")

    with allure.step("Нажатие на кнопку +"):
        calc.click_button("+")

    with allure.step("Нажать на кнопку 8"):
        calc.click_button("8")

    with allure.step("Нажать на кнопку ="):
        calc.click_button("=")

    with allure.step("Проверить что результат равен 15"):
        assert calc.get_result() == "15"

   