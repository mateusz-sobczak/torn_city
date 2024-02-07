import market
import time

key = open('../key.txt').readline()
market = market.Market(key=key)

while True:
    with open(file='datasets/tick_sake.csv', mode='a') as file:
        item_market, bazaar = market.get_items(item='Bottle of Sake', market='itemmarket,bazaar')
        file.write(f'{round(time.time())},{item_market[0]["cost"]},{bazaar[0]["cost"]}\n')
        file.close()
    time.sleep(10)
