from pages.register_page import RegPage, locator_ok_button, locator_confirm_button
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
    reg_page.number_field().send_keys('9275088597')
    reg_page.register_button().click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator_confirm_button)) # ждём кликабельную кнопку "Подтвердить"
    reg_page.code_field().send_keys('1111')
    reg_page.confirm_button().click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator_ok_button)) # ждём кликабельную кнопку "Ок"
    reg_page.ok_button().click()

    # Проверяем, что баннер на главной странице после регистрации отображается (Проверка видимости элемента)
    banner_element = browser.find_element(By.CLASS_NAME, 'promo-2')
    assert banner_element.is_displayed()
