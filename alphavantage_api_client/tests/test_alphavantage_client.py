import pytest
import json
from alphavantage_api_client import AlphavantageClient


def quoteLatestPrice(success_criteria=True,event=None):
    assert event != None
    client = AlphavantageClient()
    latest_stock_price = client.get_latest_stock_price(event)
    if "limit_reached" in latest_stock_price:
        raise ValueError(latest_stock_price["Error Message"])
    assert len(latest_stock_price) > 0
    assert latest_stock_price['success'] == success_criteria
    assert "symbol" in latest_stock_price
    assert latest_stock_price["symbol"] == event["symbol"]

def test_canQuoteStock():
    client = AlphavantageClient()
    event = {
        "symbol": "tsla"
    }
    quoteLatestPrice(True,event)

def test_canNotQuoteWrongSymbol():
    client = AlphavantageClient()
    event = {
        "symbol": "tsla2233"
    }
    quoteLatestPrice(False,event)


def test_canReachLimit():
    client = AlphavantageClient()
    event = {
        "symbol": "tsla"
    }
    limit_reached = False
    # force limit reached
    # my api key is free, so 5 calls per min and total of 500 per day
    for i in range(7):
        latest_stock_price = client.get_latest_stock_price(event)
        print(json.dumps(latest_stock_price))
        if "limit_reached" in latest_stock_price:
            limit_reached = latest_stock_price["limit_reached"]
        if limit_reached == True:
            break

    assert limit_reached == True
    assert "symbol" in latest_stock_price
    assert latest_stock_price["symbol"] == event["symbol"]