import pandas as pd
import yfinance as yf
from datetime import timedelta
from prefect import flow, task


# @task(retries=3, cache_expiration=timedelta(30))
# def fetch_data(ticker):
#     return yf.download(ticker)


@task
def save_data():
    stock_df = pd.read_csv("data.csv")
    print(stock_df)
    stock_df.to_csv("/Users/jeffhale/desktop/whereami.csv")  # use an absolute path
    return "where?"


@flow
def pipeline10(ticker="AMZN"):
    #    df = fetch_data(ticker)
    x = save_data()
    return x
