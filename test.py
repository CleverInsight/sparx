'''function to count the missing values in columns'''
from sparx.preprocess import Process
import pandas as pd
import numpy as np

DATA = pd.read_csv('data.csv')
P = Process()
print P.count_Nan(DATA['name'])
