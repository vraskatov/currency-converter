# currency_converter

A Streamlit application for converting a given amount from one currency to another using live exchange rates from [ExchangeRate-API](https://exchangerate-api.com/) and plotting historical data based on data from [Frankfurter](https://frankfurter.dev/)

## Features
- Fetches real-time exchange rates for currency pairs.
- Converts a given amount from a base currency to a target currency.
- Generates lineplots of exchange rates for a given amount of years.

## How To Run the App
- install git
- select a folder and clone the repositor into it with:\
```git clone https://github.com/vraskatov/currency-converter.git```
- create a virtual environment in the cloned folder and activate it
- pip install the requirements into the environment using:\
```pip install -r requirements.txt```
- then navigate in the terminal to where the file app.py is and run:\
```streamlit run app.py```
This should start the app.\
If the app does not open in the browser automatically paste ```http://localhost:8501/``` into a tab of your browser.


## Todos

- Split up utils.py into different modules
- Add a predictor of the currency rate
- Generate better plots
- Improve the design of the app