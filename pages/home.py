#<!--------------------------------------------importations---------------------------------------------------------------!>
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash
from predictions import xgBoost


#<!--------------------------------------------data-loading---------------------------------------------------------------!>
app = Dash(__name__)

                    #<!--------------------daily---------------------------!>

df_bamako_2023 = pd.read_csv("data/bamako_2023.csv")
#df_kayes_2023 = pd.read_csv("data/kayes_2023.csv")
#df_koulikoro_2023 = pd.read_csv("data/koulikoro_2023.csv")
df_sikasso_2023 = pd.read_csv("data/sikasso_2023.csv")
#df_segou_2023 = pd.read_csv("data/segou_2023.csv")
#df_mopti_2023 = pd.read_csv("data/mopti_2023.csv")
df_tombouctou_2023 = pd.read_csv("data/tombouctou_2023.csv")
#df_gao_2023 = pd.read_csv("data/gao_2023.csv")
#df_kidal_2023 = pd.read_csv("data/kidal_2023.csv")

                    #<!--------------------hourly---------------------------!>

df_bamako_hourly_2023= pd.read_csv("base/bamako_hourly_2023.csv")
#df_kayes_hourly_2023= pd.read_csv("base/kayes_hourly_2023.csv")
#df_koulikoro_hourly_2023= pd.read_csv("base/koulikoro_hourly_2023.csv")
df_sikasso_hourly_2023= pd.read_csv("base/sikasso_hourly_2023.csv")
#df_segou_hourly_2023= pd.read_csv("base/segou_hourly_2023.csv")
#df_mopti_hourly_2023= pd.read_csv("base/mopti_hourly_2023.csv")
df_tombouctou_hourly_2023= pd.read_csv("base/tombouctou_hourly_2023.csv")
#df_gao_hourly_2023= pd.read_csv("base/gao_hourly_2023.csv")
#df_kidal_hourly_2023= pd.read_csv("base/kidal_hourly_2023.csv")

                    #<!--------------------base operation---------------------------!>


df_bamako_2023['daylight_duration_hours'] = df_bamako_2023['daylight_duration'] / 3600
df_bamako_2023['sunshine_duration_hours'] = df_bamako_2023['sunshine_duration'] / 3600
df_sikasso_2023['daylight_duration_hours'] = df_sikasso_2023['daylight_duration'] / 3600
df_sikasso_2023['sunshine_duration_hours'] = df_sikasso_2023['sunshine_duration'] / 3600
df_tombouctou_2023['daylight_duration_hours'] = df_tombouctou_2023['daylight_duration'] / 3600
df_tombouctou_2023['sunshine_duration_hours'] = df_tombouctou_2023['sunshine_duration'] / 3600
xgB = xgBoost(df_bamako_hourly_2023)

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

###########
histogram_figure = go.Figure()
histogram_figure = px.histogram(df_sikasso_2023, x="date", y="rain_sum", color_discrete_sequence=['rgb(26, 118, 255)'], title="Somme des Précipitations - Sikasso")
histogram_figure.add_trace(px.histogram(df_tombouctou_2023, x="date", y="rain_sum", color_discrete_sequence=['rgb(255, 165, 0)'], title="Somme des Précipitations - Tombouctou").data[0])
# Mise en forme du layout
histogram_figure.update_layout(
    title='Histogramme de la Somme des Précipitations (Sikasso vs Tombouctou)',
    xaxis_title='Date',
    yaxis_title='Somme des Précipitations',
    barmode='overlay',
    showlegend=True,
    legend=dict(x=1.02, y=0.5),
    margin=dict(l=40, r=0, t=40, b=30)
)

###########
duration_difference_figure = px.line(df_sikasso_2023, x="date", y="daylight_duration_hours",color_discrete_sequence=['rgb(26, 118, 255)'], title="Différence de Durée de la Lumière du Jour (Sikasso vs Tombouctou)")
duration_difference_figure.add_trace(px.line(df_tombouctou_2023, x="date", y="daylight_duration_hours",color_discrete_sequence=['rgb(255, 165, 0)'], title="Différence de Durée de la Lumière du Jour (Tombouctou)").data[0])
duration_difference_figure.update_layout(
    xaxis_title='Date',
    yaxis_title='Différence de Durée de la Lumière du Jour (heures)',
    showlegend=True,
    legend=dict(x=1.02, y=0.5),
    margin=dict(l=40, r=0, t=40, b=30)
)
#############


#<!--------------------------------------------layout---------------------------------------------------------------!>

layout = html.Div([
                    #<!--------------------Titre page---------------------------!>
                    
    html.H1("MALI REPORT", 
            style={'textAlign': 'center',
                    "color": '#2a9fd6'
            }),
    html.Hr(),
                    #<!--------------------description---------------------------!>
                 dcc.Markdown(
                    """
                    - Le Mali présente une diversité climatique marquée, fortement influencée par sa position géographique. La majeure partie du pays, notamment le nord, se trouve dans la zone torride, faisant du Mali l'une des régions les plus chaudes de la planète. Le climat est généralement caractérisé par une chaleur intense et une faible humidité sur les trois quarts du territoire, à l'exception du sud, qui est plus humide.

                    - Le nord du Mali est principalement désertique, occupé par le Sahara, le plus grand désert chaud du monde. Les précipitations annuelles sont extrêmement limitées, inférieures à 250 mm en moyenne et quasiment nulles dans certaines régions. Les parties centrales du pays sont semi-désertiques en raison de l'influence du Sahel, recevant en moyenne moins de 500 mm de pluie par an. En revanche, le sud du pays présente un climat subhumide, avec des précipitations annuelles dépassant les 750 mm.

                    - Bien que le régime pluviométrique varie considérablement, le régime thermique reste globalement uniforme avec des températures très élevées tout au long de l'année. La température moyenne annuelle dépasse les 28 °C dans l'ensemble du pays, atteignant parfois près de 32 °C dans les régions sahéliennes. Les étés sont particulièrement torrides, avec des températures maximales dépassant fréquemment les 40 °C.

                    - Certaines régions, comme Kayes, sont connues pour leur chaleur extrême presque constante, atteignant parfois 50 °C en avril et mai. Le Sahara malien connaît également des températures parmi les plus élevées du monde, dépassant les 46 °C en juin et atteignant même 48 °C dans certaien région. Le pays bénéficie d'un ensoleillement abondant, avec une durée moyenne annuelle variant entre 2 700 heures dans le sud et plus de 3 800 heures dans le nord désertique.
                                     
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),   
                 html.Img(src=app.get_asset_url("mali.jpg"), style={'width': '100%'}),
                 dcc.Markdown(
                    """
                    **MALI WEATHER REPORT **
                    offre une analyse détaillée des données météorologiques du Mali plus precisement de huit régions parmi les régions du Mali plus le district de Bamako
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                
                html.Hr(),
                    #<!--------------------prediction_fig---------------------------!>
                dcc.Markdown(
                    """
                     Il est intéressant de noter que **MALI WEATHER REPORT ** propose également un modèle de prévisions météorologiques avec une efficacité remarquable de 99%.
                    
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(
                    figure=dict(
                        data=[
                           go.Scatter(
                               x=list(range(1, 41)),
                               y=list(xgB[0])[:40],
                               mode='lines',
                               name='Temperature réelle'
                           ),
                           go.Scatter(
                               x=list(range(1, 41)),
                               y=list(xgB[1])[:40],
                               mode='lines',
                               line=dict(dash='dash'),  # Set line style to dashed
                               name='Temperature prédite'
                           )
                       ],
                       layout=dict(
                           title='Performance du modèle XGBOOST',
                           xaxis=dict(title='Échantillons'),
                           yaxis=dict(title='Température'),
                           showlegend=True,
                           legend=dict(x=1.02, y=0.5)
                       )
                   ),
                   style={'height': 300},
               ),
                html.Hr(),
                    #<!--------------------Comparaison---------------------------!>
                dcc.Markdown(
                    """
                   **MALI WEATHER REPORT **
                    C'est aussi des comparaison entre les régions pour faciliter la prise de décision pour les déplacements, les activités agricoles ou les activités commerciales.
                    
                    Comparons les conditions météorologiques de la région Sikasso à celui de Tombouctou 
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                
                html.Hr(),
                                #<!------tmperature_fig--------!>
                dcc.Markdown(
                    """
                    La comparaison des températures entre Sikasso et Tombouctou révèle des différences significatives dans les conditions climatiques entre ces deux régions. Sikasso présente une variabilité thermique modérée, avec des températures qui semblent suivre un schéma saisonnier relativement équilibré. En revanche, Tombouctou exhibe des températures plus extrêmes, avec des pics de chaleur plus marqués, ce qui suggère un climat plus aride et chaud. Ces variations climatiques entre les deux localités peuvent être influencées par des facteurs géographiques, tels que la latitude, l'altitude, et d'autres variables météorologiques locales. Cette analyse comparative des températures offre un aperçu précieux des disparités climatiques entre Sikasso et Tombouctou au fil du temps
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),                   
                dcc.Graph(
                    figure=dict(
                        data=[
                            go.Scatter(
                                x=df_sikasso_2023["date"],
                                y=df_sikasso_2023["temperature_2m_mean"],
                                name='Sikasso',
                                marker=dict(color='rgb(26, 118, 255)')
                            ),
                            go.Scatter(
                                x=df_tombouctou_2023["date"],
                                y=df_tombouctou_2023["temperature_2m_mean"],
                                name='Tombouctou',
                                marker=dict(color='rgb(255, 165, 0)')  # Orange

                            )
                        ],
                        layout=dict(
                            title='Comparison de la Temperature (Sikasso vs Tombouctou)',
                            showlegend=True,
                            legend=dict(x=1.02, y=0.5),
                            margin=dict(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 300},
                ),
                html.Hr(),
                
                                #<!------wind_speed_fig--------!>
                dcc.Markdown(
                    """
                    La comparaison des vitesses maximales du vent à 10 mètres entre Sikasso et Tombouctou met en évidence des différences notables dans les conditions météorologiques entre ces deux régions. Sikasso présente des variations de vent relativement modérées, avec des valeurs qui suivent vraisemblablement des schémas météorologiques saisonniers. En revanche, Tombouctou exhibe des vitesses maximales du vent plus élevées, suggérant un climat potentiellement plus venteux et sec. Ces disparités peuvent être influencées par des facteurs tels que la topographie locale, la géographie et d'autres phénomènes météorologiques spécifiques à chaque région. Cette analyse comparative des vitesses maximales du vent à 10 mètres offre un aperçu des conditions éoliennes distinctes entre Sikasso et Tombouctou au fil du temps.
                   
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(
                    figure=dict(
                        data=[
                            go.Scatter(
                                x=df_sikasso_2023["date"],
                                y=df_sikasso_2023["wind_speed_10m_max"],
                                name='Sikasso',
                            ),
                            go.Scatter(
                                x=df_tombouctou_2023["date"],
                                y=df_tombouctou_2023["wind_speed_10m_max"],
                                name='Tombouctou',
                            )
                        ],
                        layout=dict(
                            title='Comparison de la variation du vent (Sikasso vs Tombouctou)',
                            showlegend=True,
                            legend=dict(x=1.02, y=0.5),
                            margin=dict(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 300},
                ),
                html.Hr(),

                                #<!------wind_speed_fig--------!>
                dcc.Markdown(
                    """
                   La comparaison des sommes de précipitations entre Sikasso et Tombouctou révèle des disparités significatives dans les régimes pluviométriques de ces deux régions. Sikasso présente des accumulations de précipitations généralement plus importantes, indiquant une tendance à des conditions plus humides. En revanche, Tombouctou montre des sommes de précipitations moins élevées, suggérant un climat potentiellement plus sec. Ces variations peuvent être attribuées à des facteurs géographiques tels que la localisation et l'influence des systèmes météorologiques régionaux. La compréhension de ces différences de précipitations entre Sikasso et Tombouctou est essentielle pour évaluer les variations climatiques et leurs impacts potentiels sur l'environnement local, l'agriculture, et d'autres secteurs dépendants des conditions météorologiques.
                   
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=histogram_figure),
                html.Hr(),

                                #<!------daylight_duration_difference--------!>
                dcc.Markdown(
                    """
                    - La durée de la lumière du jour peut varier significativement entre les régions. Cette différence peut être influencée par des facteurs géographiques tels que la latitude et l'altitude.
                    - La visualisation ci-dessus compare la différence de durée de la lumière du jour entre Sikasso et Tombouctou sur une période donnée.
                    """,
                    style={'background-color': '#2a9fd6', 'padding': '20px', 'color': 'white'},
                ),
                dcc.Graph(figure=duration_difference_figure),
                dcc.Graph(
                    figure=dict(
                        data=[
                            go.Scatter(
                                x=df_sikasso_2023["date"],
                                y=df_sikasso_2023["sunshine_duration_hours"],
                                name='Sikasso',
                            ),
                            go.Scatter(
                                x=df_tombouctou_2023["date"],
                                y=df_tombouctou_2023["sunshine_duration_hours"],
                                name='Tombouctou',
                            )
                        ],
                        layout=dict(
                            title="Différence de Durée d'Ensoleillement (Sikasso vs Tombouctou)",
                            showlegend=True,
                            legend=dict(x=1.02, y=0.5),
                            margin=dict(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 300},
                ),
                html.Hr(),



    
])
#<!-----------------------------------------------------------------------------------------------------------!>
