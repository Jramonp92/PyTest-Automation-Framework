from selenium.webdriver.common.by import By

from src.pom.pages.base_page import BasePageElement


class ResultsPage(BasePageElement):

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_BOX = (By.XPATH, "//input[contains(@class,'nav-search-input')]")
    RESULTS_CARDS = (By.CLASS_NAME, "ui-search-result__wrapper")
    PRODUCT_TITLE = (By.CLASS_NAME, "ui-search-item__group--title")

    def get_products_list_title_text(self):
        WebElements: object = self.find_multiple_elements(self.PRODUCT_TITLE)
        Cards = []
        for element in WebElements:
            Cards.append(element.get_attribute("innerText"))
        return Cards

    def Search_product_in_list(self, searchTerm):
        productLists = self.get_products_list_title_text()
        counter = 0
        for elem in productLists:
            if elem.find(searchTerm) != -1:
                counter = counter + 1
        try:
            relevant = counter > 25
        except:
            print("No hay mas de esos elementos")
        return relevant
