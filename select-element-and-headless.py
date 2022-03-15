from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

print("started program")


# headless = scrap tanpa membuka browser
options = webdriver.ChromeOptions()
options.headless = True

s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

# maximaze windows
driver.maximize_window()

# get url
driver.get("https://www.google.com/")

# search box and send values
a = driver.find_element(by=By.NAME, value='q')
a.send_keys('sencho parameswara')
time.sleep(2)

# submit query
a.submit()
time.sleep(5)
"""
search button and enter
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
"""

# get all data from search
search = driver.find_elements(by=By.XPATH, value='//*[@id="rso"]')
print(search[0].text)

# close browser
driver.minimize_window()

print('done')
