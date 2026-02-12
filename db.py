import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client: MongoClient | None = None
db = None

def connect_db():
    """
    Establish a connection to the MongoDB database.

    Returns:
        Database: Reference to the connected MongoDB database.

    Raises:
        RuntimeError: If MONGO_URI is not set in environment variables.
    """
    global client, db
    if not MONGO_URI:
        raise RuntimeError("MONGO_URI is not set in environment variables")
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=12000)
    client.admin.command("ping")
    db = client.ml_metrics
    return db

def close_db():
    """
    Close the MongoDB connection if it is active.
    """
    global client
    if client is not None:
        client.close()
        client = None

def get_db():
    """
    Retrieve the active MongoDB database connection.

    Returns:
        Database: Reference to the connected MongoDB database.

    Raises:
        RuntimeError: If the database connection has not been initialized.
    """
    global db
    if db is None:
        raise RuntimeError("Database not initialized, call connect_db first")
    return db
