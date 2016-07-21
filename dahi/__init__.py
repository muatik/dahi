from pymongo import MongoClient


def getDB():
    db = MongoClient("mongodb://localhost")["dahi"]
    return db
