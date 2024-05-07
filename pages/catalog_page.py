from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_kedr_button = (By.XPATH, '//a[@class="active" and text()="Кедр"]')
locator_facade_pvh_kedr_button = (By.XPATH, '//a[@href="/select-facade/pvh/"]')
locator_facade_type_button = (By.CLASS_NAME, 'select-facade-type-button')


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://allfdm.ru/main/factory/select-factory/')

    def factory_is_kedr_button(self):
        return self.find(locator_kedr_button)

    def facade_pvh_kedr_button(self):
        return self.find(locator_facade_pvh_kedr_button)


class FacadePvhKedrPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def facade_type_button(self):
        return self.find(locator_facade_type_button)
