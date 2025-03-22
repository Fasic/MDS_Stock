import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    'name': os.getenv('POSTGRES_DB', 'stock_db'),
    'user': os.getenv('POSTGRES_USER', 'test_user'),
    'password': os.getenv('POSTGRES_PASSWORD', 'test_password'),
    'host': os.getenv('POSTGRES_SERVER', 'db'),
    'port': int(os.getenv('POSTGRES_PORT', 5432)),
}