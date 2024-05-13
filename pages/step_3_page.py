from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_height_field_first = (By.XPATH, '//input[@name="details[0][height]"]')
locator_width_field_first = (By.XPATH, '//input[@name="details[0][width]"]')
locator_add_item_button = (By.ID, 'addItemButton')
locator_height_field_second = (By.XPATH, '//input[@name="details[1][height]"]')
locator_width_field_second = (By.XPATH, '//input[@name="details[1][width]"]')
locator_calculate_order_button = (By.ID, 'submitButton')


class StepThreeKedrPvhPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

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
