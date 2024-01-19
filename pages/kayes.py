#<!--------------------------------------------importations---------------------------------------------------------------!>
import dash
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from holoviews.plotting.plotly.dash import to_dash
from dash import Input, Output, State, dcc, html, Dash


#<!--------------------------------------------data-loading---------------------------------------------------------------!>
app = Dash(__name__)

df_kayes_2023 = pd.read_csv("data/kayes_2023.csv")
df_kayes_2023['daylight_duration_hours'] = df_kayes_2023['daylight_duration'] / 3600
df_kayes_2023['sunshine_duration_hours'] = df_kayes_2023['sunshine_duration'] / 3600
#df_kayes_2010_2023 = pd.read_csv("data/kayes_2010-2023.csv")



#<!--------------------------------------------Fig---------------------------------------------------------------!>

temperature_fig = px.line(df_kayes_2023, x='date', y='temperature_2m_mean', title='Variation de la Température Moyenne à kayes en 2023')

precipitation_fig = px.histogram(df_kayes_2023, x='date', y='rain_sum', title='Somme des Précipitations à Kayes en 2023')

wind_speed_fig = px.line(df_kayes_2023, x='date', y='wind_speed_10m_max', title='Variation de la Vitesse Maximale du Vent à kayes en 2023')

daylight_sunshine = px.line(df_kayes_2023, x='date', y=['daylight_duration_hours', 'sunshine_duration_hours'],
              title='Variation durée de la lumière du jour et durée d\'ensoleillement',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

temperature_rain = px.line(df_kayes_2023, x='date', y=['temperature_2m_mean', 'rain_sum'],
              title='Variation de la Température et des Précipitations au Fil du Temps',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

rain_precipitaton = px.line(df_kayes_2023, x='date', y=['rain_sum', 'precipitation_hours'],
              title='Variation des précipitations et nombre d\'heures des précipitations  ',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

#<!--------------------------------------------layout---------------------------------------------------------------!>

layout = html.Div([
                    #<!--------------------Titre page---------------------------!>
                    
    html.H1("KAYES REPORT", 
            style={'textAlign': 'center',
                    "color": '#2a9fd6'
            }),
    html.Hr(),
                    #<!--------------------Region description---------------------------!>
                    
                dcc.Markdown(
                    """
                    **La région de Kayes, située dans le sud-ouest du Mali, est caractérisée par un climat de type tropical, avec des variations saisonnières marquées. **
                    **En résumé, la région de Kayes présente un climat tropical avec des températures élevées, une saison des pluies caractérisée par des précipitations importantes, et une saison sèche avec des températures élevées et un manque de pluie.**

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'border-radius': '10px', 'color': 'white'},
                ),
                html.Hr(),
                    #<!--------------------temperature_fig---------------------------!>
                dcc.Markdown(
                    """
                    **Température :**
                    - Kayes se trouve dans une zone de climat tropical, influencée par sa proximité avec l'équateur. Cela se traduit par des températures relativement élevées tout au long de l'année.
                    - Les températures à Kayes sont élevées, en particulier pendant la saison sèche. Les mois de mars à mai peuvent être les plus chauds, avec des températures diurnes pouvant atteindre les 40 degrés Celsius.

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=temperature_fig),
                html.Hr(),
                    #<!--------------------precipitation_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Précipitations :**
                    - La région de Kayes connaît une saison des pluies qui s'étend généralement de juin à septembre. Pendant cette période, la région reçoit des précipitations plus importantes, avec des averses parfois fortes et des orages fréquents.
                    - La saison sèche s'étend généralement d'octobre à mai. Pendant cette période, les précipitations sont rares, et la région peut être sujette à des conditions arides. Les températures diurnes restent élevées, mais les nuits peuvent être relativement plus fraîches.

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=precipitation_fig),
                html.Hr(),
                    #<!--------------------wind_speed_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Vent et sable :**
                    - la région de Kayes connaît une variété de vents tout au long de l'année, influencés par des phénomènes saisonniers tels que la saison sèche, la saison des pluies et l'harmattan. La topographie locale et d'autres facteurs géographiques peuvent également jouer un rôle dans la dynamique des vents à Kayes.
                    
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),                   
                dcc.Graph(figure=wind_speed_fig),
                html.Hr(),
                
                    #<!--------------------daylight_sunshine---------------------------!>
                dcc.Markdown(
                    """
                    La durée d'ensoleillement et la durée du jour sont liées, mais elles ne sont pas exactement les mêmes.

                    - La durée du jour se réfère au temps total pendant lequel le soleil est au-dessus de l'horizon au cours d'une journée donnée. Elle comprend le temps du lever du soleil jusqu'au coucher du soleil.

                    - La durée d'ensoleillement, quant à elle, représente la période pendant laquelle le soleil brille effectivement et éclaire la surface de la Terre. Elle peut être légèrement plus courte que la durée du jour totale en raison de facteurs tels que l'épaisseur de l'atmosphère, les conditions météorologiques, ou la présence d'obstacles sur l'horizon.

                    La durée d'ensoleillement est généralement abondante, surtout pendant la saison sèche. Les journées peuvent être caractérisées par une longue durée d'ensoleillement, contribuant aux températures élevées pendant la journée.

                    Une durée d'ensoleillement prolongée est généralement associée à des températures plus élevées pendant la journée. Ces liens sont importants pour comprendre les caractéristiques climatiques spécifiques de la région.

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=daylight_sunshine),
                html.Hr(),

                    #<!--------------------temperature_rain---------------------------!>
                dcc.Markdown(
                    """
                    - La quantité de précipitations peut varier d'une année à l'autre, influençant ainsi la variation annuelle des températures. Des années avec des précipitations plus importantes peuvent être associées à des températures plus douces.
                       
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=temperature_rain),
                html.Hr(),

                    #<!--------------------rain_precipitaton---------------------------!>
                dcc.Markdown(
                    """
                    - La durée de précipitation peut influencer la somme des précipitations, mais elle n'est pas le seul facteur déterminant. Une pluie intense et de courte durée peut générer une somme importante de précipitations, tandis qu'une pluie légère mais prolongée peut également contribuer à une somme substantielle.
                    - L'intensité de la précipitation, c'est-à-dire la quantité de précipitations tombant par unité de temps, peut varier. Des pluies intenses sur une courte période peuvent générer une somme significative en peu de temps.
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=rain_precipitaton),
                html.Hr(),



    
])
#<!-----------------------------------------------------------------------------------------------------------!>
