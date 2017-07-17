from sparx.preprocess import *
import pandas as pd


data = pd.read_csv('data/iris.csv')

# Encode the dataframe and give the label encoded

p = Process()

a = p.encode(data)

print a
print type(a)
