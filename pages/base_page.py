from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)

    def close_popup(self):
        city_choice = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, 'closeSelectCityModal')))
        city_choice.click()

    def login(self):
        # Находим кнопку "Вход" в хедере страницы и кликаем по ней
        login_header_button = self.browser.find_element(By.CLASS_NAME, 'header__user-links')
        login_header_button.click()

        # Находим поле номера телефона и указываем значение
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Войти"]')))
        phone_number = '9275088522'
        number_field = self.browser.find_element(By.ID, 'phoneInput')

        for digit in phone_number:
            number_field.send_keys(digit)
            time.sleep(0.1)

        # Находим кнопку "Войти" в попапе и кликаем по ней
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@onclick]')))
        login_popup_button = self.browser.find_element(By.XPATH, '//button[@onclick]')
        login_popup_button.click()

        # Используем универсальный код и кликаем на кнопку "Войти
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-link')))
        code_number = '1112'
        code_field = self.browser.find_element(By.ID, 'codeInput')

        for code_send in code_number:
            code_field.send_keys(code_send)
            time.sleep(0.2)

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-link')))
        login_popup_button_2 = self.browser.find_element(By.XPATH, '//*[@id="auth-modal"]/div/div/div/form[1]/div[2]/button')
        login_popup_button_2.click()
