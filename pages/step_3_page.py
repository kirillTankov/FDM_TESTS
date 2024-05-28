from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_height_field_first = (By.XPATH, '//*[@id="order-step3"]/div/div/div[1]/div/div[3]/div/div[2]/div/div[1]/div[2]/input')
locator_width_field_first = (By.XPATH, '//*[@id="order-step3"]/div/div/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/input')
locator_add_item_button = (By.XPATH, '//a[contains(text(), "Добавить деталь")]')
locator_height_field_second = (By.XPATH, '//*[@id="order-step3"]/div/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div[2]/input')
locator_width_field_second = (By.XPATH, '//*[@id="order-step3"]/div/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div[2]/input')
locator_calculate_order_button = (By.XPATH, '//*[@id="order-step3"]/div/div/div[4]/button')


class StepThreeKedrFacadePvhPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def calculate_order_button(self):
        return self.find(locator_calculate_order_button)

    def height_field_first(self):
        return self.find(locator_height_field_first)

    def width_field_first(self):
        return self.find(locator_width_field_first)

    def add_item_button(self):
        return self.find(locator_add_item_button)

    def height_field_second(self):
        return self.find(locator_height_field_second)

    def width_field_second(self):
        return self.find(locator_width_field_second)
