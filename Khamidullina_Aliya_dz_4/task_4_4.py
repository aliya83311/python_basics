from utils import currency_rates

currencies = ["usd", "EUR", "INR", "CNY", "ddd"]

for item in currencies:
    print(currency_rates(item))
