import datetime
import os
from datetime import date, timedelta

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_KEY = os.getenv("ExchangeRateAPI")


def display_currency_name(currency_type: str, currency_details: dict) -> str:
    source_currency = st.session_state[currency_type]
    currency_name = currency_details[source_currency]
    # Line for the ExchangerateAPI only:
    #    currency_name = currency_details[source_currency]['Currency Name']
    return currency_name


# Conversion functions:
def convert_amount(source: str, target: str, amount: float) -> tuple:
    conversion_rate = get_conversion_rate(source, target, amount)
    converted_amount = convert_by_rate(conversion_rate, amount)
    return converted_amount, conversion_rate


def collect_conversion_input():
    source = st.session_state['source-currency']
    target = st.session_state['target-currency']
    amount = st.session_state['specified-amount']
    return source, target, amount


def get_conversion_rate(source: str, target: str,
                        amount: float) -> float | str:
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{source}/{target}/{amount}'
    try:
        response = requests.get(url)
        if not response.status_code == 200:
            return response.status_code

        conversion_rate = response.json()['conversion_rate']

        return conversion_rate

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

    # Is this exception necessary? Will it not be covered by a not 200 code?
    except (KeyError, ValueError) as e:
        return f"Data error: {e}"


def convert_by_rate(conversion_rate: float, amount: float):
    return conversion_rate * amount


# Prediction / plot functions:
def plot_range(base: str, symbol: str, num_years: int):
    starting_date = generate_timerange(num_years)
    historic_data = get_historic_currency_dates(base, symbol, starting_date)
    # validate_json
    historic_frame = turn_currencies_to_frame(historic_data)
    return generate_rates_line_plot(historic_frame)


def collect_plot_input():
    return st.session_state['num-years']


def generate_timerange(num_years: int) -> date:
    today = date.today()
    starting_date = today - timedelta(round(365.25 * num_years))
    return starting_date


def get_historic_currency_dates(base: str, symbol: str,
                                starting_date: datetime.date) -> dict:
    n_years_data = f'https://api.frankfurter.dev/v1/{starting_date}..?base={base}&symbols={symbol}'
    response = requests.get(n_years_data)
    return response.json()


# missing yet: def validate_json

def turn_currencies_to_frame(n_years_data: dict) -> pd.DataFrame:
    historic_frame = pd.DataFrame.from_dict(n_years_data['rates'],
                                            orient='index')
    historic_frame.index = pd.to_datetime(historic_frame.index)
    return historic_frame


def generate_rates_line_plot(n_years_frame: pd.DataFrame) -> plt.figure:
    fig, ax = plt.subplots()
    ax.plot(
        n_years_frame.index,
        n_years_frame.iloc[:, 0]
    )
    adjust_line_plot_tickers(ax)

    return fig


def adjust_line_plot_tickers(ax):
    ax.xaxis.set_major_locator(mdates.YearLocator(1, 1, 1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

    return ax


# Needed for time series exchange rate data!
# https://frankfurter.dev/
