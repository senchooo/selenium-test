from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# setup selenium
s = Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.adidas.co.id/account-login')


def login_query(user, password, query):
    # fill login form
    username = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
    username.clear()
    username.send_keys(user)
    passw = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
    passw.clear()
    passw.send_keys(password)
    time.sleep(10)

    # click login
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/main/div/div/div/div[1]/form/div[3]/button').click()
    time.sleep(3)

    # fill search box and search
    que = driver.find_element(By.CLASS_NAME, 'SearchField-Input')
    que.clear()
    que.send_keys(query, Keys.ENTER)
    time.sleep(15)


def sorting(sort_filter):
    sortlist = None
    if sort_filter == 1:
        sortlist = 'DESC recommended_score'
    elif sort_filter == 2:
        sortlist = 'ASC position'
    elif sort_filter == 3:
        sortlist = 'ASC name'
    elif sort_filter == 4:
        sortlist = 'DESC name'
    elif sort_filter == 5:
        sortlist = 'ASC price'
    elif sort_filter == 6:
        sortlist = 'DESC price'

    # click the sorting filter
    sort = driver.find_element(By.XPATH, '//*[@id="root"]/main/section/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/button')
    chose = driver.find_element(By.CSS_SELECTOR, f'button[value="{sortlist}"]')

    sort.send_keys(Keys.ENTER)
    time.sleep(3)
    chose.click()

    # for handling not yet item
    time.sleep(15)


def scrap():
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

        # click next page
        try:
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Halaman berikutnya"]').send_keys(Keys.ENTER)
        except Exception:
            break

        # handling not yet item
        time.sleep(15)


def run():
    runing = int(input('please choose\n1. scraping only\n2. scraping with sorting\nchoose your number: '))
    user = input('Input Your Username')
    password = input('Input Your Password')
    query = input('Input Your Query')

    if runing == 1:
        login_query(user=user, password=password, query=query)
        scrap()
        driver.close()
        print('all item has scrap')
    elif runing == 2:
        sorter = int(input('sort by:\n1. recomended\n2. popular\n3. name A to Z\n4. name Z to A\n5. price low to high\n6. price high to low\nEnter the number you want: '))
        login_query(user=user, password=password, query=query)
        sorting(sorter)
        scrap()
        driver.close()
        print('all item has scrap')
    else:
        print('please input correct number')
        run()

    driver.maximize_window()

run()