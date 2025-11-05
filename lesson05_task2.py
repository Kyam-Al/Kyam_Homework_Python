from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    blue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Button with Dynamic ID']"))
    )

    blue_button.click()

    time.sleep(5)

except Exception as e:
    print(f"Произошла ошибка: {e}")

