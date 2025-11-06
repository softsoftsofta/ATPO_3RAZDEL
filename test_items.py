def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # проверка наличия кнопки добавления в корзину
    add_to_basket_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    
    # assert что кнопка есть на странице
    assert len(add_to_basket_button) > 0, "Add to basket button is not presented"
