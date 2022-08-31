import pandas as pd
import yfinance as yf
from datetime import timedelta
from prefect import flow, task
from prefect import get_run_logger


@task(retries=3, cache_expiration=timedelta(30))
def fetch_data(ticker):
    return yf.download(ticker)


def save_data(stock_df):
    stock_df = pd.read_csv("data.csv")
    log = get_run_logger()
    log.debug(stock_df)
    print(stock_df)
    stock_df.to_csv("output.csv")


@flow
def pipeline5(ticker="AMZN"):
    df = fetch_data(ticker)
    save_data(df)
