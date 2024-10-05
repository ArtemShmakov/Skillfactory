import requests
import json
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote, base, amount):

        if quote == base:
            raise APIException(f'Указаны одинаковые валюты {base}.')

        quote_ticker, base_ticker = keys[quote], keys[base]

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        if amount == 0:
            raise APIException(f'Не удалось обработать количество {int(amount)}')

        url = f"https://api.apilayer.com/fixer/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "SvEYc5tQynJDjKq9l0nJuKs7pDyNwtub"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        total_base = json.loads(response.text)

        return total_base['result']
