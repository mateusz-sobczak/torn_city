import market
import time

key = open('../key.txt').readline()
market = market.Market(key=key)

item = market.get_item_id(item='Bottle of Tequila')

while True:
    with open(file='datasets/tick_tequila.csv', mode='a') as file:
        item_market, bazaar = market.get_items(item=item, market='itemmarket,bazaar')
        file.write(f'{round(time.time())},{item_market[0]["cost"]},{bazaar[0]["cost"]}\n')
        file.close()
    time.sleep(10)
