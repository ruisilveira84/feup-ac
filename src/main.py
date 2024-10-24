import read_data as rd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

if __name__ == "__main__":
    tables = rd.read_data()

    prepared_tables = prepare_data(tables)
    #feed a model year by year
    #make a prediction
