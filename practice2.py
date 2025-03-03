from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/")

driver.maximize_window()

# USING LOCATORS

# using tag and id
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("ABC@xyz.com")

#using tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys()

#using tag and attribute
driver.find_element(By.CSS_SELECTOR,"[data-testid='royal-email']")




