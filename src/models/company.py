from datetime import datetime

from peewee import AutoField, CharField, DateTimeField

from src.models.base import BaseModel


class Company(BaseModel):
    class Meta:
        table_name = 'companies'

    id = AutoField()
    name = CharField(null=False)
    short_name = CharField(max_length=10, unique=True, null=False)
    added_to_stock_market = DateTimeField(default=datetime.now)

    def __repr__(self):
        return f"<Company(id={self.id}, name={self.name}, short_name={self.short_name}, added_to_stock_market={self.added_to_stock_market})>"
