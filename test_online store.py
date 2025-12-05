import pytest
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



def test_shopping_cart(browser):

    login = Login(browser)

    login.login("standard_user", "secret_sauce")

    add_product = AddProduct(browser)

    items_to_add = [

        "Sauce Labs Backpack",

        "Sauce Labs Bolt T-Shirt",

        "Sauce Labs Onesie"

    ]

    for item_name in items_to_add:

        add_product.add_to_cart(item_name)

    

    add_product.go_to_cart()

    cart = Cart(browser)

    cart.proceed_to_checkout()

    

    client_info = ClientInfo(browser)

    client_info.enter_info("Иван", "Петров", "123456")

    

    total_page = Total(browser)

    total = total_page.get_total()

    assert total == "Total: $58.29"