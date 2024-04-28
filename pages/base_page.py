from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)

    def close_popup(self):
        city_choice = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, 'closeSelectCityModal')))
        city_choice.click()
