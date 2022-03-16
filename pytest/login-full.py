from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time

key = [
    ('agustyast@gmail.com', 'Scrap131'),  # all True
    ('agustyast@gmail.co', 'Scrap131'),  # True only password
    ('agustyast@gmail.com', 'scrap131'),  # True only email
]

url = [('https://www.adidas.co.id/pria.html'), ('https://www.adidas.co.id/wanita.html')]


@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe'), options=options)
    yield driver

    # cleanup
    driver.quit()


@pytest.mark.login
@pytest.mark.parametrize('email, password', key)
def test_login(setup, email, password):
    setup.get('https://www.adidas.co.id/account-login')
    setup.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(email)
    setup.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)
    time.sleep(10)
    setup.find_element(by=By.XPATH, value='//*[@id="root"]/main/div/div/div/div[1]/form/div[3]/button').click()
    time.sleep(10)
    tile = setup.title
    assert tile == 'Akun saya'


@pytest.mark.title
@pytest.mark.parametrize('link', url)
def test_title(setup, link):
    setup.get(link)
    tile = setup.title
    time.sleep(10)
    print(tile)

# for run with cmd:
# first, cd (locate file)
# second, pytest namefile -v -m spesificmark
# or pytest namefile -v (for run all testing)
# for report, use --html=namefile.html

