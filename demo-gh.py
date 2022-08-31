import pandas as pd
import yfinance as yf
from datetime import timedelta
from prefect import flow, task


@task(retries=3, cache_expiration=timedelta(30))
def fetch_data(ticker):
    return yf.download(ticker)


def save_data(stock_df):
    stock_df = pd.read_csv("data.csv")
    stock_df.to_csv("output.csv")


@flow
def pipeline4(ticker="AMZN"):

    # from prefect.blocks.notifications import SlackWebhook

    # slack_webhook_block = SlackWebhook.load("msg-jeff")
    # slack_webhook_block.notify("Hello from Prefect!")
    df = fetch_data(ticker)
    save_data(df)


if __name__ == "__main__":
    pipeline4()
