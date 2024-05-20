from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.catalog_page import FacadePvhKedrPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

