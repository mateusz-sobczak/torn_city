import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('tickers/datasets/tick_bottle_of_beer.csv')
fig = go.Figure([
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_ItemMarket'].astype(int), name='Item Market'),
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_Bazaar'].astype(int), name='Bazaar'),
])

sell = 885
fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
fig.update_yaxes(rangemode="tozero")
fig.update_layout(title='Bottle of Beer')
fig.show()

df = pd.read_csv('tickers/datasets/tick_bottle_of_sake.csv')
fig = go.Figure([
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_ItemMarket'].astype(int), name='Item Market'),
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_Bazaar'].astype(int), name='Bazaar')
])

sell = 900
fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
fig.update_yaxes(rangemode="tozero")
fig.update_layout(title='Bottle of Sake')
fig.show()

df = pd.read_csv('tickers/datasets/tick_bottle_of_tequila.csv')
fig = go.Figure([
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_ItemMarket'].astype(int), name='Item Market'),
    go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_Bazaar'].astype(int), name='Bazaar')
])

sell = 900
fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
fig.update_yaxes(rangemode="tozero")
fig.update_layout(title='Bottle of Tequila')
fig.show()