import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import os

from pages import (
    home,
    bamako,
    kayes,
    koulikoro,
    sikasso,
    segou,
    mopti,
    tombouctou,
    gao,
    kidal
)

app = dash.Dash(
    external_stylesheets=[dbc.themes.CYBORG],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Météo", className="display-4", style={"color": "black"})),  # Couleur du texte en blanc
        dbc.Col(
            [
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    style={
                        "color": "rgba(255,255,255,.5)",  # Couleur du bouton de bascule en blanc semi-transparent
                        "border-color": "rgba(255,255,255,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    style={
                        "color": "rgba(255,255,255,.5)",  # Couleur du bouton de bascule en blanc semi-transparent
                        "border-color": "rgba(255,255,255,.1)",
                        
                    },
                    id="sidebar-toggle",
                ),
            ],
            width="auto",
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        html.Div(
            [
                html.Hr(),
                html.P(
                    "MALI WEATHER REPORT ",
                    className="lead",
                    style={"color": "grey"},  # Couleur du texte en blanc
                ),
            ],
            id="blurb",
        ),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Accueil", href="/", active="exact", style={"color": "black"}),
                    dbc.NavLink("Bamako", href="/bamako", active="exact", style={"color": "black"}),
                    dbc.NavLink("Kayes", href="/kayes", active="exact", style={"color": "black"}),
                    dbc.NavLink("Koulikoro", href="/koulikoro", active="exact", style={"color": "black"}),
                    dbc.NavLink("Sikasso", href="/sikasso", active="exact", style={"color": "black"}),
                    dbc.NavLink("Segou", href="/segou", active="exact", style={"color": "black"}),
                    dbc.NavLink("Mopti", href="/mopti", active="exact", style={"color": "black"}),
                    dbc.NavLink("Tombouctou", href="/tombouctou", active="exact", style={"color": "black"}),
                    dbc.NavLink("Gao", href="/gao", active="exact", style={"color": "black"}),
                    dbc.NavLink("Kidal", href="/kidal", active="exact", style={"color": "black"}),
                ],
                vertical=True,
                pills=True,
                style={"height": "calc(100vh - 100px)", "overflowY": "auto","color": "black"},  
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/bamako":
        return bamako.layout
    elif pathname == "/kayes":
        return kayes.layout
    elif pathname == "/koulikoro":
        return koulikoro.layout
    elif pathname == "/sikasso":
        return sikasso.layout
    elif pathname == "/segou":
        return segou.layout
    elif pathname == "/mopti":
        return mopti.layout
    elif pathname == "/tombouctou":
        return tombouctou.layout
    elif pathname == "/gao":
        return gao.layout
    elif pathname == "/kidal":
        return kidal.layout
    else:
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )

@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""

@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True)
