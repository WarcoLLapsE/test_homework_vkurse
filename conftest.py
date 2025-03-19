import pytest
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import *


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def fake_products():
    response = requests.get(PRODUCTS_API_LINK)
    return response.json()


@pytest.fixture
def random_fake_product(fake_products):
    filtered_products = [product for product in fake_products if product["price"] > 60
                         and product['title'].startswith('Classic Black')]
    return random.choice(filtered_products)


@pytest.fixture
def select_option_by_partial_text(browser):
    def _select_option_by_partial_text(search_box_locator, dropdown_locator, partial_text):
        search_box = browser.find_element(*search_box_locator)
        search_box.send_keys(partial_text)
        wait = WebDriverWait(browser, 10)
        dropdown = wait.until(EC.visibility_of_element_located(dropdown_locator))
        options = dropdown.find_elements(By.TAG_NAME, "li")
        for option in options:
            if partial_text in option.text:
                option.click()
                return option
        raise ValueError(f"Элемент с текстом, содержащим '{partial_text}', не найден.")

    return _select_option_by_partial_text
