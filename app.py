""" 
App File
------------

Author: Guilherme M. Toso
File: app.py
Date: Aug 02, 2021

Description:

    This file is the main file of the web application. 

"""
import os
import sys
sys.path.insert(0,os.getcwd())
import streamlit as st
from multiple_pages import Navigator
from apps.views import Home, Dashboard, Prediction, Simulation


st.set_page_config(layout="wide")

app = Navigator()

app.add_page('Home', Home().app)
app.add_page('Dashboard', Dashboard().app)
app.add_page('Prediction', Prediction().app)
app.add_page('Simulation', Simulation().app)

app.run()