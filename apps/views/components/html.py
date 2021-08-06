""" 
html File
------------

Author: Guilherme M. Toso
File: html.py
Date: Aug 04, 2021

Description:

    This is the html file that contain components made by html and css

"""

import streamlit as st
import streamlit.components as components

def card(name, value,margin):

    if isinstance(value,float):
        val = f"""{value:,.2f}"""
        is_price = "$"
    else:
        val = f"""{value:,}"""
        is_price = ""
    card_str = f""" 
        <div style="margin: {margin}%;position: relative; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s; width: 15vw; height: 80vh; border-radius: 10%; background-color: #303841;">
            <div style="padding: 1%">
                <h3 style="font-family:'Montserrat',sans-serif ;font-weight:400; text-align:center;">
                    <b  style="color: #39E687;">
                        {name}
                    </b>
                </h3>
                <h2 style="font-family:'Montserrat',sans-serif ;font-weight:400;text-align:center;">
                    <b style="color: #39E687;">
                        {is_price} {val}
                    </b>
                </h2>
            </div>
        </div> 
    """
    return card_str

def row(elements):

    row_str = f"""<div style="display:flex;">"""
    for element in elements:
        row_str += element
    row_str += "</div>"
    return row_str
# def title(value):

#     component = components.v1.html(f"""
#         <h1>{value}<h1/>
#     """)