import pytest
from src.pom.tests.Testbase import BaseTest


class TestCountryPage(BaseTest):
    # Class automatically manage a tearUp and tearDown

    @pytest.mark.smoke
    def test_validate_logo(self):
        """
        Given I'm on the Select Country Page
        Then I expect to see the logo of the company
        """
        assert self.country_page.logo_is_displayed() == True

    def test_validate_country_list(self):
        """
        Given I'm on the Select Country Page
        Then I expect to see a list of countries
        And the list of  must have 18 elements
        And <Uruguay> and <Chile> are in the list
        """
        assert self.country_page.all_countries_displayed()
        assert self.country_page.get_country_list_count() == 18
        assert "Uruguay" and "Chile" in self.country_page.get_country_list_text()

    @pytest.mark.parametrize('initials, country', [('UY', 'Uruguay'), ('CL', 'Chile')])
    def test_validate_link_to_country_works(self, initials, country):
        """
        Given I amm on the Select Country Page
        When I select a Country
        Then I must be redirected to the Home Page of <country>
        """
        self.country_page.select_country(initials)
        assert country in self.country_page.get_title()
