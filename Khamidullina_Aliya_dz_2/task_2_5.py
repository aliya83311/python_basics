prices = [57.8, 46.51, 97, 9.23, 100.4, 34, 5, 2356.04]


def human_readable_price(price):
    if isinstance(price, int):
        return f"{str(price).zfill(2)} руб. 00 коп."
    else:
        cents = str(price).split(".")[1]
        roubles = int(price)
        return f"{str(roubles).zfill(2)} руб. {cents.zfill(2)} коп."


def get_rub(x):
    return int(x[:x.index(" ")])


print(f"Id списка prices {id(prices)}")
new_prices = list(map(human_readable_price, prices))
print(new_prices)
print(f"Id списка new_prices {id(new_prices)}")

new_prices.sort(key=get_rub)
print(new_prices)
print(f"Id списка new_prices {id(new_prices)}")

prices_descending = sorted(new_prices, key=get_rub, reverse=True)
print(prices_descending)
print(prices_descending[:5])
