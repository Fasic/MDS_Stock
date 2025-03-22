# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Company(peewee.Model):
    name = CharField(max_length=255)
    short_name = CharField(max_length=10, unique=True)
    added_to_stock_market = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "companies"


