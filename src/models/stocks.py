from peewee import AutoField
from peewee import DateField
from peewee import FloatField
from peewee import ForeignKeyField
from peewee import IntegerField

from src.models.base import BaseModel
from src.models.company import Company


class Stock(BaseModel):
    class Meta:
        table_name = "stocks"

    id = AutoField()
    company = ForeignKeyField(Company, backref="stocks", on_delete="CASCADE")
    date = DateField(null=False)
    open = FloatField(null=False)
    high = FloatField(null=False)
    low = FloatField(null=False)
    close = FloatField(null=False)
    adj_close = FloatField(null=False)
    volume = IntegerField(null=False)

    def __repr__(self):
        return f"<Stock(id={self.id}, company={self.company.name}, date={self.date}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, adj_close={self.adj_close}, volume={self.volume})>"
