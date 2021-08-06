""" 
Multiple Pages File
-------------------

Author: Guilherme M. Toso
File: home.py
Date: Aug 03, 2021

Description:

    In this file the framework generates the home page application.

"""

# Dependencies
import os
import streamlit as st
import numpy as np
import PIL
import platform

class Home():


    def __init__(self):

        super().__init__()
        assets_str=""
        if platform.system() == "Linux":
            assets_str = "/apps/assets/"
        elif platform.system() == "Windows":
            assets_str = "\\apps\\assets\\"
        self.path = os.getcwd() + assets_str
        self.img = np.asarray(PIL.Image.open(f"{self.path}king_county.jpg").resize((520,400)))


    def app(self):

        column_1, column_2 = st.beta_columns([2,1])

        with column_1:

            st.markdown("""
            # House Sales 
            -----------------------
            
            """)
            st.image(self.img, caption="""'King County Courthouse and King County Administration Building' 
            by Joe Mabel is licensed under CC BY-SA 4.0""", use_column_width='auto')
        
        with column_2:
            for _ in range(10):
                st.text("\n")
            st.markdown(""" 
            
            ## A Data Science Project...
            
            $~~~~$
            ... focusing on **Business Intelligence**. A simulation of a digital platform whose business model 
            is the purchase and sale of real estate using technology. The objective is to maximize the company's profits.
            The **Dashboard** page provides analysis of home purchased data, while **Prediction** provides home estimation with a
            Machine Learning system and, finally, the **Simulation** page presents situations that return profits to the 
            company by stimulating strategic decision making.
                        
             """)