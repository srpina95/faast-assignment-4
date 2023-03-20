"""Tests script for the loading_saving module"""
from unittest.mock import patch
import pandas as pd

from life_expectancy.loading_saving import load_data, save_data
from . import FIXTURES_DIR


def test_load_data_csv(input_dataframe_test_csv):
    """Test function to assert the load_data function loads what is suposed from the csv"""
    loaded_data_frame, file_type = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_testing.tsv")

    pd.testing.assert_frame_equal(loaded_data_frame, input_dataframe_test_csv)
    assert file_type in (".csv", ".tsv")

def test_load_data_json(input_dataframe_test_json):
    """Test function to assert the load_data function loads what is suposed from the json file"""
    loaded_data_frame, file_type = load_data(FIXTURES_DIR / "eurostat_life_expect.json")

    pd.testing.assert_frame_equal(loaded_data_frame, input_dataframe_test_json)
    assert file_type in (".json")


@patch("life_expectancy.loading_saving.pd.DataFrame.to_csv", autospec=True)
def test_save_data(mock_to_csv) -> None:
    """Test function to assert the save_data function calls the to_csv function as is suposed"""
    fake_df = pd.DataFrame({"a": [1, 2]})
    fake_path = "Dummy.csv"

    print_msg = "to_csv was called"
    mock_to_csv.side_effect = print(print_msg, end="")

    save_data(fake_df, fake_path)
    mock_to_csv.assert_called_with(fake_df, fake_path, index=False)
