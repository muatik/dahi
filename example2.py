from pymongo import MongoClient

from dahi import bots, contexts, storages
from dahi.contexts import ContextNotFoundError
from dahi.document import Document
from dahi.nlu import MatchNotFound
from dahi.statement import Statement
from dahi.storages import Mongo

storage = Mongo("mongodb://localhost/dahi")
contextId = "57960e326bb20030900eb6d4"


try:
    context = contexts.Builder(storage).get(contextId)
except ContextNotFoundError:
    context = contexts.Builder(storage).create({})

bot = bots.Builder(storage).create(meta={})
# bot.learn(Document(
#     botSay=Statement("elma dedin"),
#     humanSay=Statement("elma")))
try:
    print bot.respond(context, Statement(text="elma"))
except MatchNotFound:
    print "not found"
