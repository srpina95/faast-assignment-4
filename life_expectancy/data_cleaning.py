import pandas as pd


def clean_data(df_raw_wide: pd.DataFrame, country: str = "PT") -> pd.DataFrame:
    """
    This function  cleans and prepares the dataframe in order to be stored as required:

    param: df_raw_wide: dataFrame loaded previously in wide form directly from file
    param: country: country code to filter the data (default = PT)

    return: dataframe filtered and cleaned, ready to be stored
    """

    df_raw_long = pd.melt(df_raw_wide, id_vars=df_raw_wide.columns[0], var_name="year")

    df_clean = (
        df_raw_long[df_raw_long.columns[0]]
        .str.split(",", expand=True)
        .set_axis(df_raw_long.columns[0].split(","), axis="columns")
        .join(df_raw_long)
        .drop(columns=df_raw_long.columns[0])
    )

    df_clean["value"] = df_clean["value"].str.extract(r"(\d+.\d+)")
    df_clean.rename(columns={"geo\\time": "region"}, inplace=True)

    df_clean["value"] = df_clean["value"].astype("float")
    df_clean["year"] = df_clean["year"].astype("int")

    df_clean.dropna(axis=0, inplace=True)

    df_clean = df_clean[df_clean["region"] == country]

    df_clean.reset_index(inplace=True, drop=True)

    return df_clean
