import os
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "dogs_db"),
}

API_TOKEN = os.getenv("BOT_TOKEN")