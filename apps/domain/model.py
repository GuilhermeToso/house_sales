""" 
Model File
------------

Author: Guilherme M. Toso
File: model.py
Date: Aug 03, 2021

Description:

    This is the file that contain the machine learning model (XGB_Regressor).

"""

import os
PATH = os.getcwd() + "\\models"
import joblib


regressor = joblib.load(f"{PATH}\\XGBRegressor_RandomizedSearchCV_Best_Model.pkl")

