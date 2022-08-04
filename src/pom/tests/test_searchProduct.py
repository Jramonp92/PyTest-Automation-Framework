import pytest

from src.pom.tests.Testbase import BaseTest

@pytest.mark.smoke
class TestSearch(BaseTest):
    # Class automatically manage a tearUp and tearDown

    @pytest.mark.parametrize('searchTerm', ['Harry Potter', 'Pokemon'])
    def test_search_product(self, searchTerm):
        """
        Given I'm on the Home Page
        When I make a search for a product
        Then I must be redirected to the results page
        And the result page title must contain the <search term>
        And the result page must contain at least 50% coincidences with the <search term>
        """

        self.country_page.open_page('https://www.mercadolibre.com.uy')
        self.home_page.search_a_product(searchTerm)
        assert searchTerm in self.home_page.get_title()
        assert self.results_page.Search_product_in_list(searchTerm)

