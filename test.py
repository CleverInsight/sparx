from sparx.preprocess import *
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')

# data = pd.read_csv('/Users/bastinrobins/Downloads/vehicles.read_csv')

# print auto_clean(data.head(100), 'c240bDscr')

p = Process()

print p.get_version()
print p.geocode("172 5th Avenue NYC")

#print p.unique_value_count(data['name'])
print p.unique_value_count(data)

print p.unique_identifier(data)
