from dash import Input, Output, State, dcc, html
import plotly.express as px
import pandas as pd

# Chemin vers le fichier de données
data_file_path = 'data/bamako_data.csv'

# Importer le DataFrame à partir du fichier CSV
df_bamako = pd.read_csv("data/bamako_2023.csv")

# Assume que vous avez un DataFrame appelé df_bamako avec les données météorologiques
# Assurez-vous d'ajuster cela en fonction de la structure réelle de vos données

# Création d'un graphique de la température moyenne au fil du temps
temperature_fig = px.line(df_bamako, x='date', y='temperature_2m_mean', title='Température Moyenne à 2m au Fil du Temps')

# Création d'un histogramme des précipitations
precipitation_fig = px.histogram(df_bamako, x='date', y='rain_sum', title='Somme des Précipitations au Fil du Temps')

# Création d'un graphique de la vitesse maximale du vent
wind_speed_fig = px.line(df_bamako, x='date', y='wind_speed_10m_max', title='Vitesse Maximale du Vent au Fil du Temps')

# Création d'un graphique de la durée d'ensoleillement
sunshine_duration_fig = px.line(df_bamako, x='date', y='sunshine_duration', title='Durée d\'Ensoleillement au Fil du Temps')

# Création de la mise en page de la page Bamako
layout = html.Div([
    html.H3("Données Météorologiques à Bamako en 2023"),
    
    # Graphique de la température
    dcc.Graph(figure=temperature_fig),
    
    html.H4("Données Météorologiques à Bamako en 2023"),

    
    # Histogramme des précipitations
    dcc.Graph(figure=precipitation_fig),
    
    # Graphique de la vitesse maximale du vent
    dcc.Graph(figure=wind_speed_fig),
    
    # Graphique de la durée d'ensoleillement
    dcc.Graph(figure=sunshine_duration_fig)
])
