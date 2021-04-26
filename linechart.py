import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

df1 = pd.read_csv(r'C:\Users\abdul\PycharmProjects\PocketCheckLine\PocketCheckData\API_SH.XPD.OOPC.PC.CD_DS2_en_csv_v2_2166588.csv', header=2)

#print(df1.iloc[:,0].values)
trace1 = go.Scatter(x=list(df1.columns)[44:55], y=df1[df1['Country Name'] == 'France'].iloc[:, 44:55].values.flatten(), mode='lines', name='France')
trace2 = go.Scatter(x=list(df1.columns)[44:55], y=df1[df1['Country Name'] == 'Germany'].iloc[:, 44:55].values.flatten(), mode='lines', name='Germany')
data = [trace1, trace2]

layout = go.Layout(title="Health Costs in France vs Germany From 2000 to 2010", xaxis_title="Year", yaxis_title="Cost")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')



