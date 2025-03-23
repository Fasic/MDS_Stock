from peewee import PostgresqlDatabase
from peewee_migrate import Router

from ..models import Company
from ..models import Stock
from .settings import DATABASE_CONFIG

database = PostgresqlDatabase(
    DATABASE_CONFIG["name"],
    user=DATABASE_CONFIG["user"],
    password=DATABASE_CONFIG["password"],
    host=DATABASE_CONFIG["host"],
    port=DATABASE_CONFIG["port"],
)

MODELS = [Company, Stock]
router = Router(database, migrate_dir="migrations")

# Auto generate init migration file
# router.create('init_migration', auto=MODELS)

# Generate seed migration file
# router.create('seed_migration')

# Run migrations
router.run()
