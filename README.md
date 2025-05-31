# currency_converter

A Python script to convert a specified amount from one currency to another using live exchange rates from [ExchangeRate-API](https://exchangerate-api.com/).

## Features
- Fetches real-time exchange rates for any currency pair.
- Converts an amount from a base currency to a target currency.
- Validates user inputs for robustness.
- Provides clear error messages for invalid inputs or API errors.

## How It Works
The script:
1. Fetches live exchange rates for the base currency using the ExchangeRate-API.
2. Checks if the target currency is available in the rates.
3. Calculates the converted amount and displays it along with the exchange rate.

## Requirements
- Python 3.x
- The `requests` library for making HTTP requests. Install it using:
  ```bash
  pip install requests


## Connected Apps

### List of Currencies and info
- Get a list of currencies with the full name and country of use

### Histical data

## To Does

- Add a User Interface
- Add List of Currencies
- Add a predictor of the currency rate 