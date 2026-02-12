import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG") == "true"
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "CONNECTION_STRING environment variable is not set. "
        "Please set it in your .env file or environment variables. "
        "For Supabase (recommended - use connection pooler): "
        "CONNECTION_STRING=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres?sslmode=require"
    )