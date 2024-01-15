from dash import dcc, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd 
from app import app

# Get data
df_kayes_2023 = pd.read_csv("data/kayes_2023.csv")
df_kayes_2000_2009 = pd.read_csv("data/kayes_2000-2009.csv")
df_kayes_2010_2023 = pd.read_csv("data/kayes_2010_2023.csv")
df_bamako_2022 = px.data.election()[:20]  # Remplacez par votre jeu de données réel

# Create figure based on data
fig_bar = px.bar(df_kayes_2023, x="temperature_2m_mean")
fig_pie = px.pie(df_bamako_2022, names="district", values="Joly", title="Diagramme circulaire")

# Layout de l'application Dash
layout = html.Div(
    [
        # Section pour le diagramme à barres
        html.Div(
            [
                # Titre de la section
                html.H3("Diagramme à Barres"),
                
                # Ligne horizontale contenant les listes déroulantes
                html.Div(
                    [
                        # Liste déroulante pour sélectionner le jeu de données
                        dcc.Dropdown(
                            options=[
                                {"label": "2023", "value": "df_kayes_2023"},
                                {"label": "2000_2009", "value": "df_kayes_2000_2009"},
                                {"label": "2010_2023", "value": "df_kayes_2010_2023"},
                            ],
                            id="dataset-select",  # Identifiant unique de la liste déroulante
                            value="df_kayes_2023",  # Valeur par défaut de la liste déroulante
                            style={"width": "200px"},  # Largeur de la liste déroulante
                        ),
                        
                        # Liste déroulante pour sélectionner les variables du diagramme à barres
                        dcc.Dropdown(
                            id="variable-select-bar",  # Identifiant unique de la liste déroulante
                            multi=True,  # Permettre la sélection de plusieurs variables
                            style={"width": "200px"},  # Largeur de la liste déroulante
                            value="temperature_2m_mean"  # Valeur par défaut de la liste déroulante
                        ),
                    ],
                    style={"display": "flex"},  # Afficher les composants côte à côte
                ),
                
                # Graphique à barres initial
                dcc.Graph(figure=fig_bar, id="new-data-graph"),  # Identifiant unique du graphique
            ]
        ),
        
        # Section pour le diagramme circulaire (Pie Chart)
        html.Div(
            [
                html.H3("Pie Chart"),
                dcc.Graph(figure=fig_pie, id="pie-chart"),  # Ajouter un autre graphique
            ]
        ),
    ]
)

# Callback pour mettre à jour dynamiquement les options de la deuxième liste déroulante en fonction de la base de données choisie
@app.callback(
    Output("variable-select-bar", "options"),
    [Input("dataset-select", "value")]
)
def update_variable_options(selected_dataset):
    # Utilisez la liste des colonnes associées à la base de données sélectionnée
    if selected_dataset == "df_kayes_2023":
        columns = ['temperature_2m_mean', 'apparent_temperature_mean', 'daylight_duration', 'sunshine_duration', 'rain_sum', 'wind_speed_10m_max', 'shortwave_radiation_sum']
    elif selected_dataset == "df_kayes_2000_2009":
        columns = ['temperature_2m_mean', 'apparent_temperature_mean', 'daylight_duration', 'sunshine_duration', 'rain_sum', 'wind_speed_10m_max', 'shortwave_radiation_sum']
    elif selected_dataset == "df_kayes_2010_2023":
        columns = ['temperature_2m_mean', 'apparent_temperature_mean', 'daylight_duration', 'sunshine_duration', 'rain_sum', 'wind_speed_10m_max', 'shortwave_radiation_sum']
    
    # Convertissez les colonnes en options attendues par la liste déroulante
    variable_options = [{"label": col, "value": col} for col in columns]
    
    return variable_options

@app.callback(
    Output("new-data-graph", "figure"),
    [Input("dataset-select", "value"), Input("variable-select-bar", "value")]
)
def update_bar_chart(selected_dataset, selected_variable):
    # Charger le jeu de données correspondant à la sélection
    df_selected = globals()[selected_dataset]
    
    # Créer le graphique à barres mis à jour en fonction de la variable sélectionnée
    fig_updated = px.bar(df_selected, x=selected_variable)
    
    return fig_updated


