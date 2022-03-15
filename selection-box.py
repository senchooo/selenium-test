from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import pyautogui

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/select-menu')

# old selection
chooseone = Select(driver.find_element(By.ID, 'oldSelectMenu'))
chooseone.select_by_visible_text('Black')

# select with typing
driver.find_element(By.ID, 'selectOne').click()
pyautogui.typewrite('Prof.')
pyautogui.press('enter')


