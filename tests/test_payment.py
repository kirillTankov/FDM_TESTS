from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.catalog_page import FacadePvhKedrPage
from pages.step_1_page import StepOneKedrFacadePvhPage
from pages.step_2_page import StepTwoKedrFacadePvhPage
from pages.step_3_page import StepThreeKedrFacadePvhPage
from pages.order_checkout_page import OrderCheckoutPage
from pages.LK_basket_page import LkBasketPage
from pages.blank_order_page import BlankOrderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_payment(browser):
    login = BasePage(browser)
    login.browser.get('https://dev.allfdm.ru/')
    login.close_popup()
    login.login()

    catalog_page = CatalogPage(browser)
    catalog_page.open()
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/main/factory/select-factory/kedr/"]')))
    catalog_page.factory_is_kedr_button()
    catalog_page.facade_pvh_kedr_button().click()

    facade_pvh_kedr_page = FacadePvhKedrPage(browser)
    facade_pvh_kedr_page.facade_type_button().click()

    step_one_kedr_facade_pvh_page = StepOneKedrFacadePvhPage(browser)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@data-name="1223 Пастель Сливки"]')))
    step_one_kedr_facade_pvh_page.product_card_1223_button()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
    step_one_kedr_facade_pvh_page.popup_continue_button().click()

    step_two_kedr_facade_pvh_page = StepTwoKedrFacadePvhPage(browser)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//h3[text()="Квадро"]')))
    step_two_kedr_facade_pvh_page.product_card_button()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
    step_two_kedr_facade_pvh_page.popup_continue_button().click()

    step_three_kedr_facade_pvh_page = StepThreeKedrFacadePvhPage(browser)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Добавить деталь")]')))
    step_three_kedr_facade_pvh_page.height_field_first().send_keys('2500')
    step_three_kedr_facade_pvh_page.width_field_first().send_keys('1100')
    step_three_kedr_facade_pvh_page.add_item_button().click()
    step_three_kedr_facade_pvh_page.height_field_second().send_keys('2400')
    step_three_kedr_facade_pvh_page.width_field_second().send_keys('1000')
    step_three_kedr_facade_pvh_page.calculate_order_button().click()

    blank_order_page = BlankOrderPage(browser)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="title-text" and text()="Фабрика / Тип фасада"]')))
    blank_order_page.add_in_basket_button().click()
    # WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'cross')))
    # blank_order_page.close_popup_button().click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mb-4')))
    blank_order_page.go_to_basket_button().click()

    lk_basket_page = LkBasketPage(browser)
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'cart-payment')))
    lk_basket_page.go_to_checkout_button()

    order_checkout_page = OrderCheckoutPage(browser)
    # WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
    time.sleep(7)
    order_checkout_page.checkbox_city_button()
    order_checkout_page.go_to_pay_button()

    pay_card_button = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div/div[2]/div/button')))
    assert pay_card_button.is_displayed()