from pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_promotions(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.close_popup()
    main_page.scroll_to_promotion()
    main_page.go_to_promotion_page()

    photo_element = browser.find_element(By.CLASS_NAME, 'promotion-image')

    assert photo_element.is_displayed()


