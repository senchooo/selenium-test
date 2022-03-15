from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/alerts')
btn_only = driver.find_element(By.XPATH, '//*[@id="alertButton"]')
btn_ok = driver.find_element(By.XPATH, '//*[@id="confirmButton"]')
btn_prompt = driver.find_element(By.XPATH, '//*[@id="promtButton"]')

# only alert
btn_ok.click()
time.sleep(5)
# driver.switch_to.alert.accept()   # click ok button
driver.switch_to.alert.dismiss()    # click cancle button

# alert with prompts
btn_prompt.click()
time.sleep(5)
driver.switch_to.alert.send_keys('hey')
driver.switch_to.alert.accept()


time.sleep(10)
