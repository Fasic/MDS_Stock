# MDS Informatički inženjering - Tehnički zadatak

## How to Start the Project

To start the project, use Docker Compose:

```bash
docker-compose up
```

## Running Migrations

Migrations will be run automatically when the project starts. If you need to run them manually, use:

```bash
python -m src.setup.migrate
```

## Seeding Migration

There is seeding migration that adds data from CSV files to the database

## Documentation

You can find the API documentation at:
[http://localhost:8080/docs](http://localhost:8080/docs)

## Important Notes

- This is not a production-ready project. For production, you should:
    - Add better logging
    - Create different environments (development, staging, production, test)
    - Configure the project more complexly
    - Use more complex database configurations and  better ORM (like SQLAlchemy)
    - Use a smaller docker image size and a multi-stage Dockerfile
- The `.env` file is included for simplicity in running the project. It should not be part of the Git repository.

## Project Structure

- `README.md`: Provides instructions on how to start the project, run migrations, and access documentation
- `Dockerfile`: Defines the Docker image for the project, including the Python environment and dependencies.
- `docker-compose.yml`: Configures Docker Compose services, including the API and PostgreSQL database.

- `tests/test_stock_utils.py`: Contains unit tests for stock utility functions.
- `src/`: The main source directory for the project.
    - `models/`: Contains ORM peewee models for database.
    - `schemas/`: Contains data schemas (pydentic).
    - `utilities/`: Contains utility functions.
    - `setup/`: Contains setup scripts, such as `migrate.py` for migrations, `logger.py` for setting logging, and `settings.py` for setting up env.
    - `.env`: Environment configuration file (not recommended to be included in the repository).

    - `api`: Contains the FastAPI application.
        - `v1/`: Contains the API routes (controllers) for v1 of API.
    - `services/`: Contains the business logic for the API.
    - `main.py`: The entry point for the API application.
