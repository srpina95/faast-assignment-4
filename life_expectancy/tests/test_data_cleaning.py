"""Test module to test the funcion inside the data_cleaning module"""
import pandas as pd

from life_expectancy.data_cleaning import clean_data


def test_clean_data(pt_life_expectancy_expected, input_dataframe_test):
    """Test function to assert the cleaning function"""
    pt_life_expectancy_obtained = clean_data(input_dataframe_test)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained, pt_life_expectancy_expected
    )
