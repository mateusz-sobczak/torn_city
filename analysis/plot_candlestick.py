import pandas as pd
import plotly.graph_objects as go

if __name__ == '__main__':

    item = 'small_first_aid_kit'
    sell = 4400

    # Import Dataset
    df = pd.read_csv(f'../tickers/datasets/tick_{item}.csv', index_col=0)

    # Convert epoch to datetime
    df.index = pd.to_datetime(df.index, unit='s')

    # Convert TBT to OHLC
    ohlc_ItemMarket = df['Price_ItemMarket'].astype(int).resample('5Min').ohlc()
    ohlc_Bazaar = df['Price_Bazaar'].astype(int).resample('5Min').ohlc()

    fig = go.Figure(data=[go.Candlestick(
        x=ohlc_ItemMarket.index,
        open=ohlc_ItemMarket.open,
        high=ohlc_ItemMarket.high,
        low=ohlc_ItemMarket.low,
        close=ohlc_ItemMarket.close
    )])
    fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
    fig.update_layout(title=f'Item Market - {item}', yaxis_title=f'Value of {item} in $')
    fig.show()

    fig = go.Figure(data=[go.Candlestick(
        x=ohlc_Bazaar.index,
        open=ohlc_Bazaar.open,
        high=ohlc_Bazaar.high,
        low=ohlc_Bazaar.low,
        close=ohlc_Bazaar.close
    )])
    fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
    fig.update_layout(title=f'Bazaar Market - {item}', yaxis_title=f'Value of {item} in $')
    fig.show()
