import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('datasets/beer.csv')
fig = go.Figure([
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_ItemMarket'].str.replace('$', '').astype(int), name='Item Market'),
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_Bazaar'].str.replace('$', '').astype(int), name='Bazaar')
])

fig.update_layout(title='Bottle of Beer')
fig.show()

df = pd.read_csv('datasets/sake.csv')
fig = go.Figure([
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_ItemMarket'].str.replace('$', '').astype(int), name='Item Market'),
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_Bazaar'].str.replace('$', '').astype(int), name='Bazaar')
])

fig.update_layout(title='Bottle of Sake')
fig.show()

df = pd.read_csv('datasets/tequila.csv')
fig = go.Figure([
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_ItemMarket'].str.replace('$', '').astype(int), name='Item Market'),
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_Bazaar'].str.replace('$', '').astype(int), name='Bazaar')
])

fig.update_layout(title='Bottle of Tequila')
fig.show()