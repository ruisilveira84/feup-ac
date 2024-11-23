import pandas as pd
import read_data as rd

def select_data():
    pass

def remove_nulls(tables: dict[str, pd.DataFrame]):
    tables = rd.remove_null_entries(tables)
    rd.print_null_fields(tables)

    return tables

def remove_outliers():
    pass

def normalise_data():
    pass

def prepare_data(tables: dict[str, pd.DataFrame]):
    select_data()
    tables = remove_nulls(tables) #TODO add some criteria to remove nulls, not every null, maybe set a default to replace
    remove_outliers() #identify outliers correctly ()
    normalise_data()
    return tables

def add_features(teams):
    """
    Adds new features to the teams dataset:
    - win_rate: Ratio of games won to total games played.
    - point_balance: Ratio of offensive to defensive points.

    Args:
        teams (pd.DataFrame): The teams dataset.

    Returns:
        pd.DataFrame: Dataset with added features.
    """
    teams["win_rate"] = teams["won"] / teams["GP"]
    teams["point_balance"] = teams["o_pts"] / teams["d_pts"]
    return teams
