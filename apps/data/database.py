""" 
Database File
------------

Author: Guilherme M. Toso
File: database.py
Date: Aug 03, 2021

Description:

    This is the database file that handles with the House Sales' Database.

"""
import os
import pandas as pd
import geojson

class Database():

    """ 
    class Database

    This class imports the house sales dataset
    
    """


    def __init__(self):
        super().__init__()

        self.path = os.getcwd() + "\\data"

        self.dataset = pd.read_csv(f"{self.path}\\data_clean.csv", sep=",")
        self.temp_data = self.dataset.copy()

        self.numerical_features = ['sqft_living','sqft_lot','sqft_above','sqft_basement','yr_built',
            'lat','long','sqft_living15','sqft_lot15']
        self.mean = self.dataset[self.numerical_features].mean().to_frame()
        self.std = self.dataset[self.numerical_features].std().to_frame()
        
        self.price_mean = self.temp_data.price.mean()
        self.price_std = self.temp_data.price.std()
        self.price_max = self.temp_data.price.max()
        self.price_min = self.temp_data.price.min()
        self.price_mode = self.temp_data.price.mode().loc[0]
        self.price_median = self.temp_data.price.median()
        self.samples = self.temp_data.shape[0]
        self.price_corr = self.temp_data.corr().loc['price'].to_frame().sort_values(by=['price'], ascending=False)[1:6]
        with open(f'{self.path}\\kc_zipcode.geojson') as f:
            self.gj = geojson.load(f)
    def get_mean(self):

        self.mean = self.dataset[self.numerical_features].mean().to_frame()

    def get_std(self):

        self.std = self.dataset[self.numerical_features].std().to_frame()

    def update(self):
        self.price_mean = self.temp_data.price.mean()
        self.price_std = self.temp_data.price.std()
        self.price_max = self.temp_data.price.max()
        self.price_min = self.temp_data.price.min()
        self.price_mode = self.temp_data.price.mode().loc[0]
        self.price_median = self.temp_data.price.median()
        self.samples = self.temp_data.shape[0]

    def get_price_mean(self):

        self.price_mean = self.temp_data.price.mean()
        self.price_std = self.temp_data.price.std()
        

database = Database()
