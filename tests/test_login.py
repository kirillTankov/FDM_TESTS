from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(browser):
    login = BasePage(browser)
    login.browser.get('https://dev.allfdm.ru/')
    login.close_popup()
    login.login()

    out_is_displayed = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Выход")]')))
    assert out_is_displayed.is_displayed()

