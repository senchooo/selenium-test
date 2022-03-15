from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://tees.co.id/')

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/modal-dialog/div/div/form/div/div/a').click()
    print('pop up closed!')
except TimeoutException:
    print('no popup')
    pass


