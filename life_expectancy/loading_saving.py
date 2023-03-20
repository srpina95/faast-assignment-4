"""Module with the functions associated to saving and loading the dataframes from a given path"""
from pathlib import Path
import zipfile
from functools import partial
import pandas as pd


CURRENT_FILEPATH = Path(__file__).parent.resolve()

#Dict of functions to read the input file.
#If a new type of file is to be read, it should be added here
load_function_to_apply = {
    ".csv": partial(pd.read_csv, sep=","),
    ".tsv": partial(pd.read_csv, sep="\t"),
    ".json": pd.read_json
}

def load_data(file_path: Path):
    """
    This function loads a file given a file path.
    It can load files of the type (.csv, .tsv, .json).
    The function is prepared to unzzip a file if it is compressed

    :param file_path: File path to the file
    :returns: pandas dataFrame loaded from file
    :returns: suffix of the loaded file
    """

    if file_path.suffix == ".zip":
        file_path = unzipper(file_path)

    loaded_dataframe = load_function_to_apply[file_path.suffix](file_path)

    return loaded_dataframe, file_path.suffix


def save_data(dataframe: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """
    This function saves a dataframe into a specified filepath

    param: dataframe: Dataframe to be stored
    param: file_path: filepath on which to store the file

    output: file_path:  Return the stored dataframe
    """

    dataframe.to_csv(file_path, index=False)

    return dataframe



def unzipper(file_path: Path):
    """
    This function unzips the zip file with the input data if it exists

    param: file_path: Path to the zip file

    output: file_path:  filepath of the file unzipped
    """

    with zipfile.ZipFile(file_path, 'r') as zip_file:
        filename = zip_file.namelist()[0]
        extracted_file_path = Path(zip_file.extract(filename, file_path.parent))

    return extracted_file_path
