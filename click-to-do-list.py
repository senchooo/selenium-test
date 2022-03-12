from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get('https://lambdatest.github.io/sample-todo-app/')
time.sleep(5)

# click box
driver.find_element(by=By.NAME, value='li1').click()
driver.find_element(by=By.NAME, value='li2').click()
time.sleep(10)

# create to do
driver.find_element(by=By.ID, value='sampletodotext').send_keys('ketik sendiri')
time.sleep(5)

# click to do
driver.find_element(by=By.ID, value='addbutton').click()
time.sleep(10)

driver.close()



# agustyast@gmail.com
# Scrap131
# adidas yeez

