from pages.register_page import RegPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register(browser):
    reg_page = RegPage(browser)
    base_page = BasePage(browser)
    reg_page.open()
    base_page.close_popup()

    reg_page.button_for_yourself().click()
    reg_page.number_field().send_keys('9842008001')
    reg_page.register_button().click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/button')))
    reg_page.code_field().send_keys('3597')
    reg_page.confirm_button().click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'button-block-green')))
    reg_page.ok_button().click()

    banner_element = browser.find_element(By.CLASS_NAME, 'promo-2')
    assert banner_element.is_displayed()
