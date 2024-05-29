from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locator_checkbox_city_button = (By.XPATH, '//*[@id="checkout-page"]/div/div[1]/div[4]/div/div[2]/div[1]/div/label')
locator_go_to_pay_button = (By.CLASS_NAME, 'btn-success')


class OrderCheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def checkbox_city_button(self):
        element = self.find(locator_checkbox_city_button)
        self.browser.execute_script("arguments[0].click();", element)

    def go_to_pay_button(self):
        element = self.find(locator_go_to_pay_button)
        self.browser.execute_script("arguments[0].click();", element)