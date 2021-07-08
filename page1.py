import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px


from clean_data import clean_data

_, imp, _= clean_data()



def generate_page1():
    page1 = html.Div([
        dcc.Link(
            "Go to Home",
            href="/"
        ),
        html.Br(),
        dcc.Link(
            "Go to Page 2",
            href="/page-2"
        ),
        html.H1(
            "Page 1 - Imports"
        ),
        html.Div([
            dcc.Dropdown(
                id="page1_dropdown",
                options=[{"label": unique, "value": unique} for unique in imp["name"]],
                value="Brazil",
            ),
            dcc.Graph(
                id="page1_graph"
            )
        ])
    ])

    return page1

