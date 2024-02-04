import market
import time

market = market.Market(key='?')

while True:
    with open(file='beer.csv', mode='a') as file:
        beers = market.get_items(item='Bottle of Beer', market='itemmarket')
        file.write(f'{round(time.time())},${beers[0]["cost"]:,}\n')
        file.close()
    time.sleep(10)
