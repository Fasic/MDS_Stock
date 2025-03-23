import csv
from datetime import datetime
from pathlib import Path
from typing import List

from src.schemas.stock import StockCreate

COMPANIES = [
    {"name": "Amazon", "short_name": "AMZN", "added_to_stock_market": datetime(1997, 5, 15, 10, 30)},
    {"name": "Apple", "short_name": "AAPL", "added_to_stock_market": datetime(1980, 12, 12, 9, 15)},
    {"name": "Facebook", "short_name": "META", "added_to_stock_market": datetime(2012, 5, 18, 14, 0)},
    {"name": "Google", "short_name": "GOOGL", "added_to_stock_market": datetime(2004, 8, 19, 16, 45)},
    {"name": "Netflix", "short_name": "NFLX", "added_to_stock_market": datetime(2002, 5, 23, 11, 30)},
]


def get_stocks(company_name: str, company: int) -> List[dict]:
    stocks: List[dict] = []

    csv_path = Path(__file__).parent / f"{company_name}.csv"
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] != "null":
                stocks.append(
                    StockCreate(
                        company=company,
                        date=datetime.strptime(row["Date"], "%Y-%m-%d"),
                        open=float(row["Open"]) if row["Open"] != "null" else 0,
                        high=float(row["High"]) if row["High"] != "null" else 0,
                        low=float(row["Low"]) if row["Low"] != "null" else 0,
                        close=float(row["Close"]) if row["Close"] != "null" else 0,
                        adj_close=float(row["Adj Close"]) if row["Adj Close"] != "null" else 0,
                        volume=int(row["Volume"]) if row["Volume"] != "null" else 0,
                    ).model_dump()
                )
    return stocks
