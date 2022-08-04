from selenium.webdriver.common.by import By
from src.pom.pages.base_page import BasePageElement


class HomePage(BasePageElement):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_BOX = (By.XPATH, "//input[contains(@class,'nav-search-input')]")
    SEARCH_BUTTON = (By.CLASS_NAME, "nav-search-btn")

    def search_a_product(self, product):
        self.send_keys(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BUTTON)




