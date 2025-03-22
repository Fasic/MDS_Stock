# auto-generated snapshot
import datetime

import peewee
from peewee import *


snapshot = Snapshot()


@snapshot.append
class Company(peewee.Model):
    name = CharField(max_length=255)
    short_name = CharField(max_length=10, unique=True)
    added_to_stock_market = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = "companies"


@snapshot.append
class Stock(peewee.Model):
    company = snapshot.ForeignKeyField(backref="stocks", index=True, model="company")
    date = DateField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    adj_close = FloatField()
    volume = IntegerField()

    class Meta:
        table_name = "stocks"
