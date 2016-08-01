from pymongo import MongoClient

from dahi import bots, contexts, storages
from dahi.contexts import ContextNotFoundError
from dahi.storages import Mongo

storage = Mongo("mongodb://localhost/dahi")
contextId = "57960e326bb20030900eb6d4"


try:
    context = contexts.Builder(storage).get(contextId)
    print "ok"
except ContextNotFoundError:
    context = contexts.Builder(storage).create({})

print bots.Builder(storage).create({})

