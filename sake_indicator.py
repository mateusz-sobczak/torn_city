import market
import time

market = market.Market(key='?')

while True:
    with open(file='datasets/sake.csv', mode='a') as file:
        item_market, bazaar = market.get_items(item='Bottle of Sake', market='itemmarket,bazaar')
        file.write(f'{round(time.time())},${item_market[0]["cost"]},${bazaar[0]["cost"]}\n')
        file.close()
    time.sleep(10)
