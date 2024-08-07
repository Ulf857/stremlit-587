import yfinance as yf
import streamlit as st

st.write("""
# Einfache Kursapp

Gezeigt wird der BTC-Kurs in USD!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'BTC-USD'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2023-4-20')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
#st.line_chart(tickerDf.Volume)
