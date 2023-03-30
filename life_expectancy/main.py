# pylint: disable=locally-disabled, multiple-statements, W0621
"""Main file of the loading, cleaning and saving process"""
from pathlib import Path
import argparse
import pandas as pd

from life_expectancy.loading_saving import save_data, load_data
from life_expectancy.data_cleaning import clean_data_csv, clean_data_json
from life_expectancy.country import Country


CURRENT_FILEPATH = Path(__file__).parent.resolve()

clean_function_to_apply = {
    ".csv": clean_data_csv,
    ".tsv": clean_data_csv,
    ".json": clean_data_json
    }

def main(input_data_path: Path, output_data_path: Path, country: str) -> pd.DataFrame:
    """main function: ....."""
    eu_life_expectancy_raw = load_data(input_data_path)
    eu_life_expectancy_filtered = clean_data(eu_life_expectancy_raw, country=country)
    save_data(eu_life_expectancy_filtered, output_data_path)
    
    return eu_life_expectancy_filtered

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="main function for your library")
    parser.add_argument(
        "--country",
        type=str,
        required=False,
        default="PT",
        help="country code on which to focus",
    )
    parser.add_argument(
        "--input_file_name",
        type=Path,
        required=False,
        help="file name of the input file",
    )
    parser.add_argument(
        "--output_file_name",
        type=Path,
        required=False,
        default="eu_life_expectancy_cleaned.csv",
        help="file name of the output file",
    )
    args = parser.parse_args()

    #input_data_path = CURRENT_FILEPATH / "data" / args.input_file_name
    output_data_path = CURRENT_FILEPATH / "data" / args.output_file_name

    #main(input_data_path, output_data_path, args.country)
    main(Path("life_expectancy/data/eurostat_life_expect.zip"), \
         output_data_path, Country[args.country])
