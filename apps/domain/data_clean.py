""" 
Data Clean File
------------

Author: Guilherme M. Toso
File: data_clean.py
Date: Jul 16, 2021

Description:

    This is the file that cleans some input data.

"""

from apps.data.database import database
import numpy as np

class Cleaner():

    """ 
    class Cleaner

    This class cleans input data
    
    """

    def __init__(self):
        super().__init__()
        self.condition_feature = {
            'Poor':0,
            'Fair-Badly':1,
            'Average':2,
            'Good':3,
            'Very Good':4
        }

    def model_input(self, data):

        output = np.zeros((1,19))

        output[0,0] = (data['sqft_living'] - database.mean.loc['sqft_living'])/database.std.loc['sqft_living']       
        output[0,1] = (data['sqft_lot'] - database.mean.loc['sqft_lot'])/database.std.loc['sqft_lot']
        output[0,2] = (data['sqft_above'] - database.mean.loc['sqft_above'])/database.std.loc['sqft_above']
        sqft_basement = data['sqft_living'] - data['sqft_above']
        output[0,3] = (sqft_basement - database.mean.loc['sqft_basement'])/database.std.loc['sqft_basement']
        output[0,4] = (data['yr_built'] - database.mean.loc['yr_built'])/database.std.loc['yr_built']
        output[0,5] = (data['lat'] - database.mean.loc['lat'])/database.std.loc['lat']
        output[0,6] = (data['long'] - database.mean.loc['long'])/database.std.loc['long']
        output[0,7] = (data['sqft_living15'] - database.mean.loc['sqft_living15'])/database.std.loc['sqft_living15']
        output[0,8] = (data['sqft_lot15'] - database.mean.loc['sqft_lot15'])/database.std.loc['sqft_lot15']
        waterfront = 1 if data['waterfront']=='Yes' else 0
        output[0,9] = float(1 - waterfront)
        output[0,10] = float(waterfront)
        renovated = 1 if data['renovated']=='Yes' else 0
        output[0,11] = float(1-renovated)
        output[0,12] = float(renovated)
        output[0,13] = float(data['bedrooms'])
        output[0,14] = float(data['bathrooms'])
        output[0,15] = float(data['floors'])
        output[0,16] = float(data['views'])
        output[0,17] = float(self.condition_feature[data['condition']])
        output[0,18] = float(data['grade'])
        
        return output