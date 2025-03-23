import unittest
from datetime import date

from src.schemas.stock import StockData
from src.schemas.stock import StockMaxProfitData
from src.utilities.stock_utils import stock_max_profit
from src.utilities.stock_utils import stock_one_time_max_profit

empty_stocks = []
one_stocks = [StockData(date=date(2023, 1, 1), close=100)]
falling_stocks = [StockData(date=date(2023, 1, 1), close=100), StockData(date=date(2023, 1, 2), close=90), StockData(date=date(2023, 1, 3), close=80)]
stocks = [
    StockData(date=date(2023, 1, 1), close=100),
    StockData(date=date(2023, 1, 2), close=150),
    StockData(date=date(2023, 1, 3), close=50),
    StockData(date=date(2023, 1, 4), close=200),
]
dont_sell_stocks = [
    StockData(date=date(2023, 1, 1), close=100),
    StockData(date=date(2023, 1, 2), close=150),
    StockData(date=date(2023, 1, 3), close=100),
    StockData(date=date(2023, 1, 4), close=100),
    StockData(date=date(2023, 1, 4), close=50),
]


class TestOneTimeProfit(unittest.TestCase):
    def test_stock_one_time_max_profit_empty(self):
        result = stock_one_time_max_profit(empty_stocks)
        self.assertEqual(result, StockMaxProfitData(buy=None, sell=None, profit=0))

    def test_stock_one_time_max_profit_single_entry(self):
        result = stock_one_time_max_profit(one_stocks)
        self.assertEqual(result, StockMaxProfitData(buy=None, sell=None, profit=0))

    def test_stock_one_time_max_profit_no_profit(self):
        result = stock_one_time_max_profit(falling_stocks)
        self.assertEqual(result, StockMaxProfitData(buy=None, sell=None, profit=0))

    def test_stock_one_time_max_profit_multiple_profits(self):
        result = stock_one_time_max_profit(stocks)
        self.assertEqual(result, StockMaxProfitData(buy=stocks[2], sell=stocks[3], profit=150))


class TestMaxProfit(unittest.TestCase):
    def test_stock_max_profit_empty(self):
        result = stock_max_profit(empty_stocks)
        self.assertEqual(result, 0.0)

    def test_stock_max_profit_single_entry(self):
        result = stock_max_profit(one_stocks)
        self.assertEqual(result, 0.0)

    def test_stock_max_profit_no_profit(self):
        result = stock_max_profit(falling_stocks)
        self.assertEqual(result, 0.0)

    def test_stock_max_profit_multiple_profits(self):
        result = stock_max_profit(stocks)
        self.assertEqual(result, 200.0)

    def test_stock_max_profit_multiple_profits_dont_sell_end(self):
        result = stock_max_profit(dont_sell_stocks)
        self.assertEqual(result, 50.0)
