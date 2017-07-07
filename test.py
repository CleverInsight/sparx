from sparx.preprocess import *
# import pandas as pd


# data = pd.read_csv('/Users/bastinrobins/Downloads/vehicles.read_csv')

# print auto_clean(data.head(100), 'c240bDscr')

p = process()

a = "march/1/1980"

result = p.datestring_to_dd_mm_yy(a)

print result