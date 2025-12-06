from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button):
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, e_result):
        result = WebDriverWait(self.driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), e_result)
    )
        return result