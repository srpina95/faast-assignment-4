import pandas as pd

from life_expectancy.loading_saving import load_data
from . import FIXTURES_DIR, OUTPUT_DIR


def test_load_data(input_dataframe_test):
    loaded_data_frame = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_testing.tsv")
    
    pd.testing.assert_frame_equal(loaded_data_frame, input_dataframe_test)