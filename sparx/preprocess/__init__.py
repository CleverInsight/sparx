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
from sparx.preprocess import *

class Process:

    def __init__(self):
        self.version = "0.0.1"
        
    def impute(self, df, strategy='mean'):

        im = Imputer(strategy='mean')
        im.fit(df)
        return im.transform(df.values)

    @staticmethod
    def count_Nan(col_name):
        return col_name.isnull().sum()

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

    Y = dataframe.pop(target)
    X = dataframe
 



    return {
        'features' : dataframe.head(),
        'target': target
    }

