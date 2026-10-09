import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load variables from backend/.env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "rightspocket")

if not MONGO_URI:
    raise ValueError("MONGO_URI is missing from the .env file")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

# Check the database connection
try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")

    db = client[DB_NAME]
except Exception as e:
    print("MongoDB connection failed:", e)
    raise