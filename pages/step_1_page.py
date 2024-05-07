from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_product_card_button = (By.XPATH, '//img[@class="card-img-top" and @alt="1223 Пастель Сливки"]')
locator_popup_continue_button = (By.XPATH, '//button[@class="btn-primary" and @type="submit"]')


class StepOneKedrPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def product_card_button(self):
        return self.find(locator_product_card_button)

    def popup_continue_button(self):
        return self.find(locator_popup_continue_button)

