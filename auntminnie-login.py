from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('started program')

s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.delete_all_cookies()

driver.get('https://www.auntminnie.com/index.aspx?sec=log')
time.sleep(5)

# fill login form
driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_txtCN"]').send_keys('senchoparameswara')
driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_txtPassword"]').send_keys('xxxtripl3x')
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_cmdSignIn"]').click()

# get news item
driver.get('https://www.auntminnie.com/index.aspx?sec=nws&sub=rad')


# scraping data
while True:
    # handling error
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'MoreNewsItem')))
    for i in main:
        title = i.find_element(by=By.CLASS_NAME, value='Head')
        link = title.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        print(title.text, link)

    try:
        driver.find_element(by=By.LINK_TEXT, value='next »').click()
        time.sleep(5)
    except Exception:
        break

print('login sucsess')

