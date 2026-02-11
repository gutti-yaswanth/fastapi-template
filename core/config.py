import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG") == "true"
DATABASE_URL = os.getenv("CONNECTION_STRING")