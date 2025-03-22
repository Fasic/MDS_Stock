from peewee import Model, PostgresqlDatabase

from src.setup.settings import DATABASE_CONFIG

banking_database = PostgresqlDatabase(
    DATABASE_CONFIG['name'],
    user=DATABASE_CONFIG['user'],
    password=DATABASE_CONFIG['password'],
    host=DATABASE_CONFIG['host'],
    port=DATABASE_CONFIG['port']
)


class BaseModel(Model):
    class Meta:
        database = banking_database
