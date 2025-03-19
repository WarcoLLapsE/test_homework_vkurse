from selenium.webdriver.common.by import By

MAIN_STORE_LINK = 'https://fakeapi.platzi.com/'
PRODUCTS_API_LINK = 'https://api.escuelajs.co/api/v1/products'
SEARCH_BOX_BUTTON = '.astro-kmkmnagf.astro-v37mnknz>button'
SEARCH_BOX_FIELD = '.pagefind-ui__search-input'
SEARCH_RESULTS_BOX = '.pagefind-ui__results'
PRODUCT_NAME = 'section:nth-child(1) > div > article:nth-child(5) > h4'
PRODUCT_PRICE = 'section:nth-child(1) > div > article:nth-child(5) > p'
search_box_locator = (By.CSS_SELECTOR, SEARCH_BOX_FIELD)
dropdown_locator = (By.CSS_SELECTOR, SEARCH_RESULTS_BOX)
