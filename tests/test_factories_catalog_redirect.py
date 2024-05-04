from pages.main_page import MainPage


def test_redirect(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.close_popup()

    factories_to_check = [
        'mebelkor', 'kedr', 'standart', 'fasady-chernozemya', 'art-studiya-12', 'fabriche_rus', 'fasaddor',
        'orvud', 'mebel-holding', 'lotosyug', 'dreviz', 'palazzo', 'fasadel', 'hameleon', 'lores', 'DESKOR',
        'vhc', 'bora-fasad', 'ornament', 'sybirskie-meb-fas', 'laminatrus', 'adelkreis', 'tmf'
    ]

    for factory_name in factories_to_check:
        main_page.go_to_factory_page(factory_name)

        assert f'/factory/select-factory/{factory_name}' in browser.current_url

        main_page.go_to_main_page()

    '''factory_name = 'mebelkor'  # Выберите фабрику для проверки

    main_page.go_to_factory_page(factory_name)
    
    assert f'/factory/select-factory/{factory_name}' in browser.current_url
    
    main_page.go_to_main_page()''' # Здесь код для проверки лишь одной фабрики


