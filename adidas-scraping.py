from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# create item
user = 'agustyast@gmail.com'
password = 'Scrap131'
query = 'adidas yeezy'

# setup selenium
s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.adidas.co.id/account-login')
driver.maximize_window()

# fill login form
driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(user)
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="root"]/main/div/div/div/div[1]/form/div[3]/button').click()

# fill search box and search
time.sleep(5)
driver.find_element(By.CLASS_NAME, 'SearchField-Input').send_keys(query, Keys.ENTER)

# for handling error tag not found
time.sleep(15)

# start scraping
while True:
    main = driver.find_elements(By.CSS_SELECTOR, 'li.ProductCard')
    for i in main:
        detail = i.find_element(By.CLASS_NAME, 'gl-product-card__details-main')
        title = detail.find_element(By.TAG_NAME, 'span').text

        try:
            pricediscount = detail.find_element(By.CLASS_NAME, 'gl-price-item--sale').text
            pricenormal = detail.find_element(By.CLASS_NAME, 'gl-price-item--crossed').text
            discount = i.find_element(By.CSS_SELECTOR, 'div.gl-badge--urgent').text.replace('-', '')
            price = f'Discount from {pricenormal} to {pricediscount}. ({discount})'
        except Exception:
            price = detail.find_element(By.TAG_NAME, 'div').text
        if price == '':
            price = 'This product sold out'
        print(title, price)

    try:
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Halaman berikutnya"]').send_keys(Keys.ENTER)
    except Exception:
        break

    time.sleep(15)

driver.close()
