import dash_html_components as html
import dash_core_components as dcc
from dash_html_components.Br import Br


def generate_home():
    home = html.Div([
        html.H1(
            "Home"
        ),
        html.Div(
            children=[
                dcc.Link(
                    "Go to Page 1 - Imports",
                    href="/page-1"
                ),
                dcc.Link(
                    "Go to Page 2 - Exports",
                    href="/page-2"
                ),
            ],
            className="page-selector"
        ),
    ])

    return home

