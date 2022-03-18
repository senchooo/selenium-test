from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# setup selenium
s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.auntminnie.com/')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '#nav-search-btn').send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, '#txtSearch').send_keys('ct scan', Keys.ENTER)
a = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/div[2]/div[3]/h4')
print(a.text)


time.sleep(10)
