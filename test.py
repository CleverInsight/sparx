from sparx.preprocess import *
import pandas as pd


data = pd.read_csv('/Users/bastinrobins/Downloads/vehicles.read_csv')

print auto_clean(data.head(100), 'c240bDscr')
