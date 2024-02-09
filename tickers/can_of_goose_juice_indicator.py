import market
import time

key = open('../key.txt').readline()
market = market.Market(key=key)

item = market.get_item_id(item='Can of Goose Juice')

while True:
    with open(file='datasets/tick_can_of_goose_juice.csv', mode='a') as file:
        try:
            item_market, bazaar = market.get_items(item=item, market='itemmarket,bazaar')
            file.write(f'{round(time.time())},{item_market[0]["cost"]},{bazaar[0]["cost"]}\n')
            file.close()
        except Exception as err:
            print(err)
            continue
    time.sleep(10)
