"""
module that tests the class function created in the country enum
"""
from life_expectancy.country import Country

def test_country_list(output_expected_country_list):
    """Test function to assert the valid countries output list"""

    assert output_expected_country_list == Country.clean_countries_list()
