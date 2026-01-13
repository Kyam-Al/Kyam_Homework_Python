from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Calculator:

    def __init__(self, driver):
        """
        Конструктор класса
        
        :param driver: Объект драйвера в selenium
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        """
        Устанавливает задержку для выполнения операции 

        :param delay: Значение задержки в сек
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button):
        """
        Нажатие на кнопку 

        :param button: Селектор кнопки
        """
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self):
        """
        Просмотр результата 
        """
        WebDriverWait(self.driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text