from selenium.webdriver.common.by import By

class ClientInfo:

    def __init__(self, driver):

         """
        Конструктор класса

        :param driver: Объект драйвера в selenium
        """

         self.driver = driver



    def enter_info(self, first_name, last_name, postal_code):

         """
         Ввод данных авторизации
        
        :param first_name, last_name, postal_code:
        Имя, Фамилия, Пароль.
        """

         self.driver.find_element(By.ID, "first-name").send_keys(first_name)

         self.driver.find_element(By.ID, "last-name").send_keys(last_name)

         self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

         self.driver.find_element(By.ID, "continue").click()