from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(path)

driver = webdriver.Chrome(service=service)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

# Absolute Xpath
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]"))
).send_keys("t shirts")

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button"))
).click()

# Relative Xpath
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='search_query_top']"))
).send_keys("t shirts")

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='searchbox']/button"))
).click()

# Xpath Options:

# OR
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='search_query_top' or @name='search_query']"))
).send_keys("t shirts")

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//input[@id='searchbox' and @name='submit_search'/following-sibling::button]"))
).click()

# Contains and starts with
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'search_query_top')]"))
).send_keys("t shirts")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@name,'submit_search')]"))
).click()

driver.find_element(By.XPATH, "//a[text()='Women']").click()


