"""Tests for the cleaning module"""
from unittest.mock import patch
import pandas as pd


from life_expectancy.main import main
from life_expectancy.country import Country



@patch("life_expectancy.main.load_data", autospec=True)
@patch("life_expectancy.main.save_data", autospec=True)
def test_main(
    mock_save_data, mock_load_data, pt_life_expectancy_expected, input_dataframe_test_csv
):
    """Run the `clean_data` function and compare the output to the expected output"""
    mock_load_data.return_value = (input_dataframe_test_csv, "csv")
    mock_save_data.return_value = pt_life_expectancy_expected
    pt_life_expectancy_obtained = main("dummy_file_intro", "dummy_file_out", Country.PT)
    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained, pt_life_expectancy_expected
    )
