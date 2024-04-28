from pages.main_page import MainPage


def test_redirect(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.close_popup()

    factories_to_check = ['mebelkor', 'kedr', ]


    assert '/factory/select-factory' in browser.current_url

    '''for factory in factories:
        factory.click()

        assert '/factory/select-factory' in browser.current_url'''
# factories = main_page.factories()
