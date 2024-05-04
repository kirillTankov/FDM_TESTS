from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://allfdm.ru/')

    def factory(self, factory_name):
        # Засунул сюда локатор, чтобы цикл for перебирал значение фабрик
        return self.find((By.XPATH, f"//a[@class='producer' and contains(@href, '{factory_name}')]"))

    def go_to_factory_page(self, factory_name):
        return self.factory(factory_name).click()

    def go_to_main_page(self):
        self.open()




