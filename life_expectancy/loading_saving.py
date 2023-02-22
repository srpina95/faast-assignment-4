"""Module with the functions associated to saving and loading the dataframes from a given path"""
from pathlib import Path
import pandas as pd

CURRENT_FILEPATH = Path(__file__).parent.resolve()


def load_data(file_path: Path) -> pd.DataFrame:
    """
    This function loads a file given a file path

    :param file_path: File path to the file
    :returns: pandas dataFrame loaded from file
    """

    loaded_dataframe = pd.read_csv(file_path, sep="\t")

    return loaded_dataframe


def save_data(dataframe: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """
    This function saves a dataframe into a specified filepath

    param: dataframe: Dataframe to be stored
    param: file_path: filepath on which to store the file
    """

    dataframe.to_csv(file_path, index=False)

    return dataframe
