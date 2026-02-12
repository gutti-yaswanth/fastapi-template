#!/usr/bin/env python3
"""
Simple script to test database connection
Run this to verify your CONNECTION_STRING is correct before starting the server
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

CONNECTION_STRING = os.getenv("DATABASE_URL")

if not CONNECTION_STRING:
    print("❌ ERROR: CONNECTION_STRING not found in .env file")
    print("\nPlease create a .env file with:")
    print("CONNECTION_STRING=postgresql://...")
    exit(1)

print(f"Testing connection to: {CONNECTION_STRING.split('@')[1] if '@' in CONNECTION_STRING else 'database'}")

# Check if using direct connection
if "supabase.co" in CONNECTION_STRING and ":5432" in CONNECTION_STRING and "pooler" not in CONNECTION_STRING:
    print("\n⚠️  WARNING: You're using Supabase direct connection (port 5432)")
    print("   This often causes timeouts. Use the connection pooler instead:")
    print("   Supabase Dashboard → Settings → Database → Connection Pooling → Transaction mode")
    print("   It should use port 6543 and contain 'pooler' in the hostname\n")

try:
    # Configure SSL for Supabase
    connect_args = {}
    if "supabase.co" in CONNECTION_STRING:
        if "sslmode" not in CONNECTION_STRING.lower():
            connect_args = {"sslmode": "require"}
        connect_args.update({
            "connect_timeout": 10,
        })
    
    engine = create_engine(CONNECTION_STRING, connect_args=connect_args)
    
    print("Attempting to connect...")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        print("✅ Connection successful!")
        print(f"   Database version: {version[:50]}...")
        
        # Test if we can query
        result = conn.execute(text("SELECT current_database();"))
        db_name = result.fetchone()[0]
        print(f"   Connected to database: {db_name}")
        
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("\nTroubleshooting:")
    print("1. Verify your CONNECTION_STRING is correct")
    print("2. For Supabase, use the connection pooler (port 6543) not direct (port 5432)")
    print("3. Check if your IP is allowed in Supabase dashboard (Settings → Database → Connection Pooling)")
    print("4. Verify your password is correct")
    exit(1)

