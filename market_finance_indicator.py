import market

if __name__ == '__main__':
    key = open('key.txt').readline()
    market = market.Market(key=key)

    beers = market.get_items(item=180) #Bottle of Beer
    profit, cost, price = market.profit_margin(price=890)

    print(f'''
    ------BEER------
    Invest ${cost:,}
    Profit ${profit:,}\t{round((profit / cost)*100, 2)}%
    Buy at ${price:,}
    Top 3 Options:\t[1] ${beers[0]['cost']:,}\t{beers[0]['quantity']}
    \t\t\t\t[2] ${beers[1]['cost']:,}\t{beers[1]['quantity']}
    \t\t\t\t[3] ${beers[2]['cost']:,}\t{beers[2]['quantity']}''')

    sake = market.get_items(item=294) #Bottle of Sake
    profit, cost, price = market.profit_margin(price=900)

    print(f'''
    ------SAKE------
    Invest ${cost:,}
    Profit ${profit:,}\t{round((profit / cost)*100, 2)}%
    Buy at ${price:,}
    Top 3 Options:\t[1] ${sake[0]['cost']:,}\t{sake[0]['quantity']}
    \t\t\t\t[2] ${sake[1]['cost']:,}\t{sake[1]['quantity']}
    \t\t\t\t[3] ${sake[2]['cost']:,}\t{sake[2]['quantity']}''')

    tequila = market.get_items(item=426) #Bottle of Tequila
    profit, cost, price = market.profit_margin(price=900)

    print(f'''
    -----Tequila-----
    Invest ${cost:,}
    Profit ${profit:,}\t{round((profit / cost)*100, 2)}%
    Buy at ${price:,}
    Top 3 Options:\t[1] ${tequila[0]['cost']:,}\t{tequila[0]['quantity']}
    \t\t\t\t[2] ${tequila[1]['cost']:,}\t{tequila[1]['quantity']}
    \t\t\t\t[3] ${tequila[2]['cost']:,}\t{tequila[2]['quantity']}''')

    lollipop = market.get_items(item=310) #Lollipop
    profit, cost, price = market.profit_margin(price=620)

    print(f'''
    ----Lollipop----
    Invest ${cost:,}
    Profit ${profit:,}\t{round((profit / cost)*100, 2)}%
    Buy at ${price:,}
    Top 3 Options:\t[1] ${lollipop[0]['cost']:,}\t{lollipop[0]['quantity']}
    \t\t\t\t[2] ${lollipop[1]['cost']:,}\t{lollipop[1]['quantity']}
    \t\t\t\t[3] ${lollipop[2]['cost']:,}\t{lollipop[2]['quantity']}''')

    sfirstaid = market.get_items(item=68) #Small First Aid Kit
    profit, cost, price = market.profit_margin(price=4400)

    print(f'''
    ----Small First Aid Kit----
    Invest ${cost:,}
    Profit ${profit:,}\t{round((profit / cost)*100, 2)}%
    Buy at ${price:,}
    Top 3 Options:\t[1] ${sfirstaid[0]['cost']:,}\t{sfirstaid[0]['quantity']}
    \t\t\t\t[2] ${sfirstaid[1]['cost']:,}\t{sfirstaid[1]['quantity']}
    \t\t\t\t[3] ${sfirstaid[2]['cost']:,}\t{sfirstaid[2]['quantity']}''')
