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

df_bamako_2023 = pd.read_csv("data/bamako_2023.csv")
df_bamako_2023['daylight_duration_hours'] = df_bamako_2023['daylight_duration'] / 3600
df_bamako_2023['sunshine_duration_hours'] = df_bamako_2023['sunshine_duration'] / 3600
#df_bamako_2010_2023 = pd.read_csv("data/bamako_2010-2023.csv")



#<!--------------------------------------------Fig---------------------------------------------------------------!>

temperature_fig = px.line(df_bamako_2023, x='date', y='temperature_2m_mean', title='Variation de la Température Moyenne à bamako en 2023')

precipitation_fig = px.histogram(df_bamako_2023, x='date', y='rain_sum', title='Somme des Précipitations à Bamako en 2023')

wind_speed_fig = px.line(df_bamako_2023, x='date', y='wind_speed_10m_max', title='Variation de la Vitesse Maximale du Vent à bamako en 2023')

daylight_sunshine = px.line(df_bamako_2023, x='date', y=['daylight_duration_hours', 'sunshine_duration_hours'],
              title='Variation durée de la lumière du jour et durée d\'ensoleillement',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

temperature_rain = px.line(df_bamako_2023, x='date', y=['temperature_2m_mean', 'rain_sum'],
              title='Variation de la Température et des Précipitations au Fil du Temps',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

rain_precipitaton = px.line(df_bamako_2023, x='date', y=['rain_sum', 'precipitation_hours'],
              title='Variation des précipitations et nombre d\'heures des précipitations  ',
              labels={'value': 'Valeur', 'variable': 'Variable', 'date': 'Date'})

#<!--------------------------------------------layout---------------------------------------------------------------!>

layout = html.Div([
                    #<!--------------------Titre page---------------------------!>
                    
    html.H1("BAMAKO REPORT", 
            style={'textAlign': 'center',
                    "color": '#2a9fd6'
            }),
    html.Hr(),
                    #<!--------------------Region description---------------------------!>
                    
                dcc.Markdown(
                    """
                    **Bamako, la capitale du Mali, est située dans la région ouest du pays et possède un climat de type tropical sec avec une saison des pluies et une saison sèche. Voici une description climatique générale de la région de Bamako**
                    - Bamako est située dans la région sahélienne, une zone de transition entre le désert du Sahara au nord et la savane au sud. Le climat sahélien se caractérise par des variations saisonnières marquées.
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'border-radius': '10px', 'color': 'white'},
                ),
                html.Hr(),
                    #<!--------------------temperature_fig---------------------------!>
                dcc.Markdown(
                    """
                    **Température :**
                    - Bamako connaît des températures élevées tout au long de l'année. Les mois de février à mai sont souvent les plus chauds, avec des températures diurnes dépassant fréquemment les 37 degrés Celsius.
                    - Les nuits restent relativement chaudes, avec une variation de température diurne moins prononcée que dans certaines régions.
                    - Les mois de décembre et janvier peuvent être plus frais, mais les journées restent généralement ensoleillées

                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=temperature_fig),
                html.Hr(),
                    #<!--------------------precipitation_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Précipitations :**
                    - La saison des pluies à Bamako s'étend généralement de juin à septembre. C'est pendant cette période que la ville reçoit la grande majorité de ses précipitations.
                    - La saison sèche va d'octobre à mai. Pendant cette période, les précipitations sont rares, et la végétation peut devenir plus sèche.
                    
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=precipitation_fig),
                html.Hr(),
                    #<!--------------------wind_speed_fig---------------------------!>
                dcc.Markdown(
                    """
                   **Vent et sable :**
                    - Les vents à Bamako présentent une variabilité saisonnière et sont influencés par des phénomènes météorologiques régionaux tels que l'harmattan et la mousson.
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
                    
                    Pendant la saison sèche, Bamako est plus susceptible de bénéficier d'une durée d'ensoleillement plus longue, car le ciel est généralement dégagé. À l'inverse, la saison des pluies peut être associée à une couverture nuageuse plus importante, ce qui peut réduire la durée effective d'ensoleillement.
                   
                    La durée d'ensoleillement influence directement la quantité d'énergie solaire reçue par la surface terrestre. Plus la durée d'ensoleillement est longue, plus la Terre est exposée à la lumière solaire, ce qui entraîne un réchauffement de l'atmosphère et du sol.
                   
                    
                    
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=daylight_sunshine),
                html.Hr(),

                    #<!--------------------temperature_rain---------------------------!>
                dcc.Markdown(
                    """
                    Les précipitations peuvent influencer la température en raison de l'évaporation. Lorsqu'il pleut, l'eau qui atteint le sol peut s'évaporer, absorbant de l'énergie thermique et entraînant un refroidissement temporaire de l'atmosphère et de la surface terrestre.
                    Des pluies abondantes peuvent entraîner un refroidissement temporaire significatif, surtout si elles sont accompagnées de vents ou de conditions nuageuses. Cela peut réduire les températures diurnes.
                    
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
