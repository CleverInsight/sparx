"""
    Module: Machine Learning Models
    Project: Sparx
    Authors: Bastin Robins. J
    Email : robin@cleverinsight.com
"""
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler



def auto_clean(dataframe, target=None, preprocess=True, scale=True, ohe=True):

	""" Pick the dataframe and split it into features and target

		- Convert categorical to labels
		- Convert integers to labels
		- Scale the data
		- Onehotencoding is performed

	return
		(X, Y, report)
	"""
	
	pass