from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui

driver = webdriver.Chrome(service=Service(r'D:\Project\RemoteWork\selenium-test\Browsers\chromedriver.exe'))
driver.get('https://demoqa.com/date-picker')


driver.find_element(By.ID, 'datePickerMonthYearInput').click()
pyautogui.press('backspace', presses=10)
time.sleep(3)
driver.find_element(By.ID, 'datePickerMonthYearInput').send_keys('08/25/2000')
pyautogui.press('enter')

time.sleep(15)



