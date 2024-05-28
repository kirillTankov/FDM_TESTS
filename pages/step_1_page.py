from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Кедр / Фасады ПВХ
locator_product_card_1223_button = (By.XPATH, '//a[@data-name="1223 Пастель Сливки"]')
locator_popup_continue_button = (By.CLASS_NAME, 'btn-primary')


class StepOneKedrFacadePvhPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def product_card_1223_button(self):
        element = self.find(locator_product_card_1223_button)
        self.browser.execute_script("arguments[0].click();", element)

    def popup_continue_button(self):
        return self.find(locator_popup_continue_button)

