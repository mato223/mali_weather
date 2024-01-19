import dash
import plotly.graph_objects as go
import pandas as pd

from dash import Input, Output, State, dcc, html
#from predictions import linearRegression, xgBoost

# Charger les bases de données kayes_2023 et bamako_2023
df = pd.read_csv("data/bamako_hourly-2000_2023.csv")

layout = html.Div([
    html.H1("Home Page"),
    html.P("This is the content of the Bamako page. You can add more components and layout here."),
    # Add more components as needed for your Bamako page
])
