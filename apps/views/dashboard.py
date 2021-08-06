""" 
Dashboard File
------------

Author: Guilherme M. Toso
File: dashboard.py
Date: Jul 16, 2021

Description:

    This is the dashboard page. Where the user is going to see the financial information as cards and graphics.

"""


# Dependencies
import streamlit as st
from apps.data.database import database
import plotly.express as px
import plotly.graph_objects as go
from apps.views.components.html import card, row


class Dashboard():


    def __init__(self):

        super().__init__()


    def app(self):

        st.title('House Sales Dashboard')
        filter_1, filter_2, filter_3, filter_4 = st.beta_columns(4)
        with filter_1:
            price = st.number_input('Price', min_value=0.0, max_value=2500000.0,step=0.01, value=2500000.0)
            database.temp_data = database.temp_data[database.dataset.price <= price]
            database.update()
        with filter_2: 
            living_area = st.number_input('Living Area', min_value=290.0, max_value=13540.0,step=0.01, value=13540.0)
            database.temp_data = database.temp_data[database.dataset.sqft_living <= living_area]
            database.update()
        with filter_3:
            grade = st.number_input('Grade', min_value=1, max_value=13,step=1, value=13)
            database.temp_data = database.temp_data[database.dataset.grade <= grade]
            database.update()
        with filter_4:
            renovation = st.selectbox(label="The house were renovated? ",options=('Yes','No','Both'))
            if renovation == 'Both':
                database.temp_data = database.temp_data.loc[database.dataset['renovated'].isin(['Yes','No'])]

            else:
                database.temp_data = database.dataset[database.dataset.renovated == renovation]
                database.update()
        st.markdown("""---""")
        margin = 1
        cards = [card("Price Mean",database.price_mean,margin),card("Max Price",database.price_max,margin),
        card("Min Price",database.price_min,margin),card("Price Mode",database.price_mode,margin), 
        card("Price Median",database.price_median,margin),
        card("Houses", database.samples, margin)]
        st.components.v1.html(row(cards))
        col_1, col_2, col_3 = st.beta_columns(3)
        with col_1:
            st.write(self.price_graph())
        with col_2:
            st.write(self.price_by_renovation())
        with col_3:
            st.write(self.price_corr())
        column_1, column_2 = st.beta_columns(2)
        with column_1:
            st.write(self.price_map())
        with column_2:
            st.write(self.price_range_map())
    def price_graph(self):

        pg = px.histogram(
            database.temp_data, x=database.temp_data.price,color=database.temp_data.price, color_discrete_sequence= ["#39E687"] ,opacity=0.5, nbins=200,
            hover_data =None
        )

        pg.update_layout(
            width=500,
            plot_bgcolor='#20262D',
            showlegend=False,
            title="Houses per Price",
            yaxis_title="Number of Houses",
            xaxis_title="Price",
        )
        pg.update_traces(
            hovertemplate='<b>Price</b>: $%{x:,.2f}'+'<br><b>Houses</b>: %{y:,}<extra></extra>'
        )
        pg.update_yaxes(gridcolor="#424E5A")

        return pg


    def price_by_renovation(self):

        fig = go.Figure()
        fig.add_trace(
            go.Box(
                x = database.temp_data.renovated, y = database.temp_data.price, name='Price',
                marker_color = "#39E687"
            )
        )
        
        fig.update_layout(
            title="Price of Sold Houses versus Renovation",
            plot_bgcolor='#20262D',
            yaxis_title="Price",
            xaxis_title="Renovated",
            width=500
        )
        fig.update_yaxes(gridcolor="#424E5A")

        return fig

    def price_corr(self):
        
        fig = px.bar(database.price_corr, x=database.price_corr.index, y='price', color=database.price_corr.index, color_discrete_sequence=["#39E687"],
        )
        fig.update_layout(
            width=500,
            plot_bgcolor='#20262D',
            xaxis = dict( 
                tickvals = ['sqft_living', 'grade', 'sqft_living15', 'sqft_above', 'bathrooms'],
                ticktext = ['Living Area', 'Grade', '15 Living Areas', 'Above Area', 'Bathrooms']
            ),
            showlegend=False,
            yaxis_title="Correlation",
            xaxis_title="Features",
            title="Price Correlation vs Features",
        )
        fig.update_traces(
            hovertemplate='<b>Correlation</b>: %{y:.3f}'+'<br><b>Feature</b>: %{x}<extra></extra>'
        )
        return fig

    def price_map(self):

        fig = px.scatter_mapbox(database.temp_data, lat="lat", lon="long",color="price",
                  color_continuous_scale=px.colors.sequential.Emrld, size_max=1, zoom=8)
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        return fig

    def price_range_map(self):

        fig = px.scatter_mapbox(database.temp_data, lat="lat", lon="long",color="price_range",
                  color_discrete_sequence=px.colors.sequential.Emrld, size_max=1, zoom=8)
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        return fig