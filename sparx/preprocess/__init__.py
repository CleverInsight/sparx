"""
    Module: Machine Learning Models
    Project: Sparx
    Authors: Bastin Robins. J
    Email : robin@cleverinsight.com
"""
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
import dateutil.parser as parser



class Process(object):
    ''' Cleaner class which can clean the dataset
    '''

    def __init__(self):
        self.version = "0.0.1"

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

def auto_clean(dataframe, target=None, label_encode=True, auto=True, exclude=None):
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
    Usage::
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

    target = dataframe.pop(target)
    features = dataframe

    return {
        'features' : dataframe.head(),
        'target': target
    }
