from selenium.webdriver.common.by import By

class AddProduct:

    def __init__(self, driver):
        """
        Конструктор класса

        :param driver: Объект драйвера в selenium
        """

        self.driver = driver

    def add_to_cart(self, product_name):

        """
        Выполняяет переход в корзину

        :param product_name: Открывается корзина покупателя
        """

        xpath = (f"//div[text()='{product_name}']/ancestor::"

        "div[@class='inventory_item']//button")

        item_button = self.driver.find_element(By.XPATH, xpath)

        item_button.click()

    def go_to_cart(self):
            """
            Открывает корзину для её просмотра
        """

            self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
