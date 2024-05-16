'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
browser.get('https://dev.allfdm.ru/personal/login-anywhere')


phone_number = '9275088522'
number_field = browser.find_element(By.ID, 'phoneInput')

for digit in phone_number:
    number_field.send_keys(digit)
    time.sleep(0.1)

register = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/button')))
register.click()

sleep(2)

code_number = '111'
code_field = browser.find_element(By.ID, 'codeInput')

for code_send in code_number:
    code_field.send_keys(code_send)
    time.sleep(0.2)


click_catalog = browser.find_element(By.XPATH, '//a[@class="header__link nav__link nav__link--arrow "]')
click_catalog.click()

sleep(5)


'''