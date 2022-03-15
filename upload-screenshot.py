from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://demoqa.com/upload-download')

# upload file #1
driver.find_element(By.ID, 'uploadFile').send_keys(r'D:/alien.jpg')

# upload file 2 (only button)
driver.get('https://gofile.io/uploadFiles')
driver.find_element(By.CLASS_NAME, 'btn btn-primary btn-lg mb-1 uploadButton')
time.sleep(3)
pyautogui.write(r'D:\alien.jpg')
pyautogui.press('enter')

# screenshot
driver.get_screenshot_as_file('ss.jpg')


