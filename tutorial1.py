from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


service = Service(r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Corrected URL (Login page instead of Dashboard)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# Wait until username field is present and enter text
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
).send_keys("Admin")

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.NAME, "password"))
).send_keys("admin123")

# Click the login button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
).click()

# To verify login
acc_login = driver.title
exp_login = "OrangeHRM"

if acc_login == exp_login:
    print("Login Successfull")
else:
    print("Invalid Credentials")


