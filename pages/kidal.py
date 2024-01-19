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

df_kidal_2023 = pd.read_csv("data/kidal_2023.csv")
df_kidal_2023['daylight_duration_hours'] = df_kidal_2023['daylight_duration'] / 3600
df_kidal_2023['sunshine_duration_hours'] = df_kidal_2023['sunshine_duration'] / 3600
#df_kidal_2010_2023 = pd.read_csv("data/kidal_2010-2023.csv")



#<!--------------------------------------------Fig---------------------------------------------------------------!>

temperature_fig = px.line(df_kidal_2023, x='date', y='temperature_2m_mean', title='Variation de la Température Moyenne à kidal en 2023')

precipitation_fig = px.histogram(df_kidal_2023, x='date', y='rain_sum', title='Somme des Précipitations à Kidal en 2023')

wind_speed_fig = px.line(df_kidal_2023, x='date', y='wind_speed_10m_max', title='Variation de la Vitesse Maximale du Vent à kidal en 2023')

daylight_sunshine = px.line(df_kidal_2023, x='date', y=['daylight_duration_hours', 'sunshine_duration_hours'],
              title='Variation durée de la lumière du jour et durée d\'ensoleillement',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

temperature_rain = px.line(df_kidal_2023, x='date', y=['temperature_2m_mean', 'rain_sum'],
              title='Variation de la Température et des Précipitations au Fil du Temps',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

rain_precipitaton = px.line(df_kidal_2023, x='date', y=['rain_sum', 'precipitation_hours'],
              title='Variation des précipitations et nombre d\'heures des précipitations  ',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

#<!--------------------------------------------layout---------------------------------------------------------------!>

layout = html.Div([
                    #<!--------------------Titre page---------------------------!>
                    
    html.H1("KIDAL REPORT", 
            style={'textAlign': 'center',
                    "color": '#2a9fd6'
            }),
    html.Hr(),
                    #<!--------------------Region description---------------------------!>
                    
                dcc.Markdown(
                    """
                    **Kidal, une région située au nord du Mali, connaît un climat désertique caractérisé par des conditions arides et des températures extrêmes. Kidal est caractérisé par un climat désertique. Cette région fait partie du vaste désert du Sahara.**
                    
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'border-radius': '10px', 'color': 'white'},
                ),
                html.Hr(),
                    #<!--------------------temperature_fig---------------------------!>
                dcc.Markdown(
                    """
                    **Température :**
                    - Les températures à Kidal peuvent être extrêmement élevées, en particulier pendant la saison chaude. Les mois d'été, de mai à septembre, sont généralement les plus chauds, avec des températures diurnes pouvant dépasser les 40 degrés Celsius.
                    - La région présente une variation significative de la température diurne, avec des nuits fraîches par rapport aux températures élevées en journée.

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=temperature_fig),
                html.Hr(),
                    #<!--------------------precipitation_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Précipitations :**
                    - Kidal connaît une saison des pluies relativement courte, qui s'étend de juillet à septembre. Cependant, les précipitations sont généralement faibles, et la région reçoit moins de pluie par rapport aux zones plus au sud du Mali.
                    - En raison de son climat désertique, Kidal peut également connaître des variations thermiques diurnes importantes. Les nuits peuvent être nettement plus fraîches que les journées, avec des écarts de température considérables.
                    
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=precipitation_fig),
                html.Hr(),
                    #<!--------------------wind_speed_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Vent et sable :**
                    - Comme de nombreuses régions sahariennes, Kidal peut être affecté par l'harmattan, un vent sec et poussiéreux qui souffle du nord-est. Les tempêtes de sable peuvent également se produire, entraînant des conditions atmosphériques chargées de sable.
                    
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
                    - À kidal, la saison des pluies est généralement courte, et la majorité des précipitations se produit pendant cette période. Les températures pendant la saison des pluies peuvent être relativement plus basses en raison de l'effet de refroidissement lié à la pluie.
                    - Pendant la saison sèche, lorsque les précipitations sont rares, les températures à kidal tendent à être élevées. L'absence fréquente de pluie pendant cette période contribue à des conditions chaudes et arides.
                    
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
