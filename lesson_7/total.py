from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Total:

    def __init__(self, driver):

        self.driver = driver



    def get_total(self):

        total_locator = (By.CLASS_NAME, "summary_total_label")

        total = WebDriverWait(self.driver, 10).until(

            EC.visibility_of_element_located(total_locator)

        ).text

        return total