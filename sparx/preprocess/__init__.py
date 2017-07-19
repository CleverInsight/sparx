"""
    Module: Machine Learning Models
    Project: Sparx
    Authors: Bastin Robins. J
    Email : robin@cleverinsight.com
"""
from urllib import urlencode
import logging
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sparx.preprocess import Process

class Process:

    def __init__(self):
        self.version = "0.0.1"
        
    def impute(self, df, strategy='mean'):

        im = Imputer(strategy='mean')
        im.fit(df)
        return im.transform(df.values)

'''<<<<<<< HEAD'''
    @staticmethod
    def count_Nan(col_name):
        return col_name.isnull().sum()

class Process(object):
    ''' Process class consist for best micro-level preprocessing
    methods helps to clean the dataset passed as dataframes
    '''

    def __init__(self):
        self.version = "0.0.1"

    @staticmethod
    def is_categorical(dataframe):
        ''' comment '''
        if dataframe.dtypes == 'object':
            return True
        else:
            return False
        

    @staticmethod
    def dict_query_string(query_dict):
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

            p = Process()
            p.dict_query_string(query)
            >> name=Same&age=20
        '''

        return urlencode(query_dict)

    @staticmethod
    def describe(dataframe, col_name):
        ''' Return the basic description of an column in a pandas dataframe
        check if the column is an interger or float type

        Parameters:
        -----------
            dataframe: pandas dataframe
            col_name: str
                any one column name in the dataframe passed
        Usage:
        ------
            >> p = Process()
            >> p.describe(dataframe, 'Amount')
            >> {'min': 0, 'max': 100, 'mean': 50, 'median': 49 }

        '''

        try:
            return dict(min=dataframe[col_name].min(), max=dataframe[col_name].max(),\
             mean=dataframe[col_name].mean(), median=dataframe[col_name].median())

        except Exception as e:
            logging.exception(e)

    @staticmethod
    def encode(data):
        ''' Return a clean dataframe which is initially converted into utf8 format
        and all categorical variables are converted into numeric labels also each
        label encoding classes as saved into a dictionary now a tuple of first
        element is dataframe and second is the hash_map

        Parameters:
        ------------
            data : pandas dataframe

        Usage:
        ------
            >> p = Process()
            >> p.encode(pd.DataFrame())

        '''
        # Remove all the ascii unicodes
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

        # Instantiate the LabelEncoder instance
        label = LabelEncoder()

        # One shot hot encoding if its categorical variable
        hash_map = {}
        date_columns = []
        for col in data.columns:
            if data[col].dtypes == 'object':
                hash_map[col] = dict(zip(label.fit_transform(data[col].unique()),\
                 data[col].unique()))
                label.fit(data[col].values)
                data[col] = label.transform(data[col])

        return (data, hash_map)

    @staticmethod
    def impute(dataframe, col_name, statergy='mean'):
        ''' Return a dataframe which is complete imputed with respective
        column mean value

        Parameters:
        -----------
            dataframe : pandas.core.dataframe
            col_name : str
                column name to select for impute in dataframe
            statergy : str default('mean') mean, median, min, max, std
                Statergy to impute the given column

        Usage:

            >> p = Process()
            >> p.impute(dataframe, 'Age')
        '''

        return dataframe
>>>>>>> 808546fe7b50bfc73cbd8b4fdcbb0476b9d02214
