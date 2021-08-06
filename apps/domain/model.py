""" 
Model File
------------

Author: Guilherme M. Toso
File: model.py
Date: Aug 03, 2021

Description:

    This is the file that contain the machine learning model (XGB_Regressor).

"""

import platform
import os
model_str=""
if platform.system() == "Linux":
    model_str = "/models/"
elif platform.system() == "Windows":
    model_str = "\\models\\"
PATH = os.getcwd() + model_str
import joblib


regressor = joblib.load(f"{PATH}XGBRegressor_RandomizedSearchCV_Best_Model.pkl")

