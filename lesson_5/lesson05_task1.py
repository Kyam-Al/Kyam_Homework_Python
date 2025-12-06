from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")

    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

    blue_button.click()

    time.sleep(10)
except Exception as e:
    print(f"Произошла ошибка: {e}")
