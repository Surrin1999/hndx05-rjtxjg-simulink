import pandas as pd


def read(id):
    heart_data = pd.read_csv('heart.csv')
    return float(heart_data.loc[id - 1, 'exang'])
