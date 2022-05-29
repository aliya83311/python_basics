prices = [57.8, 46.51, 97, 9.23, 100.4, 34, 5, 2356.04, 10999.99, 0.99]


def get_rub(x):
    return int(x[:x.index(" ")])


def human_readable_price(seq):
    for idx, price in enumerate(seq):
        if isinstance(seq[idx], int):
            seq[idx] = f"{str(price)} руб 00 коп"
        else:
            cents = str(price).split(".")[1]
            roubles = int(price)
            seq[idx] = f"{str(roubles)} руб {cents.zfill(2)} коп"
    return seq


print(f"ID списка 'prices': {id(prices)}")
print(human_readable_price(prices))

prices.sort(key=get_rub)
print(prices)
print(f"ID списка 'prices': {id(prices)}")

prices_descending = sorted(prices, key=get_rub, reverse=True)
print(prices_descending)
print(prices_descending[:5])
