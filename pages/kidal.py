#<!--------------------------------------------importations---------------------------------------------------------------!>
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash


#<!--------------------------------------------data-loading---------------------------------------------------------------!>
app = Dash(__name__)

df_kidal_2023 = pd.read_csv("data/kidal_2023.csv")
df_kidal_hourly_2023= pd.read_csv("base/kidal_hourly_2023.csv")

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

##############

df_kidal_hourly_2023['date'] = pd.to_datetime(df_kidal_hourly_2023['date'])

df_kidal_hourly_2023['time_of_day'] = ['Day' if is_day else 'Night' for is_day in df_kidal_hourly_2023['is_day']]
data_avg_temp = df_kidal_hourly_2023.groupby(['time_of_day', df_kidal_hourly_2023['date'].dt.date])['temperature_2m'].mean().reset_index()
temp_day_night = px.line(data_avg_temp, x='date', y='temperature_2m', color='time_of_day',
              title='Variation moyenne de la température du jour et de la nuit',
              labels={'temperature_2m': 'Température Moyenne (°C)', 'date': 'Date'})
##############

temp_humd_fig = px.scatter(df_kidal_hourly_2023, x='temperature_2m', y='relative_humidity_2m', title='Corrélation entre Température et Humidité Relative',
                 labels={'temperature_2m': 'Température (°C)', 'relative_humidity_2m': 'Humidité Relative (%)'})


###############

facette_day_night = px.scatter(df_kidal_hourly_2023, x='temperature_2m', y='relative_humidity_2m', color='is_day', facet_col='time_of_day',
                 labels={'temperature_2m': 'Température (°C)', 'relative_humidity_2m': 'Humidité relative (%)'},
                 title='Scatter Plot avec Facettes')
                 
##############

polar_wind_fig = go.Figure()

polar_wind_fig.add_trace(go.Barpolar(
    r=df_kidal_hourly_2023['wind_speed_10m'],
    theta=df_kidal_hourly_2023['wind_direction_10m'],
    marker_color='rgba(75, 101, 132, 0.8)',
    name='Vitesse du Vent'
))

polar_wind_fig.update_layout(
    title='Rose des Vents - Distribution des Directions du Vent',
    font_size=12,
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, df_kidal_hourly_2023['wind_speed_10m'].max()]
        )),
    showlegend=False
)

################
df_kidal_hourly_2023['month'] = df_kidal_hourly_2023['date'].dt.strftime('%B')

month_fig = px.bar(df_kidal_hourly_2023.groupby('month')['temperature_2m'].mean().reset_index(),
             x='month', y='temperature_2m',
             title="Temperature Moyenne par Mois",
             labels={'temperature_2m': 'Température Moyenne (°C)', 'month': 'Mois'},
             category_orders={'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}
)
             
             
#################

relation_fig = px.scatter_polar(df_kidal_hourly_2023, r='temperature_2m', theta='wind_direction_10m',
                       size='wind_speed_10m', color='relative_humidity_2m',
                       title='Graphique Polaire - Variables Influencant la Température',
                       labels={'temperature_2m': 'Température (°C)',
                               'wind_direction_10m': 'Direction du Vent (degrés)',
                               'wind_speed_10m': 'Vitesse du Vent (m/s)',
                               'relative_humidity_2m': 'Humidité Relative (%)'})

##################

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
                dcc.Graph(figure=temp_day_night),
                html.Hr(),
                
                dcc.Graph(figure=temp_humd_fig),
                dcc.Graph(figure=facette_day_night),
                dcc.Graph(figure=month_fig),

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
                
                dcc.Graph(figure=polar_wind_fig),
                dcc.Graph(figure=relation_fig),
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
