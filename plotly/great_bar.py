import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import plotly.express as px

import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

a,b,c = [random.randint(0,10) for i in range(10)],[random.randint(0,10) for i in range(10)],[random.randint(0,10) for i in range(10)]

fig = go.Figure(data=[
    go.Bar(x=list(range(10)),y=a),
    go.Bar(x=list(range(10)),y=b),
    go.Bar(x=list(range(10)),y=c)
])
fig.update_layout(barmode='stack')

app.layout= html.Div([dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)