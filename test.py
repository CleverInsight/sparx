'''function to count the missing values in columns'''
from sparx.preprocess import Process
import pandas as pd
import numpy as np

'''<<<<<<< HEAD'''
DATA = pd.read_csv('data.csv')
P = Process()
print P.count_Nan(DATA['name'])
'''=======

data = pd.read_csv('data/iris.csv')

# Encode the dataframe and give the label encoded

p = Process()

print p.is_categorical(data['Species'])
>>>>>>> 808546fe7b50bfc73cbd8b4fdcbb0476b9d02214'''
