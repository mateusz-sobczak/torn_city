import time
import datetime
import pandas as pd
import plotly.graph_objects as go


def gen_candlestick(item, sell, time):

    # Import Dataset
    df = pd.read_csv(f'../tickers/datasets/tick_{item}.csv', index_col=0)

    # Convert epoch to datetime
    df.index = pd.to_datetime(df.index, unit='s')

    # Convert TBT to OHLC
    ohlc_ItemMarket = df['Price_ItemMarket'].astype(int).resample(time).ohlc()
    ohlc_Bazaar = df['Price_Bazaar'].astype(int).resample(time).ohlc()

    fig = go.Figure(data=[go.Candlestick(
        x=ohlc_ItemMarket.index,
        open=ohlc_ItemMarket.open,
        high=ohlc_ItemMarket.high,
        low=ohlc_ItemMarket.low,
        close=ohlc_ItemMarket.close
    )])
    fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
    fig.update_layout(title=f'Item Market - {item.replace("_", " ")} - {datetime.datetime.now().strftime("%H:%M:%S - %d-%m-%Y")}', yaxis_title=f'Value of {item} in $')
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1hr",
                         step="hour",
                         stepmode="backward"),
                    dict(count=1,
                         label="1day",
                         step="day",
                         stepmode="backward"),
                    dict(count=7,
                         label="1week",
                         step="day",
                         stepmode="backward"),
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    fig.write_html(f'/var/www/htdocs/torn_city/candlestick/candle_{item}_item_market.html')

    fig = go.Figure(data=[go.Candlestick(
        x=ohlc_Bazaar.index,
        open=ohlc_Bazaar.open,
        high=ohlc_Bazaar.high,
        low=ohlc_Bazaar.low,
        close=ohlc_Bazaar.close
    )])
    fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
    fig.update_layout(title=f'Bazaar Market - {item.replace("_", " ")} - {datetime.datetime.now().strftime("%H:%M:%S - %d-%m-%Y")}', yaxis_title=f'Value of {item} in $')
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1hr",
                         step="hour",
                         stepmode="backward"),
                    dict(count=1,
                         label="1day",
                         step="day",
                         stepmode="backward"),
                    dict(count=7,
                         label="1week",
                         step="day",
                         stepmode="backward"),
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    fig.write_html(f'/var/www/htdocs/torn_city/candlestick/candle_{item}_bazaar_market.html')


def gen_line(item, sell):
    df = pd.read_csv(f'../tickers/datasets/tick_{item}.csv')
    fig = go.Figure([
        go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_ItemMarket'].astype(int), name='Item Market'),
        go.Scatter(x=pd.to_datetime(df['Tick'], unit='s'), y=df['Price_Bazaar'].astype(int), name='Bazaar'),
    ])

    fig.add_hline(y=sell, line_dash='dash', line_color='green', annotation_text=f"Selling Point {sell}")
    fig.update_layout(title=f'{item.replace("_", " ")} - {datetime.datetime.now().strftime("%H:%M:%S - %d-%m-%Y")}')
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1hr",
                         step="hour",
                         stepmode="backward"),
                    dict(count=1,
                         label="1day",
                         step="day",
                         stepmode="backward"),
                    dict(count=7,
                         label="1week",
                         step="day",
                         stepmode="backward"),
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    fig.write_html(f'/var/www/htdocs/torn_city/line/line_{item}_bazaar_market.html')


if __name__ == '__main__':
    while True:
        # Nerve
        gen_candlestick('bottle_of_beer', 895, '15Min')
        gen_line('bottle_of_beer', 895)

        gen_candlestick('bottle_of_sake', 900, '15Min')
        gen_line('bottle_of_sake', 900)

        gen_candlestick('bottle_of_tequila', 900, '15Min')
        gen_line('bottle_of_tequila', 900)

        # Happy
        gen_candlestick('lollipop', 620, '15Min')
        gen_line('lollipop', 620)

        # life
        gen_candlestick('small_first_aid_kit', 4400, '15Min')
        gen_line('small_first_aid_kit', 4400)

        gen_candlestick('first_aid_kit', 7999, '15Min')
        gen_line('first_aid_kit', 7999)

        # Energy
        gen_candlestick('can_of_goose_juice', 450000, '15Min')
        gen_line('can_of_goose_juice', 450000)
        time.sleep(780)
