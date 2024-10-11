import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6610201435:AAHEv2YoM2ZEtlEdqjilv9mZGjT9Uzzrntw")
    API_ID = os.getenv("API_ID", "21740783")
    API_HASH = os.getenv("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    LOG_CHANNEL = os.getenv("LOG_CHANNEL", "0")
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "0")
    OWNER_ID = int(os.getenv("OWNER_ID", "6299192020"))
    DOWN_PATH = "downloads"
    PRESET = "ultrafast"
