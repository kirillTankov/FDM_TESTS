from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature('Закрытие попапа с городами')
def test_close_popup(browser):
    popup = BasePage(browser)
    with allure.step('Открываем страницу'):
        popup.browser.get('https://allfdm.ru/')
    popup.close_popup()
    WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.ID, 'select-city-modal-form'))) # Ожидаем когда элемент станет невидидмым
    assert not popup.find((By.ID, 'select-city-modal-form')).is_displayed()
