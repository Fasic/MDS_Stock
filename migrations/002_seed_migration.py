"""Peewee migrations -- 002_seed_migration.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['table_name']            # Return model in current state by name
    > Model = migrator.ModelClass                   # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.run(func, *args, **kwargs)           # Run python function with the given args
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.add_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)
    > migrator.add_constraint(model, name, sql)
    > migrator.drop_index(model, *col_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.drop_constraints(model, *constraints)

"""
from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator

from migrations.data.migration_data import COMPANIES
from migrations.data.migration_data import get_stocks

with suppress(ImportError):
    pass


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    Company = migrator.orm["companies"]
    Stock = migrator.orm["stocks"]

    with database.atomic():
        Company.insert_many(COMPANIES).execute()

        for company in COMPANIES:
            company_name = company.get("name")
            company = Company.get(Company.name == company_name)
            company_id = company.id

            stocks = get_stocks(company_name, company_id)
            Stock.insert_many(stocks).execute()


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
