import pytest
import allure
from selenium import webdriver
from login import Login
from clientinfo import ClientInfo
from total import Total
from cart import Cart
from addproduct import AddProduct


@pytest.fixture

def browser():

    driver = webdriver.Firefox()

    yield driver

    driver.quit()


@allure.title("Проверка корзины покупок")
@allure.description("Этот тест проверяет добавление товаров в корзину, оформление заказа и проверку общей суммы.")
def test_shopping_cart(browser):
    with allure.step("Авторизация пользователя"):
        login = Login(browser)
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        add_product = AddProduct(browser)
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item_name in items_to_add:
            add_product.add_to_cart(item_name)

    with allure.step("Переход в корзину"):
        add_product.go_to_cart()

    with allure.step("Оформление заказа"):
        cart = Cart(browser)
        cart.proceed_to_checkout()

    with allure.step("Ввод информации о клиенте"):
        client_info = ClientInfo(browser)
        client_info.enter_info("Иван", "Петров", "123456")

    with allure.step("Проверка общей суммы"):
        total_page = Total(browser)
        total = total_page.get_total()
        assert total == "Total: $58.29"
