from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
import requests
import xml.etree.ElementTree as et


def currency_rates(code):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    result = response.text
    root = et.fromstring(result)
    current_date = root.get("Date")
    current_date = datetime.strptime(current_date, '%d.%m.%Y').date()
    try:
        code = code.upper()
    except AttributeError:
        print("This function takes only strings.")
    else:
        for valute in root.findall("Valute"):
            char_code = valute.find("CharCode").text
            nominal = valute.find("Nominal").text
            if char_code == code:
                value = Decimal(valute.find("Value").text.replace(",", "."))
                value = value.quantize(Decimal("1.00"), ROUND_HALF_UP)
                return f"Today {current_date} {nominal} {code} is {value} roubles."


print(currency_rates("eur"))
print(currency_rates("UsD"))
print(currency_rates("KZT"))
print(currency_rates(456456456))
