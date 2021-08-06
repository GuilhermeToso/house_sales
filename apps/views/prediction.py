""" 
Prediction File
------------

Author: Guilherme M. Toso
File: prediction.py
Date: Jul 16, 2021

Description:

    This is the prediction page. Where the user can input data and it will return the house price prediction.
    
"""
# Dependencies
import os
import streamlit as st
from apps.domain.data_clean import Cleaner
from apps.data.database import database
from apps.domain.model import regressor



class Prediction():


    def __init__(self):

        super().__init__()
        self.price = 0.0
        self.input_data = {
            'sqft_living': 0,
            'sqft_lot':0,
            'sqft_above':0,
            'yr_built':1852,
            'lat':47.1559,
            'long':-122.519,
            'sqft_living15':0,
            'sqft_lot15':0,
            'bedrooms':0,
            'bathrooms':0,
            'floors':1,
            'waterfront':'Yes',
            'renovated':'Yes',
            'views':0,
            'condition':'Poor',
            'grade':0
        }
        self.cleaner = Cleaner()


    def app(self):

        st.title('Predict House Price')
        st.markdown("""
        ----

        With the help of Machine Learning models you can predict the house price
        -------

        ----
        """)


        price = st.empty()
        pred = st.empty()
        update_data = st.empty()

        pred_col_1, pred_col_2, pred_col_3 = st.beta_columns([2,1,1])

        with pred_col_1:        
            price.title(f"Price: ${self.price:,.2f}")
        with pred_col_2:
            predicted = pred.button("Predict Price")
        with pred_col_3:
            updated = update_data.button("Update Data")
        
        st.text("\n")

        column_1, column_2, column_3 = st.beta_columns(3)


        with column_1:
            self.input_data['sqft_living'] = st.number_input(label="Living Area (in Square Feet)", min_value=0.0, step=0.01)
            self.input_data['yr_built'] = st.number_input(label="Year Built", min_value=1852, step=1)
            self.input_data['sqft_living15'] = st.number_input(label="Living Area of the 15 Closest Neighbors (in Square Feet)", min_value=0.0, step=0.01)
            self.input_data['bathrooms'] = st.number_input(label="Bathrooms", min_value=0, step=1)
            self.input_data['renovated'] = st.radio(label="The house were renovated? ",options=('Yes','No'))
            self.input_data['grade'] = st.slider(label="Select the house grade",min_value=0, max_value=13,step=1)
        with column_2:
            self.input_data['sqft_lot'] = st.number_input(label="Land Area (in Square Feet)", min_value=0.0, step=0.01)
            self.input_data['lat'] = st.number_input(label="Latitute (4 decimal digits)", min_value=47.1559, max_value=47.7776, step=0.0001)
            self.input_data['sqft_lot15'] = st.number_input(label="Landing Area of the 15 Closest Neighbors (in Square Feet)", min_value=0.0, step=0.01)
            self.input_data['floors'] = st.number_input(label="Floors", min_value=1, step=1)
            self.input_data['views'] = st.slider(label="How is the house view",min_value=0, max_value=4,step=1)
        with column_3:
            self.input_data['sqft_above'] = st.number_input(label="House Area apart from basement (in Square Feet)", min_value=0.0, step=0.01)
            self.input_data['long'] = st.number_input(label="Longitude (3 decimal digits)", min_value=-122.519, max_value=-121.315, step=0.001)
            self.input_data['bedrooms'] = st.number_input(label="Bedrooms", min_value=0, step=1)
            self.input_data['waterfront'] = st.radio(label="There is a water front? ",options=('Yes','No'))
            self.input_data['condition'] = st.select_slider(label='Select the house overall condition',
            options=['Poor', 'Fair-Badly', 'Average', 'Good', 'Very Good'])

        cleaned_data = self.cleaner.model_input(self.input_data)

        if predicted:
            self.price = regressor.predict(cleaned_data)
            price.title(f"Price: ${self.price[0]:,.2f}")
    
        if updated:
            database.update()
        
