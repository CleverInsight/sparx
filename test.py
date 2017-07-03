from sparx.preprocess import  *
#import pandas as pd


#data = pd.read_csv('/Users/bastinrobins/Downloads/vehicles.read_csv')

#print auto_clean(data.head(100), 'c240bDscr')

p = process()
print p.string_concat("Hello", "World")


print process.get_full_name("Bastin", "Robins")