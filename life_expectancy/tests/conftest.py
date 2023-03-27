"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR


@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def input_dataframe_test_csv() -> pd.DataFrame:
    """Fixture to load the input of the cleaning script for a csv file"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw_testing.tsv", sep="\t")

@pytest.fixture(scope="session")
def input_dataframe_test_json() -> pd.DataFrame:
    """Fixture to load the input of the cleaning script for a json file"""
    return pd.read_json(FIXTURES_DIR / "eurostat_life_expect.json")

@pytest.fixture(scope="session")
def output_expected_country_list() -> pd.DataFrame:
    """Fixture to loads the expected correct list of the input countries"""
    return pd.read_csv(FIXTURES_DIR / "country_list_expected.csv").iloc[:,0].values.tolist()
