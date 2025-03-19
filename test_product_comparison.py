from selenium.webdriver.common.by import By

from locators import *


def test_fake_product_search(random_fake_product, browser, select_option_by_partial_text):
    browser.get(MAIN_STORE_LINK)
    search_box_main = browser.find_element(By.CSS_SELECTOR, SEARCH_BOX_BUTTON)
    search_box_main.click()
    browser.implicitly_wait(2)
    select_option_by_partial_text(search_box_locator, dropdown_locator, "Classic")

    ### Считаем, что поиск произошел. После поиска отобразился выбранный товар на главной странице ###

    product_name = browser.find_element(By.CSS_SELECTOR, PRODUCT_NAME).text
    product_price = browser.find_element(By.CSS_SELECTOR, PRODUCT_PRICE).text

    assert random_fake_product['title'] == product_name
    assert str(random_fake_product['price']) == product_price[1:]
