from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_go_to_checkout_button = (By.CLASS_NAME, 'cart-payment')


class LkBasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def go_to_checkout_button(self):
        element = self.find(locator_go_to_checkout_button)
        self.browser.execute_script("arguments[0].click();", element)