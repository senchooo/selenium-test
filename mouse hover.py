from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/menu')
time.sleep(5)

main = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')
sub = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
subtwo = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')

action = ActionChains(driver)

action.move_to_element(main).move_to_element(sub).move_to_element(subtwo).click().perform()

time.sleep(20)
