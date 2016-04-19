from pymongo import MongoClient

db = None

def getDB():
    if db:
        return db
    global db
    db = MongoClient("mongodb://192.168.33.12")["dahi"]
    return db
