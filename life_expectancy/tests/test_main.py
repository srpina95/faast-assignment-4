"""Tests for the cleaning module"""
import pandas as pd
from unittest.mock import patch


from life_expectancy.main import main

# def test_clean_data(pt_life_expectancy_expected, input_path_for_testing):
#     """Run the `clean_data` function and compare the output to the expected output"""
#     with mock.patch("pandas.DataFrame.to_csv") as to_csv_mock:

#         #save_data(dataframe = clean_data(load_data(file_path=input_path_for_testing)), file_path = OUTPUT_DIR / "pt_life_expectancy.csv" )
#         pt_life_expectancy_actual = to_csv_mock.assert_called_with(OUTPUT_DIR / "pt_life_expectancy.csv")
#     pd.testing.assert_frame_equal(pt_life_expectancy_actual, pt_life_expectancy_expected)


@patch("life_expectancy.main.load_data", autospec=True)
@patch("life_expectancy.main.save_data", autospec=True)
def test_main(
    mock_save_data, mock_load_data, pt_life_expectancy_expected, input_dataframe_test
):
    """Run the `clean_data` function and compare the output to the expected output"""
    mock_load_data.return_value = input_dataframe_test
    mock_save_data.return_value = pt_life_expectancy_expected
    pt_life_expectancy_obtained = main("dummy_file_intro", "dummy_file_out", "PT")
    pd.testing.assert_frame_equal(
        pt_life_expectancy_obtained, pt_life_expectancy_expected
    )
