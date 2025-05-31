import json


def load_currencies_data():
    with open('data/currency_small.json') as f:
        currencies_full = json.load(f)
        currencies_abbr = sorted(list(currencies_full.keys()))
    return currencies_abbr, currencies_full

# First function for currencies from ExchangeAPI
def get_currency_details():
    with open('data/currency_details.json') as f:
        currency_details = json.load(f)
        currency_names = sorted(list(currency_details.keys()))
    return currency_names, currency_details
