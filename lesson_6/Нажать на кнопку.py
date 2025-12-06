from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()

green_flash = WebDriverWait(driver, 16).until(
EC.presence_of_element_located((By.CLASS_NAME, "bg-success")))

text_from_flash = green_flash.text

print(text_from_flash)
