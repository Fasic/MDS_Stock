from typing import List

from src.schemas.stock import StockData
from src.schemas.stock import StockMaxProfitData


def stock_one_time_max_profit(stocks: List[StockData]) -> StockMaxProfitData:
    if not stocks:
        return StockMaxProfitData(buy=None, sell=None, profit=0)
    min_stock = stocks[0]
    max_profit = -1
    sell_stock = None
    buy_stock = None
    for stock in stocks:
        if min_stock.close > stock.close:
            min_stock = stock

        if max_profit < stock.close - min_stock.close:
            sell_stock = stock
            buy_stock = min_stock
            max_profit = sell_stock.close - min_stock.close

    return StockMaxProfitData(buy=buy_stock, sell=sell_stock, profit=max_profit)


def stock_max_profit(stocks: List[StockData]) -> float:
    balance = 0.0
    buying = True
    buy = 0
    for i in range(len(stocks) - 1):
        if buying and stocks[i + 1].close > stocks[i].close:
            buy = stocks[i]
            buying = False
        if not buying and stocks[i + 1].close < stocks[i].close:
            sell = stocks[i]
            balance = balance - buy.close + sell.close
            buying = True
    if not buying:
        balance = balance + stocks[i + 1].close
    return balance
