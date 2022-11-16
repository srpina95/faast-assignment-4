# pylint: disable=line-too-long
"""import of libraries"""
from pathlib import Path
import argparse
import pandas as pd

CURRENT_FILEPATH = Path(__file__).parent.resolve()

def load_data(file_path=CURRENT_FILEPATH / "data" / "eu_life_expectancy_raw.tsv"):
    """
    This function loads a file given a file path

    :param filePath: File path to the file
    :returns: pandas dataFrame loaded from file
    """

    loaded_dataframe = pd.read_csv(file_path, sep='\t')

    return loaded_dataframe

def clean_data(eu_life_expectancy_raw_wide, country="PT"):
    """
    This function  cleans and prepares the dataframe in order to be stored as required:

    param: euLifeExpectancyRawWide: dataFrame loaded previously in wide form directly from file
    param: country: country code to filter the data (default = PT)

    return: euLifeExpectancyClean: dataframe filtered and cleaned, ready to be stored
    """

    eu_life_expectancy_raw_long = \
    pd.melt(eu_life_expectancy_raw_wide, id_vars=eu_life_expectancy_raw_wide.columns[0], var_name="year")

    eu_life_expectancy_clean =eu_life_expectancy_raw_long[eu_life_expectancy_raw_long.columns[0]]\
        .str.split(',', expand=True)\
            .set_axis(eu_life_expectancy_raw_long.columns[0].split(','),axis='columns')\
                .join(eu_life_expectancy_raw_long)\
                    .drop(columns = eu_life_expectancy_raw_long.columns[0])

    eu_life_expectancy_clean["value"]= eu_life_expectancy_clean["value"]\
        .str.extract(r'(\d+.\d+)')
    eu_life_expectancy_clean.rename(columns={"geo\\time": "region"}, inplace=True)

    eu_life_expectancy_clean["value"]= eu_life_expectancy_clean["value"].astype('float')
    eu_life_expectancy_clean["year"]=eu_life_expectancy_clean["year"].astype("int")

    eu_life_expectancy_clean.dropna(axis=0, inplace=True)

    eu_life_expectancy_clean = eu_life_expectancy_clean[eu_life_expectancy_clean["region"]==country]

    return eu_life_expectancy_clean

def save_data(dataframe, file_path = CURRENT_FILEPATH /"data" / "pt_life_expectancy.csv"):
    """
    This function saves a dataframe into a specified filepath

    param: dataFrame: Dataframe to be stored
    param: file_path: filepath on which to store the file
    """

    dataframe.to_csv(file_path, index=False)


if __name__=="__main__": # pragma: no cover
    parser = argparse.ArgumentParser(description='main function for your library')
    parser.add_argument('--country',
                        type=str,
                        required=False,
                        default="PT",
                        help='country code on which to focus')
    parser.add_argument('--input_file_name',
                        type=str,
                        required=False,
                        default="eu_life_expectancy_raw.tsv",
                        help='file name of the input file')
    parser.add_argument('--output_file_name',
                    type=str,
                    required=False,
                    default="eu_life_expectancy_raw.csv",
                    help='file name of the output file')
    args = parser.parse_args()

    input_data_path = CURRENT_FILEPATH / "data" / args.input_file_name
    output_data_path = CURRENT_FILEPATH / "data" / args.output_file_name


    eu_life_expectancy_raw = load_data(input_data_path)
    eu_life_expectancy_filtered = clean_data(eu_life_expectancy_raw, country=args.country)
    save_data(eu_life_expectancy_filtered, output_data_path)
