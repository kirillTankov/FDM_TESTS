from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


locator_kedr_button = (By.CSS_SELECTOR, 'a[href="/main/factory/select-factory/kedr/"]')
locator_facade_pvh_kedr_button = (By.XPATH, '//a[@href="/select-facade/pvh/"]')

locator_facade_type_kedr_button = (By.CLASS_NAME, 'select-facade-type-button')


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://dev.allfdm.ru/main/factory/select-factory/')

    def factory_is_kedr_button(self):
        element = self.find(locator_kedr_button)
        self.browser.execute_script("arguments[0].click();", element)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator_facade_pvh_kedr_button))

    def facade_pvh_kedr_button(self):
        return self.find(locator_facade_pvh_kedr_button)


class FacadePvhKedrPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def facade_type_button(self):
        return self.find(locator_facade_type_kedr_button)
