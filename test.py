from sparx.preprocess import  *
import pandas as pd


data = pd.read_csv('data.csv')

#print auto_clean(data.head(100), 'c240bDscr')

p = process()
print p.impute(data['marks'])
