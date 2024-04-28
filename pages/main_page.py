from selenium.webdriver.common.by import By
from pages.base_page import BasePage


factories_locator = (By.CLASS_NAME, 'producer-logo')


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://allfdm.ru/')

    def factory(self):
        return self.find(factories_locator)

    def factories(self):
        return self.find_elements(factories_locator)

    def go_to_factory_page(self):
        return self.factory().click()





