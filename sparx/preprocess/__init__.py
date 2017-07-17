"""
    Module: Machine Learning Models
    Project: Sparx
    Authors: Bastin Robins. J
    Email : robin@cleverinsight.com
"""
import numpy as np
import pandas as pd
from urllib import urlencode
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler




class process:

	def __init__(self):
		self.version = "0.0.1"

    def dict_query_string(self, query_dict):
        ''' Return a string which is the query formed using the given dictionary
        as parameter

        Parameters
        ----------
            query_dict: Dict
                Dictionary of keys and values


        Usage
        -----
            # Input query string
            query = {'name': 'Sam', 'age': 20 }

            p = process()
            p.dict_query_string(query)
            >> name=Same&age=20
        '''

        return urlencode(query_dict)


    def describe(self, df, col_name):

        try:
            return {
                'min': df[col_name].min(),
                'max': df[col_name].max(),
                'mean': df[col_name].mean(),
                'median': df[col_name].median()
            }
        except Exception as e:
            return 'Datatype not supported'

    def encode(self, data):
        ''' Return a clean dataframe which is initially converted into utf8 format
        and all categorical variables are converted into numeric labels also each
        label encoding classes as saved into a dictionary now a tuple of first
        element is dataframe and second is the hash_map

        Parameters:
        ------------
            data : pandas dataframe


        Usage:
        ------
            >> p = process()
            >> p.encode(pd.DataFrame())


        '''
        # Remove all the ascii unicodes
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

        # Instantiate the LabelEncoder instance
        le = LabelEncoder()

        # One shot hot encoding if its categorical variable
        hash_map = {}
        date_columns = []
        for col in data.columns:
            if data[col].dtypes == 'object':
                hash_map[col] = dict(zip(le.fit_transform(data[col].unique()),\
                 data[col].unique()))
                le.fit(data[col].values)
                data[col]=le.transform(data[col])

        return (data, hash_map)


def auto_clean(dataframe, target=None, label_encode=True, scale=True, ohe=True, impute=True, auto=True, exclude=[]):
	'''
    Returns a tuple which consist of X - Features, Y - Target, Report
    which is gives the parameters passed to the function

    Parameters
    ----------
    	dataframe : Dataframes
        	pandas dataframes to be given as input
        target : str
        	Response value to predict(col name)
        label_encode: boolean
        	True (default) - Label Encode categorical variable to int64
        scale : boolean
        	True (default) - Reduce the dimension of the given vector array
        ohe: boolean
        	True (default) - One hot encoding of variables
        impute: boolean
        	True (default) - Impute the missing value using mean, median or std
        auto: str
        	True (default) - Make all decision automatically bypass all parameters
        	to true
        exclude: list
        	List of column names which needs to be removed before operation

    Examples
    --------
    Usage:
        dataframe : Dataframes
        	pd.Dataframe(['Curd ', 'GOOG APPL MS', 'A B C', 'T Test is'])
        target : str
        	Response value to predict(col name)
        label_encode: boolean
        	True (default) - Label Encode categorical variable to int64
        scale : boolean
        	True (default) - Reduce the dimension of the given vector array
        ohe: boolean
        	True (default) - One hot encoding of variables
        impute: boolean
        	True (default) - Impute the missing value using mean, median or std
        auto: str
        	True (default) - Make all decision automatically bypass all parameters
        	to true
        exclude: list
        	List of column names which needs to be removed before operation

	'''

	df_copy = dataframe.copy()


	if label_encode:
		dataframe = dataframe.apply(LabelEncoder().fit_transform)

	Y = dataframe.pop(target)
	X = dataframe




	return {
		'features' : dataframe.head(),
		'target': target
	}
