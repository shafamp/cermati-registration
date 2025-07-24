from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cermati.com/app/gabung")

# Waiting for loading page
wait = WebDriverWait(driver, 10)

# Fill in all field
wait.until(EC.presence_of_element_located((By.NAME, "mobilePhone"))).send_keys("081234567000")
driver.find_element(By.NAME, "email").send_keys("shafa.testyu@mailinator.com")
driver.find_element(By.NAME, "firstName").send_keys("Shafa")
driver.find_element(By.NAME, "lastName").send_keys("Pradinar")

# Wait until register button is enable
submit_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-button-name='register-new']"))
)

submit_button.click()
print("Daftar button successfully clicked.")

time.sleep(5)
driver.quit()