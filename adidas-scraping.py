from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get('https://www.adidas.co.id/account-login')
driver.maximize_window()

driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys('agustyast@gmail.com')
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('Scrap131')
time.sleep(10)

driver.find_element(by=By.XPATH, value='//*[@id="root"]/main/div/div/div/div[1]/form/div[3]/button').click()
