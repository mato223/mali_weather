from dash import Input, Output, State, dcc, html
import pandas as pd
import dash_bootstrap_components as dbc


df=pd.read_csv("data/kayes_2023.csv")

layout = html.Div([
    html.H1("Kayes Page"),
    html.P("This is the content of the Bamako page. You can add more components and layout here."),
    # Add more components as needed for your Bamako page
    dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
])


