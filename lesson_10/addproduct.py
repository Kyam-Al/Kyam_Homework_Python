from selenium.webdriver.common.by import By

class AddProduct:

    def __init__(self, driver):

        self.driver = driver

    def add_to_cart(self, product_name):

        xpath = (f"//div[text()='{product_name}']/ancestor::"

        "div[@class='inventory_item']//button")

        item_button = self.driver.find_element(By.XPATH, xpath)

        item_button.click()

    def go_to_cart(self):

            self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
