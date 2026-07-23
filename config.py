import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMINS = [
    123456789
]

DB_NAME = "data/users.db"

LOG_FILE = "data/logs.txt"

AI_QUEUE_LIMIT = 5

SUPPORT_USERNAME = "@YourSupport"

CHANNELS = [
    "@YourChannel"
]
