
import numpy as np
import pandas as pd
import yfinance as yf

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df_list = pd.read_html('https://finance.yahoo.com/world-indices/')
majorStockIdx = df_list[0]

stock_list= majorStockIdx['Symbol'].tolist()

tickerData = yf.Ticker(stock_list[2])
tickerDf1 = tickerData.history(period='1d',interval="1mo", start='1969-12-24', end='2020-12-28')

for row in tickerDf1.index:
    temp = row.to_pydatetime()
    if temp.month == 1:
        print(tickerData)
        print(temp.month)
    # print(row.to_pydatetime(temp.month), end = " ")

