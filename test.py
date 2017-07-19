
from sparx.preprocess import Process
from sparx.preprocess import *
from geopy.geocoders import Nominatim

import pandas as pd
import numpy as np

data = pd.read_csv('data/iris.csv')

p = Process()

print p.count_missing(data['Species'])
print p.is_categorical(data['Species'])

print p.get_version()
print p.geocode("172 5th Avenue NYC")

print p.unique_value_count(data)

print p.unique_identifier(data)
