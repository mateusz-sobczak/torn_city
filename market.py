import math
import requests


class Market:
    def get_item_id(self, item):
        r = requests.request(method='get', url='https://api.torn.com/torn/?selections=items&key=' + self.key)
        item_no = None

        for s in r.json()['items']:
            if item in r.json()['items'][s]['name']:
                item_no = s

        if item_no is None:
            exit(0)

        return item_no

    def get_items(self, item, market='bazaar'):
        r = requests.request(method='get', url='https://api.torn.com/market/' + str(item) + '?selections=' + market +'&key=' + self.key)
        if ',' in market:
            self.items = r.json()[market.split(',')[0]], r.json()[market.split(',')[1]]
        else:
            self.items = r.json()[market]
        return self.items

    def profit_margin(self, price):
        total_cost = 1; total_profit = 1
        best_price = price - math.ceil(price * 0.001) - 1

        for item in self.items:
            if item['cost'] <= best_price:
                total_cost += item['cost'] * item['quantity']
                total_profit += (price * item['quantity']) - item['cost'] * item['quantity']

        return total_profit, total_cost, best_price

    def __init__(self, key):
        self.key = str(key)
        self.items = {}
