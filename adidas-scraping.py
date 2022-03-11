from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get('https://www.adidas.co.id/account-login')
driver.maximize_window()

driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys('agustyast@gmail.com')
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('Scrap131')
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="root"]/main/div/div/div/div[1]/form/div[3]/button').click()

driver.get('https://www.adidas.co.id/pria.html?sortKey=recommended_score&sortDirection=DESC')

count = 1
while True:
    print(count)

    main = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/section/div/div/div[4]/div/ul')))
    main = driver.find_elements(By.CLASS_NAME, 'ProductCard ')

    for i in main:
            detail = i.find_element(By.CLASS_NAME, 'gl-product-card__details-main')
            title = detail.find_element(By.TAG_NAME, 'span')
            price = detail.find_element(By.TAG_NAME, 'div')
            print(title.text, price.text)

    nextpage = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > main > section > div > div > div.CategoryPage-ProductListWrapper > div > nav > div > li:nth-child(3) > a > span')))
    nextpage.click()
    time.sleep(20)
    count += 1


