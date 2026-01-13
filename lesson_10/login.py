from selenium.webdriver.common.by import By

class Login:

    def __init__(self, driver):

         """
        Конструктор класса

        :param driver: Объект драйвера в selenium
        """

         self.driver = driver

         self.driver.get("https://www.saucedemo.com/")



    def login(self, username, password):

         """
         Авторизазия стандартного пользователя

        :param username, password: Ввод логина, ввод пороля.
        """

         self.driver.find_element(By.ID, "user-name").send_keys(username)

         self.driver.find_element(By.ID, "password").send_keys(password)

         self.driver.find_element(By.ID, "login-button").click()