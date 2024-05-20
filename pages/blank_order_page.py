from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_add_in_basket_button = (By.CLASS_NAME, 'add-to-basket-js')
locator_go_to_basket_button = (By.CLASS_NAME, 'in-basket mb-4')


class BlankOrderPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def add_in_basket_button(self):
        return self.find(locator_add_in_basket_button)

    def go_to_basket_button(self):
        return self.find(locator_go_to_basket_button)