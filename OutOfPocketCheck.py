import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import subprocess
import numpy as np

df1 = pd.read_csv(r'C:\Users\abdul\PycharmProjects\PocketCheckLine\PocketCheckData\API_SH.XPD.OOPC.PC.CD_DS2_en_csv_v2_2166588.csv', header=2)
countries = df1.iloc[:,0].values

app = dash.Dash(suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    html.H1(children="Out-of-pocket Price Check"),
    html.Hr(),
    html.Div("Out-of-pocket Price Check provides data for countries all around the world"),
    html.Br(),
    dcc.Link('Go to Graphs', href='/graphs'),
    html.Br(),
    #dcc.Link('Launch calculator', href='/calculator')
    html.Button('Launch Calculator', id='submit-val', n_clicks=0),
    html.Div(id='hidden-div', style={'display': 'none'})
])

page_1_layout = html.Div(children=[
    html.H1(children="Pocket Check"),
    html.Hr(),
    html.Br(),
    html.Br(),
    html.Div("Select the countries you want to compare"),
    dcc.Dropdown(
        id='select-country',
        options=[
            {'label': country, 'value': country} for country in countries
        ],
        value=['United States'],
        multi=True

    ),
    dcc.Graph(id='graph1'),
    html.Hr(),
    html.Div("Select the countries you want to compare"),
    dcc.Dropdown(
        id='select-country2',
        options=[
            {'label': country, 'value': country} for country in countries
        ],
        value=[],
        multi=True
    ),
    dcc.Graph(id='graph2')



])

@app.callback(Output('graph1', 'figure'),
              [Input('select-country', 'value')])
def update_graph(selected_country):
    dict_fig = {'data': [{'type': 'scatter', 'x': list(df1.columns)[44:63], 'y': df1[df1['Country Name'] == country].iloc[:, 44:63].values.flatten(),
                     'mode': 'lines', 'name': country} for country in selected_country],
                'layout': go.Layout(title="Health Costs in Various Countries From 2000 to 2018", xaxis_title="Year", yaxis_title="Cost (in Dollars)")}
    return go.Figure(dict_fig)

@app.callback(Output('graph2', 'figure'),
              [Input('select-country2', 'value')])
def update_graph2(selected_country):
    list = [df1[df1['Country Name'] == country].iloc[:,62].values.flatten()[0] for country in selected_country]
    dict_fig = {'data': [{'type': 'bar', 'x': selected_country, 'y': list}],
                'layout': go.Layout(title="Current Healthcare Costs in Various Countries", xaxis_title="Country", yaxis_title="Cost (in Dollars)")}
    return go.Figure(dict_fig)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def update_page(pathname):
    if pathname == '/graphs':
        return page_1_layout
    else:
        return index_page

@app.callback(Output('hidden-div', 'children'),
              [Input('submit-val', 'n_clicks')])
def load_calculator(clicks):
    if clicks >= 1:
        child = subprocess.Popen(['python', 'C:\\Users\\abdul\\PycharmProjects\\PocketCheckLine\\CalculatorPrototype.py'])
    return 'hello'









if __name__ == '__main__':
    app.run_server()