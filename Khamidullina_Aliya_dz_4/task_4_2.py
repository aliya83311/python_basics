from decimal import Decimal, ROUND_HALF_UP
import requests
import xml.etree.ElementTree as et


def currency_rates(code):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    result = response.text
    root = et.fromstring(result)
    try:
        code = code.upper()
    except AttributeError:
        print("This function takes only strings.")
    else:
        for valute in root.findall("Valute"):
            char_code = valute.find("CharCode").text
            if char_code == code:
                value = Decimal(valute.find("Value").text.replace(",", "."))
                return value.quantize(Decimal("1.00"), ROUND_HALF_UP)


print(currency_rates("eur"))
print(currency_rates("UsD"))
print(currency_rates(456456456))
