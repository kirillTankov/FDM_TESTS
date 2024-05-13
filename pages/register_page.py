from selenium.webdriver.common.by import By
from pages.base_page import BasePage


locator_for_yourself_button = (By.CLASS_NAME, 'orange')
locator_number_field = (By.ID, 'phone')
locator_register_button = (By.XPATH, '//a[@class="btn g-btn g-btn--orange" and text()="Зарегистрироваться"]')
locator_code_field = (By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[1]/input')
locator_confirm_button = (By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/button')
locator_ok_button = (By.CLASS_NAME, 'button-block-green')


class RegPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://allfdm.ru/personal/vue/registration/')

    def button_for_yourself(self):
        return self.find(locator_for_yourself_button)

    def number_field(self):
        return self.find(locator_number_field)

    def register_button(self):
        return self.find(locator_register_button)

    def code_field(self):
        return self.find(locator_code_field)

    def confirm_button(self):
        return self.find(locator_confirm_button)

    def ok_button(self):
        return self.find(locator_ok_button)

