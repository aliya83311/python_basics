prices = [57.8, 46.51, 97, 9.23, 100.4, 34, 5, 2356.04]


def human_readable_price(price):
    if isinstance(price, int):
        return f"{str(price).zfill(2)} руб. 00 коп."
    else:
        cents = str(price).split(".")[1]
        roubles = int(price)
        return f"{str(roubles).zfill(2)} руб. {str(cents).zfill(2)} коп."


print(list(map(human_readable_price, prices)))

"""
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

prices_descending = sorted(prices, reverse=True)
print(prices_descending)
print(prices_descending[:5])
"""
