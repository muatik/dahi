from pymongo import MongoClient

db = None


def getDB():
    if db:
        return db
    global db
    db = MongoClient("mongodb://localhost")["dahi"]
    return db
