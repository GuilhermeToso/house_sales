""" 
Multiple Pages File
-------------------

Author: Guilherme M. Toso
File: multiple_pages.py
Date: Aug 02, 2021

Description:

    In this file the framework generates multiples Streamlit aplications

"""

import streamlit as st

class Navigator():

    """ 
    Class Navigator
    
    Framework responsible for handling the addition and navigation of Streamlit applications
    
    """

    def __init__(self):

        """ Constructor's Class that create the list of pages """
    
        super().__init__()
        self.pages = []

    
    def add_page(self, title=None, application=None):

        """ 
        Class method to add pages to the list of pages
        
        Args:
            title (str): The title of the application that we are ading to the pages'list.
            function (func): A Python function that renders the Streamlit application.

        """

        self.pages.append(
            {
                'title':title,
                'class':application
            }
        )

    def run(self):

        """ 
        Class method that runs the application selected
        
        """

        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        page['class']()