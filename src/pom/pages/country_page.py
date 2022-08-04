from selenium.webdriver.common.by import By
from src.pom.pages.base_page import BasePageElement
from src.pom.pages.home_page import HomePage


class CountryPage(BasePageElement):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGO = (By.CLASS_NAME, "ml-logo-es")
    COUNTRY_LIST = (By.XPATH, "//li[contains(@class,'ml-site')]")

    def logo_is_displayed(self):
        return self.is_displayed(self.COUNTRY_LIST)

    def get_country_list_text(self):
        WebElements = self.find_multiple_elements(self.COUNTRY_LIST)
        Countries = []
        for element in WebElements:
            Countries.append(element.get_attribute("innerText"))
        return Countries

    def get_country_list_count(self):
        return self.get_count_elements(self.COUNTRY_LIST)

    def all_countries_displayed(self):
        WebElements = self.find_multiple_elements(self.COUNTRY_LIST)
        for element in WebElements:
            return element.is_displayed()

    def select_country(self, country):
        self.click((By.ID, country))
