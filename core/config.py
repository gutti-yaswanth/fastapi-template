import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG") == "true"
DATABASE_URL = os.getenv("DATABASE_URL")

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
# SSL verification for Supabase (set to "false" to disable SSL verification in development)
SUPABASE_VERIFY_SSL = os.getenv("SUPABASE_VERIFY_SSL", "true").lower() == "true"

if not DATABASE_URL:
    raise ValueError(
        "CONNECTION_STRING environment variable is not set. "
        "Please set it in your .env file or environment variables. "
        "For Supabase (recommended - use connection pooler): "
        "CONNECTION_STRING=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres?sslmode=require"
    )

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_ANON_KEY environment variables are required for phone authentication. "
        "Please set them in your .env file. "
        "You can find these in your Supabase Dashboard → Settings → API"
    )