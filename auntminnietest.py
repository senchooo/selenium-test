import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Auntminnietest(unittest.TestCase):
    def test_Title(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://www.auntminnie.com/')
        print(f'Title of the main page: {self.driver.title}')

    def test_Casetitle(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://www.auntminnie.com/')
        self.driver.find_element(By.XPATH, '//*[@id="nav"]/div[1]/ul/li[3]/a').click()
        print(f'Title of the cases page: {self.driver.title}')


if __name__ == 'main':
    unittest.main()
