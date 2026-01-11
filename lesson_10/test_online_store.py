import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from login import Login
from clientinfo import ClientInfo
from total import Total
from cart import Cart
from addproduct import AddProduct


@pytest.fixture

def browser():

    driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver

    driver.quit()

@allure.epic("E-commerce платформа")
@allure.feature("Корзина и оформление заказа")
@allure.story("Покупка нескольких товаров")
@allure.title("Проверка сквозного процесса покупки (Checkout Flow)")
@allure.description("Авторизация, выбор товаров, заполнение данных и сверка финальной суммы.")
def test_shopping_cart_flow(browser: WebDriver):
    """
    Проверяет полную цепочку: от входа в систему до финального экрана оплаты.
    Особое внимание уделяется корректности расчета Total Price.
    """
    
    with allure.step("Авторизация под пользователем 'standard_user'"):
        login = Login(browser)
        login.login("standard_user", "secret_sauce")

    with allure.step("Выбор и добавление товаров в корзину"):

        add_product = AddProduct(browser)
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"]
        for item_name in items_to_add:
            add_product.add_to_cart(item_name)

    with allure.step("Переход к просмотру корзины"):
        add_product.go_to_cart()

    with allure.step("Начало оформления заказа (Checkout)"):
        cart = Cart(browser)
        cart.proceed_to_checkout()

    with allure.step("Ввод регистрационных данных покупателя"):
        client_info = ClientInfo(browser)
        client_info.enter_info("Иван", "Петров", "123456")

    with allure.step("Валидация итоговой стоимости заказа"):
        total_page = Total(browser)
        actual_total = total_page.get_total()
        expected_total = "Total: $58.29"

    assert actual_total.strip() == expected_total, \
            f"Несоответствие итоговой суммы. Ожидалось: {expected_total}, факт: {actual_total}"