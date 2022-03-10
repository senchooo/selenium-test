from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

print('started program')

s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://www.auntminnie.com/index.aspx?sec=log')
time.sleep(5)

# fill username
driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_txtCN"]').send_keys('senchoparameswara')
time.sleep(5)

# fill password
driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_txtPassword"]').send_keys('xxxtripl3x')
time.sleep(5)

# login
driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_cmdSignIn"]').click()
time.sleep(20)

driver.close()
print('login sucsess')

