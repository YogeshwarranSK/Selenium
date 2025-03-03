from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


path = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(path)

driver = webdriver.Chrome(service=service)
driver.get("http://www.automationpractice.pl/index.php")

# To maximize window
driver.maximize_window()

sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))