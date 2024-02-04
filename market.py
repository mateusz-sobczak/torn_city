import math
import requests


class Market:
    def get_items(self, item):
        if item == 'Bottle of Beer':
            item = 180
        elif item == 'Bottle of Tequila':
            item = 426
        elif item == 'Bottle of Sake':
            item = 294
        else:
            exit(0)

        r = requests.request(method='get', url='https://api.torn.com/market/' + str(item) + '?selections=bazaar&key=' + self.key)
        self.items = r.json()['bazaar']
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
