from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(path)

driver = webdriver.Chrome(service=service)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

# Wait for Email field, clear it, and enter email
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Email"))
)
email_input.clear()
email_input.send_keys("admin@yourstore.com")

# Wait for Password field, clear it, and enter password
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Password"))
)
password_input.clear()
password_input.send_keys("admin")

# Click on login
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"))
).click()
