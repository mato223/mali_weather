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

df_tombouctou_2023 = pd.read_csv("data/tombouctou_2023.csv")
df_tombouctou_2023['daylight_duration_hours'] = df_tombouctou_2023['daylight_duration'] / 3600
df_tombouctou_2023['sunshine_duration_hours'] = df_tombouctou_2023['sunshine_duration'] / 3600
#df_tombouctou_2010_2023 = pd.read_csv("data/tombouctou_2010-2023.csv")



#<!--------------------------------------------Fig---------------------------------------------------------------!>

temperature_fig = px.line(df_tombouctou_2023, x='date', y='temperature_2m_mean', title='Variation de la Température Moyenne à tombouctou en 2023')

precipitation_fig = px.histogram(df_tombouctou_2023, x='date', y='rain_sum', title='Somme des Précipitations à Tombouctou en 2023')

wind_speed_fig = px.line(df_tombouctou_2023, x='date', y='wind_speed_10m_max', title='Variation de la Vitesse Maximale du Vent à tombouctou en 2023')

daylight_sunshine = px.line(df_tombouctou_2023, x='date', y=['daylight_duration_hours', 'sunshine_duration_hours'],
              title='Variation durée de la lumière du jour et durée d\'ensoleillement',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

temperature_rain = px.line(df_tombouctou_2023, x='date', y=['temperature_2m_mean', 'rain_sum'],
              title='Variation de la Température et des Précipitations au Fil du Temps',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

rain_precipitaton = px.line(df_tombouctou_2023, x='date', y=['rain_sum', 'precipitation_hours'],
              title='Variation des précipitations et nombre d\'heures des précipitations  ',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

#<!--------------------------------------------layout---------------------------------------------------------------!>

layout = html.Div([
                    #<!--------------------Titre page---------------------------!>
                    
    html.H1("TOMBOUCTOU REPORT", 
            style={'textAlign': 'center',
                    "color": '#2a9fd6'
            }),
    html.Hr(),
                    #<!--------------------Region description---------------------------!>
                    
                dcc.Markdown(
                    """
                    **La région de Tombouctou au Mali se caractérise par un climat désertique, typique des régions sahariennes.**
                    **Tombouctou est située dans une zone de climat désertique, marquée par des conditions arides et des températures élevées.**

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'border-radius': '10px', 'color': 'white'},
                ),
                html.Hr(),
                    #<!--------------------temperature_fig---------------------------!>
                dcc.Markdown(
                    """
                    **Température :**
                    - Les températures à Tombouctou sont parmi les plus élevées au Mali. Pendant la saison chaude, qui peut durer plusieurs mois, les températures diurnes peuvent dépasser fréquemment les 40 degrés Celsius.
                    - La région connaît une saison chaude prolongée, généralement de mars à octobre, caractérisée par des températures très élevées. La saison fraîche, de novembre à février, présente des températures diurnes relativement moins élevées.
                    
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=temperature_fig),
                html.Hr(),
                    #<!--------------------precipitation_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Précipitations :**
                    - La région connaît des précipitations extrêmement faibles tout au long de l'année. Les pluies sont rares, et la région est soumise à une sécheresse importante.

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=precipitation_fig),
                html.Hr(),
                    #<!--------------------wind_speed_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Vent et sable :**
                    - Tout comme d'autres régions sahariennes, Tombouctou peut être affectée par l'harmattan pendant la saison sèche. L'harmattan est un vent sec et poussiéreux qui souffle du Sahara, entraînant des conditions atmosphériques sèches et la présence de poussière dans l'air.
                    
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
                    - Pendant la saison des pluies, qui se situe généralement de juin à septembre à Tombouctou, les précipitations sont plus fréquentes. Les averses pendant cette période peuvent contribuer à un refroidissement temporaire de l'atmosphère.
                    - Pendant la saison sèche, lorsque les précipitations sont rares, les températures diurnes peuvent atteindre des niveaux élevés. Le manque de nuages et de pluie permet à l'énergie solaire d'atteindre la surface terrestre, contribuant à des températures plus élevées.
                    
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
