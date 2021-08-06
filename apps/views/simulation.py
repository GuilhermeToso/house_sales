""" 
Simulation File
------------

Author: Guilherme M. Toso
File: simulation.py
Date: Aug 06, 2021

Description:

    This is the Simulation page. Where the user is going to see the simulated financial information to gain some ROI

"""

# Dependencies
import os
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from apps.data.database import database

class Simulation():


    def __init__(self):

        super().__init__()
        self.path = os.getcwd() + "\\data"
        self.profits = pd.read_csv(f"{self.path}\\profits.csv")

    def app(self):

        st.title('House Sales Simulation')
        st.markdown("""
            --- 
            The graphs show the company's profits in some artificial situations based on data analysis and machine learning model.
            The situation is the following, what profit would the company make if it bought the houses and remodeled them by increasing the living area?
            Because the area has the highest correlation with the price and the renovated houses are the most expensive. 
            So on the basis that the average sq. ft. renovation costs $100, we can calculate the profit, the average profit, and the gross margin. 
         """)
        col_1, col_2 = st.beta_columns(2)
        with col_1:
            st.write(self.profit_total())
        with col_2:
            st.write(self.profit_mean())
        column_1, column_2, column_3 = st.beta_columns(3)
        with column_1:
            st.write('')
        with column_2:
            st.write(self.profit_gross_margin())
        with column_3:
            st.write('')
        

    def profit_total(self):

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(x=self.profits.index, y=self.profits.profit_total, fill='tozeroy', fillcolor='rgba(57,230,135,0.4)',line_color='rgba(57,230,135,1.0)', opacity=0.4)
        )
        # labels={'index':'$Living\;Area\; [ft^{2}]$', 'profit_total':'Profit'})
        fig.update_traces(hovertemplate='Profit: %{y} <br>Area (ft<sup>2</sup>): %{x}<extra></extra>')
        fig.update_layout(
            title="Profit per Living Area",
            yaxis_title="Profit ($)",
            xaxis_title="Living Area [ft<sup>2</sup>]",
            plot_bgcolor='#20262D',
            showlegend=False,
        )
        fig.update_yaxes(gridcolor="#424E5A")

        return fig
    
    def profit_mean(self):

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(x=self.profits.index, y=self.profits.profit_total/database.samples, fill='tozeroy', fillcolor='rgba(57,230,135,0.4)',line_color='rgba(57,230,135,1.0)', opacity=0.4)
        )
        # labels={'index':'$Living\;Area\; [ft^{2}]$', 'profit_total':'Profit'})
        fig.update_traces(hovertemplate='Profit Mean: %{y} <br>Area (ft<sup>2</sup>): %{x}<extra></extra>')
        fig.update_layout(
            title="Profit Mean per Living Area",
            yaxis_title="Profit Mean ($)",
            xaxis_title="Living Area [ft<sup>2</sup>]",
            plot_bgcolor='#20262D',
            showlegend=False,
        )
        fig.update_yaxes(gridcolor="#424E5A")

        return fig

    def profit_gross_margin(self):

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(x=self.profits.index, y=self.profits.gross_margin, fill='tozeroy', fillcolor='rgba(57,230,135,0.4)',line_color='rgba(57,230,135,1.0)', opacity=0.4)
        )
        # labels={'index':'$Living\;Area\; [ft^{2}]$', 'profit_total':'Profit'})
        fig.update_traces(hovertemplate='Gross Margin: %{y}% <br>Area (ft<sup>2</sup>): %{x}<extra></extra>')
        fig.update_layout(
            title="Gross Margin per Living Area",
            yaxis_title="Gross Margin (%)",
            xaxis_title="Living Area [ft<sup>2</sup>]",
            plot_bgcolor='#20262D',
            showlegend=False,
        )
        fig.update_yaxes(gridcolor="#424E5A")

        return fig