from selenium.webdriver.common.by import By

class Cart:

    def __init__(self, driver):
         """
         Конструктор класса
        
        :param driver: Объект драйвера в selenium
        """

         self.driver = driver



    def proceed_to_checkout(self):

         """
        Начало оформления заказа
        """

         self.driver.find_element(By.ID, "checkout").click()
