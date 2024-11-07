import read_data as rd
import process_data as pd
import model_training as mt
#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

if __name__ == "__main__":
    tables = rd.read_data()

    prepared_tables = pd.prepare_data(tables)
    #create model
    model = mt.train_model(prepared_tables)
    #feed a model year by year
    #make a prediction
