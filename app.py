import streamlit as st

from data.load_data import get_currency_details, load_currencies_data
from utils import (
    convert_amount,
    display_currency_name,
    plot_range,
)

# Loading currency infos:
# Maybe abbr vs full_name is better
currency_names, currency_details = load_currencies_data()

# App Layout:
st.set_page_config('Currency Converter',
                   page_icon='assets/icons8-dollar-40.png')

# The title does not reflect the predictions yet.
st.title('Currency Converter')

col1, col2, col3 = st.columns(3)

with col1:
    source = st.selectbox(
        'source Currency',
        currency_names,
        currency_names.index('EUR'),
        key='source-currency',
    )
    source_name = display_currency_name(
        'source-currency',
        currency_details,
    )
    st.text(source_name)

with col2:
    target = st.selectbox(
        'Target Currency',
        currency_names,
        currency_names.index('USD'),
        key='target-currency',
    )

    target_name = display_currency_name(
        'target-currency',
        currency_details,
    )
    st.text(target_name)

with col3:
    amount = st.number_input(
        'Amount to be Converted',
        0.01,
        value=100.0,
        step=1.0,
    )

tab1, tab2, tab3 = st.tabs(['Conversion', 'Historical Data', 'Prediction'])

with tab1:
    conversion_button = st.button(
        label='Convert Now!',
        type='primary'
    )

    if conversion_button:
        result = convert_amount(source, target, amount)

        if isinstance(result, tuple):
            col1, col2 = st.columns(2)
            converted_amount, rate = result
            with col1:
                st.metric('Converted Amount', converted_amount)
            with col2:
                st.metric('Conversion Rate', rate)

        else:
            st.error(result)

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        years_to_plot = st.number_input(
            'Choose the years range plotted',
            min_value=1,
            max_value=5,
            value=1,
            step=1,
            key='num-years',
            label_visibility='collapsed',
        )
        st.caption('Choose the years range plotted')
    with col2:
        plot_button = st.button(
            label='Generate plot',
            type='primary',
        )

    if plot_button:
        line_plot = plot_range(source, target, years_to_plot)
        st.pyplot(fig=line_plot)

# Prediction tab: Yet to come
with tab3:
    pass

# Todos:
# Make sure Conversion for identical target and target is not possible
# Add Lineplot for the rate / currencies
# Maybe solve the design questions with tabs
# So that there is one tab for conversion
# And another tab for prediction
# Add prediction logic with XGBoost


# Useful to view from time to time:

# print(currency_details['USD'])
# st.text(currencies)
# st.text(currency_details)
# st.text(st.session_state)
# print(st.session_state)
