from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_checkbox_city_button = (By.CLASS_NAME, 'custom-control-input')
locator_go_to_pay_button = (By.CLASS_NAME, 'btn-success')


class OrderCheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def checkbox_city_button(self):
        return self.find(locator_checkbox_city_button)

    def go_to_pay_button(self):
        return self.find(locator_go_to_pay_button)