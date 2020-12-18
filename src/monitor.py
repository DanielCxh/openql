import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

title = "data title"

app.layout = html.Div(children=[
    html.H2(children='Dash Demo', style={"text-align": "center"}),

    html.Div(children = '''Daniel's Trader''',
             style = {"text-align": "center", "color": "red"}),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [3, 4, 2], 'type': 'bar', 'name': '数据源A'},
                {'x': [1, 2, 3], 'y': [2, 3, 5], 'type': 'bar', 'name': '数据源B'},
            ],
            'layout': {
                'title': title
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
