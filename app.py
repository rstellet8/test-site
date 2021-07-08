import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from home import generate_home
from page1 import generate_page1
from page2 import generate_page2

from clean_data import clean_data


app = dash.Dash(
    __name__,
    #suppress_callback_exceptions=True
)
app.title = "Teste Multipage"


app.layout = html.Div([
    dcc.Location(
        id="url",
        refresh=False
    ),
    html.Div(
        [
            html.H1(
                "Título"
            )
        ],
        className="title-wrapper"
    ),
    html.Div(
        id="page-content",
        className="body-wrapper"
    )
])


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/page-1":
        return generate_page1()
    if pathname == "/page-2":
        return generate_page2()
    else:
        return generate_home()



exp, imp, sal = clean_data()

@app.callback(
    Output("page1_graph", "figure"),
    Input("page1_dropdown", "value")
)
def page1_fig(country):
    val = imp.query("variable != 'code'")

    data = val.query(f"name == '{country}'")

    fig = px.line(
        x=data["variable"],
        y=data["value"],
        title = f"Imports - {country}",
        labels={
            "x": " ",
            "y": " "
        }
    )

    return fig


@app.callback(
    Output("page2_graph", "figure"),
    Input("page2_dropdown", "value")
)
def page2_fig(country):
    val = imp.query("variable != 'code'")

    data = val.query(f"name == '{country}'")

    fig = px.line(
        x=data["variable"],
        y=data["value"],
        title = f"Exports - {country}",
        labels={
            "x": " ",
            "y": " "
        }
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
