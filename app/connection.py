from pymongo import MongoClient ,errors


def get_db():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client.testdb
        return db
    except errors as e:
        raise e
