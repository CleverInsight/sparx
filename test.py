'''function to count the missing values in columns'''
from sparx.preprocess import Process
import pandas as pd
import numpy as np

data = pd.read_csv('data/iris.csv')

p = Process()
print p.count_Nan(data['Species'])
print p.is_categorical(data['Species'])
