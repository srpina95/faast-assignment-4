"""Test module to test the funcion inside the data_cleaning module"""
import pandas as pd

from life_expectancy.data_cleaning import clean_data_csv, clean_data_json


def test_clean_data_csv(pt_life_expectancy_expected, input_dataframe_test_csv):
    """Test function to assert the cleaning function from csv file"""
    pt_life_expectancy_obtained = clean_data_csv(input_dataframe_test_csv, country="PT")

    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained, pt_life_expectancy_expected
    )

def test_clean_data_json(pt_life_expectancy_expected, input_dataframe_test_json):
    """Test function to assert the cleaning function from json file"""
    pt_life_expectancy_obtained = clean_data_json(input_dataframe_test_json, country="PT")

    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained, pt_life_expectancy_expected
    )
