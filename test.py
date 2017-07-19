from sparx.preprocess import *
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

data = pd.read_csv('data/iris.csv')

# Encode the dataframe and give the label encoded

p = Process()

print p.is_categorical(data['Species'])


print p.get_version()
print p.geocode("172 5th Avenue NYC")

#print p.unique_value_count(data['name'])
print p.unique_value_count(data)

print p.unique_identifier(data)
