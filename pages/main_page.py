from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


locator_promotion = (By.CLASS_NAME, 'header-link')


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://allfdm.ru/')

    def factory(self, factory_name):
        # Засунул сюда локатор каждой из фабрик, чтобы цикл for перебирал значение этих фабрик
        return self.find((By.XPATH, f"//a[@class='producer' and contains(@href, '{factory_name}')]"))

    def go_to_factory_page(self, factory_name):
        factory_element = self.factory(factory_name)
        self.browser.execute_script("arguments[0].click();", factory_element)

    '''def scroll_to_factory(self, factory_name):
        factory_element = self.find(f"//a[@class='producer' and contains(@href, '{factory_name}')]")
        self.browser.execute_script("arguments[0].scrollIntoView();", factory_element)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(factory_name))''' # Это должна была быть полезная прокрутка до каждой фабрики, но и без неё всё работает

    def go_to_main_page(self):
        self.open()

    def go_to_promotion_page(self):
        return self.find(locator_promotion).click()

    def scroll_to_promotion(self):
        element = self.find(locator_promotion)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator_promotion))

