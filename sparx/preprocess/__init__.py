"""
    Module: Machine Learning Models
    Project: Sparx
    Authors: Bastin Robins. J
    Email : robin@cleverinsight.com
"""
from datetime import datetime
from urllib import urlencode
import logging
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
import dateutil.parser as parser
from geopy.geocoders import Nominatim


class Process(object):

    ''' Process class consist for best micro-level preprocessing
    methods helps to clean the dataset passed as dataframes
    '''

    def __init__(self):
        self.version = "0.0.1"

    @staticmethod
    def geocode(address):
        ''' Return full address, latitude and longitude of give address string

        Parameters:
        -----------
            address: str
                Enter a dictionary of address whose latitude and longitude
                should be returned

        Usage:
        ------
            >> p = preprocess()
            >> p.geocode("172 5th Avenue NYC")
            >> {'latitude': 40.74111015, 'adress': u'172, 5th Avenue, Flatiron,
             Manhattan, Manhattan Community Board 5, New York County, NYC,
             New York, 10010, United States of America',
            'longitude': -73.9903105}

        '''
        geolocator = Nominatim()
        location = geolocator.geocode(address)
        return dict(address=location.address, latitude=location.latitude,\
            longitude=location.longitude)

    @staticmethod
    def unique_value_count(df):
        '''
        return unique value count of each column as dict mapped

        Parameters:
        -----------
            column_name: str
                Enter the column for checking unique values

        Usage:
        ------
            >> p = preprocess()
            >> p.unique_value_count(data['name'])
            >> {'gender': {'Male': 2, 'Female': 6}, 
            'age': {32: 2, 34: 2, 35: 1, 37: 1, 21: 1, 28: 1}, 
            'name': {'Neeta': 1, 'vandana': 2, 'Amruta': 1, 'Vikrant': 2, 
            'vanana': 1, 'Pallavi': 1}}

        '''
        response = {}
        for col in df.columns:
            response[col] = dict(df[col].value_counts())
        return response

        
    @staticmethod
    def unique_identifier(data):
        unique_col = []
        for col in data.columns:
            if((len(data[col].unique())) == (data[col].size)):
                unique_col.append(col)
        return unique_col

    @staticmethod
    def datestring_to_dd_mm_yy(datestring):
        ''' Return a dictionary of year, month,day, hour, minute and second

        Parameters:
        -----------

            datestring: str
                Enter the datetime string


        Usage:
        ------

            >> p = preprocess()
            >> p.datestring_to_dd_mm_yy("march/1/1980")
            >> {'second': '00', 'hour': '00', 'year': '1980', 'day': '01',
            'minute': '00', 'month': '03'}

        '''


        date, time = str(parser.parse(datestring)).split(' ')
        date = date.split('-')
        time = time.split(':')
        return dict(year=date[0], month=date[1], day=date[2],\
         hour=time[0], minute=time[1], second=time[2])


    def get_version(self):
        ''' Return a version number'''
        return self.version


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
