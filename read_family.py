"""
Author: Surrin1999
Date: 2021-12-08
"""
import pandas as pd


def read(id):
    self_family_data = pd.read_csv('self_family.csv')
    return float(self_family_data.loc[id - 1, 'family'])
