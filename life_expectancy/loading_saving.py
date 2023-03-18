"""Module with the functions associated to saving and loading the dataframes from a given path"""
from pathlib import Path
import os
import zipfile
from functools import partial
import pandas as pd


CURRENT_FILEPATH = Path(__file__).parent.resolve()


def load_data(file_path: Path):
    """
    This function loads a file given a file path

    :param file_path: File path to the file
    :returns: pandas dataFrame loaded from file
    """

    filetype = str(file_path).rsplit('.', maxsplit=1)[-1]
    if filetype == "zip":
        file_path, filetype = unzipper(file_path)

    load_function_to_apply = {
        "csv": partial(pd.read_csv, sep=","),
        "tsv": partial(pd.read_csv, sep="\t"),
        "json": pd.read_json
    }

    loaded_dataframe = load_function_to_apply[filetype](file_path)

    return loaded_dataframe, filetype


def save_data(dataframe: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """
    This function saves a dataframe into a specified filepath

    param: dataframe: Dataframe to be stored
    param: file_path: filepath on which to store the file
    """

    dataframe.to_csv(file_path, index=False)

    return dataframe



def unzipper(file_path: Path):
    """
    This function unzips the zip file with the input data if it exists

    param: file_path: Path to the zip file

    output: file_path:  filepath of the file unzipped
    output: filetype:   filetype of the unziped file
    """

    with zipfile.ZipFile(file_path, 'r') as zip_file:
        filename = zip_file.namelist()[0]
        zip_file.extract(filename, os.path.split(os.path.abspath(file_path))[0])
    file_path = os.path.split(os.path.abspath(file_path))[0]+ "/" + filename
    filetype = file_path.split(".")[-1]

    return file_path, filetype
