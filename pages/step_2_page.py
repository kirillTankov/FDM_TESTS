from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_product_card_button = (By.XPATH, '//h3[text()="Квадро"]')
locator_popup_continue_button = (By.CLASS_NAME, 'btn-primary')


class StepTwoKedrFacadePvhPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def product_card_button(self):
        element = self.find(locator_product_card_button)
        self.browser.execute_script("arguments[0].click();", element)

    def popup_continue_button(self):
        return self.find(locator_popup_continue_button)
