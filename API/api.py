import yfinance as yf
import pandas as pd
from xbbg import blp
import datetime

def get_stock_data_yf(ticker, start_date, trading_days):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date)
    data = data.iloc[:trading_days]
    return data

def get_stock_price_data_boolmberg_start_period(ticker, start_date, number_of_trading_days):
    # start_date is a date type time value
    end_date = start_date + pd.DateOffset(months=3)
    df = blp.bdh(
    [ticker],
    ["PX_LAST"],
    start_date=start_date,
    end_date=end_date)
    df = df.reset_index()
    df.columns = ["Date", "Price"]
    return df.iloc[:number_of_trading_days]

def get_stock_price_data_boolmberg_start_end_period(ticker, start_date, end_date, number_of_trading_days):
    # start_date is a date type time value
    # 获取的数据是从以前到现在排列的
    # 返回dataframe类型的数据
    df = blp.bdh(
    [ticker],
    ["PX_LAST"],
    start_date=start_date,
    end_date=end_date)
    df = df.reset_index()
    df.columns = ["Date", "Price"]
    return df.iloc[:number_of_trading_days+1]

def get_stock_price_data_boolmberg_start_end(ticker, start_date, end_date):
    # start_date is a date type time value
    # 获取的数据是从以前到现在排列的
    # 返回dataframe类型的数据
    df = blp.bdh(
    [ticker],
    ["PX_LAST"],
    start_date=start_date,
    end_date=end_date)
    df = df.reset_index()
    df.columns = ["Date", "Price"]
    return df

# test
# ticker = "NVDA US Equity"
# start_date = datetime.date(2014,1,1)
# end_date = datetime.date(2014,1,31)
# print(get_stock_price_data_boolmberg_start_end(ticker, start_date, end_date))