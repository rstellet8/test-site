import dash_html_components as html
import dash_core_components as dcc
from clean_data import clean_data


exp, _, _= clean_data()




def generate_page2():
    page2 = html.Div([
        dcc.Link(
            "Go to Home",
            href="/"
        ),
        html.Br(),
        dcc.Link(
            "Go to Page 1",
            href="/page-1"
        ),
        html.H1(
            "Page 2 - Exports"
        ),
        html.Div([
            dcc.Dropdown(
                id="page2_dropdown",
                options=[{"label": unique, "value": unique} for unique in exp["name"]],
                value="Brazil"
            ),
            dcc.Graph(
                id="page2_graph"
            )
        ])
    ])

    return page2