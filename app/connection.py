from pymongo import MongoClient ,errors
from os import getenv

mongo_uri = getenv("MONGO_URI", "mongodb://localhost:27017/")

def get_db():
    try:
        client = MongoClient(mongo_uri)
        db = client.testdb
        return db
    except errors as e:
        raise e
